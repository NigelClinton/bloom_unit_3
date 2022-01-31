def null_count_df(df):
    frame=pd.DataFrame()
    frame['missing_no']=df.isnull().sum()
    frame['missing_rate']=df.isnull().sum()/len(df)
    frame=frame.loc[frame['missing_rate']>0].sort_values(by='missing_rate',ascending=False)
    frame['bigger_005']=frame['missing_rate'].map(lambda x:1 if x>=0.05 else 0)
    return frame

def zero_count(df):
    df.eq(0).sum().to_frame(name='zero_count')