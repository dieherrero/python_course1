import pyglet
import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander
from get_answers import Fetcher

run = True


def say(text):
    subprocess.call('say ' + text, shell=True)


def play_audio(filename):
#  filename = 'test.wav'
    chunk = 1411
    w = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(w.getsampwidth()),
        channels=w.getnchannels(),
        rate=w.getframerate(),
        output=True
    )

    data_stream = w.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = w.readframes(chunk)

    stream.close()
    pa.terminate()


r = sr.Recognizer()
cmd = Commander()


def init_speech():
    print("Listening ...")
    play_audio('sounds/test.wav')

    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
    play_audio('sounds/test.wav')

    command = ""
    try:
        command = r.recognize_google(audio)
    except:
        print("i cant understand you")

    print("your command")
    print(command)
    if command == ["quit", "exit"]:
        global run
        run = False

    cmd.discover(command)
#    say('You said: ' + command)


while run:
    init_speech()
