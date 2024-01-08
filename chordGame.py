import random
import tkinter as tk
from tkinter import ttk

class GuitarChordQuiz:
    def __init__(self, master):
        self.master = master
        master.title("Guitar Chord Quiz")
        self.note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        self.options_frame = tk.Frame(master)
        self.options_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.show_labels = True
        self.peak_button = tk.Button(self.options_frame, text="Peak", command=self.generate_note_labels)
        self.peak_button.pack(side="left")

        self.string_label = tk.Label(self.options_frame, text="Which Chord Is This?")
        self.string_label.pack()
        
        self.canvas = tk.Canvas(master, width=750, height=270)
        self.canvas.pack()

        self.new_question_frame = tk.Frame(master)
        self.new_question_frame.pack(side='right', fill='none', expand=False)

        self.chord_type_label = tk.Label(self.new_question_frame, text="Chord Type:")
        self.chord_type_combobox = ttk.Combobox(self.new_question_frame, values=["maj", "min", "dim", "aug", "7ths", "sus2", "sus4"])
        self.chord_type_combobox.set("maj")
        self.chord_type_combobox.config(state='readonly')
        self.new_question_button = tk.Button(self.new_question_frame, text="New Question", command=self.generate_new_question)

        self.chord_type_label.grid(row=0, column=1, padx=(10, 0), pady=10, sticky="w")
        self.chord_type_combobox.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.new_question_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky="w")

        self.answer_frame = tk.Frame(master)
        self.answer_frame.pack()

        self.check_label = tk.Label(self.answer_frame, text="Answer:   ")
        self.check_label.pack(side=tk.LEFT)

        self.entry = tk.Entry(self.answer_frame, width=10)
        self.entry.pack(side=tk.LEFT)

        self.check_button = tk.Button(self.answer_frame, text="Check Answer", command=self.check_answer)
        self.check_button.pack(side=tk.LEFT)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.generate_new_question()

    def generate_random_numbers(self):
        self.string_number = random.randint(1, 6)
        self.fret_number = random.randint(0, 19)
        return self.string_number, self.fret_number

    def get_note(self):
        string_notes = ['E', 'B', 'G', 'D', 'A', 'E']
        open_string_note = string_notes[self.string_number - 1]
        fretted_note_index = (self.note_names.index(open_string_note) + self.fret_number) % 12
        fretted_note = self.note_names[fretted_note_index]
        return fretted_note

    def get_string_name(self):
        string_names = ['E1', 'B2', 'G3', 'D4', 'A5', 'E6']
        return string_names[self.string_number - 1]

    def draw_guitar(self):
        self.canvas.delete("all")
        string_colors = ['black', 'black', 'black', 'black', 'black', 'black']

        # Draw the guitar body
        body_coords = [470, 50, 715, 50, 715, 200, 470, 200, 1000, 300, 850, 125, 1000, -50]
        self.canvas.create_polygon(body_coords, fill='brown', outline='black')
        neck_coords = [50, 50, 0, 40, 0, 208, 30, 215, 50, 200]
        self.canvas.create_polygon(neck_coords, fill='brown', outline='black')
        for i in range(6):
            self.canvas.create_line(0, 50 + i * 30, 800, 50 + i * 30, fill=string_colors[i], width=2)
        for fret in range(20):
            fret_position = 50 + fret * 35
            self.canvas.create_line(fret_position, 50, fret_position, 200, fill='black', width=1)
        self.canvas.create_line(49, 50, 49, 200, fill='black', width=5)
        self.canvas.create_line(716, 50, 716, 200, fill='black', width=5)
                
        string_tuning = [4, 11, 7, 2, 9, 4]
        positions = [-24, -20, -17, -12, -8, -5, 0, 4, 7, 12, 16, 19, 24]
        selected_string_position = 20 + self.string_number * 30
        selected_fret_position = 50 + self.fret_number * 35
        self.canvas.create_oval(selected_fret_position - 5, selected_string_position - 5, selected_fret_position + 5, selected_string_position + 5, fill='red')
        distances = [self.fret_number]

        for i in range(6):
            if i == self.string_number - 1:
                continue

            string_position = 50 + i * 30
            open_string_position = string_tuning[i]

            # Find the selected note on each string
            temp_fret_position = (self.fret_number + string_tuning[self.string_number - 1] - open_string_position) % 12
            valid = False
            while not valid:
                random_position = random.choice(positions)
                if 0 <= temp_fret_position + random_position <= 19:
                    # Check the distance with every item in the distances array
                    valid = all(abs(temp_fret_position + random_position - d) <= 4 for d in distances)
                    if valid:
                        distances.append(temp_fret_position + random_position)
            temp_fret_position = (temp_fret_position + random_position)
            fret_position = 50 + temp_fret_position * 35

            self.canvas.create_oval(fret_position - 5, string_position - 5, fret_position + 5, string_position + 5, fill='red')

    def generate_note_labels(self):
        if self.show_labels:
            chord_notes = self.get_chord_notes()
            chord_notes_str = ", ".join([self.note_names[note] for note in chord_notes])
            self.string_label.config(text=f"Chord Notes: {chord_notes_str}\nString: {self.get_string_name()}, Fret: {self.fret_number}, Chord: {self.get_note()}")

            string_notes = ['E', 'B', 'G', 'D', 'A', 'E']
            for string_num in range(6):
                for fret_num in range(20):
                    open_string_note = string_notes[string_num]
                    fretted_note_index = (self.note_names.index(open_string_note) + fret_num) % 12
                    fretted_note = self.note_names[fretted_note_index]

                    x_position = 43 + fret_num * 35
                    y_position = 43 + string_num * 30

                    note_label = self.canvas.create_text(x_position, y_position, text=fretted_note, font=('Arial', 8))
                    self.note_labels.append(note_label)
        else:
            for label in self.note_labels:
                self.string_label.config(text="Which Chord Is This?")
                self.canvas.delete(label)
        self.show_labels = not self.show_labels

    def get_chord_notes(self):
        root_index = self.note_names.index(self.get_note())
        third_index = (root_index + 4) % 12
        fifth_index = (root_index + 7) % 12
        return [root_index, third_index, fifth_index]

    def check_answer(self):
        user_input = self.entry.get().upper()
        correct_note = self.get_note()

        if user_input == correct_note:
            self.result_label.config(text="Correct!")
        else:
            self.result_label.config(text=f"Wrong. The chord is {correct_note}")

    def generate_new_question(self):
        if not self.show_labels:
            self.string_label.config(text="Which Chord Is This?")
            self.show_labels = not self.show_labels
        self.generate_random_numbers()
        chord_notes = self.get_chord_notes()
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.draw_guitar()
        self.note_labels = []

if __name__ == "__main__":
    root = tk.Tk()
    app = GuitarChordQuiz(root)
    root.mainloop()
