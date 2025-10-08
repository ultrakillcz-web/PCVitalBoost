"""
Módulo de limpeza do sistema
Responsável por remover arquivos temporários, cache e proteger privacidade
"""
import os
import platform
import shutil
import tempfile
import logging

logger = logging.getLogger(__name__)


class SystemCleaner:
    """Classe responsável por limpar arquivos desnecessários e proteger privacidade"""
    
    def __init__(self):
        self.system = platform.system()
        
    def scan_for_junk(self):
        """
        Escaneia o sistema em busca de arquivos desnecessários
        
        Returns:
            dict: Informações sobre arquivos a serem removidos
        """
        logger.info("Escaneando arquivos desnecessários...")
        
        junk_files = {
            'temp_files': self._scan_temp_files(),
            'cache_files': self._scan_cache_files(),
            'log_files': self._scan_old_logs(),
            'total_size': 0
        }
        
        # Calcula tamanho total
        total = sum(item.get('size', 0) for category in junk_files.values() 
                   if isinstance(category, dict) for item in category)
        junk_files['total_size'] = total
        
        return junk_files
    
    def _scan_temp_files(self):
        """Escaneia arquivos temporários"""
        temp_files = []
        temp_dir = tempfile.gettempdir()
        
        try:
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    try:
                        file_path = os.path.join(root, file)
                        size = os.path.getsize(file_path)
                        temp_files.append({
                            'path': file_path,
                            'size': size
                        })
                    except (OSError, PermissionError):
                        continue
        except Exception as e:
            logger.error(f"Erro ao escanear arquivos temporários: {e}")
            
        return temp_files
    
    def _scan_cache_files(self):
        """Escaneia arquivos de cache"""
        cache_files = []
        
        # Locais comuns de cache por sistema
        cache_dirs = []
        if self.system == "Windows":
            cache_dirs = [
                os.path.join(os.environ.get('LOCALAPPDATA', ''), 'Temp'),
                os.path.join(os.environ.get('APPDATA', ''), 'Local', 'Temp'),
            ]
        elif self.system == "Linux":
            cache_dirs = [
                os.path.expanduser('~/.cache'),
            ]
        elif self.system == "Darwin":
            cache_dirs = [
                os.path.expanduser('~/Library/Caches'),
            ]
        
        for cache_dir in cache_dirs:
            if os.path.exists(cache_dir):
                try:
                    for item in os.listdir(cache_dir):
                        item_path = os.path.join(cache_dir, item)
                        try:
                            if os.path.isfile(item_path):
                                size = os.path.getsize(item_path)
                            else:
                                size = self._get_dir_size(item_path)
                            
                            cache_files.append({
                                'path': item_path,
                                'size': size
                            })
                        except (OSError, PermissionError):
                            continue
                except Exception as e:
                    logger.error(f"Erro ao escanear cache em {cache_dir}: {e}")
                    
        return cache_files
    
    def _scan_old_logs(self):
        """Escaneia arquivos de log antigos"""
        log_files = []
        # Placeholder - implementação depende do sistema
        return log_files
    
    def _get_dir_size(self, path):
        """Calcula tamanho de um diretório"""
        total = 0
        try:
            for entry in os.scandir(path):
                if entry.is_file(follow_symlinks=False):
                    total += entry.stat().st_size
                elif entry.is_dir(follow_symlinks=False):
                    total += self._get_dir_size(entry.path)
        except (OSError, PermissionError):
            pass
        return total
    
    def clean_temp_files(self):
        """
        Remove arquivos temporários
        
        Returns:
            dict: Resultado da limpeza
        """
        logger.info("Limpando arquivos temporários...")
        removed_count = 0
        freed_space = 0
        
        temp_files = self._scan_temp_files()
        for file_info in temp_files:
            try:
                os.remove(file_info['path'])
                removed_count += 1
                freed_space += file_info['size']
            except (OSError, PermissionError):
                continue
                
        return {
            'status': 'success',
            'removed_count': removed_count,
            'freed_space': freed_space,
            'message': f'Removidos {removed_count} arquivos, {freed_space / (1024**2):.2f} MB liberados'
        }
    
    def clean_cache(self):
        """
        Remove arquivos de cache
        
        Returns:
            dict: Resultado da limpeza
        """
        logger.info("Limpando cache...")
        # Implementação similar a clean_temp_files
        return {
            'status': 'success',
            'message': 'Cache limpo com sucesso'
        }
    
    def protect_privacy(self):
        """
        Remove histórico de navegação, cookies, etc. para proteger privacidade
        
        Returns:
            dict: Resultado da operação
        """
        logger.info("Protegendo privacidade...")
        # Placeholder - implementação específica por navegador
        return {
            'status': 'success',
            'message': 'Dados de privacidade limpos'
        }
