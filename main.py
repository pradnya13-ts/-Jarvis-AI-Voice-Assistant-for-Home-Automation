import random
import winsound
from Function.temprature import get_temperature
from Head.mouth import speak
from Head.ear import listen
from Head.brain import mind
from Function.wish import make_a_wish
from Function.welcome import say_random_welcome
from Data.blg_data.blg import WAKE_KEY_WORDS, BYE_KEYWORDS, RESPONSE_BYE
from Function.verify_speaker import verify_user
from Function import temprature
from Automation.open import app_open, web_open
from Automation.close import close
from Automation.youtube import get_video_query, play_youtube_video
from object_detection.object_detector import detect_objects_from_camera
from Function.whatappmsg import send_whatsapp_message

# 🔧 Initial mode
personality_mode = "default"

# 🎭 Available personality styles
PERSONALITY_MODES = ["default", "humor", "sarcastic", "poetic"]

# 🧠 Secondary password
FAVORITE_MOVIE = "iron man"

def change_personality(command):
    global personality_mode
    for mode in PERSONALITY_MODES:
        if mode in command:
            personality_mode = mode
            speak(f"Personality switched to {mode} mode.")
            print(f"🎭 Mode changed to: {mode}")
            return True

    if any(word in command for word in ["default mode", "normal mode", "be normal"]):
        personality_mode = "default"
        speak("Switched back to default mode.")
        print("🎭 Mode changed to: default")
        return True

    return False

def jarvis():
    winsound.Beep(1000, 300)
    print("🔁 Starting JARVIS...")

    print("🔐 Voice verification required.")
    if verify_user():
        speak("Access granted. Hello, Boss!")
        print("✅ Verified by voice.")
    else:
        speak("Voice not recognized. Say your favorite movie to confirm identity.")
        print("🔐 Attempting backup authentication...")
        movie_response = listen().lower().strip()
        print(f"🎞️ Movie response received: {movie_response}")

        if FAVORITE_MOVIE in movie_response or "iron" in movie_response:
            speak("Access granted via backup verification. Welcome!")
            print("✅ Verified by favorite movie.")
        else:
            speak("Access denied. You're not my boss.")
            return

    try:
        make_a_wish()
    except Exception as e:
        print(f"[WISH ERROR] {e}")

    # 🔁 Main loop
    while True:
        winsound.Beep(1000, 300)
        command = listen().lower().strip()

        if command == "connection error":
            speak("There was a connection issue with Google. Please check your internet.")
            continue

        if not command:
            continue

        if command in WAKE_KEY_WORDS:
            print("🟢 Wake word detected.")
            say_random_welcome()
            continue

        elif command in BYE_KEYWORDS:
            speak(random.choice(RESPONSE_BYE))
            break

        elif any(trigger in command for trigger in ["switch to", "change to", "be", "normal", "default"]):
            if change_personality(command):
                continue

        elif "temperature" in command or "weather" in command:
            response = get_temperature()
            speak(response)
            continue

        elif any(word in command for word in ["send message", "send whatsapp", "tell", "text", "whatsapp"]):
            try:
                words = command.split()
                contact_name = None
                message = ""

                for name in ["mom", "dad", "madiha", "yuvi", "purvi"]:
                    if name in command:
                        contact_name = name
                        idx = command.find(name) + len(name)
                        message = command[idx:].strip()
                        break

                if not contact_name:
                    speak("Whom should I send the message to?")
                    contact_name = listen().lower().strip()

                if not message:
                    speak(f"What should I say to {contact_name}?")
                    message = listen().strip()

                result = send_whatsapp_message(contact_name, message)
                speak(result)

            except Exception as e:
                print(f"[WHATSAPP ERROR] {e}")
                speak("I couldn't send the message. Something went wrong.")
            continue

        if command.startswith(("jarvis", "buddy", "jar")):
            command = command.replace("jarvis", "").replace("buddy", "").replace("jar", "").strip()

        if command.startswith("open"):
            if "website" in command or any(ext in command for ext in [".com", ".in", ".org", ".net"]):
                web_open(command)
            else:
                app_open(command)
            continue

        elif command.startswith("close"):
            close(command)
            continue

        elif "add schedule" in command or "add task" in command or "add to my schedule" in command or "i have to" in command:
            speak("Tell me what you have to do.")
            task = listen()
            from Function.schedule import add_schedule
            result = add_schedule(task)
            speak(result)
            continue

        elif "my schedule" in command or "today's schedule" in command or "what is my schedule" in command:
            from Function.schedule import get_today_schedule
            schedule = get_today_schedule()
            speak(schedule)
            continue



        elif "youtube" in command and ("play" in command or "search" in command):
            query = get_video_query(command)
            speak(f"Playing {query} on YouTube now.")
            play_youtube_video(query)
            continue

        elif "detect object" in command or "what is this" in command or "what am I showing" in command:
            speak("Let me see what you're showing...")
            detect_objects_from_camera()
            continue

        try:
            response, _ = mind(command, mode=personality_mode)
            speak(response)
        except Exception as e:
            print(f"[MIND ERROR] {e}")
            speak("Sorry, something went wrong while thinking.")










