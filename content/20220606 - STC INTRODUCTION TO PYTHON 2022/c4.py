## Create CSV file (optional, you may want to create using a spreadsheet program, e.g. Excel / LibreOffice, OpenOffice Calc / Google Sheets)

import csv

header = ["string", "integer", "float"]
data = [["a", "1", "1.1"], ["b", "2", "2.2"], ["c", "3", "3.3"]]

with open("data.csv", "w", encoding="UTF8", newline="") as f:
    writer = csv.writer(f)
    # Write the header
    writer.writerow(header)
    # Write multiple rows
    writer.writerows(data)

## Convert CSV file to dictionary

import pandas as pd

## INTEGER
# Read specific columns of csv file using Pandas
df = pd.read_csv("data.csv", usecols=["string", "integer"])
df.dropna()
outfile = open("data_integer.csv", "w")
df.to_csv(
    outfile, index=False, header=True, line_terminator="\n", sep=",", encoding="utf-8"
)
outfile.close()

print(df)

reader = csv.reader(open("data_integer.csv", "r"))
d = {}
for row in reader:
    k, v = row
    d[k] = v

print(d)

res = str(list(d.keys()))
print(res)

res = str(list(d.values()))
print(res)

## FLOAT
# Read specific columns of csv file using Pandas
df = pd.read_csv("data.csv", usecols=["string", "float"])
df.dropna()
outfile = open("data_float.csv", "w")
df.to_csv(
    outfile, index=False, header=True, line_terminator="\n", sep=",", encoding="utf-8"
)
outfile.close()

print(df)

reader = csv.reader(open("data_float.csv", "r"))
d = {}
for row in reader:
    k, v = row
    d[k] = v

print(d)

res = str(list(d.keys()))
print(res)

res = str(list(d.values()))
print(res)