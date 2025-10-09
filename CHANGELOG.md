# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.0.0] - 2024

### Adicionado
- Estrutura inicial do projeto multiplataforma
- Módulo de atualização de drivers (`driver_updater.py`)
- Módulo de atualização de programas (`program_updater.py`)
- Módulo de otimização de sistema (`system_optimizer.py`)
- Módulo de limpeza e proteção de privacidade (`system_cleaner.py`)
- Interface gráfica com Kivy/KivyMD (`main_window.py`)
- Sistema de atualização automática (`auto_updater.py`)
- Integração com menu de contexto do sistema (`context_menu.py`)
- Ponto de entrada principal (`main.py`)
- Arquivos de configuração:
  - `requirements.txt` - Dependências Python
  - `setup.py` - Setup do pacote
  - `buildozer.spec` - Build Android/iOS
  - `PCVitalBoost.spec` - Build desktop com PyInstaller
  - `config.json` - Configurações do aplicativo
- Scripts de execução:
  - `run.sh` - Linux/macOS
  - `run.bat` - Windows
- Documentação:
  - `README.md` - Documentação principal
  - `INSTALL.md` - Guia de instalação
  - `CONTRIBUTING.md` - Guia para contribuidores
  - `docs/API.md` - Documentação da API
  - `docs/FAQ.md` - Perguntas frequentes
  - `CHANGELOG.md` - Este arquivo
- Exemplos de uso (`examples/usage_example.py`)

### Funcionalidades Principais
- ✅ Verificação e atualização de drivers
- ✅ Verificação e atualização de programas
- ✅ Otimização de memória RAM
- ✅ Otimização de inicialização do sistema
- ✅ Limpeza de arquivos temporários
- ✅ Limpeza de cache
- ✅ Proteção de privacidade
- ✅ Informações detalhadas do sistema
- ✅ Interface gráfica intuitiva
- ✅ Suporte multiplataforma (Windows, macOS, Linux, Android, iOS)
- ✅ Sistema de atualização automática
- ✅ Integração com menu de contexto

### Segurança
- Sem coleta de dados
- Sem telemetria
- Sem anúncios
- Código aberto
- Licença LGPL-2.1

---

## [Futuro] - Roadmap

### Planejado para v1.1.0
- [ ] Testes unitários completos
- [ ] Testes de integração
- [ ] Sistema de notificações
- [ ] Agendamento de tarefas
- [ ] Melhorias na UI
- [ ] Tema escuro
- [ ] Builds oficiais para todas as plataformas

### Planejado para v1.2.0
- [ ] Suporte multilíngue (inglês, espanhol)
- [ ] Relatórios detalhados de otimização
- [ ] Histórico de operações
- [ ] Backup e restauração de configurações
- [ ] Modo portátil (sem instalação)

### Planejado para v2.0.0
- [ ] Análise avançada de performance
- [ ] Recomendações inteligentes
- [ ] Perfis de otimização (Gaming, Trabalho, etc.)
- [ ] Integração com serviços em nuvem
- [ ] API REST para automação

---

[1.0.0]: https://github.com/ultrakillcz-web/PCVitalBoost/releases/tag/v1.0.0
