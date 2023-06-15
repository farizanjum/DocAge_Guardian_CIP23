# DocAge_Guardian_CIP23
DocAge Guardian is a Python program that utilizes Optical Character Recognition (OCR) to extract text from an image file. It allows users to open an image file, extract text using OCR, identify the date of birth (DOB) from the extracted text, calculate the age based on the DOB, and perform access verification based on age criteria.

Features:
- Extracts text from image files using OCR (Optical Character Recognition)
- Identifies the date of birth (DOB) from the extracted text
- Calculates the age based on the DOB and current date
- Performs access verification based on age criteria
- Provides visual feedback with colored console output using termcolor
- Generates ASCII art for access verification messages using pyfiglet
- Converts access verification messages to speech using gTTS (Google Text to Speech)
- Supports various image formats (JPEG, JPG, PNG)
- User-friendly GUI interface with an open file button
- Welcomes users with a text-to-speech greeting and ASCII art welcome message

Dependencies:
- Python 3.x
- tkinter
- PIL (Python Imaging Library)
- pytesseract
- re (Regular Expression)
- datetime
- termcolor
- pyfiglet
- gTTS (Google Text to Speech)
- playsound
- pyttsx3

Usage:
1. Run the program.
2. Click the "Open File" button to select an image file.
3. The program will extract text from the image using OCR.
4. It will identify the DOB from the extracted text and calculate the age.
5. Access verification will be performed based on the age criteria.
6. Visual and audio feedback will be provided based on the access verification result.

Note: Ensure that the required dependencies are installed before running the program.
This program can be used for various applications, such as age verification for access control systems, document processing, and more.
Feel free to contribute to this project by adding new features, improving existing functionality, or providing suggestions for enhancements. Pull requests are welcome!
