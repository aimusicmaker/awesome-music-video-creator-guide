"""Create the original 16-second, 120 BPM practice cue. Standard library only."""
from pathlib import Path
import math
import random
import struct
import wave

RATE = 44100
DURATION = 16
rng = random.Random(230926)
mix = [0.0] * (RATE * DURATION)

def add(start, duration, voice):
    begin = round(start * RATE)
    for j in range(round(duration * RATE)):
        i = begin + j
        if i >= len(mix):
            break
        mix[i] += voice(j / RATE)

def note(freq, duration, amplitude):
    def voice(t):
        attack = min(1.0, t / 0.018)
        release = min(1.0, max(0.0, duration - t) / 0.07)
        body = math.sin(2 * math.pi * freq * t) + 0.18 * math.sin(4 * math.pi * freq * t)
        return amplitude * attack * release * math.exp(-1.6*t) * body
    return voice

# Original, sparse eight-bar cue: Am7, Fmaj7, Cmaj7, G6; two bars each.
chords = [(220,261.6256,329.6276,391.9954), (174.6141,220,261.6256,329.6276),
          (130.8128,164.8138,195.9977,246.9417), (195.9977,246.9417,293.6648,329.6276)]
for bar in range(8):
    chord = chords[bar // 2]
    start = bar * 2.0
    for f in chord:
        add(start, 1.85, note(f,1.85,0.07))
    add(start, 0.85, note(chord[0]/2,0.85,0.19))
    add(start+1, 0.8, note(chord[0]/2,0.8,0.14))
    add(start+0.75, 0.42, note(chord[2]*2,0.42,0.08))
    add(start+1.5, 0.42, note(chord[1]*2,0.42,0.07))
    for beat in range(4):
        t0=start+beat*0.5
        if beat in (0,2):
            add(t0,0.25,lambda t:0.38*math.exp(-22*t)*math.sin(2*math.pi*(48*t+2.5*(1-math.exp(-30*t)))))
        else:
            add(t0,0.14,lambda t:0.14*math.exp(-32*t)*rng.uniform(-1,1))
        add(t0+0.25,0.045,lambda t:0.045*math.exp(-95*t)*rng.uniform(-1,1))
peak=max(abs(v) for v in mix)
out=bytearray()
for i,v in enumerate(mix):
    fade=min(1.0,i/(RATE*0.01),(len(mix)-1-i)/(RATE*0.12))
    out.extend(struct.pack('<h',round(v/peak*0.79*fade*32767)))
p=Path(__file__).resolve().parents[1]/'starter-kit/practice-beat-120bpm.wav'
with wave.open(str(p),'wb') as w:
    w.setnchannels(1);w.setsampwidth(2);w.setframerate(RATE);w.writeframes(out)
print(f'Wrote {p.name}: {DURATION}s, {RATE} Hz, mono, 16-bit PCM')
