from flask import Flask, render_template
import threading
import os
import webbrowser
from main import jarvis
from object_detection.object_detector import detect_objects_from_camera

app = Flask(__name__, template_folder='Template', static_folder='Static')

jarvis_running = False
object_detection_running = False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start-jarvis')
def start_jarvis():
    global jarvis_running
    if not jarvis_running:
        jarvis_running = True
        threading.Thread(target=run_jarvis).start()
        return "🤖 Jarvis is starting with your wish..."
    else:
        return "🧠 Jarvis is already running."

@app.route('/detect-objects')
def detect_objects():
    global object_detection_running
    if not object_detection_running:
        object_detection_running = True
        threading.Thread(target=run_object_detection).start()
        return "📷 YOLOv8 object detection started. Check the camera window."
    else:
        return "🧐 Object detection is already running."

def run_jarvis():
    global jarvis_running
    try:
        jarvis()  # ✅ Now works correctly
        print("[Jarvis]: Started successfully.")
    except Exception as e:
        print(f"[ERROR in Jarvis]: {e}")
    finally:
        jarvis_running = False

def run_object_detection():
    global object_detection_running
    try:
        detect_objects_from_camera()
    except Exception as e:
        print(f"[ERROR in Object Detection]: {e}")
    finally:
        object_detection_running = False

if __name__ == '__main__':
    port = 5000
    webbrowser.open(f"http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)






