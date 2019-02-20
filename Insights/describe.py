# coding: utf-8
import pandas as pd

PATH = "../Data/train_set.zip"


def main():
    pd.options.display.max_columns = 100
    data = pd.read_csv(PATH)
    print(data.describe())


if __name__ == '__main__':
    main()
