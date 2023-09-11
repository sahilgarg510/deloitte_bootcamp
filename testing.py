import pandas as pd

df = pd.read_csv(r"C:\Users\Sahil\Downloads\burberry65 (1).csv")

print(len(df['InstagramPostLink'].unique()))