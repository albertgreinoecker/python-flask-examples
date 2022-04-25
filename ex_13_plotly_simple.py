import json

from flask import Flask, render_template # Zusätzlicher Import für's rendern
from random import random
app = Flask(__name__)

@app.route('/')
def home():
    wave= []
    idxs = []
    for i in range(1,1000):
        wave.append(random())
        idxs.append(i)

    alternatives = ['yes' ,'no', 'maybe']
    count = [350, 500,400]
    return render_template('13_plotly_simple.html', wave=json.dumps(wave), idxs=json.dumps(idxs), alternatives=alternatives, count=count)

if __name__ == '__main__':
    app.run(debug=True)