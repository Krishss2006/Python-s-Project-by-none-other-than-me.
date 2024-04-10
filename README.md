Sure, here's the updated README with the code snippets placed right after the project descriptions:

```markdown
# Welcome to Krishna's Python Playground! 🐍

Hey there! Welcome to my corner of GitHub where I store all my Python projects.
 Whether you're here out of curiosity or looking for some fun Python stuff,
you're in the right place!

## About Me

👋 Hi, I'm Krishna, a 12th-grade student or uhmm! just took 12th Board So,
 no more 12th-Grade Student until the result is declared.
And I'm from the beautiful city of Lucknow, India. I'm passionate about
 programming, especially in Python.

## Projects

### [1. Number to Words Converter](#number-to-words-converter)

Ever wondered how to convert numbers into words? Look no further!
With this handy Python script, you can easily convert any number
into its word representation.

```python
def number_to_words(num):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 0 <= num <= 9:
        print(num)
        return ones[num]
    elif 11 <= num <= 19:
        return teens[num - 10]
    elif 21 <= num <= 99:
        return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")
    elif num == 10:
        return tens[1]
    else:
        return "Number out of range"

# Example usage
user_input = int(input("Enter a number: "))
result = number_to_words(user_input)
print(result)
```

### [2. Rock, Paper, Scissors Game](#rock-paper-scissors-game)

Feeling competitive? Dive into the classic game of Rock, Paper,
Scissors with this Python program. Test your luck against the computer
and see who comes out on top!

```python
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

```

### [3. Personal Dictionary](#personal-dictionary)

Expand your vocabulary with this Personal Dictionary Python script.
 It uses the NLTK library to provide definitions, synonyms, and
 antonyms for any word you enter.

```python
# use -- pip install nltk
   to install the nltk (Natural Language Tookkit) python library

import nltk  # (Natural Language Tookkit)
from nltk.corpus import wordnet

# Once the wordnet get downloaded comment out the below lines
nltk.download('wordnet')

print("Welcome to Personal Dictionary")
choice = 'y'
while choice == 'y':
    word = input('Enter the word: ')
    synsets = word

net.synsets(word)

    definitions = []
    for synset in synsets:
        definitions.append(synset.definition())

    synonyms = set()
    for synset in synsets:
        synonyms.update([lemma.name() for lemma in synset.lemmas()])

    antonyms = set()
    for synset in synsets:
        antonyms.update([
            antonym.name() for lemma in synset.lemmas()
            for antonym in lemma.antonyms()
        ])
        
    if synsets:
        print(f"\nDefinitions: {', '.join(definitions)}")
        
        if synonyms:
            print(f"\nSynonyms: {', '.join(synonyms)}")
        else:
            print(f"\nNo Synonyms available for word {word}")
            
        if antonyms:
            print(f"\nAntonyms: {', '.join(antonyms)}")
        else:
            print(f"\nNo Antonyms available for word {word}")

    else:
        print(f'\nNothing found related to given word {word}')

    choice = input("\nDo you want to continue(y/n)")
    
print("Thank you for using our service.")

```

### [4. Survey GUI App](#survey-gui-app)

Add some fun to your day with this Survey GUI App built using Tkinter.
It's a simple tkinter application that asks the user whether they are crazy 
(in a humorous way, of course). If the user clicks "Yes," it thanks them for 
accepting, and if they hover over the "No" button, it moves around randomly 
to dodge clicking.
```python
"""In order to run this program Install pyautogui by executing
 the following command in your terminal or command prompt:

    -- pip install pyautogui
"""

from tkinter import*
from tkinter import messagebox
import pyautogui
import random

root = Tk()
root.geometry("450x600")
root.title("Survey")
def yes():
    messagebox.showinfo("Accepted","Yeah! Thankyou for accpeting.")
    root.overrideredirect(False)



def gotme():
    messagebox.showinfo("Got me","You got me.")
