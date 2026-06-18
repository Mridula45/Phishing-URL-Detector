import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

print("Loading dataset...")

# Load dataset
data = pd.read_csv("dataset.csv")

print("Dataset Loaded")

# Drop index column
if "index" in data.columns:
    data = data.drop("index", axis=1)

# Target column
target = "Result"

# Convert labels: -1 → 0 (phishing), 1 → 1 (safe)
data[target] = data[target].apply(lambda x: 1 if x == 1 else 0)

# Split data
X = data.drop(target, axis=1)
y = data[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("phishing_model.pkl", "wb"))

print("✅ Model trained and saved!")