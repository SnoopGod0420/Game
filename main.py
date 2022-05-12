import tkinter as tk

window = tk.Tk()
label = tk.Label(text="Pokemon")
label.pack()

global button1, button2, button3, button4


frame = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
frame.pack(side=tk.BOTTOM)
button1 = tk.Button(master=frame, text="Gym 1", height=5, width=15)
button1.pack(side=tk.LEFT)
button2 = tk.Button(master=frame, text="Wild", height=5, width=15)
button2.pack(side=tk.LEFT)
button3 = tk.Button(master=frame, text="Menu", height=5, width=15)
button3.pack(side=tk.LEFT)
button4 = tk.Button(master=frame, text="Quit", height=5, width=15)
button4.pack(side=tk.LEFT)

def handle_click(event):
  global button1, button2, button3, button4
  button1["text"]="Fight"
  button2["text"]="Catch"
  button3["text"]="Run"
  button4["text"]=""
button1.bind("<Button-1>", handle_click)


window.mainloop()