def movetoo(event):
    x_ = random.randint(0,300)
    
    y_ = random.randint(0,500)
    button_2.place(x=x_,y=y_-69)

label_1 = Label(root, text="Kya app pagal hain?")
label_1.pack(pady=5)

label_2 = Label(root, text="Click on yes button to get close window option 🙂. ")
label_2.pack(pady=4)
button_1 = Button(root, text="Offcorse Yes! I am.", command=yes)
button_1.pack(pady=10)


button_2 = Button(root,text="Offcourse No!\n Bet you! you can't get me",command=gotme)
button_2.pack(pady=10)
button_2.bind("<Enter>", movetoo)


root.overrideredirect(True)
root.mainloop()
```

### [5. Message Spammer](#message-spammer)

Need to annoy your friends (or test a chat app's resilience)? This Python script
lets you spam messages with random insults. Use it responsibly!

```python
"""
Let's Spam - Important Message before running the code.

Install pyautogui by executing the following command in your
terminal or command prompt:

    -- pip install pyautogui

Now, please read the message below carefully.
Keep in mind to position your Code Editor and your messaging
 application side by side, so you can quickly terminate
the program if any problems arise.
If you need to close the program during runtime:
    - If you are using IDLE, simply take your cursor to the
 close button of the Interpreter and click on the 'x' button.
    - If you are using another editor like VSCode, terminate
the terminal running the program."""
    
import pyautogui
import random
import time

n = int(input("Enter number of message you would like to send: "))

# List of messages
lst = ['Monkey', 'Donkey', 'Dog','Pig','Idiot','Bastard']
print("Under 10 sec, take cursor to chat box and place it.\nUse this at your own risk.")
print("")

# Display timing from 1 to 10 seconds
for i in range(1, 11):
    print(f"{i}sec...", end='\r', flush=True)
    time.sleep(1)

print("\nStarted")
count = 0
# Get the current time
start_time = time.time()

# Press Enter 100 times with a random message
for _ in range(n):
    print(f"Number of message sent {count}", end="\r", flush=True)

    # Generate a random message
    random_message = f"You're {random.choice(lst)}"
    # Type the message
    pyautogui.write(random_message)
    # Press Enter
    pyautogui.press('enter')
    count+=1
    time.sleep(0.6)  # Adjust the sleep duration if needed
print(f"Number of message sent {count}")

# Calculate and display the total time taken
end_time = time.time()
total_time = end_time - start_time
print(f"Script execution completed in {total_time:.2f} seconds.")

```

### [6. QR Code Generator](##qr-code-generator)

Feeling like a modern-day Romeo or Juliet? Use this QR Code Generator to express 
your heart's desires without saying a word. Simply create a QR code, paste it on 
your chest, and let your crush decode your hidden messages with a simple scan.
Who needs love letters when you've got QR codes? 🥰

```python
""" First install
        -- pip install qrcode[pil]
    in order to use this code.  """

import qrcode
from datetime import datetime

# Input your data here
data = "Here, you can generate your own Qr code just follow the link- https://t.me/pythonbykrishss/40"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Get the current date and time
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

# Combine the filename with the current date and time
filename = f"my_qr_code_{current_datetime}.png"

# Save the image with the updated filename
img.save(filename)
print("Qr code generated check out in your directory.")
```

### [7. Link to Project Zip File](#link-to-project-zip-file) - Coming soon!

Stay tuned for a downloadable zip file containing all my Python projects for your convenience.

## Contributions

Got ideas for new Python projects or improvements to existing ones? Feel free to fork this repository and submit your pull requests. Let's collaborate and create some awesome Python magic together!

## Let's Connect

📫 Want to chat about Python, programming, or anything else under the sun? Hit me up on [YouTube]([https://youtube.com/krishsscodes06](https://youtube.com/@krishsscodes?si=IfXHPSyjYNGbhPC-))!

Enjoy exploring my Python playground, and happy coding! 🎉
```
