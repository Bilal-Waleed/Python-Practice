import pyjokes

joke = pyjokes.get_joke()
print(joke)


import pyttsx3
engine = pyttsx3.init()
engine.say("heey my name is ")
engine.runAndWait()