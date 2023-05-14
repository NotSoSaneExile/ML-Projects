import pandas as pd
import os
import sys
from os.path import abspath, dirname
# Add the parent directory of the src package to the system path
parent_dir = dirname(dirname(abspath(__file__)))
sys.path.append(parent_dir)
from src.data_prep import load_data

def test_load_churn_data():
    # Define the path to the CSV file
    file_path = os.path.join(parent_dir, 'data', 'churn_dataset.csv')
    
    # Load the data using the load_data function
    df = load_data(file_path)
    
    # Verify that the data is loaded correctly
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (7043, 21)
    assert set(df.columns) == set(['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
                                   'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                                   'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
                                   'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn'])
    