#!/usr/bin/python3

# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# Stephane BARTHELEMY wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. Stephane
# ----------------------------------------------------------------------------
# "LICENCE BEERWARE" (Révision 42):
# Stephane BARTHELEMY a créé ce fichier. Tant que vous conservez cet avertissement,
# vous pouvez faire ce que vous voulez de ce truc. Si on se rencontre un jour et
# que vous pensez que ce truc vaut le coup, vous pouvez me payer une bière en
# retour. Stephane
# ----------------------------------------------------------------------------

#sudo pip install pyttsx3
#sudo pip install simpleaudio
#sudo pip install pydub ; brew install ffmpeg

import pyttsx3 
import simpleaudio 
import datetime
from pydub import AudioSegment

def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))

def horloge_parlante():    
    engine = pyttsx3.init() 
    #for voice in engine.getProperty('voices'):
    #    print(voice)
    change_voice(engine, "fr_FR", "VoiceGenderMale")

    now = datetime.datetime.now()
    next = now + datetime.timedelta(0,60)

    text = date_time = next.strftime("Au quatrième top , il sera exactement %-H heure et %-M minutes")
    #engine.say(text)
    engine.save_to_file(text, '/tmp/text.mp3')
    engine.runAndWait() 

    audio = AudioSegment.from_file("/tmp/text.mp3")
    audio.export("text.wav", format="wav")

    fin = now + datetime.timedelta(0,audio.duration_seconds + 1)
    if fin.second > 55:
        while True:
            now = datetime.datetime.now()
            if now.second == 0:
                break
        next = now + datetime.timedelta(0,60)

        text = date_time = next.strftime("Au quatrième top , il sera exactement %-H heure et %-M minutes")
        #engine.say(text)
        engine.save_to_file(text, '/tmp/text.mp3')
        engine.runAndWait() 

        audio = AudioSegment.from_file("/tmp/text.mp3")
        audio.export("text.wav", format="wav")

    mp3_obj = simpleaudio.WaveObject.from_wave_file("text.wav")
    text_obj = mp3_obj.play()
    text_obj.wait_done()

    while True:
        now = datetime.datetime.now()
        if now.second >= 57:
            break

    wave_obj = simpleaudio.WaveObject.from_wave_file("beep.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

    while True:
        now = datetime.datetime.now()
        if now.second >= 58:
            break

    wave_obj = simpleaudio.WaveObject.from_wave_file("beep.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

    while True:
        now = datetime.datetime.now()
        if now.second >= 59:
            break

    wave_obj = simpleaudio.WaveObject.from_wave_file("beep.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

    while True:
        now = datetime.datetime.now()
        if now.second != 59:
            break
    wave_obj = simpleaudio.WaveObject.from_wave_file("beep.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

horloge_parlante()