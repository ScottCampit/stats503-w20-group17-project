"""

"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import flask

# Custom functions
from db import loadDataSet as load_db
import plot

# Initialize application
server = flask.Flask(__name__)
app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                server=server)
app.title = "STATS503 Project"

# Load dataset
Xtrain, Xtest, Ytrain, Ytest = load_db()

# Make plot objects
bxPlt   = plot.makeBoxPlot(Xtrain,  Ytrain)   # Make the boxplot object
pairPlt = plot.makePairPlot(Xtrain, Ytrain)   # Make the pairplot object
coord   = plot.makeCoordinatePlot(Xtrain)     # Make the coordinate plot object

# Dashboard
app.layout = html.Div([
    html.H1(
            children='Exploratory data analysis for STATS503 project'
    ),
    dcc.Graph(
        id='Box-plot',
        figure=bxPlt
    ),
    dcc.Graph(
        id="Pairplot",
        figure=pairPlt
    ),
    dcc.Graph(
        id="Coordinate plot",
        figure=coord
    )
])

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8080, debug=True)