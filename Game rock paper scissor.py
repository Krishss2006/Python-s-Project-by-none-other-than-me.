# program of Rock paper scissor

import random
import time

print("\n\n\=====Welcome to=====")
print(" \n   ====Play Games ====")
print("\n====Rock paper & Scissor====")
print('''
\t1. Rock
\t2. Paper
\t3. Scissor
''')
user_scr = 0
comp_scr = 0

while True:
    opt = ['Rock','Paper','Scissor']
    cmp_ch = random.choice(opt)
    usr = int(input("Enter your choice(1 to 3): "))-1
    if usr == 0  or usr == 1 or usr== 2:
            print(f"\n\t        You chose: '{opt[usr]}' \n\tComputer chose:  '{cmp_ch}'")
            if (opt[usr] == cmp_ch):               
                print("\n\t\tDraw\n")
                time.sleep(1)
                print(f"\tYour score: {user_scr}  Computer's score \
{comp_scr}\n")                
            elif (opt[usr] == "Rock" and cmp_ch == "Paper") or \
               (opt[usr]  == "Paper" and cmp_ch == "Scissor") or \
               (opt[usr]  == "Scissor" and cmp_ch == "Rock"):
                print("\n\t\tYou loose\n")
                time.sleep(1)
                comp_scr+=1
                print(f"\tYour score: {user_scr}  Computer's score \
{comp_scr}\n")
                
            else:
                print("\n\t\tYOu won\n")
                time.sleep(1)
                user_scr+=1
                print(f"\tYour score: {user_scr}  Computer's score \
{comp_scr}\n")
    
    
    else:
        print("\n\t\tWrong Choice\n\t\tTry again\n")
