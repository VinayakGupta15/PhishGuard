from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load processed data
X_train, X_test, y_train, y_test = joblib.load('processed_data.pkl')

# Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
print(f"Classification Report:\n{classification_report(y_test, y_pred)}")

# Save model
joblib.dump(model, 'phishing_model.pkl')
print("Model training complete.")
