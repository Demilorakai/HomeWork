import re

class ValidCarNumber:
    ValidCarNumber = input("Transport number: ")
    is_valid = re.search(r"([0-9]{2})-KG-([0-9]{3})-BAD", ValidCarNumber)
    if not is_valid:
        print("Transport number Invalid!")
    elif ValidCarNumber[is_valid.start():is_valid.end()] == ValidCarNumber:
        print("Transport number Valid!!!")