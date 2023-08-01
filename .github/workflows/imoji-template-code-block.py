import csv
import json
import pandas as pd

f = "C:/amit/USD_CAR_CARS__ON_big_table_output_schema/USD_CAR_CARS__ON_big_table_output_schema.csv"


def read_csv(f):
    # f = "C:/amit/USD_CAR_CARS__ON_big_table_output_schema/USD_CAR_CARS__ON_big_table_output_schema.csv"

    with open(f, 'r') as file:
        raw = csv.reader(file)
        d = list(raw)
        return d


data = read_csv(f)
print(data)
