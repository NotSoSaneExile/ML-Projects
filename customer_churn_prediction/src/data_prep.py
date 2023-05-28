import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

def load_data(filepath: str):
    churn_df = pd.read_csv(filepath)
    return churn_df

def clean_data(df):
    # Drop unnecessary columns
    df = df.drop(['customerID', 'TotalCharges'], axis=1)

    # Convert binary categorical variable Churn to numerical
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # Define transformer for categorical variables
    categorical_transformer = Pipeline(steps=[
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Define preprocessor to apply to all columns
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', categorical_transformer, ['gender', 'Partner', 'Dependents', 'PhoneService',
                                              'MultipleLines', 'InternetService', 'OnlineSecurity',
                                              'OnlineBackup', 'DeviceProtection', 'TechSupport',
                                              'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
                                              'PaymentMethod'])
        ])

    # Apply preprocessing to input data
    X = preprocessor.fit_transform(df)

    return X, df['Churn']

def split_data(X, y, test_size=0.2, random_state=42, shuffle=True):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)
    return X_train, X_test, y_train, y_test
