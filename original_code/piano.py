from betterplaysound import *
from tkinter import *
import threading

class Piano:

    notes = {"C":"python_grand_piano/Cgrand.wav", "C#":"python_grand_piano/Csharpgrand.wav", "D":"python_grand_piano/Dgrand.wav",
             "D#":"python_grand_piano/Dsharpgrand.wav", "E":"python_grand_piano/Egrand.wav", "F":"python_grand_piano/Fgrand.wav",
             "F#":"python_grand_piano/Fsharpgrand.wav", "G":"python_grand_piano/Ggrand2.wav", "G#":"python_grand_piano/Gsharpgrand2.wav",
             "A":"python_grand_piano/Agrand2.wav", "A#":"python_grand_piano/Asharpgrand2.wav", "B":"python_grand_piano/Bgrand2.wav"}

    def __init__(self):

        self.root = Tk()
        self.key = []
        self.root.title("Piano.io")
        self.button = None
        self.label = StringVar()
        self.intvar = IntVar()

    def create_piano_buttons(self):
        column_num = 1
        for i in self.notes.keys():
            color = self.get_note_color(i)
            text_color = self.get_text_color(i)
            note = self.get_right_audio(i)
            self.button = Button(self.root, text= i, width=5, height=10, bg=color, fg=text_color, command=self.create_note_command(note))
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

    def get_right_audio(self, key):
        if key in self.notes:
            return self.notes[key]
        else:
            return None

    def create_note_command(self, note):
        def command():
            self.play_note(note)

        return command

    def play_note(self, note):

        x = threading.Thread(target=playsound, args=(note,))
        x.start()


def main():
    obj = Piano()
    obj.create_piano_buttons()
    obj.root.mainloop()

if __name__ == "__main__":
    main()