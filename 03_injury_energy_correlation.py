import pandas as pd

def correlate_injuries_with_energy(injury_path='data/injury_log.csv', energy_path='data/energy_mood_log.csv'):
    injury_df = pd.read_csv(injury_path)
    energy_df = pd.read_csv(energy_path)
    low_energy_days = energy_df[energy_df['energy_level'] == 'low']['date'].tolist()
    correlated = injury_df[injury_df['date'].isin(low_energy_days)]
    print("Injuries that occurred on low energy days:")
    print(correlated)

if __name__ == "__main__":
    correlate_injuries_with_energy()