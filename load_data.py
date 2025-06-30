import pandas as pd

def load_lift_data(filepath='../data/lifts.csv'):
    df = pd.read_csv(filepath, parse_dates=['date'])
    df['volume'] = df['weight'] * df['reps']
    return df

if __name__ == '__main__':
    df = load_lift_data()
    print(df.head())
