import sounddevice as sd
import soundfile as sf
import subprocess
import os

def record_audio(directory, filename, duration=5, samplerate=44100):
    # Create the recordings directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    
    # Set up the file path
    filepath = os.path.join(directory, filename)
    
    # Record audio
    print("Get ready to say something cool! Recording starts in 3... 2... 1...")
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='float64')
    sd.wait()
    
    # Save the audio to a file
    sf.write(filepath, audio, samplerate)
    
    print(f"Audio recorded and saved successfully as {filename} in {directory}")

def recognize_speech(audio_file):
    try:
        result = subprocess.run(["whisper", audio_file], capture_output=True, text=True)
        if result.returncode == 0:
            text = result.stdout.lower()
            print("You said:", text)
            return text
        else:
            print("Error:", result.stderr)
            return ""
    except Exception as e:
        print("Error occurred while recognizing speech:", e)
        return ""
