import pyautogui as ui
import time
import webbrowser

from Data.blg_data.blg import opening_responses, opened_responses
from Head.mouth import speak  # ✅ Import speak function
from Data.blg_data import blg
import random


def app_open(text):
    app_name = text.replace("open", "").strip()
    speak(f"{random.choice(opening_responses)} Opening {app_name}.")  # Dynamic opening line
    ui.press("win")
    time.sleep(0.5)
    ui.write(app_name)
    time.sleep(0.5)
    ui.press("enter")
    speak(f"{random.choice(opened_responses)}")


domain_extensions = [".com", ".in", ".org", ".net", ".edu"]


def web_open(command):
    command = command.lower().replace("open", "").replace("website", "").strip()
    command = command.replace(" dot ", ".").replace("dot ", ".").replace(" dot", ".")
    command = command.replace(" ", "")

    if any(ext in command for ext in domain_extensions):
        url = f"https://www.{command}"
    else:
        url = f"https://www.{command}.com"

    speak(f"{random.choice(opening_responses)} Opening {command}")
    try:
        webbrowser.open_new_tab(url)
    except:
        ui.hotkey("win", "r")
        time.sleep(0.5)
        ui.write("chrome")
        ui.press("enter")
        time.sleep(2)
        ui.write(url)
        ui.press("enter")

    speak(random.choice(opened_responses))
    print(f"🌐 Opening: {url}")
