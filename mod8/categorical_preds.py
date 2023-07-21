import pandas as pd
import numpy as np


def load_data(path):
    '''
    Given a path (str) to a csv returns a pandas dataframe
    '''
    df = pd.read_csv(path)
    return df

def bool_to_bin(df):
    '''
    Converts all True or False Values into binary (0 or 1)
    Returns a new df with the updates
    '''
    df_updated = df.copy(deep=True) # make a copy 
    for col in df.columns:
        if df[col].dtype == bool:
            df_updated[col] = df[col].astype(int)
    return df_updated

def remove_missing(df):
    '''
    Removes all records that contain missing values
    This will include categorical and numeric data
    A new df is returned rather than updated the one passed in
    '''
    df_copy = df.copy(deep=True)
    df_copy = df_copy.dropna() # removes all records with nan (missing values)
    return df_copy

def other_columns_describe(df, col, printInd):
    '''
    Function makes a count data frame of unique values of a column 
    and prints the results in order if printInd is set to True
    '''
    # Group by the unique values and provide a count
    countsDf = df.groupby([col], dropna=False).size().reset_index(name='counts')
    countsDf["rel_freq"] = (countsDf["counts"] / countsDf["counts"].sum() ) * 100 # make a relative frequency
    
    # figure out the threshold
    if printInd:
        print(countsDf.sort_values(by=["rel_freq"], ascending = True))
    return countsDf

def other_columns(df, col, threshold):
    '''
    Updates columns with frequency below a threshold to be labeled as other
    New df returned
    '''
    df_copy = df.copy(deep=True) # make a copy
    # Group by the unique values and provide a count
    countDf= other_columns_describe(df, col, False)
    
    # get all col values below the threshold
    countDf = countDf.loc[countDf["rel_freq"] < threshold]
    other_values = countDf[col].tolist()
    
    # update those columns to be other type
    df_copy.loc[(df_copy[col].isin(other_values)), col] = "other"
    
    return df_copy

def one_hot(df, col):
    '''
    Performs one hot encoding on a single column
    A new dataframe is returned
    One hot encoding is a list of binary values
    '''
    df_c = df.copy(deep=True)
    uniqueV = df[col].unique().tolist()
    cnt = len(uniqueV)
    one_hot_encoding = []
    
    for i, rw in df_c.iterrows():
        index = uniqueV.index(rw[col]) # index in unique list
        encoding = [ 1 if index ==i else 0 for i in range(cnt)] # set 1 if index else 0
        one_hot_encoding.append(encoding)
    df_c[col] = one_hot_encoding
    return df_c

def prep_for_training(df, label):
    '''
    To feed data into a ML model like NN,
    we need the data split into a features and label
    and the data should be stored in numpy arrays instead of pandas dfs
    '''
    cols = df.columns.tolist()
    cols.remove(label)
    
    y = df[label].to_numpy()
    x = df[cols].to_numpy()
    return x, y

def all_prep(file):
    carsDf = load_data(file)
    # convert True and False to 0 and 1
    carsDf = bool_to_bin(carsDf)
    
    # update each string record
    # Find all remaining columns
    str_cols = []
    threshold_mapping = {'manufacturer_name': 0.1,'model_name': 0.01,'transmission': 0.01,'color': 1,
                         'engine_fuel': 0.5,'engine_type': 0.001,'body_type': 1,'state': 0.1,
                         'drivetrain': 1,'location_region': 1}
    for col in carsDf:
        if carsDf[col].dtypes == object:
            str_cols.append(col)
    
    # Convert low frequency records to category other
    # combine Levels
    for col in str_cols:
        carsDf = other_columns(carsDf, col, threshold_mapping[col])

    
    # apply one hot to all columns
    carsDf = pd.get_dummies(carsDf, columns= str_cols)

    # remove Nans/Missing values
    carsDf= remove_missing(carsDf)

    # convert data to be feed into a ML model
    x, y = prep_for_training(carsDf,"price_usd")

    return x, y, carsDf



if __name__ == "__main__":
    x,y, df = all_prep("../data/cars.csv")