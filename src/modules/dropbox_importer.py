"""
Módulo para importar arquivos do Dropbox
"""
import os
import json
import logging
import webbrowser
from pathlib import Path
from typing import Optional, Dict, List

logger = logging.getLogger(__name__)

try:
    import dropbox
    from dropbox import DropboxOAuth2FlowNoRedirect
    DROPBOX_AVAILABLE = True
except ImportError:
    DROPBOX_AVAILABLE = False
    logger.warning("Dropbox SDK não está instalado. Execute: pip install dropbox")


class DropboxImporter:
    """Gerencia importação de arquivos do Dropbox"""
    
    def __init__(self, app_key: Optional[str] = None, app_secret: Optional[str] = None):
        """
        Inicializa o importador do Dropbox
        
        Args:
            app_key: Chave da aplicação Dropbox
            app_secret: Segredo da aplicação Dropbox
        """
        self.app_key = app_key or os.getenv('DROPBOX_APP_KEY')
        self.app_secret = app_secret or os.getenv('DROPBOX_APP_SECRET')
        self.access_token = None
        self.dbx = None
        self.config_file = Path.home() / '.pcvitalboost' / 'dropbox_config.json'
        
        if not DROPBOX_AVAILABLE:
            raise ImportError("Dropbox SDK não está instalado. Execute: pip install dropbox")
        
        self._load_token()
    
    def _load_token(self):
        """Carrega token salvo"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    self.access_token = config.get('access_token')
                    if self.access_token:
                        self.dbx = dropbox.Dropbox(self.access_token)
                        logger.info("Token do Dropbox carregado com sucesso")
        except Exception as e:
            logger.error(f"Erro ao carregar token: {e}")
    
    def _save_token(self, token: str):
        """Salva token para uso futuro"""
        try:
            self.config_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config_file, 'w') as f:
                json.dump({'access_token': token}, f)
            logger.info("Token do Dropbox salvo com sucesso")
        except Exception as e:
            logger.error(f"Erro ao salvar token: {e}")
    
    def authenticate(self) -> bool:
        """
        Realiza autenticação com Dropbox usando OAuth2
        
        Returns:
            True se autenticação foi bem sucedida
        """
        if not self.app_key:
            logger.error("DROPBOX_APP_KEY não configurada")
            return False
        
        try:
            auth_flow = DropboxOAuth2FlowNoRedirect(
                self.app_key,
                consumer_secret=self.app_secret,
                token_access_type='offline'
            )
            
            authorize_url = auth_flow.start()
            logger.info(f"URL de autorização: {authorize_url}")
            
            # Abre navegador para autorização
            webbrowser.open(authorize_url)
            
            # Retorna True para indicar que o processo foi iniciado
            # O código de autorização deve ser fornecido pelo usuário
            return True
            
        except Exception as e:
            logger.error(f"Erro na autenticação: {e}")
            return False
    
    def complete_authentication(self, auth_code: str) -> bool:
        """
        Completa o processo de autenticação com o código fornecido
        
        Args:
            auth_code: Código de autorização do Dropbox
            
        Returns:
            True se autenticação foi completada com sucesso
        """
        try:
            auth_flow = DropboxOAuth2FlowNoRedirect(
                self.app_key,
                consumer_secret=self.app_secret,
                token_access_type='offline'
            )
            auth_flow.start()
            
            oauth_result = auth_flow.finish(auth_code)
            self.access_token = oauth_result.access_token
            self.dbx = dropbox.Dropbox(self.access_token)
            
            # Salva token
            self._save_token(self.access_token)
            
            logger.info("Autenticação completada com sucesso")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao completar autenticação: {e}")
            return False
    
    def is_authenticated(self) -> bool:
        """Verifica se está autenticado"""
        return self.dbx is not None
    
    def list_files(self, path: str = '') -> List[Dict]:
        """
        Lista arquivos no Dropbox
        
        Args:
            path: Caminho no Dropbox (vazio para raiz)
            
        Returns:
            Lista de arquivos e pastas
        """
        if not self.is_authenticated():
            logger.error("Não autenticado no Dropbox")
            return []
        
        try:
            result = self.dbx.files_list_folder(path)
            files = []
            
            for entry in result.entries:
                if isinstance(entry, dropbox.files.FileMetadata):
                    files.append({
                        'name': entry.name,
                        'path': entry.path_display,
                        'size': entry.size,
                        'modified': entry.client_modified.isoformat() if entry.client_modified else None,
                        'type': 'file'
                    })
                elif isinstance(entry, dropbox.files.FolderMetadata):
                    files.append({
                        'name': entry.name,
                        'path': entry.path_display,
                        'type': 'folder'
                    })
            
            return files
            
        except Exception as e:
            logger.error(f"Erro ao listar arquivos: {e}")
            return []
    
    def download_file(self, dropbox_path: str, local_path: str) -> bool:
        """
        Baixa arquivo do Dropbox
        
        Args:
            dropbox_path: Caminho do arquivo no Dropbox
            local_path: Caminho local onde salvar o arquivo
            
        Returns:
            True se download foi bem sucedido
        """
        if not self.is_authenticated():
            logger.error("Não autenticado no Dropbox")
            return False
        
        try:
            # Garante que o diretório local existe
            local_file = Path(local_path)
            local_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Baixa arquivo
            self.dbx.files_download_to_file(str(local_file), dropbox_path)
            logger.info(f"Arquivo baixado com sucesso: {local_path}")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao baixar arquivo: {e}")
            return False
    
    def import_file(self, dropbox_path: str, destination_dir: Optional[str] = None) -> Optional[str]:
        """
        Importa arquivo do Dropbox para o sistema local
        
        Args:
            dropbox_path: Caminho do arquivo no Dropbox
            destination_dir: Diretório de destino (padrão: Downloads)
            
        Returns:
            Caminho do arquivo baixado ou None se falhou
        """
        if not destination_dir:
            destination_dir = str(Path.home() / 'Downloads' / 'PCVitalBoost')
        
        # Extrai nome do arquivo do caminho
        filename = Path(dropbox_path).name
        local_path = os.path.join(destination_dir, filename)
        
        if self.download_file(dropbox_path, local_path):
            return local_path
        
        return None
    
    def get_account_info(self) -> Optional[Dict]:
        """
        Obtém informações da conta Dropbox
        
        Returns:
            Dicionário com informações da conta
        """
        if not self.is_authenticated():
            logger.error("Não autenticado no Dropbox")
            return None
        
        try:
            account = self.dbx.users_get_current_account()
            return {
                'name': account.name.display_name,
                'email': account.email,
                'account_id': account.account_id
            }
        except Exception as e:
            logger.error(f"Erro ao obter informações da conta: {e}")
            return None
    
    def disconnect(self):
        """Desconecta e remove credenciais salvas"""
        try:
            if self.config_file.exists():
                self.config_file.unlink()
            self.access_token = None
            self.dbx = None
            logger.info("Desconectado do Dropbox")
        except Exception as e:
            logger.error(f"Erro ao desconectar: {e}")
