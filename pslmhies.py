# -*- coding: utf-8 -*-
"""PSLMHIES.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/141l61pdKmUgZEEv2K1tVo1bItnvL_9Lf
"""

from google.colab import drive
import sys

# Mount Google Drive
drive.mount('/content/drive')

# Get the absolute path of the current folder
abspath_curr = '/content/drive/My Drive/Colab Notebooks/'

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.preprocessing import MinMaxScaler

Hies_data = pd.read_stata(abspath_curr + '/data/PSLM_HIES/310_HIES201819_Rescaledbyhhsize_24618obs.dta')
print(Hies_data.head())

Pslm_data = pd.read_stata(abspath_curr + '/data/PSLM_HIES/310_PSLM201920_Rescaledbyhhsize_160654obs.dta')
Pslm_data.head()

Pslm_data['rural']



"""## Summary of PSLM and HIES

"""

variables_list1 = [
    "W_dkw_inspiped",
    "W_dkw_inshandpump",
    "W_dkw_insmotorpump",
    "W_dkw_insclosedwell",
    "W_dkw_insopenwell",
    "W_dkw_insprotsprng",
    "W_dkw_insunprsprng",
    "W_dkw_outpiped",
    "W_dkw_outhandpump",
    "W_dkw_outmotorpump",
    "W_dkw_outclosedwell",
    "W_dkw_outopenwell",
    "W_dkw_outprotsprng",
    "W_dkw_outunprsprng",
    "W_dkw_pond",
    "W_dkw_bottwater",
    "W_dkw_tanker",
    "W_dkw_filtration",
    "W_dkw_other",
    "W_toilet_notoilet",
    "W_toilet_flushpub",
    "W_toilet_flushtank",
    "W_toilet_flushpit",
    "W_toilet_flushopen",
    "W_toilet_raiselat",
    "W_toilet_pitlat",
    "W_toilet_other",
    "W_toiletshared",
    "W_toiletprivate",
    "H_cooking_firewood",
    "H_cooking_gas",
    "H_cooking_lpg",
    "H_cooking_dung",
    "H_cooking_crop",
    "H_cooking_other",
    "H_floor_earth",
    "H_floor_ceramic",
    "H_floor_cement",
    "H_floor_bricks",
    "H_floor_other",
    "H_roof_rccrbc",
    "H_roof_wood",
    "H_roof_sheet",
    "H_roof_grader",
    "H_roof_other",
    "H_walls_burntbricks",
    "H_walls_mudbricks",
    "H_walls_wood",
    "H_walls_stones",
    "H_walls_other",
    "D_iradio",
    "D_itelevsion",
    "D_ilcdled",
    "D_irefrigerator",
    "D_ifreezer",
    "D_iwashing",
    "D_idryer",
    "D_iairconditioning",
    "D_iaircooler",
    "D_ifan",
    "D_istove",
    "D_icookingrange",
    "D_imicrowave",
    "D_isewingmachine",
    "D_iknitting",
    "D_iiron",
    "D_iwaterfilter",
    "D_idonkeypump",
    "D_iturbine",
    "D_ichair",
    "D_itable",
    "D_iups",
    "D_igenerator",
    "D_isolarpanel",
    "D_iheater",
    "D_igeaser",
    "D_ibicycle",
    "D_imotorcyclescotter",
    "D_irichshaw",
    "D_icar",
    "D_ivantruckbus",
    "D_iboat",
    "D_itractortralloy",
    "D_iclock"
]

selected_variables = Pslm_data[variables_list1]
means = selected_variables.mean()
std_devs = selected_variables.std()
# Count the number of missing values for each variable
missing_values = selected_variables.isna().sum()


selected_variables1 = Hies_data[variables_list1]
means1 = selected_variables1.mean()
std_devs1 = selected_variables1.std()
# Count the number of missing values for each variable
missing_values1 = selected_variables1.isna().sum()

Summary_data = pd.DataFrame({'Mean': means, 'Std':std_devs, 'Missing Values':missing_values,
                             'Mean1': means1, 'Std1':std_devs1, 'Missing Values1':missing_values1})

Summary_data

"""## Summary of Urban for both PSLM and HIES"""

selected_variables = Pslm_data[Pslm_data['rural'] == 'urban'][variables_list1]
means = selected_variables.mean()
std_devs = selected_variables.std()
# Count the number of missing values for each variable
missing_values = selected_variables.isna().sum()


selected_variables_hies = Hies_data[Hies_data['rural'] == 'urban'][variables_list1]
means1 = selected_variables1.mean()
std_devs1 = selected_variables1.std()
# Count the number of missing values for each variable
missing_values1 = selected_variables1.isna().sum()

Summary_data = pd.DataFrame({'Mean': means, 'Std':std_devs, 'Missing Values':missing_values,
                             'Mean1': means1, 'Std1':std_devs1, 'Missing Values1':missing_values1})

Summary_data

"""## Summary of Rural for both PSLM and HIES"""

selected_variables = Pslm_data[Pslm_data['rural'] == 'rural'][variables_list1]
means = selected_variables.mean()
std_devs = selected_variables.std()
# Count the number of missing values for each variable
missing_values = selected_variables.isna().sum()


selected_variables_hies = Hies_data[Hies_data['rural'] == 'rural'][variables_list1]
means1 = selected_variables1.mean()
std_devs1 = selected_variables1.std()
# Count the number of missing values for each variable
missing_values1 = selected_variables1.isna().sum()

