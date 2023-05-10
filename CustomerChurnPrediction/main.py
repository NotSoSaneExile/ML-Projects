import pandas as pd
from ydata_profiling import ProfileReport
churn_dataset = pd.read_csv("churn-dataset.csv")
profile = ProfileReport(churn_dataset, title='Churn Report', explorative=True)
profile.to_file(output_file='churn_report.html')
