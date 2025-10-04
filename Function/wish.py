from datetime import datetime, date
import random

from Data.blg_data import blg
from Head.mouth import speak
from Data.blg_data.blg import *

# ---------------------------
# Random Greeting
# ---------------------------
def random_greeting():
    speak(random.choice(blg.GREETINGS))

# ---------------------------
# Time-Based Greeting Key
# ---------------------------
def get_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    elif 17 <= hour < 21:
        return "evening"
    else:
        return "night"

# ---------------------------
# Get Random Quote
# ---------------------------
def get_random_quote():
    return random.choice(blg.QUOTES)

# ---------------------------
# Final Wish Function
# ---------------------------
def make_a_wish():
    today = date.today()
    now = datetime.now()
    formatted_date = today.strftime("%A, %d %B %Y")
    formatted_time = now.strftime("%I:%M %p")

    time_of_day = get_greeting()
    wish = random.choice(blg.WISHES[time_of_day])
    quote = get_random_quote()

    message = f"{wish} Today is {formatted_date}, and the time is {formatted_time}. {quote}"
    speak(message)


# ---------------------------
# Execute
# ---------------------------







