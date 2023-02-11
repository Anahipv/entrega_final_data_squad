import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib import style
import matplotlib.ticker as ticker
from functions import remove_columns

df_madrid = pd.read_csv('airbnb_madrid_clean.csv', sep=',')
important_amenities = ['Kitchen', 'Internet', 'Air conditioning', 'Heating', 'Washer', 
'Dryer', 'Elevator', 'Wheelchair accessible', 'TV', 'Pool', '24-hour check-in']

my_palette = ['#FF5A5F', '#00A699', '#FC642D', '#C2341F', '#FF9A21', '#FF1D5F', '#21FFB9', '#E6DB1E','#0072A8', '#FCE12D', '#B821FF', '#C29348']

## Chart 1 : 'Percentage of properties with amenities' - Barplot
## ==============================================================================
# list_count = []
# for amenity in important_amenities:
#     count = 0
#     for i in range(len(df_madrid)):
#         if df_madrid[amenity].iat[i]:
#             count += 1
#     list_count.append(count)


# rows = df_madrid.shape[0]
# list_percentage = list(map(lambda x: int(100*x/rows), list_count))

# bp = sns.barplot(x=important_amenities, y=list_percentage, palette= my_palette)
# bp.set_title('Percentage of properties with amenities', fontsize=20, fontweight='bold')
# for i in range(len(important_amenities)):
#     plt.text(i,list_percentage[i]/2, str(list_percentage[i])+'%', color='white', fontweight='bold', horizontalalignment='center')
# plt.xticks(rotation=60, fontsize=8)


## Chart 2 : 'Price per neighborhood according to the type of room' - Scatterplot
## ==============================================================================
# sp = sns.scatterplot(x='Neighbourhood Group Cleansed', y='Price', data=df_madrid, hue='Room Type', palette= my_palette)
# sp.set_title('Price per neighborhood according to the room type', fontsize=20, fontweight='bold')
# plt.xticks(rotation=60, fontsize=9)


## Chart 3 : 'Price per room type' - Boxplot
## ==============================================================================
# bx = sns.boxplot(x='Room Type', y='Price', data=df_madrid, fliersize=0.5, palette= my_palette)
# bx.grid(axis='y', color='gray', linestyle='dashed')
# bx.set_title('Price per room type', fontsize=20, fontweight='bold')
# bx.set_yticks(range(0, 250, 10))
# plt.ylim(ymax=250, ymin=0)

## Chart 4 : 'Price per bedrooms' - Boxplot
## ==============================================================================
# bx = sns.boxplot(x='Bedrooms', y='Price', data=df_madrid, fliersize=0.5, palette= my_palette)
# bx.grid(axis='y', color='gray', linestyle='dashed')
# bx.set_title('Price per bedrooms', fontsize=20, fontweight='bold')
# bx.set_yticks(range(0, 600, 10))
# plt.ylim(ymax=600, ymin=0)

## Chart 5 : 'Price per bathrooms' - Boxplot
## ==============================================================================
# bx = sns.boxplot(x='Bathrooms', y='Price', data=df_madrid, fliersize=0.5, palette= my_palette)
# bx.grid(axis='y', color='gray', linestyle='dashed')
# bx.set_title('Price per bathrooms', fontsize=20, fontweight='bold')
# bx.set_yticks(range(0, 600, 10))
# plt.ylim(ymax=600, ymin=0)

## Chart 6 : 'Price per accommodates' - Boxplot
## ==============================================================================
# bx = sns.boxplot(x='Accommodates', y='Price', data=df_madrid, fliersize=0.5, palette= my_palette)
# bx.grid(axis='y', color='gray', linestyle='dashed')
# bx.set_title('Price per accommodates', fontsize=20, fontweight='bold')
# bx.set_yticks(range(0, 600, 10))
# plt.ylim(ymax=600, ymin=0)

## Chart 7 : 'Price per guest included' - Boxplot
## ==============================================================================
# bx = sns.boxplot(x='Guests Included', y='Price', data=df_madrid, fliersize=0.5, palette= my_palette)
# bx.grid(axis='y', color='gray', linestyle='dashed')
# bx.set_title('Price per guest included', fontsize=20, fontweight='bold')
# bx.set_yticks(range(0, 600, 10))
# plt.ylim(ymax=600, ymin=0)

