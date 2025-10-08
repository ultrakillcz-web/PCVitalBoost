# Guia de Instalação - PCVitalBoost

## Instalação no Windows

### Método 1: Executável Standalone (Recomendado)

1. Baixe o arquivo `PCVitalBoost.exe` da [página de releases](https://github.com/ultrakillcz-web/PCVitalBoost/releases)
2. Execute o arquivo baixado
3. Siga as instruções do instalador

### Método 2: Instalação via Python

1. Instale Python 3.8+ do [site oficial](https://www.python.org/downloads/)
2. Abra o Prompt de Comando
3. Execute:
   ```cmd
   pip install git+https://github.com/ultrakillcz-web/PCVitalBoost.git
   pcvitalboost
   ```

## Instalação no macOS

### Via Python

1. Instale Python 3.8+ (pode usar Homebrew: `brew install python`)
2. Abra o Terminal
3. Execute:
   ```bash
   pip3 install git+https://github.com/ultrakillcz-web/PCVitalBoost.git
   pcvitalboost
   ```

## Instalação no Linux

### Ubuntu/Debian

```bash
# Instale dependências
sudo apt update
sudo apt install python3 python3-pip

# Instale o PCVitalBoost
pip3 install git+https://github.com/ultrakillcz-web/PCVitalBoost.git

# Execute
pcvitalboost
```

### Fedora/RHEL

```bash
# Instale dependências
sudo dnf install python3 python3-pip

# Instale o PCVitalBoost
pip3 install git+https://github.com/ultrakillcz-web/PCVitalBoost.git

# Execute
pcvitalboost
```

### Arch Linux

```bash
# Instale dependências
sudo pacman -S python python-pip

# Instale o PCVitalBoost
pip install git+https://github.com/ultrakillcz-web/PCVitalBoost.git

# Execute
pcvitalboost
```

## Instalação no Android

1. Baixe o arquivo APK da [página de releases](https://github.com/ultrakillcz-web/PCVitalBoost/releases)
2. Habilite "Fontes Desconhecidas" nas configurações de segurança
3. Instale o APK baixado

## Instalação no iOS

1. Baixe o aplicativo da App Store (quando disponível)
2. Ou use TestFlight para versões beta

## Verificação da Instalação

Após instalar, execute:

```bash
pcvitalboost --version
```

Você deve ver a versão do PCVitalBoost instalada.

## Problemas Comuns

### Windows: "Python não é reconhecido como comando"

Reinstale o Python e marque a opção "Add Python to PATH" durante a instalação.

### Linux/macOS: "Permission denied"

Execute o comando de instalação com `--user`:

```bash
pip3 install --user git+https://github.com/ultrakillcz-web/PCVitalBoost.git
```

### Erro de dependências

Atualize o pip:

```bash
pip install --upgrade pip
```

## Desinstalação

```bash
pip uninstall pcvitalboost
```

Para mais informações, consulte a [documentação completa](README.md).
