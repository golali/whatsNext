from surprise import Dataset
from surprise import Reader
import pandas as pd
import matplotlib.pyplot as plt


# Load the built-in MovieLens 100k dataset
data = Dataset.load_builtin('ml-100k')
raw_ratings = data.raw_ratings

# Convert to DataFrame
df = pd.DataFrame(raw_ratings, columns=['user', 'item', 'rating', 'timestamp'])
df.head()
print(f"Unique users: {df['user'].nunique()}")
print(f"Unique movies: {df['item'].nunique()}")
print(f"Rating range: {df['rating'].min()} to {df['rating'].max()}")
print(df['rating'].value_counts().sort_index())


# df['rating'].hist(bins=9)
# plt.title("Rating Distribution")
# plt.xlabel("Rating")
# plt.ylabel("Count")
# plt.show()