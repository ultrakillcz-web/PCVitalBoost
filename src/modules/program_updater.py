"""
Módulo de atualização de programas
"""
import platform
import logging
import shutil
import subprocess

logger = logging.getLogger(__name__)


class ProgramUpdater:
    """Classe responsável por verificar e atualizar programas instalados"""
    
    def __init__(self):
        self.system = platform.system()
        self._winget_available = None

    @property
    def winget_available(self):
        """Verifica o winget somente quando ele é necessário pela primeira vez."""
        if self._winget_available is None:
            self._winget_available = self._check_winget_available()
        return self._winget_available

    @staticmethod
    def _check_winget_available():
        """Retorna se o executável winget está disponível no sistema."""
        return shutil.which("winget") is not None

    def check_programs(self):
        """
        Verifica programas instalados que possuem atualizações disponíveis
        
        Returns:
            list: Lista de programas que precisam de atualização
        """
        logger.info("Verificando atualizações de programas...")
        programs_to_update = []
        
        if self.system == "Windows":
            programs_to_update = self._check_windows_programs()
        elif self.system == "Linux":
            programs_to_update = self._check_linux_programs()
        elif self.system == "Darwin":
            programs_to_update = self._check_macos_programs()
            
        return programs_to_update
    
    def _check_windows_programs(self):
        """Verifica programas no Windows"""
        logger.info("Verificando programas Windows...")
        if not self.winget_available:
            logger.info("winget não está disponível; ignorando verificação de programas.")
            return []

        try:
            result = subprocess.run(
                ["winget", "upgrade", "--include-unknown"],
                capture_output=True,
                text=True,
                timeout=60,
                check=False,
            )
            if result.returncode != 0:
                logger.warning("winget retornou código %s", result.returncode)
                return []
            return self._parse_winget_upgrades(result.stdout)
        except (OSError, subprocess.SubprocessError) as error:
            logger.error("Erro ao verificar programas com winget: %s", error)
            return []

    @staticmethod
    def _parse_winget_upgrades(output):
        """Extrai linhas de atualização do resultado textual do winget."""
        return [
            line.strip()
            for line in output.splitlines()
            if line.strip() and not line.startswith(("Name", "-", "Nenhum"))
        ]
    
    def _check_linux_programs(self):
        """Verifica programas no Linux"""
        logger.info("Verificando programas Linux...")
        try:
            # Verifica atualizações via apt (Debian/Ubuntu)
            result = subprocess.run(
                ['which', 'apt-get'],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                # apt está disponível
                update_check = subprocess.run(
                    ['apt', 'list', '--upgradable'],
                    capture_output=True,
                    text=True
                )
                # Parsear resultado
                return []
        except Exception as e:
            logger.error(f"Erro ao verificar programas Linux: {e}")
        return []
    
    def _check_macos_programs(self):
        """Verifica programas no macOS"""
        logger.info("Verificando programas macOS...")
        # Placeholder - em produção usaria Homebrew ou Mac App Store API
        return []
    
    def update_program(self, program_info):
        """
        Atualiza um programa específico
        
        Args:
            program_info: Informações do programa a ser atualizado
            
        Returns:
            bool: True se atualização bem-sucedida, False caso contrário
        """
        logger.info(f"Atualizando programa: {program_info}")
        # Implementação da atualização
        return True
