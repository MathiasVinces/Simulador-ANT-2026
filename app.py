from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

def cargar_preguntas():
    ruta = os.path.join(os.path.dirname(__file__), 'data', 'preguntas.json')
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/preguntas-completas')
def obtener_todas():
    # Enviamos todas en orden para practicar el cuestionario completo
    return jsonify(cargar_preguntas())

if __name__ == '__main__':
    app.run(debug=True)