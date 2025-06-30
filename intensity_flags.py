import pandas as pd
from load_data import load_lift_data

def flag_intensity(df, threshold=0.9):
    df['is_high_intensity'] = df.groupby('exercise')['weight'].transform(
        lambda x: x >= x.max() * threshold
    )
    return df[df['is_high_intensity']]

if __name__ == '__main__':
    df = load_lift_data()
    flagged = flag_intensity(df)
    print("High intensity sets:")
    print(flagged[['date', 'exercise', 'weight', 'reps', 'is_high_intensity']])
