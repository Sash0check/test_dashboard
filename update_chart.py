import pandas as pd

if __name__ == '__main__':
    data = {'x': [1, 2, 3], 'y': [4, 1, 2]}
    df = pd.DataFrame(data)
    df.to_csv("data.csv", index=False)