from gtts import gTTS

def text_to_audio(text, filename="poem_output.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print(f"Audio saved as {filename}")
