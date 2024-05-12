from TTS.api import TTS
tts = TTS(model_name = "tts_models/en/multi-dataset/tortoise-v2")
def tts_file(texthere):
    tts.tts_to_file(texthere)


text = "is my voice natural enough?"

tts_file(text)
