import joblib
import json
import pandas as pd

from sklearn.metrics import accuracy_score, confusion_matrix

config_path = "config.json"


# Load config. settings and Build the path to the files
with open(config_path, "r") as config_file:
    config = json.load(config_file)

path_to_model = config["model_path_classifier"]
path_to_X_test_data = config["data_path_X_test"]
path_to_y_test_data = config["data_path_y_test"]

# Load the trained model
classifier_dt = joblib.load(path_to_model)

# Load the test dataset
X_test = pd.read_pickle(path_to_X_test_data)
y_test = pd.read_pickle(path_to_y_test_data)

# Perform predictions
predictions = classifier_dt.predict(X_test)

# Calculate accuracy and confusion matrix
accuracy = accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)
