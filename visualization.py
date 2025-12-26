import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("quotes_dataset.csv")

# Top 5 authors
df["Author"].value_counts().head(5).plot(kind="bar")
plt.title("Top 5 Authors")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.show()

# Tags per quote
df["Tag_Count"] = df["Tags"].apply(lambda x: len(x.split(",")))
df["Tag_Count"].plot(kind="hist")
plt.title("Distribution of Tags per Quote")
plt.xlabel("Number of Tags")
plt.ylabel("Frequency")
plt.show()
