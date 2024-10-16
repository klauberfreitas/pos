import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('global-assets/datasets/amazon-reviews.csv')

train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

train_df.to_csv('global-assets/datasets/amazon-reviews-train.csv', index=False)
test_df.to_csv('global-assets/datasets/amazon-reviews-test.csv', index=False)