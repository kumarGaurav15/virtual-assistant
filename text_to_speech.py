import pyttsx3


def text_to_speech(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 70)  # Adjust the speech rate if needed  
    engine.say(text)    
    engine.runAndWait() 


text_to_speech("Hello, I am Bood AI. How can I assist you today?")  