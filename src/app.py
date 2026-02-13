import json
import pandas as pd
import requests
import streamlit as st

#configuracao
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

#Careegar os dados
perfil = json.load(open('/Users/user/Desktop/Edu/data/perfil_investidor.json'))
transacoes = pd.read_csv('/Users/user/Desktop/Edu/data/transacoes.csv')
historico = pd.read_csv('/Users/user/Desktop/Edu/data/historico_atendimento.csv')
produtos = json.load(open('/Users/user/Desktop/Edu/data/produtos_financeiros.json'))

#montar contexto
contexto = f"""
CLIENTE: {perfil['nome']},{perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ { perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS
{json.dumps(produtos,indent=2, ensure_ascii=False)}
"""

#system prompt
SYSTEM_PROMPT = """Voce é o Edu, umm educador financeiro amigável e didático

OBJETIVO:
Ensinar conceitos de finanças de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS:
-Nunca recomende investimentos específicos - apenas explique como funcionam;
-JAMAIS responda a perguntas fora do tema ensino de finanças pessoais.
Quando ocorrer, responda lemmbrando o seu papel de educador financeiro;
-Use os dados fornecidos para dar exemplos personalizados;
-Linguagem aimples, como se explicassse para um amigo;
-Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
-Sempre pergunte se o cliente entendeu;
-Responda de forma sucinta e direta, comm no máximo 3 parágrafos.
"""

#Chamar o Ollama
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE:
    {contexto}
    
    Pergunta: {msg}"""
    
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']
    

#interface
st.title("Olá! Sou Edu, seu educador financeiro ")

# Chat input CORRETO (walrus operator)
if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    # Mensagem do usuário
    st.chat_message("user").write(pergunta)
    
    # Spinner enquanto pensa
    with st.spinner("Edu está pensando..."):
        resposta = perguntar(pergunta)
        # Mensagem do assistente
        st.chat_message("assistant").write(resposta)
