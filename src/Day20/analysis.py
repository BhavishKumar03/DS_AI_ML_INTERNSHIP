"""Script version of the EDA steps performed in the notebook."""
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('customer_analytics.csv')
    print(df.head())
    print(df.info())
    df['Education'] = df['Education'].fillna(df['Education'].mode()[0])
    df = df.dropna(subset=['AnnualIncome'])
    df = df.drop_duplicates()
    print('Cleaned data size:', df.shape)
