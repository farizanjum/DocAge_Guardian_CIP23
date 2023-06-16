"""
This code is a Python program that allows the user to open an image file, extract text from the
image using OCR (Optical Character Recognition), identify the date of birth (DOB)from the extracted text,
calculate the age based on the DOB, and perform access verification.
based on age criteria.
"""
#FILE NAME:"DocAge Guardian"


#A GUI based library usually use to create buttons.
import tkinter as tk
# It is a modulethat provides a file dialog box to allow users to select files from their system.
from tkinter import filedialog
# It is a library for handling images in Python.
from PIL import Image
#it's Optical Character Recognition engine. It allows extracting text from images. 
import pytesseract
#It's python inbuilt module allows pattern matching and searching within strings using regular expressions.
import re
#It allows creating, manipulating, and formatting dates and times.
from datetime import datetime, timedelta
# It is a Python library for printing colored text in the console.
import termcolor
# It is a Python library for generating ASCII art from text.
import pyfiglet
# It provides functions to print text in different colors and styles.
from termcolor import colored
# FYI, gTTS stands for Google Text To Speech, it is a Python library to interface 
# with Google Translate's text-to-speech API. 
import gtts
#From gTTs library, we have to import module playsound for playing sound in system
from playsound import playsound
#another, text to speech library
import pyttsx3

# Create the Tkinter window
window = tk.Tk()
window.title("Image Input")


# Function to handle button click event
def open_file():
    welcome_docage()
    welcome_message()
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    image = Image.open(file_path)
    # Process the image as desired
    

    #extract text from the image
    text=pytesseract.image_to_string(image)
    print("Extracted Text:")
    print(text)
    
    # Identify the date of birth (DOB)
    dob_pattern = r"DOB: (\d{2}-\d{2}-\d{4})"# Assuming the DOB format is dd-mm-yyyy
    dob_match = re.search(dob_pattern, text)

    if dob_match:
        # Extract the date of birth
        dob = dob_match.group(1)
        print("Date of Birth:")
        print(dob)
        
        # Calculate the age
        dob_obj = datetime.strptime(dob, "%m-%d-%Y") #the date of birth is in format "DOB: mm-dd-yyyy"

        today = datetime.now().date()
        age = today.year - dob_obj.year - ((today.month, today.day) < (dob_obj.month, dob_obj.day))
        print("Age:", age)

        # Check if the person is 18 years or older
        if age >= 18:
            termcolor.cprint("Access Granted!", "green") #Case 1:testid_3_case1
            slant_text_art_green()
            voice_1_case_1()
            
        else:
            termcolor.cprint("Acess Denied! user is under 18." , "red") #Case 2:testid_1_case2
            slant_text_art_red()
            voice_2_case_2()
    else:
        termcolor.cprint("Date of birth not found.", "yellow") #Case 3:testid_2_case3
        slant_text_art_yellow()
        voice_3_case_3()




def slant_text_art_green():
    # Define the text to style
    text = "Access Granted!"
    # Choose slant font
    font = "slant"
    # Generate the ASCII art using pyfiglet
    ascii_art = pyfiglet.figlet_format(text, font=font)
    # Colorize the ASCII art using termcolor
    colored_art = colored(ascii_art, color="green")
    # Print the colored ASCII art
    print(colored_art)



def slant_text_art_red():
    # Define the text to style
    text = "Access Not Granted! "
    # Choose slant font
    font = "slant"
    # Generate the ASCII art using pyfiglet
    ascii_art = pyfiglet.figlet_format(text, font=font)
    # Colorize the ASCII art using termcolor
    colored_art = colored(ascii_art, color="red")
    # Print the colored ASCII art
    print(colored_art)



def slant_text_art_yellow():
    # Define the text to style
    text = "DOB Not Found! "
    # Choose slant font
    font = "slant"
    # Generate the ASCII art using pyfiglet
    ascii_art = pyfiglet.figlet_format(text, font=font)
    # Colorize the ASCII art using termcolor
    colored_art = colored(ascii_art, color="yellow")
    # Print the colored ASCII art
    print(colored_art)




def voice_1_case_1():
    # make request to google to get synthesis
    tts = gtts.gTTS("Access Granted!")
    # save the audio file
    tts.save("voice_1_case_1.mp3")
    # play the audio file
    playsound("voice_1_case_1.mp3")



def voice_2_case_2():
    # make request to google to get synthesis
    tts = gtts.gTTS("Access Not Granted! User is under 18.")
    # save the audio file
    tts.save("voice_2_case_2.mp3")
    # play the audio file
    playsound("voice_2_case_2.mp3")



def voice_3_case_3():
    # make request to google to get synthesis
    tts = gtts.gTTS("Date of birth Not Found!")
    # save the audio file
    tts.save("voice_3_case_3.mp3")
    # play the audio file
    playsound("voice_3_case_3.mp3")




def welcome_message():
    # initialisation
    engine = pyttsx3.init()
    # testing
    engine.say("Hello! welcome to DocAge Guardian")
    engine.runAndWait()




def welcome_docage():
    # Define the text to style
    text = "Welcome to DocAge Guardian"
    # Choose slant font
    font = "slant"
    # Generate the ASCII art using pyfiglet
    ascii_art = pyfiglet.figlet_format(text, font=font)
    # Colorize the ASCII art using termcolor
    colored_art = colored(ascii_art, color="red")
    # Print the colored ASCII art
    print(colored_art)



    # Create the Open File button
button = tk.Button(window, text="Open File", command=open_file)
button.pack()

# Run the Tkinter event loop
window.mainloop()