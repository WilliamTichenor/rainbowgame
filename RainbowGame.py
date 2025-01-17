import copy
import tkinter as tk


def onClick(i):
    print(i)
    lights[i]['bg'] = colors[i]
    lights[i]['state'] = "normal"

buttons = []
lights = []
colors = ["red","orange","yellow","green","blue","indigo","violet"]

window = tk.Tk()

for i in range(0,7):
    lights.append(tk.Label(window,
                           bg = "grey",
                           state = "disabled",
                           width = 20,
                           height = 10))
    lights[i].grid(row = 0, column = i, padx = 10, pady = 10)

    buttons.append(tk.Button(window,
                             text = str(i),
                             command=lambda n=i: onClick(n),
                             width = 20,
                             height = 10))
    buttons[i].grid(row = 1, column = i, padx = 10, pady = 10)

window.mainloop()