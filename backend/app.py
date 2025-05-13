from flask import Flask, request, jsonify
from flask_cors import CORS
from fuzzy_logic.inference import NetworkDiagnosisSystem
import traceback

app = Flask(__name__)
CORS(app)

diagnosis_system = NetworkDiagnosisSystem()

@app.route('/api/diagnose', methods=['POST'])
def diagnose():
    try:
        data = request.get_json()
        print("Datos recibidos:", data)  # Debug print
        
        # Validar que todos los síntomas requeridos estén presentes
        required_symptoms = ['conectividad', 'velocidad', 'acceso_servidor', 'señal_wifi', 'errores_dns']
        for symptom in required_symptoms:
            if symptom not in data:
                return jsonify({
                    'error': f'Falta el síntoma requerido: {symptom}'
                }), 400

        # Validar valores permitidos
        valid_values = {
            'conectividad': ['nula', 'baja', 'media', 'buena'],
            'velocidad': ['lenta', 'moderada', 'rápida'],
            'acceso_servidor': ['inaccesible', 'lento', 'fluido'],
            'señal_wifi': ['débil', 'aceptable', 'fuerte'],
            'errores_dns': ['frecuente', 'ocasional', 'nula']
        }

        for symptom, value in data.items():
            if value not in valid_values[symptom]:
                return jsonify({
                    'error': f'Valor inválido para {symptom}: {value}. Valores permitidos: {valid_values[symptom]}'
                }), 400

        # Realizar el diagnóstico usando la clase
        result = diagnosis_system.diagnose(data)
        return jsonify(result)

    except Exception as e:
        print("Error completo:", traceback.format_exc())  # Debug print
        return jsonify({
            'error': f'Error al procesar la solicitud: {str(e)}'
        }), 500

@app.route('/api/test-cases', methods=['GET'])
def get_test_cases():
    """Retorna casos de prueba predefinidos."""
    test_cases = [
        {
            'nombre': 'Falla ISP',
            'sintomas': {
                'conectividad': 'nula',
                'velocidad': 'lenta',
                'acceso_servidor': 'inaccesible',
                'señal_wifi': 'aceptable',
                'errores_dns': 'frecuente'
            }
        },
        {
            'nombre': 'Problema de Cable',
            'sintomas': {
                'conectividad': 'baja',
                'velocidad': 'moderada',
                'acceso_servidor': 'lento',
                'señal_wifi': 'fuerte',
                'errores_dns': 'nula'
            }
        },
        {
            'nombre': 'Falla en Router',
            'sintomas': {
                'conectividad': 'nula',
                'velocidad': 'lenta',
                'acceso_servidor': 'inaccesible',
                'señal_wifi': 'débil',
                'errores_dns': 'ocasional'
            }
        },
        {
            'nombre': 'Problema DNS',
            'sintomas': {
                'conectividad': 'media',
                'velocidad': 'moderada',
                'acceso_servidor': 'fluido',
                'señal_wifi': 'fuerte',
                'errores_dns': 'frecuente'
            }
        },
        {
            'nombre': 'Cobertura Wi-Fi Insuficiente',
            'sintomas': {
                'conectividad': 'baja',
                'velocidad': 'lenta',
                'acceso_servidor': 'lento',
                'señal_wifi': 'débil',
                'errores_dns': 'nula'
            }
        }
    ]
    return jsonify(test_cases)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 