# Importação de Arquivos do Dropbox

O PCVitalBoost agora suporta importação de arquivos diretamente do Dropbox, permitindo que você acesse e importe arquivos de configuração, backups ou outros dados armazenados na nuvem.

## Pré-requisitos

1. **Instalar o SDK do Dropbox**:
   ```bash
   pip install dropbox
   ```

2. **Criar uma aplicação Dropbox** (apenas para desenvolvedores ou uso avançado):
   - Acesse [Dropbox App Console](https://www.dropbox.com/developers/apps)
   - Clique em "Create app"
   - Escolha "Scoped access"
   - Escolha "Full Dropbox" ou "App folder"
   - Dê um nome para sua aplicação
   - Após criar, você terá acesso ao `App key` e `App secret`

3. **Configurar credenciais**:
   
   Você pode configurar as credenciais de duas formas:
   
   **Opção 1: Variáveis de ambiente** (recomendado)
   ```bash
   # Linux/macOS
   export DROPBOX_APP_KEY="sua_chave_aqui"
   export DROPBOX_APP_SECRET="seu_segredo_aqui"
   
   # Windows
   set DROPBOX_APP_KEY=sua_chave_aqui
   set DROPBOX_APP_SECRET=seu_segredo_aqui
   ```
   
   **Opção 2: Passar diretamente no código**
   ```python
   from src.modules import DropboxImporter
   importer = DropboxImporter(
       app_key='sua_chave',
       app_secret='seu_segredo'
   )
   ```

## Uso Básico

### Via Interface Gráfica

1. Execute o PCVitalBoost
2. Clique no botão "Importar do Dropbox"
3. Se for a primeira vez, você será direcionado para autenticar sua conta Dropbox
4. Após a autenticação, seus arquivos serão listados
5. Selecione um arquivo para importar

### Via Código Python

```python
from src.modules import DropboxImporter

# Criar instância
importer = DropboxImporter()

# Autenticar (primeira vez)
if not importer.is_authenticated():
    importer.authenticate()  # Abre navegador
    # Obtenha o código de autorização do navegador
    auth_code = input("Cole o código: ")
    importer.complete_authentication(auth_code)

# Listar arquivos
files = importer.list_files()
for file in files:
    print(f"{file['name']} ({file['type']})")

# Importar arquivo
local_path = importer.import_file('/caminho/arquivo.txt')
print(f"Arquivo salvo em: {local_path}")

# Obter informações da conta
account = importer.get_account_info()
print(f"Conectado como: {account['name']}")

# Desconectar
importer.disconnect()
```

## Recursos

### Autenticação
- **OAuth2**: Processo seguro de autenticação
- **Token persistente**: Após autenticar uma vez, o token é salvo em `~/.pcvitalboost/dropbox_config.json`
- **Renovação automática**: Token renovado automaticamente quando necessário

### Operações Disponíveis

#### 1. Listar Arquivos
```python
files = importer.list_files(path='')  # '' = raiz
# Retorna lista de dicionários com:
# - name: nome do arquivo/pasta
# - path: caminho completo
# - type: 'file' ou 'folder'
# - size: tamanho em bytes (apenas arquivos)
# - modified: data de modificação (apenas arquivos)
```

#### 2. Baixar Arquivo
```python
success = importer.download_file(
    dropbox_path='/meu_arquivo.txt',
    local_path='/home/user/Downloads/meu_arquivo.txt'
)
```

#### 3. Importar Arquivo
```python
# Importa para ~/Downloads/PCVitalBoost por padrão
local_path = importer.import_file('/meu_arquivo.txt')

# Ou especificar destino
local_path = importer.import_file(
    '/meu_arquivo.txt',
    destination_dir='/caminho/customizado'
)
```

#### 4. Informações da Conta
```python
account = importer.get_account_info()
# Retorna:
# - name: nome do usuário
# - email: email da conta
# - account_id: ID da conta
```

#### 5. Verificar Autenticação
```python
if importer.is_authenticated():
    print("Autenticado!")
else:
    print("Necessário autenticar")
```

#### 6. Desconectar
```python
importer.disconnect()  # Remove token salvo
```

## Exemplo Completo

Veja o arquivo `examples/dropbox_import_example.py` para um exemplo completo e interativo.

Para executá-lo:
```bash
python examples/dropbox_import_example.py
```

## Segurança

- **Tokens seguros**: Armazenados em arquivo local protegido
- **OAuth2**: Processo de autenticação padrão da indústria
- **Sem senha**: Nunca armazenamos sua senha do Dropbox
- **Permissões limitadas**: Apenas acesso aos arquivos conforme configurado na aplicação

## Solução de Problemas

### Erro: "Dropbox SDK não está instalado"
**Solução**: Execute `pip install dropbox`

### Erro: "DROPBOX_APP_KEY não configurada"
**Solução**: Configure as variáveis de ambiente ou passe as credenciais diretamente

### Erro: "Não autenticado no Dropbox"
**Solução**: Execute o processo de autenticação chamando `authenticate()` e `complete_authentication()`

### Token expirado
**Solução**: O token é automaticamente renovado. Se persistir, desconecte e autentique novamente:
```python
importer.disconnect()
importer.authenticate()
```

## Limitações

- Requer conexão com internet
- Tamanho máximo de arquivo depende da sua conta Dropbox
- Taxa de requisições limitada pela API do Dropbox

## Referências

- [Documentação da API Dropbox](https://www.dropbox.com/developers/documentation)
- [Dropbox Python SDK](https://github.com/dropbox/dropbox-sdk-python)
- [OAuth 2.0](https://oauth.net/2/)
