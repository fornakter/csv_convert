import csv
import pandas as pd


def open():
    text = []
    with open('product.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            text.append(row)
    title = []
    for i in range(12):
        title.append(text[i])
        df = pd.DataFrame(title)
        df.to_csv("product1.csv", sep=';')


if __name__ == '__main__':
    open()
