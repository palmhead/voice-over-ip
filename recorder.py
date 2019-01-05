import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
print("recording.")

frames = []

for i in range(0, int(RATE / CHUNK * 15)):
    data = stream.read(CHUNK)
    frames.append(data)

print(frames) # i know.

stream.stop_stream()
stream.close()
p.terminate()