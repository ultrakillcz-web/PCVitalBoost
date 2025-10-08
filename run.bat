@echo off
REM Script de inicialização do PCVitalBoost para Windows

echo Iniciando PCVitalBoost...

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo Python nao encontrado. Por favor, instale Python 3.8 ou superior.
    pause
    exit /b 1
)

REM Verifica se as dependências estão instaladas
python -c "import kivy" >nul 2>&1
if errorlevel 1 (
    echo Instalando dependencias...
    pip install -r requirements.txt
)

REM Executa o aplicativo
python src\main.py %*
