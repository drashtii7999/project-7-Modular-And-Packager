import datetime
import time
import math
import random
import uuid


def main():
    while True:
        print("\n--- MULTI-UTILITY TOOLKIT ---")
        print("1. Date & Time")
        print("2. Math")
        print("3. Random Password")
        print("4. Generate UUID")
        print("5. Save File")
        print("6. Explore Module")
        print("0. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            print(datetime.datetime.now())
            print("Time:", time.strftime("%H:%M:%S"))

        elif ch == "2":
            n = float(input("Enter number: "))
            print("Square root:", math.sqrt(n))
            print("Factorial:", math.factorial(int(n)))

        elif ch == "3":
            print("Password:", ''.join(
                random.choices(
                    "abcXYZ123@#$", k=8)))

        elif ch == "4":
            print("UUID:", uuid.uuid4())

        elif ch == "5":
            text = input("Enter text: ")
            save_file(text)

        elif ch == "6":
            print(dir(random))

        elif ch == "0":
            print("Thank you!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

import math

def save_file(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")
    print("File saved!")

def math_tool(n):
    return math.sqrt(n)

