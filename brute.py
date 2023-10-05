import random
import numbers

chars = ("abcdefghijklmnopqrstuvwxyz012456789!@#$^&*_-")
chars_list = list(chars)
password = input("enter your password: ")
guess = ""

while guess != password:
    guess = random.choices(chars_list, k=len(password))
    print(guess)
    guess = "".join(guess)
print(f"your password is: {guess}")