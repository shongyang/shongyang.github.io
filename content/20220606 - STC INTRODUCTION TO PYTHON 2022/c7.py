# Make sure this file is moved to the unzipped folder before use.

########### VERSION A, Tax > Tech

import os

counter = 0
path = os.getcwd()
for file in os.listdir(path):
    if file.find("sunway tax club") > -1:
        counter = counter + 1
        os.rename(
            os.path.join(path, file),
            os.path.join(path, file.replace("sunway tax club", "sunway tech club")),
        )
if counter == 0:
    print("No file has been found")

########## REVERSAL, Tech > Tax

counter = 0
path = os.getcwd()
for file in os.listdir(path):
    if file.find("sunway tech club") > -1:
        counter = counter + 1
        os.rename(
            os.path.join(path, file),
            os.path.join(path, file.replace("sunway tech club", "sunway tax club")),
        )
if counter == 0:
    print("No file has been found")

############ ADVANCED, using Regular Expression

import re

counter = 0
path = os.getcwd()
for file in os.listdir(path):

    x = re.search("^sunway.*club.", file)

    if x:
        print("match")
        to_replace = x.group()
        os.rename(
            os.path.join(path, file),
            os.path.join(path, file.replace(to_replace, "sunway tech club")),
        )
    else:
        if file.find("sunway tax club") > -1:
            counter = counter + 1
            os.rename(
                os.path.join(path, file),
                os.path.join(
                    path, file.replace("sunway tax club", "sunway tech club ")
                ),
            )
if counter == 0:
    print("No file has been found")
