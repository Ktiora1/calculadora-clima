
from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_sensacao_termica(temp_celsius, velocidade_kmh):
    if velocidade_kmh <= 0:
        return temp_celsius

    if temp_celsius <= 10:
        sensacao = (13.12 + 0.6215 * temp_celsius
                    - 11.37 * velocidade_kmh**0.16
                    + 0.3965 * temp_celsius * velocidade_kmh**0.16)
    elif 10 < temp_celsius <= 25:
        sensacao = temp_celsius - (velocidade_kmh * 0.05)
    else:
        sensacao = temp_celsius - (velocidade_kmh * 0.02)

    return round(sensacao, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        temp = float(request.form['temperatura'])
        vel = float(request.form['velocidade'])
        resultado = calcular_sensacao_termica(temp, vel)
    return render_template('index.html', resultado=resultado)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)