import pytest
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from ml.data import process_data
from ml.model import train_model, inference, compute_model_metrics

# Load small subset of dataset for testing
data_path = "./data/census.csv"
data = pd.read_csv(data_path)

# random sample for testing
test_sample = data.sample(n=50, random_state=42)

cat_features = [
    "workclass", "education", "marital-status", "occupation", 
    "relationship", "race", "sex", "native-country"
]

# split sample into train/test
train_df, test_df = train_test_split(test_sample, test_size=0.2, random_state=42)

# Test #1: ML functions return expected type
def test_process_train_inference_types():
    """
    Test that processed data, labels, and predictions are numpy arrays or expected shape.
    """
    X_train, y_train, encoder, lb = process_data(
        train_df,
        categorical_features=cat_features,
        label="salary",
        training=True
    )
    model = train_model(X_train, y_train)
    X_test, y_test, _ ,_ = process_data(
        test_df,
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=lb
    )
    preds = inference(model, X_test)

    assert isinstance(X_test, np.ndarray)
    assert isinstance(y_test, np.ndarray)
    assert isinstance(preds, np.ndarray)
    assert preds.shape == y_test.shape


# Test #2: ML Model uses expected algorithm
def test_model_algorithm():
    """
    Test that the trained model is a RandomForestClassifier.
    """
    X_train, y_train, _ ,_ = process_data(
        train_df,
        categorical_features=cat_features,
        label="salary",
        training=True
    )
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier)


# Test #3: compute_model_metrics returns expected value type
def test_compute_metrics_types():
    """
    Test that compute_model_metrics returns three floats: precision, recall, f1.
    """
    X_train, y_train, encoder, lb = process_data(
        train_df,
        categorical_features=cat_features,
        label="salary",
        training=True
    )
    model = train_model(X_train, y_train)
    X_test, y_test, _ ,_ = process_data(
        test_df,
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=lb
    )
    preds = inference(model, X_test)
    p, r, f1 = compute_model_metrics(y_test, preds)

    assert isinstance(p, float)
    assert isinstance(r, float)
    assert isinstance(f1, float)
