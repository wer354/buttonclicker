from tkinter import *
root = Tk()
root.title("click counter")
root.geometry("300x50")
myLabel = Label(root, text="Look! I clicked the button ")
myLabel.pack()
count = 0
def clicked():
    global count
    count+=1
    myLabel.configure(text=f'Look! I clicked the button {count} times!')
myButton = Button(root, text="click me~", command=clicked)
myButton.pack()
root.mainloop()