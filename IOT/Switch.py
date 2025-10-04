import speech_recognition as sr
import pyttsx3
from gpiozero import LED
from time import sleep

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# GPIO setup (replace with your pin number)
light = LED(17)  # GPIO17 (Pin 11)
fan = LED(27)    # GPIO27 (Pin 13)

# Function to listen to voice
def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except:
        return ""

# Main loop
if __name__ == "__main__":
    speak("Jarvis system online. How can I help you?")
    while True:
        command = listen_command()

        # LIGHT CONTROL
        if "turn on light" in command:
            light.on()
            speak("Turning on the light.")
        elif "turn off light" in command:
            light.off()
            speak("Turning off the light.")

        # FAN CONTROL
        elif "turn on fan" in command:
            fan.on()
            speak("Turning on the fan.")
        elif "turn off fan" in command:
            fan.off()
            speak("Turning off the fan.")

        elif "exit" in command or "shutdown" in command:
            speak("Goodbye! Powering down the system.")
            break

        sleep(1)
