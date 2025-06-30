import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_lift_data

def plot_weekly_trends(df):
    df['week'] = df['date'].dt.isocalendar().week
    trend_data = df.groupby(['week', 'exercise'])['volume'].sum().unstack(fill_value=0)

    trend_data.plot(kind='bar', stacked=True, figsize=(12, 6))
    plt.title('Weekly Training Volume by Exercise')
    plt.xlabel('Week Number')
    plt.ylabel('Total Volume (lbs)')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    df = load_lift_data()
    plot_weekly_trends(df)
