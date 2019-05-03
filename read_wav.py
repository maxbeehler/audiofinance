import soundfile as sf

data, samplerate = sf.read('data/sample.wav')
print(len(data))
print(samplerate)
