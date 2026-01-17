from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# 1. RUTA PRINCIPAL: Carga el simulador futurista
@app.route('/')
def index():
    return render_template('index.html')

# 2. RUTA DE PRIVACIDAD: Requisito obligatorio para AdSense
@app.route('/privacidad')
def privacidad():
    return render_template('privacidad.html')

#TERMINOS Y CONDICIONES
@app.route('/terminos')
def terminos():
    return render_template('terminos.html')

# 3. API DE PREGUNTAS: Entrega el JSON con las 160 preguntas
@app.route('/api/preguntas-completas')
def obtener_preguntas():
    try:
        # Ruta dinámica para encontrar el archivo en el servidor
        ruta_json = os.path.join(app.root_path, 'data', 'preguntas.json')
        with open(ruta_json, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        return jsonify(datos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 4. RUTA ADS.TXT: Validación de propiedad para Google AdSense
@app.route('/ads.txt')
def ads_txt():
    # Google te dará un código parecido a este una vez que te registres
    return "google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0"

# 5. CONFIGURACIÓN PARA RENDER: Arregla el error de "Port Binding"
if __name__ == '__main__':
    # Render asigna un puerto dinámico mediante la variable de entorno PORT
    puerto = int(os.environ.get("PORT", 5000))
    # '0.0.0.0' permite que el servidor externo acceda a la app
    app.run(host='0.0.0.0', port=puerto, debug=False)