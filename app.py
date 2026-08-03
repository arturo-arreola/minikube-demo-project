from flask import Flask, jsonify

app = Flask(__name__)

def obtener_estado_sistema(cpu_usage):
  """Devuelve alerta si la CPU pasa del 80%, de lo contrario OK"""
  if cpu_usage >= 80:
    return "ALERTA"
  return "OK"

@app.route('/')
def hello():
  return "Hola GitOps! Esta version incluye Pruebas Unitarias"

@app.route('/status/<int:cpu>')
def status(cpu):
  estado = obtener_estado_sistema(cpu)
  return jsonify({
    "cpu_actual ": cpu,
    "estado_sistema": estado
  })


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)