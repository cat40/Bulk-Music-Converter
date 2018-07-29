'''
todo: look at ffmpeg python libraries
'''
import os
import Tkinter as tk
import tkFileDialog as filedialog
import sys

'''
todo:
display directory name somewhere
make spinboxes a drop-down menu
'''
VALIDEXTS = ['.mp3', '.mp4']  # todo add more
dirname = None

def goByBy():
    window.destroy()
    sys.exit()

def openMusicFile():
    global dirname
    dirname = filedialog.askdirectory()

def run():
    # make sure directory has been initalized
    if dirname is None:
        return
    fromext = from_.get()
    toext = to.get()
    for fname in (os.path.join(root, filename) for root, _, filenames in os.walk(dirname) for filename in filenames):
        base, ext = os.path.splitext(fname)
        if ext == fromext:
            cmd = 'ffmpeg "{topath}" -i "{frompath}"'.format(topath=base+toext, frompath=fname)
            print cmd
            os.system(cmd)


window = tk.Tk()
window.protocol('WM_DELETE_WINDOW', goByBy)  # doesn't seem to work at the moment
window.geometry('400x400')

mainmenu = tk.Menu(window)
filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label='Open', command=openMusicFile)
mainmenu.add_cascade(label='File', menu=filemenu)

window.config(menu=mainmenu)

fromlabel = tk.Label(window, text='convert from')
tolabel = tk.Label(window, text='to')
from_ = tk.Spinbox(window, values=tuple(VALIDEXTS), wrap=True, text='from')
to = tk.Spinbox(window, values=tuple(VALIDEXTS), wrap=True, text='to')
fromlabel.pack()
from_.pack()
tolabel.pack()
to.pack()

start = tk.Button(window, command=run, text='start')
start.pack()

tk.mainloop()
