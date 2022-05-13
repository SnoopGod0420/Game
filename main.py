import tkinter as tk

window = tk.Tk()
label = tk.Label(text="Pokemon")
label.pack()

global button1, button2, button3, button4, buttonState

buttonState="Outside"
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

def handle_clickGym(event):
  global button1, button2, button3, button4, buttonState
  buttonState="GymFight"
  button1["text"]="Fight"
  button2["text"]="Potion"
  button3["text"]="Run"
  button4["text"]=""
  buttonListner()

def handle_clickRun(event):
  global button1, button2,     button3, button4, buttonState
  buttonState="Outside"
  button1["text"]="Gym 1"
  button2["text"]="Wild"
  button3["text"]="Menu"
  button4["text"]="Quit"
  buttonListner()
def handle_clickWild(event):
  global button1, button2,     button3, button4, buttonState
  buttonState="WildFight"
  button1["text"]="Fight"
  button2["text"]="Catch"
  button3["text"]="Run"
  button4["text"]=""
  buttonListner()

def buttonListner():
  if buttonState=="Outside":
    print(buttonState)
    button1.bind("<Button-1>", handle_clickGym)
    button2.bind("<Button-1>", handle_clickWild)
  if buttonState=="GymFight":
    print(buttonState)
    button3.bind("<Button-1>", handle_clickRun)
  if buttonState=="WildFight":
    print(buttonState)
    button3.bind("<Button-1>", handle_clickRun)
buttonListner()
window.mainloop()