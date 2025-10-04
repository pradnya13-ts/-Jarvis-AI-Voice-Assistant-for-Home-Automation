import speech_recognition as sr
import pyttsx3
import Adafruit_DHT
import time

# Initialize speech engine
engine = pyttsx3.init()


# Function to make Jarvis speak
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to get temperature & humidity
def get_temperature():
    sensor = Adafruit_DHT.DHT11  # or Adafruit_DHT.DHT22
    pin = 4  # GPIO pin where sensor is connected
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        return f"The current temperature is {temperature:.1f} degrees Celsius with {humidity:.1f}% humidity."
    else:
        return "Sorry, I couldn't read the temperature data."


# Function to listen for commands
def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        return "None"
    except sr.RequestError:
        return "None"


# Main loop
if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I help you?")
    while True:
        command = listen_command()

        if "temperature" in command:
            temp_report = get_temperature()
            print(temp_report)
            speak(temp_report)

        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

        time.sleep(1)
