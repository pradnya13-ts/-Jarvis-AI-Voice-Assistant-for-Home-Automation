import asyncio
import threading
import os
import edge_tts
import pygame
import time

VOICE = "en-AU-WilliamNeural"

def remove_file(file_path):
    """Tries to remove the file with retries if it's still in use."""
    for _ in range(5):
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Deleted audio file: {file_path}")
            break
        except Exception as e:
            print(f"Error removing file: {e}")
            time.sleep(0.3)  # wait before retry

async def amain(TEXT, output_file):
    try:
        print("Generating speech...")
        communicator = edge_tts.Communicate(text=TEXT, voice=VOICE)
        await communicator.save(output_file)
        print(f"Saved audio to {output_file}")

        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread.start()
        thread.join()

    except Exception as e:
        print(f"[TTS ERROR] {e}")
    finally:
        remove_file(output_file)

def play_audio(file_path):
    try:
        print("Playing audio...")
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.delay(100)

        pygame.mixer.music.stop()
        pygame.mixer.quit()
        time.sleep(0.2)  # ensure file is released
        print("Playback finished.")

    except Exception as e:
        print(f"[AUDIO ERROR] {e}")
        pygame.mixer.quit()

def speak(TEXT, output_file=None):
    if output_file is None:
        output_file = os.path.join(os.getcwd(), "speak.mp3")
    asyncio.run(amain(TEXT, output_file))





