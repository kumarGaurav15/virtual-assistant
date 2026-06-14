import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            audio = r.listen(source)
    except Exception as e:
        # microphone or PyAudio backend not available
        print("Microphone not available:", e)
        return ""
    try:
        voice_data = ""
        voice_data = r.recognize_google(audio)
        print (voice_data)
        return voice_data
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Sorry, my speech service is down.")





