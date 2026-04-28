import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report

def evaluate_model():
    print("Model evaluation in progress...")
    X_test = pd.read_csv('data/X_test.csv')
    y_test = pd.read_csv('data/y_test.csv').values.flatten()
    
    model = joblib.load('models/iris_model.joblib')
    predictions = model.predict(X_test)
    
    acc = accuracy_score(y_test, predictions)
    print(f"Accuracy: {acc:.4f}")
    print("\nClassification report:")
    print(classification_report(y_test, predictions))

if __name__ == "__main__":
    evaluate_model()