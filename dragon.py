import os
import webbrowser
import google_voice as voice  # Assuming voice.text_to_speech() function is defined elsewhere
import vtop
import recorder as ears

# Function to open a link in the default web browser
def open_link(url):
    try:
        webbrowser.open(url)
    except Exception as e:
        print("Error occurred while opening the link:", e)

links = {
    "youtube": "https://www.youtube.com/feed/subscriptions"
}

def shutdown():
    os.system("sudo shutdown now")

def sleep():
    os.system("sudo sleep now")

# Continuous listening loop
while True:
    ears.record_audio("recordings", "recorded.wav")
    text = ears.recognize_speech(os.path.join("recordings", "recorded.wav"))
    print(text)
    print(")))))))))))))))))))))))))))))))))))))))))))")
    if text:
        words = text.lower().split()
        for i in range(len(words) - 1):
            if words[i] == "open":
                if words[i+1] in links:
                    voice.text_to_speech("Ok brother, opening YouTube!")  # Assuming text_to_speech is implemented elsewhere
                    open_link(links[words[i+1]])
                    break  # Exit the loop after opening the link
            
            # Perform actions based on recognized text
        if "hey buddy" in words or "hey" in text:
            print("Hey there! How's it going?")
        if "close" in words or "quit" in text:
            quit()
        if "shutdown" in words:
            shutdown()
        if "sleep" in words:
            sleep()
        if "digital assignment" in words:
            vtop.get_da("VARDHIN0369", "TheDarkFire#9")  # Assuming get_da is implemented elsewhere
