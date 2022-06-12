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

## CSV to Dictionary to Sum

import pandas as pd

# A Sample class with init method
class csv_to_dictsum:

    # init method or constructor
    # Constructors are used to initializing the object’s state, runs as soon as an object of a class is instantiated.
    def __init__(self, file):
        self.file = file

    # Sample Method
    def sum(self):
        with open(self.file, mode="r") as infile:
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


import pyautogui

input1 = pyautogui.prompt(text="", title="", default="data.csv")
p = csv_to_dictsum(input1)
p.sum()
