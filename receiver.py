import pyaudio
import wave
import socket
import sys
from threading import Thread

frames = []

def play(stream, CHUNK):
    print("playing")
    while True:
        for data in frames:
            stream.write(data)
            print("a")


def receive(CHUNK):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.bind((UDP_IP, UDP_PORT))
    except socket.error:
        print("binding error.")
        sys.exit()

    for i in range (0, int(RATE / CHUNK * 10)):
        data, addr = sock.recvfrom(CHUNK * CHANNELS * 2) # receive chunks
        frames.append(data)


if __name__ == "__main__":
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)
    
    thread_receive = Thread(target = receive, args=(CHUNK,))
    thread_play = Thread(target = play, args=(stream, CHUNK,))
    thread_receive.setDaemon(True)
    thread_play.setDaemon(True)
    thread_receive.start()
    thread_play.start()
    thread_receive.join()
    thread_play.join()
