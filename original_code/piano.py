import tkinter
from tkinter import *

class Piano:

    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    def __init__(self):

        self.root = Tk()
        self.key = []
        self.root.title("Piano.io")
        self.button = None
        self.label = StringVar()
        self.intvar = IntVar()


    def create_piano_buttons(self):
        column_num = 1
        for i in self.notes:
            color = self.get_note_color(i)
            text_color = self.get_text_color(i)
            self.button = Button(self.root, text= i, width=5, height=10, bg=color, fg=text_color)
            self.button.grid(row=1, column=column_num)
            column_num += 1

    def get_note_color(self, note):
        if "#" in note:
            return "black"
        else:
            return "white"

    def get_text_color(self, note):
        if "#" in note:
            return "white"
        else:
            return "black"

def main():
    obj = Piano()
    obj.create_piano_buttons()
    obj.root.mainloop()

if __name__ == "__main__":
    main()