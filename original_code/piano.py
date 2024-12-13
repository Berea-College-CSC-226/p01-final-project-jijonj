##############################################################
##  Author: Julio Jijon
##  Username: jijonj
##  Purpose: working piano made with Tkinter
##############################################################

from betterplaysound import *
from tkinter import *
import threading
from multiprocessing import Process


class Piano:

    # dictionary to map keyboard keys to musical notes
    key_to_note = {
        "q": "C", "2": "C#", "w": "D", "3": "D#", "e": "E",
        "r": "F", "5": "F#", "t": "G", "6": "G#", "y": "A",
        "7": "A#", "u": "B", "v": "C2", "g": "C#2", "b": "D2",
        "h": "D#2", "n": "E2", "m": "F2", "k": "F#2", ",": "G2",
        "l": "G#2", ".": "A2", ";": "A#2", "/": "B2"
    }

    # dictionary of piano types with corresponding sound files
    piano_types = {
        "Grand": {
            "C": "python_grand_piano/Cgrand.wav", "C#": "python_grand_piano/Csharpgrand.wav",
            "D": "python_grand_piano/Dgrand.wav",
            "D#": "python_grand_piano/Dsharpgrand.wav", "E": "python_grand_piano/Egrand.wav",
            "F": "python_grand_piano/Fgrand.wav",
            "F#": "python_grand_piano/Fsharpgrand.wav", "G": "python_grand_piano/Ggrand2.wav",
            "G#": "python_grand_piano/Gsharpgrand2.wav",
            "A": "python_grand_piano/Agrand2.wav", "A#": "python_grand_piano/Asharpgrand2.wav",
            "B": "python_grand_piano/Bgrand2.wav",
            "C2": "python_grand_piano/C2grand.wav", "C#2": "python_grand_piano/Csharp2grand.wav",
            "D2": "python_grand_piano/D2grand.wav",
            "D#2": "python_grand_piano/Dsharp2grand.wav", "E2": "python_grand_piano/E2grand.wav",
            "F2": "python_grand_piano/F2grand.wav",
            "F#2": "python_grand_piano/Fsharp2grand.wav", "G2": "python_grand_piano/G2grand.wav",
            "G#2": "python_grand_piano/Gsharp2grand.wav",
            "A2": "python_grand_piano/A2grand.wav", "A#2": "python_grand_piano/Asharp2grand.wav",
            "B2": "python_grand_piano/B2grand.wav",
        },
        "Electric": {
            "C": "python_grand_piano/C1electric.wav", "C#": "python_grand_piano/Csharp1electric.wav",
            "D": "python_grand_piano/D1electric.wav",
            "D#": "python_grand_piano/Dsharp1electric.wav", "E": "python_grand_piano/E1electric.wav",
            "F": "python_grand_piano/F1electric.wav",
            "F#": "python_grand_piano/Fsharp1electric.wav", "G": "python_grand_piano/G1electric.wav",
            "G#": "python_grand_piano/Gsharp1electric.wav",
            "A": "python_grand_piano/A1electric.wav", "A#": "python_grand_piano/Asharp1electric.wav",
            "B": "python_grand_piano/B1electric.wav",
            "C2": "python_grand_piano/C2electric.wav", "C#2": "python_grand_piano/Csharp2electric.wav",
            "D2": "python_grand_piano/D2electric.wav",
            "D#2": "python_grand_piano/Dsharp2electric.wav", "E2": "python_grand_piano/E2electric.wav",
            "F2": "python_grand_piano/F2electric.wav",
            "F#2": "python_grand_piano/Fsharp2electric.wav", "G2": "python_grand_piano/G2electric.wav",
            "G#2": "python_grand_piano/Gsharp2electric.wav",
            "A2": "python_grand_piano/A2electric.wav", "A#2": "python_grand_piano/Asharp2electric.wav",
            "B2": "python_grand_piano/B2electric.wav",
        }
    }

    def __init__(self):
        """
        initialize the main window and default settings
        :return None:

        """

        # create the main tkinter window
        self.root = Tk()
        self.key = []
        self.root.title("Piano.io")  # set window title
        self.notes = self.piano_types["Grand"]  # default piano type is Grand
        self.button = None
        self.label = StringVar()
        self.intvar = IntVar()
        self.buttons = {}

        # call method to create the menu bar
        self.create_menu_bar()

        # label at the top of the window
        self.title_label = Label(self.root, text="Piano", font=("Arial", 24), bg="white", fg="black")
        self.title_label.grid(row=0, column=0, columnspan=25, pady=10)

        # reset button to reset key colors
        self.reset_button = Button(self.root, text="Reset Key Colors", width=25, height=2, bg="lavender", fg="black",
                                   command=self.reset_colors)
        self.reset_button.grid(row=0, column=0, columnspan=6, pady=1)

        # bind each key on the keyboard to a note
        for key, notes in self.key_to_note.items():
            self.root.bind(key, lambda event, note=notes: self.piano_press(event, note))

    def create_piano_buttons(self):
        """
        function that creates the piano buttons

        :return:
        """
        column_num = 1
        # loop through the piano notes and create buttons for each
        for i in self.notes.keys():
            color = self.get_note_color(i)  # determine the color of the button
            text_color = self.get_text_color(i)  # determine the text color (black or white)
            note = self.get_right_audio(i)  # get the corresponding audio file for the note
            self.button = Button(self.root, text=i, width=5, height=10, bg=color, fg=text_color,
                                 command=self.create_note_command(note))
            self.button.grid(row=1, column=column_num)  # place the button in the grid
            self.buttons[i] = self.button  # add the button to the buttons dictionary
            column_num += 1  # increment column number

    def create_menu_bar(self):
        """
        function that creates the menu bar buttons

        :return:
        """
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)  # configure the root window to use the menu bar

        # create the menus in the menu bar
        piano_menu = Menu(menu_bar, tearoff=0)
        major_scale_menu = Menu(menu_bar, tearoff=0)
        minor_scale_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Piano Type", menu=piano_menu)
        menu_bar.add_cascade(label="Major Chords", menu=major_scale_menu)
        menu_bar.add_cascade(label="Minor Chords", menu=minor_scale_menu)

        # add major scales to the major scale menu
        for note in self.key_to_note.values():
            if note == "C2":
                break
            major_scale_menu.add_radiobutton(label=note, command=lambda scale=note: self.highlight_major_scale(scale))

        # add minor scales to the minor scale menu
        for note in self.key_to_note.values():
            if note == "C2":
                break
            minor_scale_menu.add_radiobutton(label=note, command=lambda scale=note: self.highlight_minor_scale(scale))

        # add options to select piano type (Grand, Electric)
        for piano_type in self.piano_types:
            piano_menu.add_radiobutton(label=piano_type, command=lambda t=piano_type: self.change_piano_type(t))

    def highlight_major_scale(self, root_note):
        """
        function that highlights the major scale based on the passed-in value

        :param root_note: the passed in root note to determine what scale to highlight
        :return:
        """
        note_list = list(self.key_to_note.values())
        root_index = note_list.index(root_note)

        # define the intervals for a major scale
        major_scale_intervals = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23]

        # calculate the notes in the major scale
        major_scale_notes = []
        for interval in major_scale_intervals:
            index = root_index + interval
            if index >= len(note_list):  # handle wrapping around the note list
                index = index - len(note_list)
            major_scale_notes.append(note_list[index])

        # highlight the buttons that correspond to the major scale notes
        for note, button in self.buttons.items():
            if note in major_scale_notes:
                button.config(bg="salmon")  # highlight with salmon color
            else:
                button.config(bg=self.get_note_color(note))  # reset to default color

    def highlight_minor_scale(self, rootnote):
        """
        function that highlights the minor scale based on the passed-in root note

        :param rootnote: root note that helps determine what scale to highlight
        :return:
        """
        note_list = list(self.key_to_note.values())
        root_index = note_list.index(rootnote)

        # define the intervals for a minor scale
        minor_scale_intervals = [0, 2, 3, 5, 7, 8, 10, 12, 14, 15, 17, 19, 20, 22]

        minor_scale_notes = []
        for interval in minor_scale_intervals:
            index = root_index + interval
            if index >= len(note_list):  # handle wrapping around the note list
                index = index - len(note_list)
            minor_scale_notes.append(note_list[index])

        # highlight the buttons that correspond to the minor scale notes
        for note, button in self.buttons.items():
            if note in minor_scale_notes:
                button.config(bg="purple")  # highlight with purple color
            else:
                button.config(bg=self.get_note_color(note))  # reset to default color

    def reset_colors(self):
        """
        function that resets the key colors back to normal

        :return:
        """
        # reset all key colors to their default state
        for note, button in self.buttons.items():
            button.config(bg=self.get_note_color(note))

    def change_piano_type(self, piano_type):
        """
        function that changes the piano type (ie. electric)

        :param piano_type: determines what audio files to use
        :return:
        """
        # change the piano type and update the buttons
        self.notes = self.piano_types[piano_type]
        self.update_buttons()

    def update_buttons(self):
        """
        function that updates the button's audio files

        :return:
        """
        # update the buttons with new sound files for the selected piano type
        for note, button in self.buttons.items():
            button.config(command=self.create_note_command(note))

    def get_note_color(self, note):
        """
        function that gets the correct note color for the keys

        :param note: note determines if the key is black or white
        :return: "black" "white"
        """
        # return black color for sharp notes, white for others
        if "#" in note:
            return "black"
        else:
            return "white"

    def get_text_color(self, note):
        """
        function that gets the correct text color so that the text is visible

        :param note: note determines which color to use
        :return: "white" "black"
        """
        # return white text for sharp notes, black for others
        if "#" in note:
            return "white"
        else:
            return "black"

    def get_right_audio(self, key):
        """
        function that gets the right audio file determined by the key

        :param key: determines which audio file to use
        :return self.notes[key]: returns audio file
        """
        # return the correct audio file for the given note
        if key in self.notes:
            return self.notes[key]
        else:
            return None

    def create_note_command(self, note):
        """
        function that creates a command for the note button

        :param note: passes the note to the play_note function
        :return:
        """
        # create a command for the note button
        def command():
            self.play_note(note)

        return command

    def piano_press(self, event, note):
        """
        function that handles key events for pressing notes

        :param event:
        :param note: passes the note pressed to the play_note_and_change_color function
        :return:
        """

        # method to handle key press events
        self.play_note_and_change_color(note)

    def play_note_and_change_color(self, note):
        """
        function that plays the note and changes the color to indicate that it's been pressed

        :param note: determines which button is pressed
        :return:
        """
        button = self.buttons.get(note)
        if button:
            # change button color temporarily to indicate it is pressed
            original_color = button.cget("bg")
            button.config(bg="lightblue")
            self.root.after(200, lambda: button.config(bg=original_color))  # revert back to original color

        audio_file = self.notes.get(note)
        self.play_note(audio_file)  # play the sound for the note

    def play_note(self, note):
        """
        function that helps play multiple notes

        :param note: determines which note is played
        :return:
        """
        x = Process(target=playsound, args=(note,))
        x.start()


def main():
    """
    main function that creates an object of the piano class and starts the program

    :return:
    """
    obj = Piano()
    obj.create_piano_buttons()
    obj.root.mainloop()


if __name__ == "__main__":
    main()  # call main function
