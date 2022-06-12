import re

## Suppose we have a text with many email addresses
input1 = input(
    "Key in an email address; or multiple email addresses, each separated with a COMMA  =   "
)

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r"[\w\.]+@[\w\.]+", input1)  # abc.def@ghi.jkl.mno, ...
for email in emails:
    # do something with each found email string
    print(email)  # abc.def@ghi.jkl.mno
    match = re.search(r"([\w\.-]+)@([\w]+).([\w]+).([\w]+)", email)
    print(match.group(1))  # abc.def
    print(match.group(2))  # @ghi > ghi
    print(match.group(3))  # .jkl > jkl
    print(match.group(4))  # .mno > mno
