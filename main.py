import os
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)
engine.say("Welcome Wizard, WizardAI here,, Ready for Today?? Have a nice one CEO")
engine.runAndWait()

music_folder = os.path.expanduser("C:/Users/Home/Music/11th_Dimension_Album/11th Dimension Album/20-Ski-Mask-The-Slump-God-Shibuya-(HiphopKit.com).mp3")
os.system(f'start wmplayer "{music_folder}"')
