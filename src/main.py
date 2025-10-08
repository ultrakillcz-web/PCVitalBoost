#!/usr/bin/env python3
"""
PCVitalBoost - Aplicativo multiplataforma para otimização de PC
Ponto de entrada principal do aplicativo
"""
import os
import sys
import logging
from pathlib import Path

# Configura logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('pcvitalboost.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


def main():
    """Função principal do aplicativo"""
    logger.info("Iniciando PCVitalBoost...")
    
    try:
        # Importa a UI
        from src.ui import PCVitalBoostUI
        
        # Inicia o aplicativo
        app = PCVitalBoostUI()
        app.run()
        
    except Exception as e:
        logger.error(f"Erro ao iniciar aplicativo: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