Summary_data = pd.DataFrame({'Mean': means, 'Std':std_devs, 'Missing Values':missing_values,
                             'Mean1': means1, 'Std1':std_devs1, 'Missing Values1':missing_values1})

Summary_data

"""## PCA for PSLM"""

# Extract the selected columns
selected_variables = Pslm_data[variables_list1].copy()

# Drop rows with missing values
selected_variables = selected_variables.dropna()

# Perform Min-Max scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(selected_variables)

# Perform PCA
pca = PCA(n_components=1)
asset_index = pca.fit_transform(scaled_data)

# Print the explained variance
print('PCA variance explained: %.2f%%' % (100 * pca.explained_variance_ratio_[0]))

# Create the basis vector DataFrame
basis_vector = pd.DataFrame({'Asset': variables_list1, 'Magnitude': pca.components_[0]})

# Sort the basis vector by magnitude in descending order
basis_vector = basis_vector.sort_values(by='Magnitude', ascending=False)

# Save the basis vector to a CSV file
basis_vector.to_csv('asset_index_PSLM_basis_vector.csv', index=False)

"""## PCA for Urban of PSLM"""

selected_variables = Pslm_data[Pslm_data['rural']=='urban'][variables_list1]
# Drop rows with missing values
selected_variables = selected_variables.dropna()

# Perform Min-Max scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(selected_variables)

# Perform PCA
pca = PCA(n_components=1)
asset_index = pca.fit_transform(scaled_data)

# Print the explained variance
print('PCA variance explained: %.2f%%' % (100 * pca.explained_variance_ratio_[0]))

# Create the basis vector DataFrame
basis_vector = pd.DataFrame({'Asset': variables_list1, 'Magnitude': pca.components_[0]})

# Sort the basis vector by magnitude in descending order
basis_vector = basis_vector.sort_values(by='Magnitude', ascending=False)

# Save the basis vector to a CSV file
basis_vector.to_csv('asset_index_PSLM_URBAN_basis_vector.csv', index=False)

"""## PCA for Rural of PSLM"""

selected_variables = Pslm_data[Pslm_data['rural']=='rural'][variables_list1]
# Drop rows with missing values
selected_variables = selected_variables.dropna()

# Perform Min-Max scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(selected_variables)

# Perform PCA
pca = PCA(n_components=1)
asset_index = pca.fit_transform(scaled_data)

# Print the explained variance
print('PCA variance explained: %.2f%%' % (100 * pca.explained_variance_ratio_[0]))

# Create the basis vector DataFrame
basis_vector = pd.DataFrame({'Asset': variables_list1, 'Magnitude': pca.components_[0]})

# Sort the basis vector by magnitude in descending order
basis_vector = basis_vector.sort_values(by='Magnitude', ascending=False)

# Save the basis vector to a CSV file
basis_vector.to_csv('asset_index_PSLM_RURAL_basis_vector.csv', index=False)

"""##PCA for HIES"""

# Extract the selected columns
selected_variables = Hies_data[variables_list1].copy()

# Drop rows with missing values
selected_variables = selected_variables.dropna()

# Perform Min-Max scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(selected_variables)

# Perform PCA
pca = PCA(n_components=1)
asset_index = pca.fit_transform(scaled_data)

# Print the explained variance
print('PCA variance explained: %.2f%%' % (100 * pca.explained_variance_ratio_[0]))

# Create the basis vector DataFrame
basis_vector = pd.DataFrame({'Asset': variables_list1, 'Magnitude': pca.components_[0]})

# Sort the basis vector by magnitude in descending order
basis_vector = basis_vector.sort_values(by='Magnitude', ascending=False)

# Save the basis vector to a CSV file
basis_vector.to_csv('asset_index_HIES_basis_vector.csv', index=False)

"""## PCA for Urban of HIES"""

# Extract the selected columns
#selected_variables = Hies_data[variables_list1].copy()
selected_variables = Hies_data[Hies_data['rural']=='urban'][variables_list1]
# Drop rows with missing values
selected_variables = selected_variables.dropna()

# Perform Min-Max scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(selected_variables)

# Perform PCA
pca = PCA(n_components=1)
asset_index = pca.fit_transform(scaled_data)

# Print the explained variance
print('PCA variance explained: %.2f%%' % (100 * pca.explained_variance_ratio_[0]))

# Create the basis vector DataFrame
basis_vector = pd.DataFrame({'Asset': variables_list1, 'Magnitude': pca.components_[0]})

# Sort the basis vector by magnitude in descending order
basis_vector = basis_vector.sort_values(by='Magnitude', ascending=False)

# Save the basis vector to a CSV file
basis_vector.to_csv('asset_index_HIES_URBAN_basis_vector.csv', index=False)

"""## PCA for Rural of HIES"""

selected_variables = Hies_data[Hies_data['rural']=='rural'][variables_list1]
# Drop rows with missing values
selected_variables = selected_variables.dropna()

# Perform Min-Max scaling
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(selected_variables)

# Perform PCA
pca = PCA(n_components=1)
asset_index = pca.fit_transform(scaled_data)

# Print the explained variance
print('PCA variance explained: %.2f%%' % (100 * pca.explained_variance_ratio_[0]))

# Create the basis vector DataFrame
basis_vector = pd.DataFrame({'Asset': variables_list1, 'Magnitude': pca.components_[0]})

# Sort the basis vector by magnitude in descending order
basis_vector = basis_vector.sort_values(by='Magnitude', ascending=False)

# Save the basis vector to a CSV file
basis_vector.to_csv('asset_index_HIES_RURAL_basis_vector.csv', index=False)