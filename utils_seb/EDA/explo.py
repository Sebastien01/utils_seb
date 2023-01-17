import pandas as pd


def display_nunique(df:pd.DataFrame):
    """
    Displays the number of uniques values for each col in DF
    """
    
    df = sorted([(col, df[col].nunique()) for col in df.columns], key=lambda x: x[1], reverse=True)
    return pd.DataFrame(df,columns=['col_name', 'n_uniques'])