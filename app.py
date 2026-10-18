import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    prompt = (data.get("prompt") or "").strip()
    if not prompt:
        return jsonify(error="Digite uma mensagem."), 400
    # Configure uma API compatível com OpenAI no painel do provedor.
    api_key = os.getenv("AI_API_KEY", "").strip()
    base_url = os.getenv("AI_BASE_URL", "").strip() or None
    model = os.getenv("AI_MODEL", "").strip()
    if not api_key or not model:
        return jsonify(error="A interface online está pronta, mas falta configurar um provedor de IA e seu modelo. A hospedagem do site não inclui IA ilimitada gratuita."), 503
    try:
        client = OpenAI(api_key=api_key, base_url=base_url)
        result = client.chat.completions.create(
            model=model,
            messages=[
                {"role":"system","content":"Você é a IA SUPREMA STUDIO. Responda em português claro, com segurança e honestidade."},
                {"role":"user","content":prompt}
            ],
            timeout=60
        )
        return jsonify(answer=result.choices[0].message.content or "")
    except Exception as exc:
        app.logger.exception("Falha na API de IA")
        return jsonify(error="Não foi possível obter resposta do provedor de IA. Confira as configurações e os limites da conta."), 502

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
