import pandas as pd
import numpy as np

# read in employee data
df = pd.read_csv('dirty_data.csv')

# set seed for reproducibility
np.random.seed(0)

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

## Scaling & Normalization ##########################################
