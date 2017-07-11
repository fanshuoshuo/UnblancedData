"""
from kaggle :https://www.kaggle.com/dalpozz/creditcardfraud
author      :joparga3
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("creditcard.csv")
print(data.head())

count_classes = pd.value_counts(data['Class'], sort = True).sort_index()
count_classes.plot(kind = 'bar')
plt.title("Fraud class histogram")
plt.xlabel("Class")
plt.ylabel("Frequency")
plt.show()

