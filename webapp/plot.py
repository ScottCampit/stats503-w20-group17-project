"""

"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

import pandas as pd
from sklearn import preprocessing

def makeBoxPlot(Xtrain, Ytrain):
    """

    :param Xtrain:
    :param Ytrain:
    :return:
    """
    # Create boxplots
    i = 0
    bxPlt = make_subplots(rows=1, cols=len(Xtrain.columns))
    for col in Xtrain.columns:
        bxPlt.add_trace(
            go.Box(y=Xtrain[col], x=Ytrain,
                   boxpoints='all', jitter=0.3,
                   name=Xtrain.columns[i]),
            row=1, col=i+1
        )
        i += 1
    bxPlt.update_layout(
        title="Feature distribution",
        xaxis_title="Features",
        yaxis_title="Value distribution"
    )
    return go.Figure(bxPlt)

def makePairPlot(Xtrain, Ytrain):
    """

    :param Xtrain:
    :param Ytrain:
    :return:
    """
    # Create pairplot
    pairPlt = px.scatter_matrix(Xtrain,
                                color=Ytrain)
    pairPlt.update_traces(diagonal_visible=False)
    pairPlt.update_layout(
        title="Feature distribution"
    )
    return go.Figure(pairPlt)

def makeCoordinatePlot(Xtrain):
    """

    :param Xtrain:
    :return:
    """
    # Coordinate plot
    le = preprocessing.LabelEncoder()
    month_names = Xtrain["Month"].unique()
    month_names = month_names.tolist()

    Xtrain["Month"] = le.fit_transform(Xtrain["Month"].values)
    month_values = Xtrain["Month"].unique()
    month_values = month_values.tolist()

    month_dict = dict(zip(month_names, month_values))
    coord = px.parallel_coordinates(Xtrain,
                                    color="Month",
                                    labels=month_dict)
    return go.Figure(coord)

if __name__ == "__main__":
    from db import loadDataSet as load_db
    Xtrain, Xtest, Ytrain, Ytest = load_db()

    # Plot the box plot
    bxPlt = makeBoxPlot(Xtrain, Ytrain)
    bxPlt.show()

    # Plot the pair plot
    pairPlt = makePairPlot(Xtrain, Ytrain)
    pairPlt.show()

    # Plot the coordinate plot
    coord = makeCoordinatePlot(Xtrain)
    coord.show()