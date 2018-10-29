import requests
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
from gtts import gTTS
from time import sleep
import os
import pyglet

url = 'https://ascodevida.com'
r = requests.get(url)
soup = BeautifulSoup(r.text)
for adv in soup.findAll('a', {"class": "advlink"}):
    print adv.text

    tts = gTTS(text=adv.text, lang='es')
    filename = '/tmp/temp.mp3'
    tts.save(filename)

    music = pyglet.media.load(filename, streaming=False)
    music.play()

    sleep(music.duration) #prevent from killing
    os.remove(filename)
