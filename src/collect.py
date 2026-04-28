import pandas as pd
from sklearn.datasets import load_iris
import os

def collect_data():
    print("Collection in progress...")
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/raw_data.csv', index=False)
    print("Data collected successfully in data/raw_data.csv")

if __name__ == "__main__":
    collect_data()