## Chart 8 : 'Price per amenities rating' - Boxplot
## ==============================================================================
# bx = sns.boxplot(x='Amenities Rating', y='Price', data=df_madrid, fliersize=0.5, palette= my_palette)
# bx.grid(axis='y', color='gray', linestyle='dashed')
# bx.set_title('Price per amenities rating', fontsize=20, fontweight='bold')
# bx.set_yticks(range(0, 600, 10))
# plt.ylim(ymax=600, ymin=0)

## Chart 9 : 'Price per neighborhood according to the type of room' - version 2 - Barplot
## ==============================================================================
# room_types = df_madrid['Room Type'].unique()
# list_df_room_types = []
# for room_type in room_types:
#     df_filtered = df_madrid[df_madrid['Room Type'] == room_type]
#     list_df_room_types.append(df_filtered)

# for index, df in enumerate(list_df_room_types):
#     rt = sns.barplot(x='Neighbourhood Group Cleansed', y='Price', data=df, palette= my_palette)
#     rt.set_title(room_types[index], fontsize=30)
#     plt.xticks(rotation=90, fontsize=10)
#     plt.show()


## Chart 10 : 'Density of price' - Displot
## ==============================================================================
# dp = sns.distplot(df_madrid['Price'], color= '#FF5A5F')
# dp.set_title('Density of price', fontsize=20, fontweight='bold')


df_madrid = remove_columns(['Host ID', 'Host Name', 'Street', 'Neighbourhood Cleansed', 'City', 'State', 'Bed Type',
'Country', 'Latitude', 'Longitude', 'ID', 'Number of Reviews', 'Host Identity Verified', 'Neighbourhood Group Cleansed'], df_madrid)
df_madrid.drop(df_madrid.columns[0], axis=1, inplace= True)


## Chart 11: distribution for each numeric variable
## ==============================================================================
# fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(15, 10))
# axes = axes.flat
# num_columns = df_madrid.select_dtypes(include=['float64', 'int']).columns
# num_columns = num_columns.drop('Price')

# for i, colum in enumerate(num_columns):
#     sns.regplot(
#         x           = df_madrid[colum],
#         y           = df_madrid['Price'],
#         color       = '#FF5A5F',
#         marker      = '.',
#         scatter_kws = {'alpha':0.4},
#         line_kws    = {'color':'#00A699','alpha':0.7},
#         ax          = axes[i]
#     )
#     axes[i].set_title(f'price vs {colum}', fontsize = 7, fontweight = 'bold')
#     axes[i].yaxis.set_major_formatter(ticker.EngFormatter())
#     axes[i].xaxis.set_major_formatter(ticker.EngFormatter())
#     axes[i].tick_params(labelsize = 6)
#     axes[i].set_xlabel('')
#     axes[i].set_ylabel('')

# for i in [11]:
#     fig.delaxes(axes[i])
    
# fig.tight_layout()
# plt.subplots_adjust(top=0.9)
# fig.suptitle('Correlation with price', fontsize = 10, fontweight = 'bold')


## Chart 12: correlation matrix with numeric columns
## ==============================================================================
# fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(4, 4))

# corr_matrix = df_madrid.select_dtypes(include=['float64', 'int']).corr(method='pearson')

# sns.heatmap(
#     corr_matrix,
#     annot     = True,
#     cbar      = False,
#     annot_kws = {'size': 6},
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



# Chart 12: distribution for each categorical columns
# ==============================================================================
# fig, axes = plt.subplots(nrows=4, ncols=4, figsize=(9, 5))
# axes = axes.flat
# cat_columns = df_madrid.select_dtypes(include=['object']).columns

# for i, colum in enumerate(cat_columns):
#     sns.violinplot(
#         x     = colum,
#         y     = 'Price',
#         data  = df_madrid,
#         palette= my_palette,
#         ax    = axes[i]
#     )
#     axes[i].set_title(f'price vs {colum}', fontsize = 7, fontweight = 'bold')
#     axes[i].yaxis.set_major_formatter(ticker.EngFormatter())
#     axes[i].tick_params(labelsize = 6)
#     axes[i].set_xlabel('')
#     axes[i].set_ylabel('')

# for i in [15]:
#     fig.delaxes(axes[i])
    
# fig.tight_layout()
# plt.subplots_adjust(top=0.9)
# fig.suptitle('Distribution of weigth per group', fontsize = 10, fontweight = 'bold')

# plt.show()
