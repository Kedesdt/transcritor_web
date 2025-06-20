from server import app
from flask import render_template, request, jsonify
from server.transcriber_module.transcriber import Transcriber
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "..", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "audio" not in request.files:
            return render_template(
                "index.html", transcription="Nenhum arquivo enviado."
            )
        file = request.files["audio"]
        if file.filename == "":
            return render_template(
                "index.html", transcription="Nenhum arquivo selecionado."
            )
        mode = request.form.get("model", "small")
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        transcriber = Transcriber(model=mode)

        transcription = transcriber.transcribe(filepath)
        try:
            os.remove(filepath)
        except Exception as e:
            print(f"Erro ao remover arquivo: {e}")
        return render_template("index.html", transcription=transcription)

    return render_template("index.html", transcription="Bem vindo ao transcritor!")


@app.route("/transcrever", methods=["POST"])
def transcrever():
    if "audio" not in request.files:
        return {"error": "Nenhum arquivo enviado."}, 400
    file = request.files["audio"]
    if file.filename == "":
        return {"error": "Nenhum arquivo selecionado."}, 400
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    mode = request.form.get("mode", "small")
    # print(mode)
    transcriber = Transcriber(model=mode)

    transcription = transcriber.transcribe(filepath)
    try:
        os.remove(filepath)
    except Exception as e:
        print(f"Erro ao remover arquivo: {e}")
    return jsonify({"transcription": transcription})
