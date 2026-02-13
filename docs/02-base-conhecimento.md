# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato |Para que serve no Edu?|
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, ou seja, dar continuidade ao atendente de forma mais eficiente. |
| `perfil_investidor.json` | JSON | Personalizar explicações sobre as dúvidas e necessidades de aprendizado do cliente|
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponiveis para que eles possam ser ensinados ao cliente. |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar essas informações de forma didática. |

---

## Estratégia de Integração

### Como os dados são carregados?

```python
import pandas as pd
import json

historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

with open('data/perfil_investidor.json', 'r', encoding = 'utf-8') as f:
    perfil = json.load(f)
with open('data/produtos_financeiros.json', 'r', encoding = 'utf-8') as f:
    produtos = json.load(f)

```
### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```text

DADOS DO CLIENTE:
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSACOES DO CLIENTE:

HISTÓRICO DE ATENDIMENTO DO CLIENTE:

PRODUTOS DISPONÍVEIS PARA ENSINO:

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
