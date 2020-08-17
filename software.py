import pyttsx3
import os
pyttsx3.speak("Hello, Welcome to the Stimulation")
pyttsx3.speak("what would you like me to do")
x=input()
if ("open" in x or "run" in x or "launch" in x) and ("notepad" in x or "notebook" in x):
	os.system("chrome")