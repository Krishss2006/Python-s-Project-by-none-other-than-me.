import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image
import numpy as np
import os
from tkinter import ttk
import threading

# ASCII characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def pixels_to_ascii(image):
    pixels = np.array(image.getdata())
    ascii_str = "".join(ASCII_CHARS[pixel // 25] for pixel in pixels)
    return ascii_str

def image_to_ascii(image_path, new_width=100, progress_callback=None):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}.")
        print(e)
        return

    image = resize_image(image, new_width)
    grayscale_image = grayify(image)
    ascii_str = pixels_to_ascii(grayscale_image)
    img_width = grayscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join(ascii_str[i:(i + img_width)] for i in range(0, ascii_str_len, img_width))

    filename, _ = os.path.splitext(os.path.basename(image_path))
    output_path = os.path.join(os.path.dirname(image_path), f"{filename}.txt")

    with open(output_path, "w") as f:
        f.write(ascii_img)
    
    if progress_callback:
        progress_callback(100)  # Indicate completion
    
    print(f"ASCII art created and saved to {output_path}")

# Function to handle dropped files
def on_drop(event):
    file_path = event.data
    file_path = file_path.strip('{').strip('}')  # Remove curly braces
    progress_bar['value'] = 0
    status_label.config(text="Processing...")
    
    # Use a thread to avoid blocking the GUI
    threading.Thread(target=lambda: process_image(file_path)).start()

# Function to update the progress bar
def update_progress(value):
    progress_bar['value'] = value
    if value == 100:
        status_label.config(text="Done!")

# Function to process the image
def process_image(file_path):
    image_to_ascii(file_path, new_width=1000, progress_callback=update_progress)

# Setting up the Tkinter GUI
root = TkinterDnD.Tk()
root.title("Drag and Drop Image to ASCII Art Converter")
root.geometry("400x200")

# Label for drag-and-drop area
label = tk.Label(root, text="Drag and Drop an Image Here", bg="lightgray", fg="black", width=50, height=10)
label.pack(padx=20, pady=20)

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

# Status label
status_label = tk.Label(root, text="")
status_label.pack(pady=5)

# Bind the drop event
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

# Run the Tkinter event loop
root.mainloop()
