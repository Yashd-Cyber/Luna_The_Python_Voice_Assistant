import pyttsx3
import speech_recognition as sr
import os
import datetime
import random
import smtplib
import wikipedia
import webbrowser
import requests
from time import sleep

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Set voice properties (female voice)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Typically, voices[1] is female (this may vary depending on system)
engine.setProperty('rate', 135)  # Slow down for a softer voice
engine.setProperty('volume', 0.9)  # Volume at 90%

def speak(text):
    """Converts text to speech and speaks it."""
    engine.say(text)
    engine.runAndWait()

def wish_me():
    """Greets the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Luna, your assistant. How can I help you today?")

def listen_command():
    """Listens for a command from the user and returns it as text."""
    recognizer = sr.Recognizer()

    # Attempt to choose the correct microphone
    with sr.Microphone() as source:
        print("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        recognizer.energy_threshold = 4000  # Increase sensitivity to sound (if too low, it may not detect quiet speech)
        audio = recognizer.listen(source, timeout=10)  # Timeout to avoid hanging forever

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that. Please try again.")
        speak("Sorry, I couldn't understand that. Could you please repeat?")
        return None
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        speak("Sorry, there was an issue with the speech recognition service.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        speak("An error occurred while processing your command.")
        return None

def take_notes():
    """Take notes and save them to a text file."""
    speak("Please tell me what you want to write down.")
    note_content = listen_command()
    if note_content:
        file_name = "note.txt"
        with open(file_name, "a") as file:
            file.write(f"{note_content}\n")
        speak(f"The note has been saved to {file_name}.")

def open_website():
    """Open a website in the browser."""
    speak("What website would you like to open?")
    website = listen_command()
    if website:
        if "http" not in website:
            website = "https://" + website
        webbrowser.open(website)
        speak(f"Opening {website} in your browser.")

def send_email():
    """Compose and send an email."""
    speak("What is the recipient's email address?")
    recipient = listen_command()
    
    if recipient:
        speak("What is the subject of the email?")
        subject = listen_command()
        
        speak("What would you like to say in the email?")
        body = listen_command()
        
        if recipient and subject and body:
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('your_email@gmail.com', 'your_password')  # Use app password for Gmail 2FA
                message = f"Subject: {subject}\n\n{body}"
                server.sendmail('your_email@gmail.com', recipient, message)
                server.quit()
                speak(f"Email sent successfully to {recipient}.")
            except Exception as e:
                speak("Sorry, I couldn't send the email. Please check your credentials and internet connection.")

def search_wikipedia():
    """Search for a topic on Wikipedia."""
    speak("What topic would you like to search for on Wikipedia?")
    topic = listen_command()
    if topic:
        try:
            summary = wikipedia.summary(topic, sentences=3)
            speak(f"Here is what I found about {topic}: {summary}")
        except wikipedia.exceptions.DisambiguationError:
            speak(f"There are multiple results for {topic}. Could you specify?")
        except wikipedia.exceptions.HTTPTimeoutError:
            speak("Sorry, there was a timeout while accessing Wikipedia.")
        except Exception as e:
            speak("Sorry, I couldn't find information on that topic.")

def get_weather():
    """Fetch the weather for a given city using an API."""
    speak("Which city's weather would you like to know about?")
    city = listen_command()
    
    if city:
        api_key = "your_api_key_here"  # Replace with your API key from OpenWeatherMap
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
        
        response = requests.get(complete_url)
        data = response.json()
        
        if data["cod"] == 200:
            main_data = data["main"]
            weather_data = data["weather"][0]
            temperature = main_data["temp"]
            description = weather_data["description"]
            
            speak(f"The weather in {city} is {description} with a temperature of {temperature}°C.")
        else:
            speak(f"Sorry, I couldn't find the weather for {city}.")

def shutdown_computer():
    """Shutdown the computer."""
    speak("Shutting down the computer.")
    os.system("shutdown /s /f /t 1")  # For Windows, use the corresponding shutdown command for other OS

def restart_computer():
    """Restart the computer."""
    speak("Restarting the computer.")
    os.system("shutdown /r /f /t 1")  # For Windows, use the corresponding restart command for other OS

def handle_query():
    """Handle the commands and queries."""
    query = listen_command()
    
    if query:
        if 'hello' in query or 'hi' in query:
            speak("Hello, how can I assist you today?")
        
        elif 'note' in query or 'document' in query:
            take_notes()
        
        elif 'email' in query or 'send email' in query:
            send_email()
        
        elif 'search' in query or 'wikipedia' in query:
            search_wikipedia()
        
        elif 'weather' in query:
            get_weather()
        
        elif 'open' in query:
            open_website()
        
        elif 'shutdown' in query:
            shutdown_computer()
        
        elif 'restart' in query:
            restart_computer()
        
        elif 'thank you' in query or 'bye' in query:
            speak("You're welcome! Goodbye!")
            exit()

# Main program loop
if __name__ == "__main__":
    wish_me()
    
    while True:
        try:
            handle_query()
        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, I encountered an error. Let me try again.")
            continue
