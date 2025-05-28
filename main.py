
from flask import Flask, request, jsonify
import pandas as pd
import io

app = Flask(__name__)

@app.route('/analisis_rendimiento', methods=['POST'])
def analisis_rendimiento():
    file = request.files.get('excel_file')
    texto = request.form.get('descripcion_textual')
    objetivo = request.form.get('objetivo', 'analizar')

    if file:
        try:
            df = pd.read_excel(file)
            resumen = df.describe(include='all').to_dict()
        except Exception as e:
            return jsonify({"error": "No se pudo leer el archivo Excel.", "detalle": str(e)}), 400
    else:
        resumen = "No se proporcionó archivo Excel."

    return jsonify({
        "resumen_excel": resumen,
        "descripcion_textual": texto,
        "objetivo": objetivo,
        "mensaje": "Análisis realizado correctamente." if file else "Sin archivo Excel, análisis parcial."
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
