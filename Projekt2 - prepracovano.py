"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Kristyna Fiedorova
email: adamcova.kris@gmail.com
discord: kristynafiedorova_88612
"""
from time import time
from datetime import timedelta
from random import randint
import random

separator = "-" * 47
game_over = "** GAME OVER **".center(len(separator))



def generate_number():
    """
    Generates a random 4-digit number with unique digits.
    The first digit is non-zero (1-9).
    The remaining three digits are unique and may include zero.

    Returns:
        A 4-digit number as a string.
    """
    code = random.sample(range(1, 10), 1)  # První číslo není 0
    code += random.sample([digit for digit in range(10) if digit not in code], 3) 
    return "".join(map(str,code))


def validate_guess(guess):
    """ 
    Validates the user's guess. 
    The guess must be only 4-digit number starting with non-zero digit 
    and containing unique digits.

    Returns:
        None: If the input is valid.
        str: An error message if the input is invalid.
    """     

    if not guess.isdigit():  # obsahuje nečíselné znaky
        return "Invalid input. Please enter only digits."
    elif len(guess) != 4:  # kratší nebo delší než 4 čísla
        return "Your guess must be exactly 4 digits."
    elif guess[0] == "0":  # začíná 0
        return "Your guess can't start with 0."
    elif len(set(guess)) != 4:  # obsahuje duplicity
        return "Each digit in your guess must be unique."


def calculate_bulls_and_cows(numbers, guess):
    """
    Compares the user's guess with the correct number and calculates 
    the number of bulls and cows. Bulls represent digits in the same position, 
    while cows represent digits that exist in the correct number but are in the 
    different position.

    Args:
        numbers (str): The correct 4-digit number.
        guess (str): The user's guess.

    Returns:
        tuple: A tuple containing the count of bulls and cows.
    """
    
    bulls = 0
    cows = 0
    for n_digit, g_digit in zip(numbers, guess):  # porovná pozice čísel
        if g_digit == n_digit:
            bulls += 1  # číslo se vyskytuje na stejné pozici
        elif g_digit in numbers:
            cows += 1  # číslo se vyskytuje na jiné pozici
    
    return bulls, cows


def print_intro():
    """
    Prints introduction message for the game.

    Returns:
        None
    """
    print(f"""
Hi there!
{separator}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{separator}
Enter the number:
{separator}
""")
    

def print_statistics(game_statistic):
    """ 
    Prints the game statistics at the end of the session.

    Displays a summary of all games played, including the game number 
    and the number of attempts for each game.

    Args:
        game_statistics (dict): A dictionary where keys are game numbers 
        and values are the number of attemps for each game.

    Returns:
        None
    """
    print(f"""{separator}
{game_over}
{separator} 
Thanks for playing! 
Here are your game statistics:""")
    for game, stats in game_statistic.items():
        print(f"Game {game}: {stats} guesses")


def play_game():
    """
    Runs the main game loop for bulls and cows.

    The game generates a random 4-digit number with unique digits, 
    and the user may guess it. The function provides feedback on each guess 
    (bulls and cows) and tracks the number of attempts and elapsed time. 
    After the game ends, statistics are displayed.

    The users can quit by entering 'q'.

    Returns:
        None: The function does not return any value. The game runs until 
        the user chooses to quit.  
    """
    game_statistic = {}  # slovník pro ukládání statistik

    while True: #smyčka pro více her
        numbers = generate_number()
        print(numbers) ###ODSTRANIT PŘED ODEVZDÁNÍM###
        print_intro()

        attempts = 0  # ukládá počty pokusů
        start_time = time()  # začne měřit čas

        while True: # začíná hra
            guess = input("You can quit the game by 'q'. Enter the number: ") 
            if guess == "q": # ukončí hádání
                print("You quit the game. Thanks for playing!")
                return
            attempts += 1  # přidává jednotlivé pokusy

            error = validate_guess(guess)
            if error:
                print(error)
                continue
            if guess == numbers:  # pokud se shodují ukončí hru
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

            bulls, cows = calculate_bulls_and_cows(numbers, guess)
            bull_sp = "bull" if bulls == 1 else "bulls"
            cow_sp = "cow" if cows == 1 else "cows"

            print(f""">>>> {guess}
{bulls} {bull_sp}, {cows} {cow_sp}
Number of guess: {attempts}""")
        
        next_game = input("To play again, press 'y', to quit and see your stats, press any other key: ")  # zeptá se na další hru
        if next_game != "y":
            print_statistics(game_statistic)
            break

if __name__== "__main__":
    play_game()