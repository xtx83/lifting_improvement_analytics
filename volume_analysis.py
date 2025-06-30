import pandas as pd
from load_data import load_lift_data

def weekly_volume_summary(df):
    df['week'] = df['date'].dt.isocalendar().week
    volume_summary = (
        df.groupby(['week', 'exercise'])
          .agg(total_volume=('volume', 'sum'), avg_intensity=('weight', 'mean'))
          .reset_index()
          .sort_values(by=['week', 'exercise'])
    )
    return volume_summary

if __name__ == '__main__':
    df = load_lift_data()
    summary = weekly_volume_summary(df)
    print(summary)
