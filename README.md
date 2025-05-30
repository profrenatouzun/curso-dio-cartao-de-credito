# Identificador de Bandeiras de Cartão de Crédito

Este projeto é uma aplicação Python que identifica a bandeira de cartões de crédito com base no número do cartão. O sistema é capaz de identificar as principais bandeiras como Visa, MasterCard, American Express, entre outras.

## Funcionalidades

- Identificação automática da bandeira do cartão de crédito
- Validação do número do cartão
- Suporte para múltiplas bandeiras (Visa, MasterCard, American Express, etc.)

## Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:
```bash
git clone [seu-repositorio]
cd [nome-do-diretorio]
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como usar

```python
from credit_card_identifier import identify_card_brand

# Exemplo de uso
card_number = "4532123456788901"
brand = identify_card_brand(card_number)
print(f"A bandeira do cartão é: {brand}")
```

## Estrutura do Projeto

```
.
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── credit_card_identifier.py
└── tests/
    ├── __init__.py
    └── test_credit_card_identifier.py
```

## Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes. 