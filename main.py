import speech_recognition as sr # Speech Recognition used to recognize speech
import os                       # Removes the files
import cv2                      # Open camera and capture photo
import ssl
import sys
import time             
import pygame
import random           
import pyttsx3
import certifi
import requests         # Used to go HTTP server
import playsound        # Plays the audio file
import pyscreeze        # Python module Used to take screenshots of screen
import webbrowser       # Opens the web browser
import bs4 as bs
import urllib.request
from PIL import Image   # Image processing library for PIL(Python Imaging Library)
from gtts import gTTS   # Google Text to Speech converter
from time import ctime  # Time and Date Details
from bs4 import BeautifulSoup

r = sr.Recognizer() #Recognizer

#User audio coverted to text
def record_audio(ask=False):
    with sr.Microphone() as source: #Microphone used to record the audio
        if ask:
            girl_speak(ask)
        audio = r.listen(source)  #Listen for the user's input
        voice_data=''
    try:
        voice_data = r.recognize_google(audio) #Recognize the user's input
    except sr.UnknownValueError:
            girl_speak("Sorry, I couldn't understand what you said") #Error: If the AI Assitant doesn't understand what User said
    except sr.RequestError as e:
        girl_speak("Sorry, AI service is down for user") #Error: AI Assistant is down for user
        print(">>", voice_data.lower())
    return voice_data

def girl_speak(text):
    text = str(text)
    girl_ai.say(text)
    girl_ai.runAndWait()

def girl_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en") #AI Assistant (Text to speech[voice-English])
    tts = gTTS(text=audio_string, lang="hi") #AI Assistant (Text to speech[voice-Hindi])
    r = random.randint(2,30000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)            #Save the audio file with MP3
    playsound.playsound(audio_file) #Play the audio file when user input the voice
    print(f"Sara: {audio_string}") #print what AI Assitant said
    os.remove(audio_file) # Remove the audio file

# Define a function for to respond to user input    
def word_exits(terms):
    for term in terms:
        if term in voice_data:
            return True
    return False

#AI identifying the Human(person)
class human:
    name = ''
    def Name(self, name):
        self.name = name

#Hindi Language Spoken By AI Assitant
def hindi_read(terms):
    for term in terms:
        if term in voice_data:
            return True
    return False

