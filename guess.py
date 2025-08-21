import random

number = random.randint(1, 5)
while True:
    try:
        guess = input("Guess a number between 1 and 5: ")
        if int(guess) == number:
            print("Correct!")
            break
        else:
            print("Incorrect!")
            continue
    except (EOFError, ValueError):
        break
    


