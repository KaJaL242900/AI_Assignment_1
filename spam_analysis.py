# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("spam.csv", encoding='latin-1')

# Keep required columns only
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# Display basic info
print("First 5 rows:\n", df.head())
print("\nShape of dataset:", df.shape)

#Count spam vs not spam
print("\nCount:\n", df['label'].value_counts())

#Separate spam and not spam
spam = df[df['label'] == 'spam']
not_spam = df[df['label'] == 'ham']

print("\nSpam messages:", len(spam))
print("Not spam messages:", len(not_spam))

#Save separate CSV files
spam.to_csv("spam_messages.csv", index=False)
not_spam.to_csv("not_spam_messages.csv", index=False)

#Convert labels to numeric (optional)
df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})

# Visualization
df['label'].value_counts().plot(kind='bar')
plt.title("Spam vs Not Spam")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()
