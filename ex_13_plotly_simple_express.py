import json
from flask import Flask, render_template
import plotly
import plotly.express as px
import pandas as pd #Eine Bibliothek für die Datenanalyse

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.DataFrame({
        'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges',
                  'Bananas'],
        'Amount': [4, 1, 2, 2, 4, 5],
        'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
    })
    fig = px.bar(df, x='Fruit', y='Amount', color='City',
                 barmode='group')

    print (fig)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('13_plotly_simple_express.html', graphJSON=graphJSON)

@app.route('/additional')
def gapminder():
    df = px.data.iris()
    fig = px.scatter_matrix(df, dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
                            color="species")
    iris = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    long_df = px.data.medals_long()
    fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
    medal = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('13_plotly_simple_express_additional.html', iris=iris, medal=medal)


if __name__ == '__main__':
    app.run(debug=True)