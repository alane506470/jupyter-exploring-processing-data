import numpy as np
from loadData import loadDate
import pandas as pd
def getData():
    df = loadDate()
    return df
def getDummies():
    df=getData()
    df['Deck']=df.Cabin.map(lambda x:get_deck(x))
    df['Title']=df.Name.map(lambda x:getTitleGroup(x))
    df['Fare_Bin']=pd.qcut(df.Fare,4,labels=['very_low','low','high','very_high'])
    df['isMother'] = np.where((df.Sex=='female')&(df.Parch>0)&(df.Age>18)&(df.Title!= 'Miss'),1,0)
    df['FamilySize']= df.Parch+df.SibSp+1
    df['AgeState']=np.where(df.Age>=18,'Adult','Child')
    df['isMale']=np.where(df.Sex=='male',1,0)
    #對分類要素進行編碼
    df=pd.get_dummies(df,columns=['Deck','Fare_Bin','Pclass','Title','Embarked','AgeState'])
    return df
def getTitleGroup(name):
    title_group={'mr':'Mr',
                 'mrs':'Mrs',
                 'miss':'Miss',
                 'master':'Master',
                 'don':'Sir',
                 'rev':'Sir',
                 'dr':'Officer',
                 'mme':'Mrs',
                 'ms':'Mrs',
                 'major':'Officer',
                 'lady':'Lady',
                 'sir':'Sir',
                 'mlle':'Miss',
                 'col':'Officer', 
                 'capt':'Officer',
                 'the countess':'Lady',
                 'jonkheer':'Sir',
                 'dona':'Lady'}
    first_name_with_title = name.split(',')[1]
    title=first_name_with_title.split('.')[0]
    #拿掉所有空格，轉成小寫
    title= title.strip().lower()
    return repr(title_group[title])
def get_deck(cabin):
    return np.where(pd.notnull(cabin),str(cabin)[0].upper(),'Z')
getDummies()
