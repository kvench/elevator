from speechkit import text_to_record
import wave, struct, pyaudio
floors= int(9)
start_floor = int(1)
def play_file(name):
    file = wave.open(name)
    n = file.getnframes()
    data = file.readframes(n)
    play(data, framerate=file.getframerate())

def play(data, framerate=44100):
    p = pyaudio.PyAudio()
    output_stream = p.open(format=pyaudio.paInt16,
                           channels=1,
                           rate=framerate,
                           output=True)
    output_stream.write(data)
    output_stream.close()



def say(text)
    file = text_to_record(text)
    play_file(file)


say("Введите нужный этаж от 0 до 9")
processing_floor = int(input())
if processing_floor > 9:
    say("Введите нужный этаж от 0 до 9")
elif processing_floor 0>:
    say("Введите нужный этаж от 0 до 9")
    














0
