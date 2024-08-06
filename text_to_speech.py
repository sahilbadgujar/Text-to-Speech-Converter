from gtts import gTTS
import os

def text_to_speech(text, language='en', output_file='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    print(f"Saved to {output_file}")

if __name__ == "__main__":
    text = "Hello, this is a text to speech conversion example."
    text_to_speech(text)
    os.system("start output.mp3")  
