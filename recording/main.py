import pyaudio
import wave
import argparse
import sounddevice as sd
import numpy
import threading
import os
from time import time

assert numpy


def recording(file_way: str, sec: float):
    """
    Will record your voice an mp3 file in the directory you specify
    :param file_way: Directory where the file will be written
    :param sec: How long will the recording last
    :return: Nope
    """
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = sec
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=1,
                    frames_per_buffer=1024)
    print("* recording")
    frames = []
    start = time()
    for i in range(0, int(RATE / 1024 * RECORD_SECONDS)):
        data = stream.read(1024)
        frames.append(data)

    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    os.chdir(file_way)
    wf = wave.open('output.mp3', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    end = time()
    print('Your recording {0:.2f} sec'.format(end - start))


def echo():
    """
    The function plays your voice in real time
    Finishes its work if you press any button
    :return: Nope
    """

    def int_or_str(text: str):
        """Helper function for argument parsing."""
        try:
            return int(text)
        except ValueError:
            return text

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '-l', '--list-devices', action='store_true',
        help='show list of audio devices and exit')
    args, remaining = parser.parse_known_args()
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])
    parser.add_argument(
        '-i', '--input-device', type=int_or_str,
        help='input device (numeric ID or substring)')
    parser.add_argument(
        '-o', '--output-device', type=int_or_str,
        help='output device (numeric ID or substring)')
    parser.add_argument(
        '-c', '--channels', type=int, default=2,
        help='number of channels')
    parser.add_argument('--dtype', help='audio data type')
    parser.add_argument('--samplerate', type=float, help='sampling rate')
    parser.add_argument('--blocksize', type=int, help='block size')
    parser.add_argument('--latency', type=float, help='latency in seconds')
    args = parser.parse_args(remaining)

    def callback(indata: int, outdata: int, frames: list, time: float, status: bool):
        if status:
            print(status)
        outdata[:] = indata

    try:
        with sd.Stream(device=(args.input_device, args.output_device),
                       samplerate=args.samplerate, blocksize=args.blocksize,
                       dtype=args.dtype, latency=args.latency,
                       channels=args.channels, callback=callback, ):
            input()
    except KeyboardInterrupt:
        parser.exit()
    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))


def main_fun():
    file_way = input()
    sec = float(input('Enter recording time'))
    print('To stop hearing yourself press any button')
    t = threading.Thread(target=echo, args=())
    t2 = threading.Thread(target=recording, args=(file_way, sec))
    t2.start()
    t.start()


if __name__ == '__main__':
    main_fun()
