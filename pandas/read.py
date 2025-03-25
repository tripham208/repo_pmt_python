import pandas as pd

if __name__ == '__main__':
    """
    There can be too much data to hold in memory
    Solution: load data in chunks
    """
    for chunk in pd.read_csv('data.csv', chunksize=1000):
        pass