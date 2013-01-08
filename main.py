# create a soundfile in AU format playing a sine wave
# of a given frequency, duration and volume
# tested with Python25   by vegaseat     29jan2008

from struct import pack
from math import sin, pi

def au_file(name='test.au', freq=400, dur=1000, vol=0.5):
    """
    creates an AU format audio file of a sine wave
    of frequency freq (Hz)
    for duration dur (milliseconds)
    at volume vol (max is 1.0)
    """
    fout = open(name, 'wb')
    # header needs size, encoding=2, sampling_rate=8000, channel=1
    fout.write('.snd' + pack('>5L', 24, 8*dur, 2, 8000, 1))
    factor = 2 * pi/8000
    # write data
    #freqs = [400, 600, 400, 800, 550]
    freqs = range(0, 1000, 30)
    for ju in range(100, 0, -10):
      for seg in range(0,30 * dur, ju):
          t = seg / 8000.0
          w = t * 2 * pi
          # sine wave calculations
          i = int(seg / 4000) % len(freqs)
          freq = freqs[i]
          sin_seg = sin(400+400*sin(seg * factor * .01)*seg/dur)
          # sin_seg = sin(freq*seg*factor)
          #sin_seg = sin((freq + 1*sin(w*5)) * w)
          fout.write(pack('b', vol * 127 * sin_seg))
    fout.close()

# test the module ...
if __name__ == '__main__':
    au_file(name='sound800.au', freq=800, dur=10000, vol=0.8)
    
    # if you have Windows, you can test the audio file
    # otherwise comment this code out
