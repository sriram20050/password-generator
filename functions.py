def letter_count():
    global lcount
    while True:
        try:
            lcount = int(input("How many letters? "))
            if lcount > 2:
                return lcount
            else:
                print("Low letter count, please re-enter.")
                continue
        except ValueError:
            print("Enter a valid count value of letters.")
            continue
        
def schar_count():
    global chars
    while True:
        try:
            chars = int(input("How many special characters? "))
            return chars
        except ValueError:
            print("Enter a valid count value of special characters.")
            continue

def numbers():
    global nums
    while True:
        try:
            nums = int(input("How many numbers? "))
            if nums > 2:
                return nums
            else:
                print("Low amount of numbers, please re-enter")
                continue
        except ValueError:
            print("Value does not consist of count of numericals, please re-enter.")
            continue

letter_count()
schar_count()
numbers()