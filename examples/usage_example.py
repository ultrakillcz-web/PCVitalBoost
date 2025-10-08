#!/usr/bin/env python3
"""
Exemplo de uso dos módulos do PCVitalBoost
Este script demonstra como usar cada módulo programaticamente
"""

import sys
import os

# Adiciona o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.modules import (
    DriverUpdater,
    ProgramUpdater,
    SystemOptimizer,
    SystemCleaner
)
from src.auto_updater import AutoUpdater


def example_driver_updates():
    """Exemplo: Verificar e atualizar drivers"""
    print("\n=== Verificando Drivers ===")
    
    updater = DriverUpdater()
    drivers = updater.check_drivers()
    
    print(f"Drivers encontrados: {len(drivers)}")
    
    # Para atualizar um driver específico:
    # for driver in drivers:
    #     updater.update_driver(driver)


def example_program_updates():
    """Exemplo: Verificar e atualizar programas"""
    print("\n=== Verificando Programas ===")
    
    updater = ProgramUpdater()
    programs = updater.check_programs()
    
    print(f"Programas para atualizar: {len(programs)}")


def example_system_optimization():
    """Exemplo: Otimizar sistema"""
    print("\n=== Otimizando Sistema ===")
    
    optimizer = SystemOptimizer()
    
    # Obter informações do sistema
    info = optimizer.get_system_info()
    print(f"CPU: {info['cpu_percent']}%")
    print(f"Memória: {info['memory_percent']}%")
    print(f"Disco: {info['disk_usage']}%")
    
    # Otimizar memória
    result = optimizer.optimize_memory()
    print(f"Otimização de memória: {result['message']}")


def example_system_cleanup():
    """Exemplo: Limpar sistema"""
    print("\n=== Limpando Sistema ===")
    
    cleaner = SystemCleaner()
    
    # Escanear arquivos desnecessários
    junk = cleaner.scan_for_junk()
    total_mb = junk['total_size'] / (1024**2)
    print(f"Arquivos desnecessários encontrados: {total_mb:.2f} MB")
    
    # Para limpar (descomente com cuidado):
    # result = cleaner.clean_temp_files()
    # print(f"Limpeza: {result['message']}")


def example_auto_update():
    """Exemplo: Verificar atualizações do app"""
    print("\n=== Verificando Atualizações ===")
    
    updater = AutoUpdater(current_version='1.0.0')
    update_info = updater.check_for_updates()
    
    if update_info and update_info.get('available'):
        print(f"Nova versão disponível: {update_info['version']}")
    else:
        print("Aplicativo atualizado!")


def main():
    """Função principal"""
    print("PCVitalBoost - Exemplos de Uso")
    print("=" * 50)
    
    # Executar exemplos
    example_driver_updates()
    example_program_updates()
    example_system_optimization()
    example_system_cleanup()
    example_auto_update()
    
    print("\n" + "=" * 50)
    print("Exemplos concluídos!")


if __name__ == '__main__':
    main()
