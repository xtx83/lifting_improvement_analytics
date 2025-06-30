import pandas as pd
from load_data import load_lift_data

def detect_prs(df):
    return df.groupby('exercise').agg(
        heaviest_lift=('weight', 'max'),
        best_rep_volume=('volume', 'max'),
        most_reps=('reps', 'max')
    ).reset_index()

if __name__ == '__main__':
    df = load_lift_data()
    prs = detect_prs(df)
    print("Personal Records:") 
    print(prs)
