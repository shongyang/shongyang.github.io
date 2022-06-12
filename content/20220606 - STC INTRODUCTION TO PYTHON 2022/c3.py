import pyautogui as pg
import re

while True:
    input1 = pg.prompt(
        text="Please input email address", title="", default="example@example.com"
    )

    # print(input1)

    match = re.search(r"([\w.-]+)@([\w.-]+)", input1)
    if match:
        print(match.group())  ## 'example@example.com' (the whole match)
        print(match.group(1))  ## 'example' (the username, group 1)
        print(match.group(2))  ## 'example.com' (the host, group 2)
    elif input1 == "":
        break
    else:
        print("this ain't an email, try again")
