import pyaudio
import wave
import socket
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True, output=True, frames_per_buffer=CHUNK)
print("recording.")

frames = []

for i in range(0, int(RATE / CHUNK * 10)):
    data = stream.read(CHUNK)
    sock.sendto(data, (UDP_IP, UDP_PORT))

stream.stop_stream()
stream.close()
p.terminate()