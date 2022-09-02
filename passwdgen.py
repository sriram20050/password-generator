from functions import * 
import random
import string

def main():
    # Generating per input length the random letters
    for i in range(lcount):
        print(random.choice(string.ascii_letters),end="")

    # Generating per input length random special characters
    for j in range(chars):
        print(random.choice('!@#$%&*'),end="")

    # Generating per input length the random numbers
    for k in range(nums):
        print(random.choice(random.choice(string.digits)),end="")

if __name__ == "__main__":
    main()