'''
todo: look at ffmpeg python libraries
'''
import os
import Tkinter as tk
import tkFileDialog as filedialog
import sys

'''
todo:
run button
'''
VALIDEXTS = ['.mp3', '.mp4']  # todo add more
def goByBy():
    window.destroy()
    sys.exit()

def openMusicFile():
    global fname
    fname = filedialog.askdirectory()


window = tk.Tk()
window.protocol('WM_DELETE_WINDOW', goByBy)  # doesn't seem to work at the moment
window.geometry('400x400')

mainmenu = tk.Menu(window)
filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Open', command=openMusicFile)
mainmenu.add_cascade(label='File', menu=filemenu)

window.config(menu=mainmenu)

from_ = tk.Spinbox(window, values=tuple(VALIDEXTS), wrap=True)
to = tk.Spinbox(window, values=tuple(VALIDEXTS), wrap=True)
from_.pack()
to.pack()

tk.mainloop()
