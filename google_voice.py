from gtts import gTTS
import sounddevice as sd
import wave

def text_to_speech(text):
    # Convert text to speech
    tts = gTTS(text=text, lang='en')
    
    # Save the audio to a file
    tts.save("output.wav", 44100)
    
    # Load the audio file
    with wave.open("output.wav", 'rb') as wf:
        framerate = wf.getframerate()
        audio = wf.readframes(wf.getnframes())
    
    # Play the audio file
    sd.play(audio, samplerate=framerate)
    sd.wait()

def text_to_wav(text, filename):
    tts = gTTS(text=text, lang='hi')  # Create a gTTS object
    tts.save(filename)  # Save the speech as a WAV file

 
