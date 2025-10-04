# -Jarvis-AI-Voice-Assistant-for-Home-Automation
Jarvis is an artificial intelligence-powered voice assistant designed to simplify daily tasks and control smart home devices with natural voice commands. Inspired by Iron Man’s J.A.R.V.I.S., this project combines speech recognition, natural language processing (NLP), and IoT-based home automation into a single assistant.
🤖 Jarvis – AI Voice Assistant with Home Automation & Object Detection

Jarvis is a Python-based artificial intelligence voice assistant inspired by Iron Man’s J.A.R.V.I.S. It can understand natural language, control IoT devices, detect objects through a camera, and even manage your daily tasks — all through voice commands.
It runs locally and provides a web interface powered by Flask for easy access and monitoring.

✨ Features

🎙 Voice-controlled AI Assistant – Talk naturally to control apps, get info, and more.

🏠 Home Automation Integration – Connect with Raspberry Pi or IoT relays to switch lights, fans, or other appliances on/off.

🌡 Temperature Monitoring – Reads live temperature/humidity data from connected sensors.

📷 Real-Time Object Detection – Uses YOLOv8 to identify objects via your webcam or Pi Camera.

💬 Multi-Personality Modes – Switch Jarvis’s personality to humor, sarcastic, or poetic.

📱 WhatsApp Message Sender – Send messages by voice.

📅 Smart Scheduler – Add and retrieve daily tasks through voice commands.

🔐 Voice Verification – Recognizes authorized users before activating.

🌐 Web Dashboard – Launch Jarvis or Object Detection from a Flask web interface.

🧠 Tech Stack
Component	Technology
Core Language	Python 3
Voice I/O	speech_recognition, pyttsx3, winsound
Web Framework	Flask
AI Logic	Custom NLP + optional OpenAI/ChatGPT API
Object Detection	YOLOv8 (ultralytics)
Home Automation	GPIO / MQTT (Raspberry Pi)
Scheduler & WhatsApp	Custom Python functions
Frontend	HTML / CSS / JS templates served by Flask

🧩 Project Structure
Jarvis 4.0/
│
├── .venv/
│
├── Adeline/
│   └── aspeak.py
│
├── Automation/
│   ├── close.py
│   ├── open.py
│   └── youtube.py
│
├── Data/
│
├── Function/
│   ├── register.wav
│   ├── register_voice.py
│   ├── schedule.py
│   ├── temprature.py
│   ├── user_voice_embedding.npy
│   ├── verify_speaker.py
│   ├── welcome.py
│   ├── whatappmsg.py
│   └── wish.py
│
├── Head/
│   ├── brain.py
│   ├── ear.py
│   └── mouth.py
│
├── IOT/
│   ├── Switch.py
│   └── Temperature.py
│
├── object_detection/
│   └── object_detector.py
│
├── Static/
│   ├── jarv arc.png
│   ├── jarv1.png
│   └── jarvis.jpg
│
├── Template/
│   └── index.html
│
├── training_model/
│   └── model.py
│
├── app.py
├── main.py
├── PyWhatKit_DB.txt
├── README.md
└── yolov8n.pt


🚀 How It Works

Run app.py to start the Flask web server.

python app.py


This will automatically open http://127.0.0.1:5000 in your browser.

From the web UI:

🧠 Click “Start Jarvis” → launches the voice assistant.

📷 Click “Detect Objects” → opens YOLOv8 real-time detection.

Jarvis listens for commands such as:

“Turn on the living room light.”

“What’s the temperature?”

“Play music on YouTube.”

“Send a message to Mom.”

“Detect object.”

⚙️ Setup Instructions

Clone the Repository

git clone https://github.com/yourusername/Jarvis-AI.git
cd Jarvis-AI


Install Dependencies

pip install -r requirements.txt


Run the App

python app.py


(Optional) For Raspberry Pi / IoT:

Connect your relay or sensors to GPIO pins.

Update pin numbers in your automation scripts.

🧰 Example Commands
Command	Action
“Jarvis, what’s the temperature?”	Reads temperature via DHT sensor
“Turn on the fan.”	Activates GPIO relay
“Send a message to Madiha.”	Sends WhatsApp message
“Play Despacito on YouTube.”	Opens and plays video
“Detect object.”	Activates YOLOv8 detection
“Goodbye Jarvis.”	Gracefully shuts down assistant
🔮 Future Enhancements

📱 Mobile dashboard for remote monitoring

☁️ Cloud-based command logging

🧬 Face recognition for authentication

🤝 Integration with Alexa / Google Home

🧩 MQTT support for smart-home ecosystems

🏆 Credits

Developed by Pradnya Chandrakant Bhakare



Inspired by Tony Stark’s J.A.R.V.I.S. — powered by Python and AI.
