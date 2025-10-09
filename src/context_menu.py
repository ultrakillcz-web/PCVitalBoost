"""
Integração com menu de contexto do sistema operacional
Adiciona atalhos no botão direito do mouse
"""
import platform
import os
import sys
import logging
import winreg  # Para Windows

logger = logging.getLogger(__name__)


class ContextMenuIntegration:
    """Classe para integrar com menu de contexto do sistema"""
    
    def __init__(self):
        self.system = platform.system()
        self.app_path = os.path.abspath(sys.argv[0])
        
    def add_context_menu(self):
        """
        Adiciona atalhos ao menu de contexto
        
        Returns:
            bool: True se bem-sucedido
        """
        if self.system == "Windows":
            return self._add_windows_context_menu()
        elif self.system == "Linux":
            return self._add_linux_context_menu()
        elif self.system == "Darwin":
            return self._add_macos_context_menu()
        return False
    
    def _add_windows_context_menu(self):
        """Adiciona menu de contexto no Windows"""
        try:
            # Adiciona entrada no registro do Windows
            key_path = r"Directory\\Background\\shell\\PCVitalBoost"
            
            # Cria chave principal
            key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
            winreg.SetValue(key, "", winreg.REG_SZ, "Otimizar com PCVitalBoost")
            winreg.CloseKey(key)
            
            # Cria comando
            command_path = f"{key_path}\\command"
            key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, command_path)
            winreg.SetValue(key, "", winreg.REG_SZ, f'"{self.app_path}"')
            winreg.CloseKey(key)
            
            logger.info("Menu de contexto adicionado com sucesso no Windows")
            return True
            
        except Exception as e:
            logger.error(f"Erro ao adicionar menu de contexto no Windows: {e}")
            return False
    
    def _add_linux_context_menu(self):
        """Adiciona menu de contexto no Linux"""
        # Para Linux, depende do gerenciador de arquivos (Nautilus, Dolphin, etc.)
        logger.info("Integração de menu de contexto no Linux requer configuração manual")
        return True
    
    def _add_macos_context_menu(self):
        """Adiciona menu de contexto no macOS"""
        # Para macOS, usa Automator ou serviços
        logger.info("Integração de menu de contexto no macOS requer configuração manual")
        return True
    
    def remove_context_menu(self):
        """
        Remove atalhos do menu de contexto
        
        Returns:
            bool: True se bem-sucedido
        """
        if self.system == "Windows":
            try:
                key_path = r"Directory\\Background\\shell\\PCVitalBoost"
                winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, f"{key_path}\\command")
                winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, key_path)
                logger.info("Menu de contexto removido com sucesso")
                return True
            except Exception as e:
                logger.error(f"Erro ao remover menu de contexto: {e}")
                return False
        return True
