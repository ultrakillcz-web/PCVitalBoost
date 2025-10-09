# API Documentation - PCVitalBoost

## Módulos Principais

### driver_updater.py

#### Classe: DriverUpdater

Responsável por verificar e atualizar drivers do sistema.

**Métodos:**

```python
def __init__(self)
```
Inicializa o atualizador de drivers.

```python
def check_drivers(self) -> list
```
Verifica drivers desatualizados no sistema.

**Retorna:** Lista de drivers que precisam de atualização.

```python
def update_driver(self, driver_info) -> bool
```
Atualiza um driver específico.

**Parâmetros:**
- `driver_info`: Informações do driver a ser atualizado

**Retorna:** True se atualização bem-sucedida, False caso contrário.

---

### program_updater.py

#### Classe: ProgramUpdater

Responsável por verificar e atualizar programas instalados.

**Métodos:**

```python
def __init__(self)
```
Inicializa o atualizador de programas.

```python
def check_programs(self) -> list
```
Verifica programas instalados que possuem atualizações disponíveis.

**Retorna:** Lista de programas que precisam de atualização.

```python
def update_program(self, program_info) -> bool
```
Atualiza um programa específico.

**Parâmetros:**
- `program_info`: Informações do programa a ser atualizado

**Retorna:** True se atualização bem-sucedida, False caso contrário.

---

### system_optimizer.py

#### Classe: SystemOptimizer

Responsável por otimizar o desempenho do sistema.

**Métodos:**

```python
def __init__(self)
```
Inicializa o otimizador de sistema.

```python
def get_system_info(self) -> dict
```
Obtém informações do sistema.

**Retorna:** Dicionário com informações sobre CPU, memória, disco, etc.

```python
def optimize_memory(self) -> dict
```
Otimiza uso de memória RAM.

**Retorna:** Resultado da otimização.

```python
def optimize_startup(self) -> dict
```
Otimiza programas de inicialização.

**Retorna:** Resultado da otimização.

```python
def defragment_disk(self) -> dict
```
Desfragmenta disco (apenas Windows com HDD).

**Retorna:** Resultado da operação.

---

### system_cleaner.py

#### Classe: SystemCleaner

Responsável por limpar arquivos desnecessários e proteger privacidade.

**Métodos:**

```python
def __init__(self)
```
Inicializa o limpador de sistema.

```python
def scan_for_junk(self) -> dict
```
Escaneia o sistema em busca de arquivos desnecessários.

**Retorna:** Informações sobre arquivos a serem removidos.

```python
def clean_temp_files(self) -> dict
```
Remove arquivos temporários.

**Retorna:** Resultado da limpeza.

```python
def clean_cache(self) -> dict
```
Remove arquivos de cache.

**Retorna:** Resultado da limpeza.

```python
def protect_privacy(self) -> dict
```
Remove histórico de navegação, cookies, etc. para proteger privacidade.

**Retorna:** Resultado da operação.

---

### auto_updater.py

#### Classe: AutoUpdater

Classe para gerenciar atualizações automáticas do aplicativo.

**Métodos:**

```python
def __init__(self, current_version='1.0.0')
```
Inicializa o auto-atualizador.

**Parâmetros:**
- `current_version`: Versão atual do aplicativo

```python
def check_for_updates(self) -> dict
```
Verifica se há atualizações disponíveis.

**Retorna:** Informações sobre atualização disponível ou None.

```python
def download_update(self, download_url) -> bool
```
Baixa e instala atualização.

**Parâmetros:**
- `download_url`: URL para download da atualização

**Retorna:** True se download bem-sucedido.

---

### context_menu.py

#### Classe: ContextMenuIntegration

Classe para integrar com menu de contexto do sistema.

**Métodos:**

```python
def __init__(self)
```
Inicializa a integração com menu de contexto.

```python
def add_context_menu(self) -> bool
```
Adiciona atalhos ao menu de contexto.

**Retorna:** True se bem-sucedido.

```python
def remove_context_menu(self) -> bool
```
Remove atalhos do menu de contexto.

**Retorna:** True se bem-sucedido.

---

## UI Components

### main_window.py

#### Classe: MainScreen

Tela principal do aplicativo.

**Métodos:**

```python
def __init__(self, app_instance, **kwargs)
```
Inicializa a tela principal.

```python
def update_drivers(self, instance)
```
Atualiza drivers do sistema.

```python
def update_programs(self, instance)
```
Atualiza programas instalados.

```python
def optimize_system(self, instance)
```
Otimiza o sistema.

```python
def clean_system(self, instance)
```
Limpa arquivos desnecessários.

#### Classe: PCVitalBoostUI

Aplicativo principal.

**Métodos:**

```python
def build(self)
```
Constrói a interface do aplicativo.

---

## Exemplos de Uso

Veja a pasta `examples/` para exemplos de uso dos módulos.
