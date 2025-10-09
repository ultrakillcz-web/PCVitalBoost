"""
Testes básicos para os módulos do PCVitalBoost
"""
import sys
import os
import unittest

# Adiciona o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.modules import (
    DriverUpdater,
    ProgramUpdater,
    SystemOptimizer,
    SystemCleaner
)


class TestDriverUpdater(unittest.TestCase):
    """Testes para o módulo DriverUpdater"""
    
    def setUp(self):
        self.updater = DriverUpdater()
    
    def test_initialization(self):
        """Testa inicialização do módulo"""
        self.assertIsNotNone(self.updater)
        self.assertIsNotNone(self.updater.system)
    
    def test_check_drivers(self):
        """Testa verificação de drivers"""
        drivers = self.updater.check_drivers()
        self.assertIsInstance(drivers, list)


class TestProgramUpdater(unittest.TestCase):
    """Testes para o módulo ProgramUpdater"""
    
    def setUp(self):
        self.updater = ProgramUpdater()
    
    def test_initialization(self):
        """Testa inicialização do módulo"""
        self.assertIsNotNone(self.updater)
        self.assertIsNotNone(self.updater.system)
    
    def test_check_programs(self):
        """Testa verificação de programas"""
        programs = self.updater.check_programs()
        self.assertIsInstance(programs, list)


class TestSystemOptimizer(unittest.TestCase):
    """Testes para o módulo SystemOptimizer"""
    
    def setUp(self):
        self.optimizer = SystemOptimizer()
    
    def test_initialization(self):
        """Testa inicialização do módulo"""
        self.assertIsNotNone(self.optimizer)
    
    def test_get_system_info(self):
        """Testa obtenção de informações do sistema"""
        info = self.optimizer.get_system_info()
        self.assertIsInstance(info, dict)
        self.assertIn('cpu_percent', info)
        self.assertIn('memory_percent', info)
        self.assertIn('disk_usage', info)
    
    def test_optimize_memory(self):
        """Testa otimização de memória"""
        result = self.optimizer.optimize_memory()
        self.assertIsInstance(result, dict)
        self.assertIn('status', result)
        self.assertEqual(result['status'], 'success')


class TestSystemCleaner(unittest.TestCase):
    """Testes para o módulo SystemCleaner"""
    
    def setUp(self):
        self.cleaner = SystemCleaner()
    
    def test_initialization(self):
        """Testa inicialização do módulo"""
        self.assertIsNotNone(self.cleaner)
        self.assertIsNotNone(self.cleaner.system)
    
    def test_scan_for_junk(self):
        """Testa escaneamento de arquivos desnecessários"""
        junk = self.cleaner.scan_for_junk()
        self.assertIsInstance(junk, dict)
        self.assertIn('total_size', junk)
        self.assertIn('temp_files', junk)


if __name__ == '__main__':
    unittest.main()
