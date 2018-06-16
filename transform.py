import pandas as pd

def to_csv():

    df = pd.read_json('data.json')
    df.to_csv('data.csv')

    return print(' \n Transformation is Done! Look it Data.csv in your project directory. \n')
