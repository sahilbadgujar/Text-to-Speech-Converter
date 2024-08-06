from gtts import gTTS
language = "en"
text = "open google"
speech = gTTS(text = text)
speech.save("open_google.mp3")
#0728,2228