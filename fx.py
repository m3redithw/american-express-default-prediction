import pandas as pd
import numpy as np
import datetime as dt

def aggregate_features(df, num_cols):
    
    new_df = pd.DataFrame({'customer_ID': df['customer_ID'].unique()})
    
    for col in num_cols:
        min = df.groupby('customer_ID')[col].min()
        max = df.groupby('customer_ID')[col].max()
        mean = df.groupby('customer_ID')[col].mean()
        std = df.groupby('customer_ID')[col].std()
        first = df.groupby('customer_ID')[col].first()
        last = df.groupby('customer_ID')[col].last()
        change = last - first
    
        stats = pd.DataFrame({f'{col}_min': min, f'{col}_max': max,
                              f'{col}_median': mean, f'{col}_std': std,
                              f'{col}_last': last, f'{col}_change': change})
    
        stats.reset_index(drop=True, inplace=True)
    
        new_df = pd.concat([new_df, stats], axis=1)
        
    new_df.set_index('customer_ID', inplace=True)
    
    new_df.fillna(0, inplace=True)
    
    return new_df



def handle_categories(df):
    
    categorical_columns = ['B_30', 'B_38', 'D_114', 'D_116', 'D_117', 'D_120', 'D_126', 'D_63', 'D_64', 'D_66', 'D_68']
    
    dummy_df = pd.get_dummies(df[categorical_columns].astype('category'), dummy_na=True)
    
    id_df = pd.DataFrame(df['customer_ID'])
    
    dummy_df = pd.concat([id_df, dummy_df], axis=1)
    
    dummy_last = dummy_df.groupby('customer_ID').agg('last')
    
    return dummy_last, categorical_columns





def age_calculator(df):
    
    def datetimer(string):
        return dt.datetime.strptime(string, '%Y-%m-%d')
    
    df['S_2'] = df['S_2'].apply(datetimer)
    
    min_dates = pd.DataFrame(df.groupby('customer_ID').S_2.min())
                             
    min_dates.rename(columns={'S_2': 'min_dates'}, inplace=True)
                             
    df = df.merge(min_dates, how='left', on='customer_ID')
                             
    df['age'] = (df['S_2'] - df['min_dates']).dt.days
                             
    df.drop(columns=['S_2', 'min_dates'], inplace=True)
                             
    return df


def impute_numerical_nulls(df, num_cols):
    
    for col in num_cols:
        df[col].fillna(col.mean(), inplace=True)
        
    return df    
                