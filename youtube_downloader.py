from pytubefix import *
import shutil
import os

yt = YouTube(input('Cole aqui sua url: '))

#print(yt.thumbnail_url)

title = yt.title
stream = yt.streams.get_highest_resolution()
print('aguarde...')
stream.download()

print('download finalizado com sucesso')

all_files = os.listdir('./')
mp4_files = [file for file in all_files if file.endswith('.mp4')]

if mp4_files:
  user_profile = os.environ.get('USERPROFILE')
  for file in mp4_files:
    full_path = f'{user_profile}\\Videos\\{file}'
    shutil.move(file, full_path)
    #os.system('py video_converter.py %s' % file)