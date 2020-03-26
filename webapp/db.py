"""

"""

import pandas as pd
from sklearn.model_selection import train_test_split

def loadDataSet(url='https://archive.ics.uci.edu/ml/machine-learning-databases/00468/online_shoppers_intention.csv',
                nameOfResponse='Revenue', trainSize=0.7, seed=630):
    """

    :param url:
    :param trainSize:
    :param seed:
    :return:
    """

    # Load dataset
    data = pd.read_csv(url)
    data = data[data['Revenue'].notna()]
    X    = data.loc[:, data.columns != 'Revenue']
    Y    = data[nameOfResponse]

    # Split into training and testing datasets
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(
        X, Y, train_size=trainSize, random_state=seed
    )

    return Xtrain, Xtest, Ytrain, Ytest

if __name__ == "__main__":
    Xtrain, Xtest, Ytrain, Ytest = loadDataSet()