import speech_recognition as sr

recognizer = sr.Recognizer()
wake_word = 'smart'

def active_recognizer():
    try:

        with sr.Microphone() as source:
            print("listening...\n")
            audio = recognizer.listen(source)

        audio_text = recognizer.recognize_google(audio)
        print(audio_text + "\n")

        if wake_word in audio_text:
            audio_text = audio_text.replace(wake_word, "")
            print("You said: " + audio_text)

        elif wake_word not in audio_text:
            print("Please add the Wake-Word while telling!\n")

        else:
            active_recognizer()



    except sr.UnknownValueError:
        print("Couldn't hear anything...\nspeak again!\n\n")
        active_recognizer()

while True:
    active_recognizer()