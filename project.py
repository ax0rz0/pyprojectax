import random #allows me to 'randomise', possible features is encrypting and decrypting the file for literally no reason 
import math #math
import io #i dont need this
import os #this MAKES and MANAGES the files universally
import time #half of these aren't needed but i prefer importing unrequired packages anyway to reduce possible error
banner = """
\033[31m
                                                                                                                           

                                                     ,----,                                                                          ,---,  
                                                   ,/   .`|                                                                       ,`--.' |  
,-.----.              ,--,    ,--,               ,`   .'  :  ,---,                          ,---,                                 |   :  :  
\    /  \           ,--.'|  ,--.'|             ;    ;     /,--.' |                        .'  .' `\    ,--,                       '   '  ;  
;   :    \   ,---.  |  | :  |  | :           .'___,/    ,' |  |  :                      ,---.'     \ ,--.'|                       |   |  |  
|   | .\ :  '   ,'\ :  : '  :  : '           |    :     |  :  :  :                      |   |  .`\  ||  |,                        '   :  ;  
.   : |: | /   /   ||  ' |  |  ' |           ;    |.';  ;  :  |  |,--.   ,---.          :   : |  '  |`--'_       ,---.     ,---.  |   |  '  
|   |  \ :.   ; ,. :'  | |  '  | |           `----'  |  |  |  :  '   |  /     \         |   ' '  ;  :,' ,'|     /     \   /     \ '   :  |  
|   : .  /'   | |: :|  | :  |  | :               '   :  ;  |  |   /' : /    /  |        '   | ;  .  |'  | |    /    / '  /    /  |;   |  ;  
;   | |  \'   | .; :'  : |__'  : |__             |   |  '  '  :  | | |.    ' / |        |   | :  |  '|  | :   .    ' /  .    ' / |`---'. |  
|   | ;\  \   :    ||  | '.'|  | '.'|            '   :  |  |  |  ' | :'   ;   /|        '   : | /  ; '  : |__ '   ; :__ '   ;   /| `--..`;  
:   ' | \.'\   \  / ;  :    ;  :    ;            ;   |.'   |  :  :_:,''   |  / |        |   | '` ,/  |  | '.'|'   | '.'|'   |  / |.--,_     
:   : :-'   `----'  |  ,   /|  ,   /             '---'     |  | ,'    |   :    |        ;   :  .'    ;  :    ;|   :    :|   :    ||    |`.  
|   |.'              ---`-'  ---`-'                        `--''       \   \  /         |   ,.'      |  ,   /  \   \  /  \   \  / `-- -`, ; 
`---'                                                                   `----'          '---'         ---`-'    `----'    `----'    '---`"  
                                                                                                                                            
                                                      -- Terminal Edition --                                                          
\033[31m
"""
print(banner)
# rolls dice and stores previous roll
def roll_dice():
    print("Rolling the dice", end="")
    for _ in range(3):  # animation for the dots
        time.sleep(1)  # sleep time
        print(".", end="", flush=True)  # add animation
    print() # blank space
    time.sleep(0.5)  
    roll = random.randint(1, 6)  # rolls the dice
    print(roll)  # prints the result
    store_roll(roll)  # store the roll in a file

# function to store the roll in a text file, ty gpt i cant figure this out 
def store_roll(roll):
    with open("dice_rolls.txt", "a") as file:  # open file
        file.write(f"{roll}\n")  # write the roll followed by a newline

# function to display previous rolls (ty gpt4o)
def display_previous_rolls():
    if os.path.exists("dice_rolls.txt"):
        with open("dice_rolls.txt", "r") as file:
            rolls = file.readlines()  # read all lines
            print("Previous Rolls:")
            for line in rolls:
                print(line.strip())  # print each roll, stripping whitespace
    else:
        print("No previous rolls found.")

# program >>LOOP<<
while True:
    UserInput = input("Type 'rtd' to roll the dice. Type 'previous' to display the dice rolling history, or 'exit' to quit: ").lower()
    
    if UserInput == "rtd":
        roll_dice()
    elif UserInput == "previous":
        display_previous_rolls()
    elif UserInput == "exit":
        print("See you again soon! ;)")
        time.sleep(0.5)
        print("Unloading and executing viruses, rats and malware..  ") #screw with the user
        time.sleep(2)
        print("Done!")
        time.sleep(0.5)
        break  # breaks the loop
    else:
        print("That command uh, doesn't exist, try again maybe using rtd or previous, or exit.")
