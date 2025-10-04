import random
from Head.mouth import speak
from Data.blg_data.blg import *
from Data.blg_data import blg


def say_random_welcome():
    message = random.choice(blg.WELCOME_MESSAGES)
    print(message)
    speak(message)



