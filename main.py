from tkinter import filedialog as fd
from tkinter import *
import qrcode
from PIL import Image
from termcolor import colored

print(colored('''
 ██████  ██████   ██████  ██████  ██████  ███████      ██████  ███████ ███    ██ ███████ ██████   █████  ████████  ██████  ██████  
██    ██ ██   ██ ██      ██    ██ ██   ██ ██          ██       ██      ████   ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
██    ██ ██████  ██      ██    ██ ██   ██ █████       ██   ███ █████   ██ ██  ██ █████   ██████  ███████    ██    ██    ██ ██████  
██ ▄▄ ██ ██   ██ ██      ██    ██ ██   ██ ██          ██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
 ██████  ██   ██  ██████  ██████  ██████  ███████      ██████  ███████ ██   ████ ███████ ██   ██ ██   ██    ██     ██████  ██   ██ 
    ▀▀                                                                                                                             
                                                    made by @Sublimer.js & @nordbearbot                                                                               

''','magenta'))

data = input('Введите данные (начните с http:// если это ссылка): ')
print('Подождите, генерирую код...')
code = qrcode.make(data)
file = filedialog.asksaveasfilename(
	filetypes=(('PNG файлы', '*.png'), ('JPG файлы', '*.jpg;*.jpeg'), ('GIF файлы', '*.gif'))
	)
code.save(file)
myimage = Image.open(file)
myimage.load()
myimage.show()
