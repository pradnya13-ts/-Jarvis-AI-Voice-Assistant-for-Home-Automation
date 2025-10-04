from resemblyzer import VoiceEncoder, preprocess_wav
import sounddevice as sd
import numpy as np
import soundfile as sf

def register_voice():
    print("🎙️ Speak clearly to register your voice (5 seconds)...")
    duration = 5
    sample_rate = 16000
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    audio = np.squeeze(recording)
    sf.write("register.wav", audio, sample_rate)

    wav = preprocess_wav("register.wav")
    encoder = VoiceEncoder()
    embedding = encoder.embed_utterance(wav)
    np.save("C:\\Users\\Dell\\PycharmProjects\\Jarvis 4.0\\Function\\user_voice_embedding.npy", embedding)
    print("✅ Voice registered and embedding saved.")

# Call this once
register_voice()


