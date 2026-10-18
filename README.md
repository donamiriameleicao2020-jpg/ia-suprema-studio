# IA SUPREMA STUDIO — versão web inicial

Esta pasta converte a ideia da interface desktop em uma aplicação web Flask, adequada para teste e publicação em hospedagem Python.

## Importante sobre custos
- A hospedagem Render tem um plano gratuito com limites e pode suspender o serviço por inatividade.
- O site não inclui uso ilimitado gratuito de IA. Para responder de verdade, configure um provedor compatível com a API OpenAI em `AI_API_KEY`, `AI_BASE_URL` (opcional) e `AI_MODEL`.
- Nunca coloque a chave no HTML ou no repositório público; configure-a como variável de ambiente no painel de hospedagem.
- Esta versão ainda não implementa geração/edição de imagens, vídeo nem leitura de PDF. A interface marca essas áreas como não configuradas para não fingir que funcionam.
- A aplicação não usa Ollama no computador local quando publicada na nuvem. Um Ollama local não fica acessível ao site hospedado automaticamente.

## Publicar gratuitamente no Render
1. Crie uma conta no GitHub e um repositório novo. Como o código não contém segredos, pode ser público.
2. Envie todos os arquivos desta pasta para o repositório.
3. No Render, escolha **New > Web Service** e conecte o repositório.
4. Selecione o plano **Free**.
5. Build command: `pip install -r requirements.txt`
6. Start command: `gunicorn app:app`
7. Crie as variáveis `AI_API_KEY`, `AI_BASE_URL` (se o provedor exigir) e `AI_MODEL` no painel. Para apenas testar a interface, elas podem ficar sem configurar, mas o chat mostrará aviso.
8. Clique em Deploy. O Render mostrará o link público quando o deploy terminar.

## Rodar no computador
Python 3.11+:
`pip install -r requirements.txt`
`python app.py`
Abra `http://127.0.0.1:5000`.

Esta é uma adaptação web inicial, não uma conversão completa de todos os recursos do aplicativo desktop original.
