import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats # for Box-Cox tranformation
from mlxtend.preprocessing import minmax_scaling # minmax scaling

# set seed for reproducibility
np.random.seed(0)

# read in employee data
df = pd.read_csv('csv_files/dirty_data.csv')

## Missing Values ################################################
# get number of missing values per col
missing_counts = df.isnull().sum()

# get percent of missing data
total_cells = np.product(df.shape) # 300
total_missing = missing_counts.sum() # 47
percent_missing = (total_missing/total_cells)*100 # 15.666

# Imputation: is determining if data is missing because it doesn't
# exist or is not recorded. Data that doesn't exist (e.g. the
# height of first-born child to a man without children) could
# potentially be left as NaN, while not recorded data could possibly
# be guessed. Look at the dataset to determine what to do.

# Dropping rows/cols is a quick & dirty way to handle this.
# (Note: this probably shouldn't be done on important projects)
df.dropna() # removes rows with NaN values
df.dropna(axis=1) # removes cols with NaN values

# Replace all missing values
df.fillna('Unknown')

# Backfill missing values (copy next value) then replace.
# This may not make sense to do for all datasets (like this one).
# axis=0 (default) copies across rows (downwards), 1 is across cols.
df.bfill().fillna('Unknown')

## Scaling ###########################################################
# Transorm data so that it fits within a certain range/scale.
# such as 0-1 or 0-100. This helps compare variables equally. For
# example, scaling Yen and USD (1 yen is worth less than 1 USD).
# Or scaling height and weight.

# generate 1000 random points from exponential distribution
data = np.random.exponential(size=1000)

# min-max scale the data between 0 and 1
scaled_data = minmax_scaling(data, columns=[0])

# plot both together
fig, ax = plt.subplots(1, 2, figsize=(15,3)) # 1 row, 2 cols, size inch
sns.histplot(data, ax=ax[0], kde=True, legend=False)
ax[0].set_title('Original Data')
sns.histplot(scaled_data, ax=ax[1], kde=True, legend=False)
ax[1].set_title('Scaled Data')
plt.savefig('plots/scaled.png') # The scaled data retains its shape

## Normalization #####################################################
# Change data so it can be described as a normal distribution.

# Normal (Guassian) Distribution: Roughly equal amount of observations
# fall above and below the mean. The mean and median are equal.
# Also called a bell curve.

# normalize data from prev section using boxcox.
# (Note: this produces a tuple when input is multidimensional where
#    result[0] is the transformed data and result[1] is lambda value)
normalized_data = stats.boxcox(data)

# plot both together
fig, ax = plt.subplots(1, 2, figsize=(15,3)) # 1 row, 2 cols, size inch
sns.histplot(data, ax=ax[0], kde=True, legend=False)
ax[0].set_title('Original Data')
sns.histplot(normalized_data, ax=ax[1], kde=True, legend=False)
ax[1].set_title('Normalized Data')
plt.savefig('plots/normalized.png') # The shape of the data changed

## Parsing Dates ####################################################
