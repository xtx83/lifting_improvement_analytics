import pandas as pd
import matplotlib.pyplot as plt
from load_data import load_lift_data

def plot_exercise_progress(df, exercise):
    subset = df[df['exercise'] == exercise]
    daily_max = subset.groupby('date')['weight'].max().reset_index()

    plt.figure(figsize=(10, 5))
    plt.plot(daily_max['date'], daily_max['weight'], marker='o')
    plt.title(f'{exercise.replace("_", " ").title()} Progress Over Time')
    plt.xlabel('Date')
    plt.ylabel('Max Weight')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    df = load_lift_data()
    plot_exercise_progress(df, 'bench_press')
