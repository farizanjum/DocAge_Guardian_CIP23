"""
This code is a Python program that allows the user to open an image file, extract text from the
image using OCR (Optical Character Recognition), identify the date of birth (DOB) from the extracted text,
calculate the age based on the DOB, and perform access verification based on age criteria.
"""
#FILE NAME:"DocAge Guardian"

# Import necessary libraries and modules
# A GUI based library usually used to create buttons.
import tkinter as tk
# A module that provides a file dialog box to allow users to select files from their system.
from tkinter import filedialog
# A library for handling images in Python.
from PIL import ImageTk, Image
# An OCR engine that allows extracting text from images.
import pytesseract
# A Python module for pattern matching and searching within strings using regular expressions.
import re
# A module that provides functions to manipulate dates and times.
from datetime import datetime
# A library for printing text in different colors and styles.
from termcolor import colored
# A Python library for generating ASCII art from text.
import pyfiglet
# A Python library to interface with Google Translate's text-to-speech API.
import gtts
# A module from the gTTS library to play sound in the system.
from playsound import playsound
# A text-to-speech library.
import pyttsx3

# Create the Tkinter window
window = tk.Tk()
window.title("DocAge Guardian")

# Load and display the background image
background = Image.open("bg_docage_final.png")
background = background.resize((500, 500))
background_image = ImageTk.PhotoImage(background)
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Set window size and position
window.geometry("500x500")
# Set window to not be resizable
window.resizable(False, False)

# Load and display the logo image
logo_image = Image.open("Glow_doclogo.png")
logo_image = logo_image.resize((200, 200))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(window, image=logo_photo, bg="black")
logo_label.pack(pady=20)

# Function to handle button click event
def open_file():
    # Open a file dialog to allow the user to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    # Open the image file
    image = Image.open(file_path)
    # Process the image as desired

    # Extract text from the image using OCR
    text = pytesseract.image_to_string(image)
    
    # Identify the date of birth (DOB) from the extracted text using a regular expression pattern
    dob_pattern = r"DOB: (\d{2}-\d{2}-\d{4})"  # Assuming the DOB format is dd-mm-yyyy
    dob_match = re.search(dob_pattern, text)

    if dob_match:
        # Extract the date of birth
        dob = dob_match.group(1)
        
        # Calculate the age based on the DOB
        dob_obj = datetime.strptime(dob, "%m-%d-%Y")
        today = datetime.now().date()
        age = today.year - dob_obj.year - ((today.month, today.day) < (dob_obj.month, dob_obj.day))

        # Check if the person is 18 years or older
        if age >= 18:
            # Set the access label to "Access Granted!" with green text color         #CASE 1: testid_3_case_1
            access_label.config(text="Access Granted!", fg="green")
            # Play the "Access Granted" voice message
            voice_1()
        else:
            # Set the access label to "Access Denied! User is under 18." with red text color   #CASE 2: testid_1_case_2
            access_label.config(text="Access Denied! User is under 18.", fg="red")
            # Play the "Access Denied" voice message
            voice_2()
    else:
        # Set the access label to "Date of Birth Not Found." with yellow text color     #CASE 1: testid_2_case_3
        access_label.config(text="Date of Birth Not Found.", fg="yellow")
        # Play the "Date of Birth Not Found" voice message
        voice_3()
"""
TEST ID GOOGLEDRIVE LINK: https://drive.google.com/drive/folders/117AcUudxLuW4K25L6z8fsT_mHrXtgXVK?usp=drive_link
"""

# Function to play the "Access Granted" voice message
def voice_1():
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    # Set the text to be spoken
    engine.say("Heyy, Access Granted!")
    # Run the text-to-speech engine
    engine.runAndWait()
    
# Function to play the "Access Denied" voice message
def voice_2():
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    # Set the text to be spoken
    engine.say("Heyy, Access Denied!")
    # Run the text-to-speech engine
    engine.runAndWait()

# Function to play the "Date of Birth Not Found" voice message
def voice_3():
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    # Set the text to be spoken
    engine.say("Sorry, Date of Birth Not Found.")
    # Run the text-to-speech engine
    engine.runAndWait()

# Function to display a welcome message using text-to-speech
def welcome_message():
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    # Set the welcome message
    welcome_text = "Hello! Welcome to DocAge Guardian."
    # Speak the welcome message
    engine.say(welcome_text)
    # Run the text-to-speech engine
    engine.runAndWait()

# Display the welcome message with sound
welcome_message()

# Create the Open File button
open_button = tk.Button(window, text="Open File", command=open_file, bg="#794cec")
open_button.pack(pady=10)

# Create the access label
access_label = tk.Label(window, text="", font=("Helvetica", 16), bg="black", fg="white")
access_label.pack(pady=20)

# Create the output label
output_label = tk.Label(window, text="", font=("Helvetica", 100), bg="black", fg="white")
output_label.pack()

# Run the Tkinter event loop
window.mainloop()
