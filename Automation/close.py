import pygetwindow as gw
import pyautogui as ui
import time
import psutil

from Data.blg_data.blg import closing_responses, closed_responses
from Head.mouth import speak  # ✅ Import speak function
from Data.blg_data import blg
from Head.mouth import speak
import random

def focus_window_by_title(title_keyword):
    """
    Focuses the first window matching the title keyword (e.g., 'YouTube')
    """
    windows = gw.getWindowsWithTitle(title_keyword)
    if windows:
        window = windows[0]
        window.activate()
        print(f"🪟 Focused window: {window.title}")
        time.sleep(0.5)
        return True
    else:
        print(f"❌ No window found with title containing: {title_keyword}")
        return False


def close_specific_tab(command):
    """
    Tries to find and close a browser tab/window based on spoken command
    """
    keywords = command.lower().replace("close", "").replace("tab", "").strip()
    if keywords:
        success = focus_window_by_title(keywords)
        if success:
            speak(f"Closing tab with {keywords}")
            ui.hotkey("ctrl", "w")
            print(f"❌ Closed tab containing: {keywords}")
        else:
            speak(f"Could not find a tab with {keywords}")
            print("🔍 Could not locate tab.")
    else:
        speak("No specific tab name found")
        print("⚠️ No specific tab name found in command.")




def close(command):
    command = command.lower()
    speak(random.choice(closing_responses))

    if "tab" in command and not any(app in command for app in ["chrome", "firefox", "edge"]):
        close_specific_tab(command)
    elif "window" in command:
        keyword = command.replace("close", "").replace("window", "").strip()
        if keyword:
            success = focus_window_by_title(keyword)
            if success:
                time.sleep(0.5)
                ui.hotkey("alt", "f4")
        else:
            ui.hotkey("alt", "f4")
    elif "chrome" in command or "browser" in command:
        for proc in psutil.process_iter(['pid', 'name']):
            if "chrome" in proc.info['name'].lower():
                proc.kill()
    else:
        ui.hotkey("alt", "f4")

    speak(random.choice(closed_responses))


# Example usage:
# close("close YouTube tab")
# close("close chrome")
