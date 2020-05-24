import pandas as pd
import numpy as np
import os
def loadDate():
    raw_data_path = os.path.join(os.path.pardir,'data','raw')
    train_file_path = os.path.join(os.path.join(raw_data_path,'train.csv'))
    test_file_path = os.path.join(os.path.join(raw_data_path,'test.csv'))
    train_df = pd.read_csv(train_file_path,index_col='PassengerId')
    test_df = pd.read_csv(test_file_path,index_col='PassengerId')
    df= pd.concat((train_df,test_df),axis=0)
    return df
