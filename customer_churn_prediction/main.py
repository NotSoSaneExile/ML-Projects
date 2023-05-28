import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from src.data_prep import load_data, clean_data

# Load and preprocess data
data = load_data('data/churn_dataset.csv')
X, y = clean_data(data)

# Train model with cross-validation
clf = LogisticRegression(random_state=42)
scores = cross_val_score(clf, X, y, cv=5)

# Print cross-validation scores
print("Cross-validation scores:", scores)
print("Mean cross-validation score:", scores.mean())

# Fit final model
clf.fit(X, y)

# Save model to disk
with open('models/logistic_regression_model.pkl', 'wb') as f:
    pickle.dump(clf, f)