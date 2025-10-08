# PCVitalBoost

Aplicativo multiplataforma (PC, Android, iOS) para atualização de drivers/programas, otimização de desempenho e limpeza do computador.

## 🚀 Características

- **Multiplataforma**: Funciona em Windows, macOS, Linux, Android e iOS
- **Atualização de Drivers**: Verifica e atualiza drivers do sistema automaticamente
- **Atualização de Programas**: Mantém todos os seus programas atualizados
- **Otimização de Desempenho**: Melhora a velocidade e eficiência do sistema
- **Limpeza Inteligente**: Remove arquivos desnecessários e protege sua privacidade
- **Interface Intuitiva**: Design simples e fácil de usar
- **Sem Anúncios**: 100% livre de propagandas
- **Atualização Automática**: Mantém o aplicativo sempre atualizado
- **Integração com Sistema**: Atalhos no menu de contexto (botão direito)
- **Seguro e Eficiente**: Desenvolvido com foco em segurança e desempenho

## 📋 Funcionalidades

### 1. Atualização de Drivers
- Escaneia drivers desatualizados
- Baixa e instala atualizações automaticamente
- Suporte para Windows, Linux e macOS

### 2. Atualização de Programas
- Verifica programas instalados
- Identifica versões desatualizadas
- Facilita o processo de atualização

### 3. Otimização do Sistema
- Analisa uso de CPU e memória
- Otimiza programas de inicialização
- Melhora desempenho geral do sistema
- Informações detalhadas do sistema

### 4. Limpeza e Privacidade
- Remove arquivos temporários
- Limpa cache de aplicativos
- Exclui logs antigos
- Protege privacidade removendo dados sensíveis
- Calcula espaço que pode ser liberado

## 🛠️ Instalação

### Requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação via pip

```bash
# Clone o repositório
git clone https://github.com/ultrakillcz-web/PCVitalBoost.git
cd PCVitalBoost

# Instale as dependências
pip install -r requirements.txt

# Execute o aplicativo
python src/main.py
```

### Instalação via setup.py

```bash
# Clone o repositório
git clone https://github.com/ultrakillcz-web/PCVitalBoost.git
cd PCVitalBoost

# Instale o aplicativo
pip install .

# Execute
pcvitalboost
```

## 📱 Build para Diferentes Plataformas

### Windows, macOS, Linux (Desktop)

Use PyInstaller para criar executáveis:

```bash
# Instale PyInstaller
pip install pyinstaller

# Crie o executável
pyinstaller PCVitalBoost.spec

# O executável estará em dist/PCVitalBoost
```

### Android

Use Buildozer para criar APK:

```bash
# Instale Buildozer (Linux/macOS)
pip install buildozer

# Instale dependências do Android SDK
# Veja: https://buildozer.readthedocs.io/

# Build APK
buildozer android debug

# O APK estará em bin/
```

### iOS

Use Buildozer ou Kivy iOS tools:

```bash
# Requer macOS com Xcode instalado
# Veja: https://kivy.org/doc/stable/guide/packaging-ios.html

buildozer ios debug
```

## 🎯 Uso

### Interface Gráfica

Execute o aplicativo e use a interface intuitiva:

1. **Tela Principal**: Visualize informações do sistema
2. **Atualizar Drivers**: Clique para verificar e atualizar drivers
3. **Atualizar Programas**: Clique para verificar atualizações de software
4. **Otimizar Sistema**: Melhore o desempenho do seu PC
5. **Limpar Sistema**: Remova arquivos desnecessários

### Menu de Contexto

Após a instalação, você pode:
- Clicar com botão direito em áreas vazias do Windows Explorer
- Selecionar "Otimizar com PCVitalBoost"
- O aplicativo será executado automaticamente

## 🏗️ Estrutura do Projeto

```
PCVitalBoost/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Ponto de entrada principal
│   ├── auto_updater.py         # Sistema de atualização automática
│   ├── context_menu.py         # Integração com menu de contexto
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── driver_updater.py   # Atualização de drivers
│   │   ├── program_updater.py  # Atualização de programas
│   │   ├── system_optimizer.py # Otimização do sistema
│   │   └── system_cleaner.py   # Limpeza e privacidade
│   └── ui/
│       ├── __init__.py
│       └── main_window.py      # Interface gráfica
├── requirements.txt            # Dependências Python
├── setup.py                    # Instalação do pacote
├── buildozer.spec             # Configuração para Android/iOS
├── PCVitalBoost.spec          # Configuração PyInstaller
├── LICENSE                     # Licença LGPL 2.1
└── README.md                   # Este arquivo
```

## 🔧 Desenvolvimento

### Configurar Ambiente de Desenvolvimento

```bash
# Clone o repositório
git clone https://github.com/ultrakillcz-web/PCVitalBoost.git
cd PCVitalBoost

# Crie ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Instale dependências de desenvolvimento
pip install -r requirements.txt
```

### Executar em Modo de Desenvolvimento

```bash
python src/main.py
```

## 📄 Licença

Este projeto está licenciado sob a GNU Lesser General Public License v2.1 (LGPL-2.1).
Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para suporte, abra uma [issue](https://github.com/ultrakillcz-web/PCVitalBoost/issues) no GitHub.

## ⚠️ Avisos Importantes

- **Backup**: Sempre faça backup de dados importantes antes de usar ferramentas de limpeza
- **Permissões**: O aplicativo pode requerer permissões de administrador para algumas operações
- **Privacidade**: Nenhum dado é coletado ou enviado para servidores externos
- **Segurança**: Use apenas em sistemas que você possui ou tem permissão para modificar

## 🎨 Capturas de Tela

_(Capturas de tela serão adicionadas após o desenvolvimento da interface)_

## 🗺️ Roadmap

- [x] Estrutura básica do projeto
- [x] Módulo de atualização de drivers
- [x] Módulo de atualização de programas
- [x] Módulo de otimização do sistema
- [x] Módulo de limpeza e privacidade
- [x] Interface gráfica básica
- [x] Sistema de atualização automática
- [x] Integração com menu de contexto
- [ ] Testes unitários
- [ ] Testes de integração
- [ ] Build para Android
- [ ] Build para iOS
- [ ] Sistema de notificações
- [ ] Agendamento de tarefas
- [ ] Relatórios detalhados
- [ ] Suporte multilíngue

---

Desenvolvido com ❤️ pela equipe PCVitalBoost
