import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import style
import matplotlib.ticker as ticker
from functions import remove_columns

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

#bx = sns.boxplot(x="Guests Included", y="Price", data=df_madrid, fliersize=0.5)
#bx.grid(axis="y", color="gray", linestyle="dashed")
#plt.ylim(ymax=600, ymin=0)
#bx.set_yticks(range(0, 600, 10))
#plt.show()

#bx = sns.boxplot(x="Amenities Rating", y="Price", data=df_madrid, fliersize=0.5)
#bx.grid(axis="y", color="gray", linestyle="dashed")
#plt.ylim(ymax=600, ymin=0)
#bx.set_yticks(range(0, 600, 10))
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

#sns.scatterplot(x='Bathrooms', y="Price", data=df_madrid)
#plt.xticks(rotation=90, fontsize=10)
#plt.show()

# sns.scatterplot(x='Amenities Score', y="Price", data=df_madrid)
# plt.xticks(rotation=90, fontsize=10)
# plt.show()


df_madrid = remove_columns(['Host ID', 'Host Name', 'Street', 'Neighbourhood Cleansed', 'City', 'State', 'Bed Type',
'Country', 'Latitude', 'Longitude', 'ID', 'Number of Reviews', 'Host Identity Verified', 'Neighbourhood Group Cleansed'], df_madrid)
df_madrid.drop(df_madrid.columns[0], axis=1, inplace= True)

# Gráfico de distribución para cada variable numérica
# ==============================================================================
# Ajustar número de subplots en función del número de columnas
# fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(15, 10))
# axes = axes.flat
# columnas_numeric = df_madrid.select_dtypes(include=['float64', 'int']).columns
# columnas_numeric = columnas_numeric.drop('Price')

# for i, colum in enumerate(columnas_numeric):
#     sns.regplot(
#         x           = df_madrid[colum],
#         y           = df_madrid['Price'],
#         color       = "gray",
#         marker      = '.',
#         scatter_kws = {"alpha":0.4},
#         line_kws    = {"color":"r","alpha":0.7},
#         ax          = axes[i]
#     )
#     axes[i].set_title(f"precio vs {colum}", fontsize = 7, fontweight = "bold")
#     axes[i].yaxis.set_major_formatter(ticker.EngFormatter())
#     axes[i].xaxis.set_major_formatter(ticker.EngFormatter())
#     axes[i].tick_params(labelsize = 6)
#     axes[i].set_xlabel("")
#     axes[i].set_ylabel("")

# # Se eliminan los axes vacíos
# for i in [11]:
#     fig.delaxes(axes[i])
    
# fig.tight_layout()
# plt.subplots_adjust(top=0.9)
# fig.suptitle('Correlación con precio', fontsize = 10, fontweight = "bold")



# Heatmap matriz de correlaciones
# ==============================================================================
# fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(4, 4))

# corr_matrix = df_madrid.select_dtypes(include=['float64', 'int']).corr(method='pearson')

# sns.heatmap(
#     corr_matrix,
#     annot     = True,
#     cbar      = False,
#     annot_kws = {"size": 6},
#     vmin      = -1,
#     vmax      = 1,
#     center    = 0,
#     cmap      = sns.diverging_palette(20, 220, n=200),
#     square    = True,
#     ax        = ax
# )
# ax.set_xticklabels(
#     ax.get_xticklabels(),
#     rotation = 45,
#     horizontalalignment = 'right',
# )

# ax.tick_params(labelsize = 8)



# Gráfico relación entre el precio y cada cada variables cualitativas
# ==============================================================================
# Ajustar número de subplots en función del número de columnas
fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(9, 5))
axes = axes.flat
columnas_object = df_madrid.select_dtypes(include=['object']).columns

for i, colum in enumerate(columnas_object):
    sns.violinplot(
        x     = colum,
        y     = 'Price',
        data  = df_madrid,
        color = "white",
        ax    = axes[i]
    )
    axes[i].set_title(f"precio vs {colum}", fontsize = 7, fontweight = "bold")
    axes[i].yaxis.set_major_formatter(ticker.EngFormatter())
    axes[i].tick_params(labelsize = 6)
    axes[i].set_xlabel("")
    axes[i].set_ylabel("")

# Se eliminan los axes vacíos
for i in [15]:
    fig.delaxes(axes[i])
    
fig.tight_layout()
plt.subplots_adjust(top=0.9)
fig.suptitle('Distribución del precio por grupo', fontsize = 10, fontweight = "bold");



plt.show()
