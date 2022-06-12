## From Challenge 04 - Create CSV file (optional, you may want to create using a spreadsheet program, e.g. Excel / LibreOffice, OpenOffice Calc / Google Sheets)

import csv

header = ["string", "integer", "float"]
data = [["a", "1", "1.1"], ["b", "2", "2.2"], ["c", "3", "3.3"]]

with open("data.csv", "w", encoding="UTF8", newline="") as f:
    writer = csv.writer(f)
    # Write the header
    writer.writerow(header)
    # Write multiple rows
    writer.writerows(data)

## Read selected columns from .csv file (INTEGER)

with open("data.csv", mode="r") as infile:
    reader = csv.reader(infile)
    with open("data_new.csv", mode="w") as outfile:
        writer = csv.writer(outfile)
        # mydict = {cols[0]: cols[1] for cols in reader}
        mydict = {rows[0]: rows[1] for rows in reader}

mydict.pop("string")
print(mydict)

integerstosum = list(mydict.values())

print(integerstosum)

sum = 0
for i in integerstosum:
    try:
        sum += int(i)
    except Exception:
        sum += float(i)

print(sum)

## Read selected columns from .csv file (FLOAT)

with open("data.csv", mode="r") as infile:
    reader = csv.reader(infile)
    with open("data_new.csv", mode="w") as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]: rows[2] for rows in reader}

mydict.pop("string")
print(mydict)

floatstosum = list(mydict.values())

print(floatstosum)

sum = 0
for f in floatstosum:
    try:
        sum += float(f)
    except Exception:
        sum += int(f)

print(sum)