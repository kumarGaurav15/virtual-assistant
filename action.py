
import re
import text_to_speech
import speech_to_text
import webbrowser
import datetime
import weather


def Action(data):
    user_data = data.lower()
    user_data = re.sub(r"[^\w\s']", '', user_data)

    if "what is your name" in user_data or "what's your name" in user_data or "whats your name" in user_data:
        text_to_speech.text_to_speech("My name is Bood AI.")
        return "My name is Bood AI."
    
    elif "i am alone" in user_data or "i'm alone" in user_data or "im alone" in user_data or ("alone" in user_data and "i" in user_data):
        text_to_speech.text_to_speech('You are not alone. I am here with you.')
        return 'You are not alone. I am here with you.'
    
    elif any(word in user_data for word in [
            "madharchod", "madarchod", "madar chod",
            "bosdike", "bhosdike", "bhosadi ke",
            "bhosadike", "bhosadike", "bhosdi ke"]):
        text_to_speech.text_to_speech("teri maa ki choot")
        return "teri maa ki choot"

    elif "hello" in user_data:
        text_to_speech.text_to_speech("Hello, how can I assist you today?")
        return "Hello, how can I assist you today?"
    
    elif any(phrase in user_data for phrase in [
            "weather", "what's the weather", "whats the weather",
            "what is the weather", "weather today", "tell me the weather",
            "forecast"]):
        try:
            temperature, condition = weather.get_weather()
            weather_info = f"The current temperature is {temperature} and the condition is {condition}."
        except Exception as e:
            weather_info = "I could not fetch the weather right now. Please try again later."
            print("Weather lookup failed:", e)
        text_to_speech.text_to_speech(weather_info)
        return weather_info

    elif "how are you" in user_data:
        text_to_speech.text_to_speech("I'm doing well, thank you for asking. How can I assist you today?")
        return "I'm doing well, thank you for asking"

    elif "what time is it" in user_data or "current time" in user_data or "time" in user_data:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        text_to_speech.text_to_speech(f"The current time is {current_time}.")
        return f"The current time is {current_time}."


    elif "shut down" in user_data:
        text_to_speech.text_to_speech("Shutting down. Goodbye!")
        return "Shutting down. Goodbye!"
    
    elif"play music" in user_data:
        webbrowser.open("https://www.youtube.com/watch?v=xE3BGWksJas&t=9s") 
        text_to_speech.text_to_speech("Playing music on YouTube.")  
        return "Playing music on YouTube."
    
    elif "open google" in user_data:
        webbrowser.open("https://www.google.com")
        text_to_speech.text_to_speech("Opening Google.")
        return "Opening Google."

    else:
        text_to_speech.text_to_speech("Sorry, I didn't understand that. Can you please repeat?")  
        return "Sorry, I didn't understand that. Can you please repeat?"  

        

