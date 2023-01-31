import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning import df_madrid, important_amenities
import pandas as pd

list_count = []
for amenity in important_amenities:
    count = 0
    for i in range(len(df_madrid)):
        if df_madrid[amenity].iat[i]:
            count += 1
    list_count.append(count)

#sns.barplot(x=important_amenities, y=list_count)
#plt.xticks(rotation=90, fontsize=10)
#plt.show()

dict_freq = {}
for index in range(len(df_madrid)):
    type_prop = df_madrid["Room Type"].iat[index]
    if type_prop in dict_freq:
        dict_freq[type_prop] += 1
    else:
        dict_freq[type_prop] = 1

print(dict_freq)
#sns.scatterplot(x="Neighbourhood Group Cleansed", y="Price", data=df_madrid, hue="Room Type")
#plt.xticks(rotation=90, fontsize=10)
#plt.show()

#bx = sns.boxplot(x="Room Type", y="Price", data=df_madrid, fliersize=0.5)
#bx.grid(axis="y", color="gray", linestyle="dashed")
#plt.ylim(ymax=250, ymin=0)
#bx.set_yticks(range(0, 250, 10))
#plt.show()

bx = sns.boxplot(x=["Air conditioning", "Pool", "Breakfast"], y="Price", data=df_madrid, fliersize=0.5)
bx.grid(axis="y", color="gray", linestyle="dashed")
plt.ylim(ymax=250, ymin=0)
bx.set_yticks(range(0, 250, 10))
plt.show()