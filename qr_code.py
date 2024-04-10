import telebot
import qrcode
from PIL import Image

# Initialize your Telegram bot using the API token
bot = telebot.TeleBot('6877821362:AAHqjfOSBnpvmORuhR40u8JYZ6gh9gWH2hM')

# Default colors
default_foreground_color = "black"
default_background_color = "white"

# Dictionary to store user names and IDs
user_data = {}

# Function to save user data to a text file
def save_user_data():
    with open("user.txt", "w") as file:
        for user_id, user_info in user_data.items():
            file.write(f"User ID: {user_id}, Display Name: {user_info['display_name']}, User Name: {user_info['user_name']}, "
                       f"Phone Number: {user_info.get('phone_number', 'N/A')}, "
                       f"Country: {user_info.get('country', 'N/A')}, "
                       f"City: {user_info.get('city', 'N/A')}\n")

# Load user data from the text file (if available)
try:
    with open("user.txt", "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) == 6:
                user_id = int(parts[0].split(": ")[1])
                display_name = parts[1].split(": ")[1]
                user_name = parts[2].split(": ")[1]
                phone_number = parts[3].split(": ")[1]
                country = parts[4].split(": ")[1]
                city = parts[5].split(": ")[1]
                user_data[user_id] = {
                    "display_name": display_name,
                    "user_name": user_name,
                    "phone_number": phone_number,
                    "country": country,
                    "city": city
                }
except FileNotFoundError:
    pass
except Exception as e:
    print(f"Error loading user data: {str(e)}")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if message.from_user.last_name:
        user_name += " " + message.from_user.last_name

    # Extract phone number if available
    phone_number = message.contact.phone_number if message.contact else 'N/A'

    # Extract location (country and city) if available
    location = message.location
    country = location.country if location else 'N/A'
    city = location.city if location else 'N/A'

    user_data[user_id] = {
        "display_name": user_name,
        "user_name": message.from_user.username,
        "phone_number": phone_number,
        "country": country,
        "city": city
    }
    save_user_data()

    bot.reply_to(message, f"Welcome to the QR Code Bot, {user_name}! Here's how to use it:\n\n"
                          "To generate a QR code, send '/qr [text]'.\n"
                          "For example, '/qr Hello' will generate a QR code with the default colors.\n\n"
                          "You can just send 'Hello' for a friendly greeting!")

def save_user_data():
    with open("user.txt", "w") as file:
        for user_id, user_name in user_data.items():
            file.write(f"User ID: {user_id}, User Name: {user_name}\n")

# Load user data from the text file (if available)
try:
    with open("user.txt", "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) == 2:
                user_id = int(parts[0].split(": ")[1])
                user_name = parts[1].split(": ")[1]
                user_data[user_id] = user_name
except FileNotFoundError:
    pass
except Exception as e:
    print(f"Error loading user data: {str(e)}")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if message.from_user.last_name:
        user_name += " " + message.from_user.last_name

    bot.reply_to(message, f"Welcome to the QR Code Bot, {user_name}! Here's how to use it:\n\n"
                          "To generate a QR code, send '/qr [text]'.\n"
                          "For example, '/qr Hello' will generate a QR code with the default colors.\n\n"
                          "You can just send 'Hello' for a friendly greeting!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if message.from_user.last_name:
        user_name += " " + message.from_user.last_name

    # Store user name and ID in the dictionary
    if user_id not in user_data:
        user_data[user_id] = user_name
        save_user_data()  # Save the user data to the text file
    elif user_id in user_data and user_data[user_id] != user_name:
        # Update the user name if it has changed
        user_data[user_id] = user_name
        save_user_data()  # Save the updated user data to the text file

    if text == "hello":
        bot.reply_to(message, f"Hello, {user_name}! See the instruction /help?")
    elif text.startswith("/qr"):
        try:
            parts = text.split()
            if len(parts) < 2:
                bot.reply_to(message, "Please provide the text for the QR code.")
                return
            text_to_encode = ' '.join(parts[1:])

            # Use default colors
            foreground_color = default_foreground_color
            background_color = default_background_color

            # Generate a QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(text_to_encode)
            qr.make(fit=True)

            img = qr.make_image(fill_color=foreground_color, back_color=background_color)

            # Save the QR code as a file
            img.save("qrcode.png")

            # Send the QR code to the user
            bot.send_photo(message.chat.id, open("qrcode.png", "rb"))

        except Exception as e:
            bot.reply_to(message, f"An error occurred: {str(e)}")
    else:
        bot.reply_to(message, "I'm not sure what you mean. Send '/help' to see how to use this bot.")

# Start the bot
bot.polling()