def respond(voice_data):
    #Name
    if word_exits(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        girl_speak(f"okay, i will remember that "+ person_name)
        person.Name(person_name)
       
    if word_exits(['tell me your name', 'What is your name', 'your name', 'whats your name']):
        if person.name:
            girl_speak(f"My name is Sara , {person.name}")
        else:
            girl_speak("My name is Sara, your name?")
          
    if word_exits(["what is my name"]):
        girl_speak(f"your name is "+ person.name)
        
    #Greetings
    if word_exits(['hello', 'hi', 'hey', 'hey there']):
        girl_speak(f"Hello " + person.name)
        
    if word_exits(["how are you","how are you doing"]):
        girl_speak("I'm very well, thanks for asking " + person.name) 
               
    #Time Displayed 
    if word_exits(['what time is it', 'time', 'tell me the time', 'can u tell the time']):
            girl_speak(ctime())
    
    #Search
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        girl_speak('I have Searched for ' + search)
        
    # Weather
    if 'weather' in voice_data:
        search_term = voice_data.split("for")[-1]
        url = 'https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5'
        webbrowser.get().open(url)
        girl_speak('I have searched for ' + search_term)
    
    #Take a Screenshot
    if word_exits(['screenshot', 'take screen', 'take a picture', 'SS']):
        screenshot = pyscreeze.screenshot()
        pil_image = Image.frombytes("RGB", screenshot.size, screenshot.tobytes())
        # Save the screenshot using PIL
        pil_image.save('D:\Screen\screenshot.png')
        girl_speak('Here is Your ScreenShot!')

    #Image capture successful and saved
    if word_exits(['Show image']):
        # Open the image file
        img = Image.open("D:\images86.jpg")
        # Display the image
        img.show()
        girl_speak("Here is your image")
        
    #Youtube
    if 'YouTube' in voice_data:
        search = record_audio('which youtube video do you want to search for?')
        url = 'https://www.youtube.com/results?search_query='  + search
        webbrowser.get().open(url)
        girl_speak('I have found your video '+ search)
        
    # Instagram
    if 'Instagram' in voice_data:
        instagram_path = r'C:\Program Files (x86)\Instagram\Instagram.exe'
        
        #The file attempting to open it
        if os.path.exists(instagram_path):
            os.startfile(instagram_path)
            girl_speak("Here is your instagram app")
        else:
            print("Instagram app not found on this system.")
        
    #get price for any products, grocery
    if word_exits(["the price of"]):
        search_price= voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_price
        webbrowser.get().open(url)
        girl_speak("Here is what I found for " + search_price + " on google")
    
    # Toss a coin    
    if word_exits(["flip","coin","toss"]):
        outcomes = ["Head", "Tail"]
        result = random.choice(outcomes)
        girl_speak("The computer choose to " + result)
        
    #Game zone
    if word_exits(["play game"]):
        game = record_audio('Which game do you want to play?')
        if game == 'offline game':
            url = 'https://offline-dino-game.firebaseapp.com/'
            webbrowser.get().open(url)
            girl_speak('Here is your offline game')
        else:
            girl_speak('Sorry, I don\'t know that game')
    
    if word_exits(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves=["rock", "paper", "scissor"]
    
        comp=random.choice(moves)
        per_move=voice_data
        
        girl_speak("The computer chose " + comp)
        girl_speak("You chose " + per_move)
        
        # Initialize counters for the number of wins for each player
        player_wins = 0
        computer_wins = 0
        
        # Assuming 'per_move' and 'comp' are the variables representing the moves of the player and the computer respectively
        # Update the win counters based on the game outcome
        if per_move == comp:
            girl_speak("the match is draw")
        elif (per_move == "rock" and comp == "scissor") or (per_move == "paper" and comp == "rock") or (per_move == "scissor" and comp == "paper"):
            girl_speak("Player wins")
            player_wins += 1
            if player_wins == 3:
                girl_speak("Congratulations! You have won!")
                # Reset the win counters for a new game
                player_wins = 0
                computer_wins = 0
        elif (per_move == "rock" and comp == "paper") or (per_move == "paper" and comp == "scissor") or (per_move == "scissor" and comp == "rock"):
            girl_speak("Computer wins")
            computer_wins += 1
            if computer_wins == 3:
                girl_speak("Congratulations! The computer has won!")
                # Reset the win counters for a new game
                player_wins = 0
                computer_wins = 0
        else:
            girl_speak("Game Over!")
        
    #Calculator
    if word_exits(["plus","minus","multiply","divide","power","+","-","*","/"]):
        operator = voice_data.split()[1]

        if operator == '+':
            girl_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif operator == '-':
            girl_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif operator == 'multiply' or 'x':
            girl_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif operator == 'divide':
            girl_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif operator == 'power':
            girl_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            girl_speak("Wrong Operator")
        
    #Location
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://www.google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        girl_speak('Here is your location of ' + location)

    # Current location
    if word_exits(["where am i"]):
        Ip_info = requests.get('https://api.ipdata.co?api-key=test').json()
        loc = Ip_info['region']
        girl_speak('You are currently located here '+ {loc})

   # Your Exact location as per Google map
    if word_exits(["what is my exact location"]):
        url = "https://www.google.nl/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        girl_speak("You must be here, as per Google map")
         
    #Define the words
    if word_exits(['define']):
        define_word = record_audio("what definitions u want ")
        # Make a GET request to the Oxford Learners Dictionaries website
        url = "https://en.wikipedia.org/wiki/" + define_word
        req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        resp = urllib.request.urlopen(req)
        # Parse the HTML content of the page with BeautifulSoup
        if resp.getcode() == 200:
            soup = BeautifulSoup(resp.read(), 'html.parser')
            definition_paragraphs = soup.find_all('p')
            # Find the element containing the word definition
            print("\nparagraph:")
            # Print the definition, if found
            if definition_paragraphs:
                # Print the first paragraph as the definition
                girl_speak("Here is what I found:\n " + definition_paragraphs[0].text)
            elif definition_paragraphs:
                girl_speak(f"Here is what I found:\n " + definition_paragraphs[1].text)
        else:
            girl_speak(f"Failed to retrieve the definition for {define_word}")
    
    # Camera opens and captures the photo
    if word_exits(['take photo','capture','open camera']):
        # Open the camera
        camera = cv2.VideoCapture(0)    
        # Check if the camera is opened successfully
        if not camera.isOpened():
           girl_speak("Error: Could not open the camera")
        else:
           while True:
            # Capture a photo
            return_value, image = camera.read()
            # Display the frame
            frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            cv2.imshow('Camera', frame)
            # Exit the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break     
        # Save the captured photo to a file
        if return_value:
            cv2.imwrite("D:\Screen\photo.jpg", image)
            girl_speak("Photo captured successfully and saved")
        else:
            girl_speak("Error: Could not capture photo")
        # Release the camera
        camera.release()
        cv2.destroyAllWindows()
        
    #Exit  
    if word_exits(['exit', 'see you later', 'good bye','quit']):
        girl_speak("Bye!, gone offline!")
        exit()

time.sleep(1)    #Wait for 1 second

person = human()
person.name = ""
girl_ai = pyttsx3.init()
#Initialize Pygame
pygame.init()

girl_speak('How may I assist  you?')
while (1):
    voice_data = record_audio('Listening user voice...')  #Set the language to English or Hindi based on the user's request
    print("Ques>>",{voice_data})    #Print the user's input
    respond(voice_data)        #function to respond to user input