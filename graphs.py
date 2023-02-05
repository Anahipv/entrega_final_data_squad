import matplotlib.pyplot as plt
import seaborn as sns
# from data_cleaning import important_amenities  
##CARO: si importamos algo de data_cleaning no scorre todo el archivo, si no es necesario lo evitaria
import pandas as pd
import numpy as np

###aca por eso deje mejor leer el csv que importar el data frame
df_madrid = pd.read_csv("airbnb_madrid_clean.csv", sep=",")

# list_count = []
# for amenity in important_amenities:
#     count = 0
#     for i in range(len(df_madrid)):
#         if df_madrid[amenity].iat[i]:
#             count += 1
#     list_count.append(count)


# rows = df_madrid.shape[0]
# list_percentage = list(map(lambda x: int(100*x/rows), list_count))

#bp = sns.barplot(x=important_amenities, y=list_percentage)
#bp.set_title("Percentage of properties with amenities", fontsize=30)
#for i in range(len(important_amenities)):
    #plt.text(i,list_percentage[i]/2, str(list_percentage[i])+"%", color="white", fontweight="bold", horizontalalignment="center")
#plt.xticks(rotation=90, fontsize=10)
#plt.show()

#dict_freq = {}
#for index in range(len(df_madrid)):
    #type_prop = df_madrid["Room Type"].iat[index]
    #if type_prop in dict_freq:
        #dict_freq[type_prop] += 1
    #else:
        #dict_freq[type_prop] = 1

#sns.scatterplot(x="Neighbourhood Group Cleansed", y="Price", data=df_madrid, hue="Room Type")
#plt.xticks(rotation=90, fontsize=10)
#plt.show()

# bx = sns.boxplot(x="Room Type", y="Price", data=df_madrid, fliersize=0.5)
# bx.grid(axis="y", color="gray", linestyle="dashed")
# plt.ylim(ymax=250, ymin=0)
# bx.set_yticks(range(0, 250, 10))
# plt.show()

# bx = sns.boxplot(x="Bedrooms", y="Price", data=df_madrid, fliersize=0.5)
# bx.grid(axis="y", color="gray", linestyle="dashed")
# plt.ylim(ymax=600, ymin=0)
# bx.set_yticks(range(0, 600, 10))
# plt.show()

# bx = sns.boxplot(x="Bathrooms", y="Price", data=df_madrid, fliersize=0.5)
# bx.grid(axis="y", color="gray", linestyle="dashed")
# plt.ylim(ymax=600, ymin=0)
# bx.set_yticks(range(0, 600, 10))
# plt.show()

# bx = sns.boxplot(x="Accommodates", y="Price", data=df_madrid, fliersize=0.5)
# bx.grid(axis="y", color="gray", linestyle="dashed")
# plt.ylim(ymax=600, ymin=0)
# bx.set_yticks(range(0, 600, 10))
# plt.show()

bx = sns.boxplot(x="Amenities Rating", y="Price", data=df_madrid, fliersize=0.5)
bx.grid(axis="y", color="gray", linestyle="dashed")
plt.ylim(ymax=600, ymin=0)
bx.set_yticks(range(0, 600, 10))
plt.show()

#bx = sns.boxplot(x=["Air conditioning", "Pool", "Breakfast"], y="Price", data=df_madrid, fliersize=0.5)
#bx.grid(axis="y", color="gray", linestyle="dashed")
#plt.ylim(ymax=250, ymin=0)
#bx.set_yticks(range(0, 250, 10))
#plt.show()

#room_types = df_madrid["Room Type"].unique()
#list_df_room_types = []
#for room_type in room_types:
    #df_filtered = df_madrid[df_madrid["Room Type"] == room_type]
    #list_df_room_types.append(df_filtered)

#for index, df in enumerate(list_df_room_types):
    #rt = sns.barplot(x="Neighbourhood Group Cleansed", y="Price", data=df)
    #rt.set_title(room_types[index], fontsize=30)
    #plt.xticks(rotation=90, fontsize=10)
    #plt.show()

#sns.distplot(df_madrid["Price"])
#plt.show()


##Gracifos con Y en Price y X variables

# sns.scatterplot(x='Bedrooms', y="Price", data=df_madrid)
# plt.xticks(rotation=90, fontsize=10)
# plt.show()

# sns.scatterplot(x='Bathrooms', y="Price", data=df_madrid)
# plt.xticks(rotation=90, fontsize=10)
# plt.show()

# sns.scatterplot(x='Amenities Score', y="Price", data=df_madrid)
# plt.xticks(rotation=90, fontsize=10)
# plt.show()