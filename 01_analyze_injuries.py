import pandas as pd

def analyze_injuries(path='data/injury_log.csv'):
    df = pd.read_csv(path)
    print("Injury count by body part:")
    print(df['body_part'].value_counts())
    print("\nInjury count by severity:")
    print(df['severity'].value_counts())

if __name__ == "__main__":
    analyze_injuries()