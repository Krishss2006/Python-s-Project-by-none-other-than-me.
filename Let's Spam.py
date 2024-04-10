"""
Let's Spam - Important Message before running the code.

Install pyautogui by 
    -- pip install pyautogui <- run it on terminal or cmd

Now read below message.
Keep in mind place The Code Editor and Your \
Message App Side by side in order to terminate the 
program during any probelem. 
If needed to close the program on runtime\
then, if you are using IDLE So, simply take your cursor\
to close button of Interpreter and click
on close button [x]. \
if using another like VSCode Terminate Terminal. """

    
import pyautogui
import random
import time

n = int(input("Enter number of message you would like\
to send: "))

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
