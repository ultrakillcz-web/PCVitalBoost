#!/bin/bash
# Script de inicialização do PCVitalBoost para Linux/macOS

echo "Iniciando PCVitalBoost..."

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Python 3 não encontrado. Por favor, instale Python 3.8 ou superior."
    exit 1
fi

# Verifica se as dependências estão instaladas
python3 -c "import kivy" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Instalando dependências..."
    pip3 install -r requirements.txt
fi

# Executa o aplicativo
python3 src/main.py "$@"
