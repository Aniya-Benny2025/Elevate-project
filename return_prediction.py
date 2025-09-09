import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load datasets
orders = pd.read_csv("data/orders.csv")
returns = pd.read_csv("data/returns.csv")

# Merge on order_id
df = pd.merge(orders, returns, on="order_id", how="left")
df["is_returned"] = df["return_reason"].notnull().astype(int)

# Encode categorical variables
categorical_cols = ["category", "supplier", "geography", "channel"]
encoder = LabelEncoder()
for col in categorical_cols:
    df[col] = encoder.fit_transform(df[col].astype(str))

# Features and target
X = df[["category", "supplier", "geography", "channel", "price"]]
y = df["is_returned"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict return probabilities
df["return_probability"] = model.predict_proba(X)[:, 1]
df["risk_level"] = pd.cut(df["return_probability"],
                          bins=[0, 0.33, 0.66, 1],
                          labels=["Low", "Medium", "High"])

# Export high-risk products
high_risk = df[df["risk_level"] == "High"]
high_risk.to_csv("data/high_risk_products.csv", index=False)
print("✅ High-risk products exported to data/high_risk_products.csv")
