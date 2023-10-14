import vosk
import sounddevice as sd
import queue
import json

model = vosk.Model("model-small")
samplerate = 44100
device = 18

q = queue.Queue()


def q_callback(indata, frames, time, status):
    q.put(bytes(indata))


def va_listen(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize=22050, device=device, dtype='int16',
                           channels=1, callback=q_callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])


# dev = sd.default.device = 18, 0
# s = int(sd.query_devices(dev[0], 'input')['default_samplerate'])
# print(s)
