from pytubefix import *

yt = YouTube(input('Cole aqui sua url: '))

print(yt.title)
print(yt.thumbnail_url)

stream = yt.streams.get_highest_resolution()
stream.download()

print('download finalizado com sucesso')