# pip install pyttsx 
# "This library allowing us to write code, and it will speak whatever we write." 

import pyttsx3
engine = pyttsx3.init()
engine.say("My name is Bilal waleed")
engine.runAndWait()