import tkinter as tk
from tkinter import ttk
from noteGame import GuitarNoteQuiz
from chordGame import GuitarChordQuiz
from noteLearn import GuitarNoteLearn
from scaleLearn import GuitarScaleLearn

class MainMenu:
    def __init__(self, master):
        self.master = master
        menu_bar = tk.Menu(master)
        master.config(menu=menu_bar)

        game_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Menu", menu=game_menu)
        game_menu.add_command(label="Learn Notes", command=self.start_learn_note_mode)
        game_menu.add_command(label="Learn Scales", command=self.start_learn_scale_mode)
        game_menu.add_command(label="Note Select Game", command=self.start_note_select_mode)
        game_menu.add_command(label="Chord Game", command=self.start_chord_game_mode)
        game_menu.add_separator()
        game_menu.add_command(label="Main Menu", command=self.show_menu)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Preferences", command=self.start_chord_game_mode)

        self.show_menu()

    def clear_panel(self):
        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Menu):
                continue
            widget.destroy()

    def show_menu(self):
        self.clear_panel()
        self.master.title("Learn Guitar!")
        self.learn_note_button = tk.Button(self.master, text="Note Chart", command=self.start_learn_note_mode, width=20, height=5)
        self.learn_note_button.grid(row=0, column=0, padx=1, pady=1)

        self.learn_scale_frame = tk.Frame(self.master)
        self.learn_scale_frame.grid(row=0, column=1, padx=1, pady=1)
        self.scale_description = tk.Label(self.learn_scale_frame, text="Learn How To Play Scales!")
        self.scale_description.pack()
        self.scale_type_combobox = ttk.Combobox(self.learn_scale_frame, values=["Major (Ionian)", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Minor (Aeolian)", "Locrian", "Major Pentatonic", "Minor Pentatonic"])
        self.scale_type_combobox.set("Major (Ionian)")
        self.scale_type_combobox.config(state='readonly')
        self.scale_type_combobox.pack()
        self.learn_scale_button = tk.Button(self.learn_scale_frame, text="Open", command=self.start_learn_scale_mode)
        self.learn_scale_button.pack()
        
        self.chord_game_frame = tk.Frame(self.master)
        self.chord_game_frame.grid(row=1, column=0, padx=1, pady=1)
        self.chord_description = tk.Label(self.chord_game_frame, text="Test Your Chord Knowledge!")
        self.chord_description.pack()
        self.chord_type_combobox = ttk.Combobox(self.chord_game_frame, values=["Major", "Minor", "Diminished", "Augmented", "7ths", "Suspended 2th", "Suspended 4th"])
        self.chord_type_combobox.set("Major")
        self.chord_type_combobox.config(state='readonly')
        self.chord_type_combobox.pack()
        self.chord_game_button = tk.Button(self.chord_game_frame, text="Open", command=self.start_chord_game_mode)
        self.chord_game_button.pack()

        self.test_note_button = tk.Button(self.master, text="Note Game", command=self.start_note_select_mode, width=20, height=5)
        self.test_note_button.grid(row=1, column=1, padx=1, pady=1)
        
    def start_note_select_mode(self):
        self.clear_panel()
        game = GuitarNoteQuiz(self.master)

    def start_chord_game_mode(self):
        self.clear_panel()
        game = GuitarChordQuiz(self.master)

    def start_learn_note_mode(self):
        self.clear_panel()
        game = GuitarNoteLearn(self.master)

    def start_learn_scale_mode(self):
        self.clear_panel()
        game = GuitarScaleLearn(self.master)

if __name__ == "__main__":
    root = tk.Tk()
    menu = MainMenu(root)
    root.mainloop()
