# clock time simple
import tkinter
from time import strftime



clock = tkinter.Label()

clock.pack()
clock['font'] = 'Helvetica 120 bold'
clock['text'] = strftime('%H:%M:%S')


def tictac():
    agora = strftime('%H:%M:%S')
    if agora != clock['text']:
        clock['text'] = agora
    clock.after(100, tictac)


tictac()
clock.mainloop()
# Renato Barbosa
