from pytubefix import *
import shutil
import os

yt = YouTube(input('Cole aqui sua url: '))

#print(yt.title)
#print(yt.thumbnail_url)

title = yt.title

stream = yt.streams.get_highest_resolution()
stream.download()

print('download finalizado com sucesso')

all_files = os.listdir('./')
mp4_files = [file for file in all_files if file.endswith('.mp4')]

if mp4_files:
  for file in mp4_files:
    shutil.move(file, 'public/downloaded/%s' % file)