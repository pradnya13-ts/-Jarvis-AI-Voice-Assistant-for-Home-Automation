import speech_recognition as sr
import os
import threading
from mtranslate import translate
from colorama import Fore, Style, init
from googletrans import Translator
import time

translator = Translator()

init(autoreset=True)  #automatically reset after each print


def print_loop():
    while True:
        print(Fore.LIGHTGREEN_EX + "I am Listening...", end="", flush=True)
        print(Style.RESET_ALL, end="", flush=True)
        print("", end="", flush=True)


def Trans_hindi_to_english(txt, retries=3):
    for attempt in range(retries):
        try:
            result = translator.translate(txt, src='hi', dest='en')
            return result.text
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(1)
    return txt  # Return original if all attempts fail


def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 35000
    recognizer.dynamic_energy_adjustment_damping = 0.03  #less more active voice listening
    recognizer.dynamic_energy_ratio = 1.9
    recognizer.pause_threshold = 0.7
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.7
    recognizer.non_speaking_duration = 0.4

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.LIGHTGREEN_EX + "I am Listening...", end="", flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\r" + Fore.LIGHTYELLOW_EX + "Got it, i am Recognizing...", end="", flush=True)
                recognized_txt = recognizer.recognize_google(audio, language="en-IN").lower()
                if recognized_txt:
                    translated_txt = Trans_hindi_to_english(recognized_txt)
                    print("\r" + Fore.BLUE + "Prad : ", translated_txt)
                    return translated_txt
                else:
                    return ""

            except sr.UnknownValueError:
                recognized_txt = ""

            finally:
                print("\r", end="", flush=True)

        os.system("cls" if os.name == "nt" else "clear")
        #threading
        listen_thread = threading.Thread(target=listen)
        print_thread = threading.Thread(target=print_loop)
        listen_thread.start()
        print_thread.start()
        listen_thread.join()
        print_thread.join()
