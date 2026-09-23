"""Assemble a four-shot motion-still demo; requires FFmpeg on PATH or --ffmpeg."""
from pathlib import Path
import argparse
import subprocess

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--ffmpeg', default='ffmpeg')
a = p.parse_args()
r = Path(__file__).resolve().parents[1]
# Crop inside the original train panel, excluding the triptych divider.
# No animation is generated inside the image; the editor moves the still frame.
views = [('1.0+0.0010*on','iw/2-iw/zoom/2','ih/2-ih/zoom/2'),
         ('1.34','iw-iw/zoom','0'),
         ('1.38','iw/2-iw/zoom/2','ih-ih/zoom'),
         ('1.12-0.0010*on','iw/2-iw/zoom/2','ih/2-ih/zoom/2')]
filters = ['[0:v]crop=510:906:1026:58,split=4[a][b][c][d]']
for label,(zoom,x,y) in zip('abcd',views):
    filters.append(f"[{label}]zoompan=z='{zoom}':x='{x}':y='{y}':d=96:s=720x1280:fps=24,setsar=1[{label}out]")
filters.append('[aout][bout][cout][dout]concat=n=4:v=1:a=0,format=yuv420p[v]')
cmd = [a.ffmpeg,'-hide_banner','-loglevel','error','-y',
       '-i',str(r/'assets/music-video-directions.png'),
       '-i',str(r/'starter-kit/practice-beat-120bpm.wav'),
       '-filter_complex',';'.join(filters),'-map','[v]','-map','1:a',
       '-t','16','-c:v','libx264','-crf','22','-preset','medium',
       '-c:a','aac','-b:a','160k','-movflags','+faststart',
       str(r/'starter-kit/night-train-edit-demo.mp4')]
subprocess.run(cmd,check=True)
print('Created 16-second motion-still editing demo, not a MusicMaker generation.')
