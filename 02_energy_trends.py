import pandas as pd
import matplotlib.pyplot as plt

def plot_energy_trend(path='data/energy_mood_log.csv'):
    df = pd.read_csv(path)
    df['date'] = pd.to_datetime(df['date'])
    energy_map = {'low': 1, 'moderate': 2, 'high': 3}
    df['energy_score'] = df['energy_level'].map(energy_map)
    trend = df.groupby('date')['energy_score'].mean()
    trend.plot(title='Average Energy Score Over Time')
    plt.xlabel('Date')
    plt.ylabel('Energy Score')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_energy_trend()