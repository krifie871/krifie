"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kristýna Fiedorová
email: adamcova.kris@gmail.com
discord: kristynafiedorova_88612
"""

# seznam registrovaných uživatelů
registered_user = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

# vloží jméno a heslo
user = input("user:",)
password = input("password:",)

print(41 * "-")

# pokud je uživatel mezi registrovanými uživateli, pozdraví ho to a pustí dál
if not registered_user.get(user) == password:
    print("Unregistered user or password, terminating the program..")
    quit()    
else: print("Welcome to the app,", user) #pustí mě to k dalšímu kódu

print("We have 3 texts to be analyzed.")
print(41 * "-")

'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
choose_text = input("Choose your text between 1-3:")  #uživatel si vybere text přečíslovaný na 1-3

if not choose_text.isdigit():
    print("Invalid input, terminating the program..")
    quit()
else:
    choose_text = int(choose_text) -1 #pokud vybere číslo, tak přečísluje texty

    if choose_text not in range(0, 3): #pokud uživatel nezadá 1-3, upozorní a ukončí program
        print("Text is not available, terminating the program..")
        quit()
        
print(41 * "-")

# odstraní z textu "." a ","
text_cleaned = TEXTS[choose_text].replace(".", "") \
                                 .replace(",", "")

# jednotlivá slova v textu vybraným uživatelem 
words = text_cleaned.split()

# STATITIKY PRO VYBRANÝ TEXT:
# počet slov
count_words = len(words)
print("There are", count_words, "words in the selected text.")

# počet slov začínajících velkým písmenem 
count_words_cap = [word for word in words if word.istitle()]
print("There are", (len(count_words_cap)), "titlecase words.")

# počet slov psanými velkými písmeny
count_words_up = [word for word in words if word.isalpha() and word.isupper()]
print("There are", (len(count_words_up)), "uppercase words")

# počet slov psanými malými písmeny
count_words_low = [word for word in words if word.islower()]
print("There are", (len(count_words_low)), "lowercase words.")

# počet čísel
count_numbers = []

for word in words:
    if word.isdigit():
        count_numbers.append(int(word))

print("There are", (len(count_numbers)), "numeric strings.")

# suma všech čísel
count_sum = sum(count_numbers)
print("The sum of all the numbers",(count_sum))

print(41 * "-")

#PROGRAM zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. 

word_lengths = {}
for word in words:
    length = len(word) # délky slov v textu
    if length in word_lengths:
        word_lengths[length] += 1 # pokud tam ta délka je, tak ji připočte k četnosti
    else:
        word_lengths[length] = 1 # pokud tam ta délka ještě není, tak nastaví hodnotu jedna
              

word_lengths_sorted = sorted(word_lengths.items()) #seřadí mi klíče ve slovníku 

print("LEN|   OCCURENCES    |NR.")
print(41 * "-")

#iterování přes klíč i hodnoty
for length, frequency in word_lengths_sorted:
    print(str(length).ljust(3) + "|" + ("*" * frequency).ljust(17) + "| " + str(frequency))