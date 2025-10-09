# Perguntas Frequentes (FAQ)

## Instalação

### O aplicativo funciona em qual sistema operacional?

PCVitalBoost é multiplataforma e funciona em:
- Windows 7, 8, 10, 11
- macOS 10.14 ou superior
- Linux (Ubuntu, Debian, Fedora, Arch, etc.)
- Android 6.0 ou superior
- iOS 12 ou superior

### Preciso instalar Python?

**Desktop (Windows/Mac/Linux):**
- Se usar o executável standalone: Não
- Se instalar via pip: Sim, Python 3.8+

**Mobile (Android/iOS):**
- Não, o aplicativo já vem completo

### Como instalar no Windows sem Python?

Baixe o arquivo `.exe` da página de releases e execute. O instalador cuidará de tudo.

## Uso

### O aplicativo é seguro?

Sim! PCVitalBoost é:
- Código aberto (você pode verificar o código)
- Sem telemetria ou coleta de dados
- Sem anúncios
- Licenciado sob LGPL-2.1

### Posso perder dados usando o limpador?

O limpador remove apenas:
- Arquivos temporários
- Cache de aplicativos
- Logs antigos

Arquivos importantes (documentos, fotos, etc.) nunca são tocados. Ainda assim, recomendamos fazer backup regularmente.

### Como atualizar drivers com segurança?

O PCVitalBoost:
1. Verifica drivers compatíveis
2. Baixa apenas de fontes confiáveis
3. Cria ponto de restauração (Windows)
4. Permite reverter se necessário

### O aplicativo consome muitos recursos?

Não! PCVitalBoost é otimizado para:
- Usar menos de 100MB de RAM
- Consumo mínimo de CPU
- Executar em background sem impacto

### Precisa de internet?

Para algumas funções:
- **Sim:** Atualização de drivers/programas, auto-update
- **Não:** Limpeza, otimização, informações do sistema

## Funcionalidades

### Quais drivers podem ser atualizados?

Dependendo do sistema:
- **Windows:** Todos os drivers de hardware
- **Linux:** Drivers via gerenciador de pacotes
- **macOS:** Atualizações de sistema

### Quais programas podem ser atualizados?

- **Windows:** Programas instalados via instalador
- **Linux:** Pacotes do apt, yum, pacman, etc.
- **macOS:** Apps da App Store e Homebrew

### Como funciona a otimização?

PCVitalBoost otimiza:
1. **Memória:** Identifica e fecha processos desnecessários
2. **Inicialização:** Desabilita programas que iniciam automaticamente
3. **Disco:** Análise de uso e sugestões

### A limpeza remove vírus?

Não, PCVitalBoost não é um antivírus. Ele remove apenas arquivos desnecessários. Para proteção contra malware, use um antivírus dedicado.

## Problemas Comuns

### "Permissão negada" ao executar

**Solução:**
- Windows: Execute como Administrador
- Linux/Mac: Use `sudo` ou configure permissões

### Atualizações não funcionam

**Verificar:**
1. Conexão com internet
2. Firewall não está bloqueando
3. Permissões de administrador

### Interface não carrega

**Tente:**
1. Reinstalar dependências: `pip install -r requirements.txt --force-reinstall`
2. Atualizar drivers gráficos
3. Verificar logs em `pcvitalboost.log`

### Aplicativo trava ou congela

**Soluções:**
1. Feche outros programas pesados
2. Aumente memória virtual
3. Reporte o bug no GitHub com logs

## Privacidade

### Quais dados são coletados?

**Nenhum!** PCVitalBoost não coleta, armazena ou transmite dados pessoais.

### Onde os dados ficam armazenados?

Todos os dados ficam localmente no seu dispositivo:
- Configurações: `config.json`
- Logs: `pcvitalboost.log`

### Como remover completamente o aplicativo?

```bash
# Desinstalar via pip
pip uninstall pcvitalboost

# Remover configurações (opcional)
# Windows: %APPDATA%\PCVitalBoost
# Linux/Mac: ~/.config/pcvitalboost
```

## Desenvolvimento

### Como contribuir?

Veja [CONTRIBUTING.md](../CONTRIBUTING.md) para instruções detalhadas.

### Onde reportar bugs?

Abra uma [issue no GitHub](https://github.com/ultrakillcz-web/PCVitalBoost/issues).

### Posso usar em projetos comerciais?

Sim! A licença LGPL-2.1 permite uso comercial. Veja [LICENSE](../LICENSE) para detalhes.

### Como compilar para Android?

```bash
# Instale Buildozer
pip install buildozer

# Build APK
buildozer android debug
```

Veja [INSTALL.md](../INSTALL.md) para mais detalhes.

## Outras Perguntas

### PCVitalBoost tem vírus?

Não! É código aberto e pode ser auditado. Alguns antivírus podem dar falso positivo com executáveis Python.

### Preciso pagar?

Não! PCVitalBoost é 100% gratuito e sem anúncios.

### Tem suporte técnico?

Suporte comunitário via GitHub Issues. Contribuições são bem-vindas!

### Quando sai a próxima versão?

Acompanhe o [roadmap no README](../README.md#-roadmap) e as [releases](https://github.com/ultrakillcz-web/PCVitalBoost/releases).

---

Não encontrou sua pergunta? [Abra uma issue](https://github.com/ultrakillcz-web/PCVitalBoost/issues)!
