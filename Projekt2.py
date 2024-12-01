"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Kristyna Fiedorova
email: adamcova.kris@gmail.com
discord: kristynafiedorova_88612
"""
from time import time
from datetime import timedelta
from random import randint

separator = "-" * 47
game_over = "** GAME OVER **".center(len(separator))
game_statistic = {}  # slovník pro ukládání statistik

while True:  # smyčka pro více her
    number = []
    while len(number) < 4:  # chci přesně 4 čísla
        digit = randint(0, 9)  # můžu vybírat náhodná čísla od 0 do 9
        if len(number) == 0 and digit == 0:  # pokud je první číslo 0, přeskočí tento krok
            continue  
        if digit not in number:  # přidá číslo do number, pokud tam ještě není    
            number.append(digit)

    numbers = ''.join(map(str, number))  # spojí čísla do jedné sekvence
    print(numbers)  #ODSTRANIT PŘED ODEVZDÁNÍM

    print(f"""
Hi there!
{separator}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{separator}
Enter the number:
{separator}
""")

    
    attempts = 0  # ukládá počty pokusů
    start_time = time()  # začne měřit čas

    
    while True:  # začíná hra
        guess = input("You can quit the game by 'q'. Enter the number: ")
        attempts += 1  # přidává jednotlivé pokusy

        if guess == "q":  # ukončí hádání
            print("You quit the game. Thanks for playing!")
            break
        elif not guess.isdigit():  # obsahuje nečíselné znaky
            print("Invalid input. Please enter only digits.")
            continue
        elif len(guess) != 4:  # kratší nebo delší než 4 čísla
            print("Your guess must be exactly 4 digits.")
            continue
        elif guess[0] == "0":  # začíná 0
            print("Your guess can't start with 0.")
            continue
        elif len(set(guess)) != 4:  # obsahuje duplicity
            print("Each digit in your guess must be unique.")
            continue
        elif guess == numbers:  # pokud se shodují ukončí hru
            stop_time = time()  # ukončí měření času
            delta_time = round(stop_time - start_time)  # zaokrouhlí na celá čísla
            formatted_time = str(timedelta(seconds=delta_time))  # vytvoří časový formát
            
            # přidání statistik do slovníku
            game_number = len(game_statistic) + 1
            game_statistic[game_number] = attempts

            print(f""">>>> {guess}
Correct, you've guessed the right number
in {attempts} guesses.
{separator}
That's amazing!""")
            print(f"You finished the game in {formatted_time}!")
            break
        else:  # pokud se neshodují, počítá bulls and cows
            bulls = 0
            cows = 0
            for n_digit, g_digit in zip(numbers, guess):  # porovná pozice čísel
                if g_digit == n_digit:
                    bulls += 1  # číslo se vyskytuje na stejné pozici
                elif g_digit in numbers:
                    cows += 1  # číslo se vyskytuje na jiné pozici

            bull_sp = "bull" if bulls == 1 else "bulls"
            cow_sp = "cow" if cows == 1 else "cows"

            print(f""">>>> {guess}
{bulls} {bull_sp}, {cows} {cow_sp}
Number of guess: {attempts}""")

    next_game = input("To play again, press 'y', to quit and see your stats, press any other key: ")  # zeptá se na další hru
    if next_game != "y":
        print(f"""{separator}
{game_over}
{separator} 
Thanks for playing! 
Here are your game statistics:""")
        for game, stats in game_statistic.items():
            print(f"Game {game}: {stats} guesses")
        break