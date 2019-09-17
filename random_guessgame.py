import random
win_no = random.randint(1,100)
guess = 1
n = int(input("guess no between 1 to 100"))
game_over = False

while not game_over:
    if n == win_no:
        print(f"you win, noof guesses is {guess}")
        game_over = True
    else:
        if n < win_no:
            print("too low")
           
        else:
            print("too high")
        guess += 1
        n = int(input("guess again"))   