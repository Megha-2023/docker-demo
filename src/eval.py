import pandas as pd
import joblib
import json
import os
from sklearn.metrics import accuracy_score, classification_report, precision_score

def evaluate_model():
    print("Model evaluation in progress...")
    
    X_test = pd.read_csv('data/X_test.csv')
    y_test = pd.read_csv('data/y_test.csv').values.flatten()
    model = joblib.load('models/iris_model.joblib')
    
    predictions = model.predict(X_test)
    
    acc = accuracy_score(y_test, predictions)
    prec = precision_score(y_test, predictions, average='macro')
    
    print(f"Accuracy: {acc:.4f}")
    print("\nClassification report:")
    print(classification_report(y_test, predictions))
    
    save_metrics(acc, prec)

def save_metrics(acc, prec, filepath="models/metrics.json"):
    from datetime import datetime
    
    metrics = {
        "accuracy": acc,
        "precision": prec,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, "w") as f:
        json.dump(metrics, f, indent=4)
    print(f"Metrics saved to {filepath}")

if __name__ == "__main__":
    evaluate_model()