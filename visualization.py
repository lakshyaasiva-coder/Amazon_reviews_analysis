import os
print(os.getcwd())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter 
import re
df = pd.read_csv(r"C:\Users\ADMIN\Desktop\KPRCAS\INTERNSHIP\amazon_review_\train.csv", header=None,names=['label','title','text'])
print(df.columns)
print(df.head())
plt.figure(figsize=(6,4))
sns.countplot(x='label', data=df)
plt.title("Sentiment Distribution")
plt.xlabel("Label")
plt.ylabel("Number of reviews")
plt.show()

df['review_length'] = df['text'].apply(len)
plt.figure(figsize=(8,4))
sns.histplot(
    df['review_length'],
    bins=50
)
plt.title("Review Length Distribution")
plt.xlabel("Number of Characters")
plt.ylabel("Frequency")
plt.show()
