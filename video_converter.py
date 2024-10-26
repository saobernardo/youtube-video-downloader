import os
import sys

parametros = sys.argv
parametros.pop(0)

os.system('ffmpeg -i public/downloaded/"%s" "%s_output.avi"' % (parametros[0], parametros[0]))

print('Vídeo %s convertido com sucesso' % parametros[0])