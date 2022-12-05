import os
from pydub import AudioSegment
import sys
sys.path.append('/path/to/ffmpeg')

# files                                                                         
src = "./mandarin/"
dst = "./my_data/mandarin/"

# convert mp3 to wav          
for file in os.listdir(src):
    if file.endswith(".mp3"):
        sound = AudioSegment.from_mp3(src + file)
        sound.export(dst + file[:-4] + ".wav", format="wav", parameters=["-ar", "16000"])
              
