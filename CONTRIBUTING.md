# Contribuindo para o PCVitalBoost

Obrigado por considerar contribuir para o PCVitalBoost! 🎉

## Como Contribuir

### Reportando Bugs

Se você encontrar um bug:

1. Verifique se já existe uma [issue](https://github.com/ultrakillcz-web/PCVitalBoost/issues) aberta
2. Se não, crie uma nova issue com:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs atual
   - Screenshots (se aplicável)
   - Informações do sistema (SO, versão do Python, etc.)

### Sugerindo Melhorias

Para sugerir novas funcionalidades:

1. Abra uma [issue](https://github.com/ultrakillcz-web/PCVitalBoost/issues)
2. Use o prefixo `[FEATURE]` no título
3. Descreva detalhadamente a funcionalidade
4. Explique o valor que ela traria

### Enviando Pull Requests

1. **Fork** o repositório
2. **Clone** seu fork:
   ```bash
   git clone https://github.com/SEU_USUARIO/PCVitalBoost.git
   ```
3. Crie uma **branch** para sua feature:
   ```bash
   git checkout -b feature/minha-feature
   ```
4. Faça suas alterações
5. **Commit** com mensagens claras:
   ```bash
   git commit -m "Adiciona funcionalidade X"
   ```
6. **Push** para seu fork:
   ```bash
   git push origin feature/minha-feature
   ```
7. Abra um **Pull Request**

## Padrões de Código

### Python

- Siga a [PEP 8](https://pep8.org/)
- Use docstrings para documentar funções e classes
- Mantenha funções pequenas e focadas
- Escreva código legível e autoexplicativo

### Exemplo de Docstring

```python
def minha_funcao(param1, param2):
    """
    Breve descrição da função
    
    Args:
        param1 (tipo): Descrição do parâmetro 1
        param2 (tipo): Descrição do parâmetro 2
        
    Returns:
        tipo: Descrição do retorno
    """
    pass
```

### Commits

Use mensagens de commit claras e descritivas:

- `feat: Adiciona nova funcionalidade X`
- `fix: Corrige bug em Y`
- `docs: Atualiza documentação`
- `refactor: Refatora módulo Z`
- `test: Adiciona testes para W`

## Estrutura do Projeto

```
PCVitalBoost/
├── src/                    # Código fonte
│   ├── modules/           # Módulos principais
│   └── ui/                # Interface gráfica
├── tests/                 # Testes (a ser criado)
├── docs/                  # Documentação adicional
└── requirements.txt       # Dependências
```

## Desenvolvimento

### Configurar Ambiente

```bash
# Clone o repositório
git clone https://github.com/ultrakillcz-web/PCVitalBoost.git
cd PCVitalBoost

# Crie ambiente virtual
python -m venv venv

# Ative o ambiente
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Instale dependências
pip install -r requirements.txt
```

### Executar Testes

```bash
# Quando os testes estiverem implementados
python -m pytest tests/
```

### Executar Linter

```bash
# Instale flake8
pip install flake8

# Execute verificação
flake8 src/
```

## Checklist do Pull Request

Antes de submeter seu PR, verifique:

- [ ] Código segue os padrões do projeto
- [ ] Documentação foi atualizada (se necessário)
- [ ] Testes passam (quando implementados)
- [ ] Sem warnings do linter
- [ ] Commit messages são claros
- [ ] PR tem descrição detalhada

## Código de Conduta

- Seja respeitoso e profissional
- Aceite críticas construtivas
- Foque no que é melhor para o projeto
- Seja colaborativo e prestativo

## Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob a LGPL-2.1.

## Dúvidas?

Não hesite em abrir uma issue ou entrar em contato!

---

Obrigado por contribuir! 🚀
