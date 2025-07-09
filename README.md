# Projeto de BOT de conversas com IA para Discord:

Talkord é o meu Projeto de bot de Discord que lê mensagens enviadas no canal do Discord e responde utilizando inteligência artificial. 
Ele usa o modelo **GPT da OpenAI** com suporte completo a prompts naturais.

## Requisitos:

- Python 3.11+
- Conta no Discord Development para gerar uma API Key (TOKEN_DISCORD)
- Conta na OpenAI para gerar uma API Key (TOKEN_OPENAI)

## Como utilizar:
# Clone o repositório:

git clone https://github.com/lucas-git-dev/bot-discord-conversa-ia.git
cd talkord
conda activate discord-talk

## Variáveis do .env:

TOKEN_DISCORD = Coloque aqui o token do seu BOT
TOKEN_OPENAI = Coloque aqui o token da sua conta OpenAI

# Ideias de Melhorias:

- [ ] Adaptar para atendimento específico de lojas com contexto
- [ ] Anotação de pedidos em um banco de dados para facilitar atendimento
- [ ] Detectar linguagem do usuário e adaptar a resposta
- [ ] Adicionar cache ou banco de dados para perguntas frequentes
- [ ] Nome personalizado para cada Servidor de Discord