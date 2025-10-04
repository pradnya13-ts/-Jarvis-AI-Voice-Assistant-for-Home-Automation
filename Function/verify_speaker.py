from resemblyzer import VoiceEncoder, preprocess_wav
import sounddevice as sd
import numpy as np
import os
import tempfile
import soundfile as sf  # To write temporary audio file


def verify_user(threshold=0.75):
    # Path to saved embedding
    embedding_path = "C:\\Users\\Dell\\PycharmProjects\\Jarvis 4.0\\Function\\user_voice_embedding.npy"

    if not os.path.exists(embedding_path):
        print("❌ Error: Registered voice not found.")
        return False

    # Load stored voice embedding
    stored_embedding = np.load(embedding_path)

    # Record current voice input
    print("🎙️ Speak now for voice verification...")
    duration = 4  # seconds
    sample_rate = 16000
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    live_audio = np.squeeze(recording)

    # Save recording temporarily to preprocess
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
        sf.write(temp_wav.name, live_audio, sample_rate)
        preprocessed = preprocess_wav(temp_wav.name)

    # Embed and compare
    encoder = VoiceEncoder()
    live_embedding = encoder.embed_utterance(preprocessed)
    similarity = np.inner(stored_embedding, live_embedding)
    print(f"🔍 Voice similarity score: {similarity:.2f}")

    if similarity >= threshold:
        print("✅ Verified: Voice match.")
        return True
    else:
        print("❌ Verification failed: Voice does not match.")
        return False

