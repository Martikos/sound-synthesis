# vegaseat
from struct import pack
from math import sin, pi

def au_file(name='test.au', freq=400, dur=1000, vol=0.5):

    fout = open(name, 'wb')
    fout.write('.snd' + pack('>5L', 24, 8*dur, 2, 8000, 1))
    factor = 2 * pi/8000
    freqs = [400, 600, 400, 800, 550]
    jump = 32;
    for seg in range(0,200 * dur, jump):
        t = seg / 8000.0
        w = t * 2 * pi
        i = int(seg / 4000) % len(freqs)
        freq = freqs[i]
        sin_seg = sin(400+400*sin(seg * factor * .01)*seg/dur)
        fout.write(pack('b', vol * 127 * sin_seg))
    fout.close()

au_file(name='./soundfiles/soundfile-1.au', freq=800, dur=10000, vol=0.8)
