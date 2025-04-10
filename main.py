import os 
import eel

eel.init('www')

os.system('start chrome.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode='chrome', host='localhost', block=True)