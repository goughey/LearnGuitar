import random
import tkinter as tk

class GuitarNoteQuiz:
    def __init__(self, master):
        self.master = master
        master.title("Guitar Note Quiz")
        self.note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        self.options_frame = tk.Frame(master)
        self.options_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.show_labels = True
        self.peak_button = tk.Button(self.options_frame, text="Peak", command=self.generate_note_labels)
        self.peak_button.pack(side="left")

        self.string_label = tk.Label(self.options_frame, text="")
        self.string_label.pack()

        self.canvas = tk.Canvas(master, width=750, height=270)
        self.canvas.pack()

        self.bottom_frame = tk.Frame(master)
        self.bottom_frame.pack(side="top", fill="both", expand=True, padx=10)

        self.answer_frame = tk.Frame(self.bottom_frame)
        self.answer_frame.pack()

        self.check_label = tk.Label(self.answer_frame, text="Answer:   ")
        self.check_label.pack(side='left')

        self.entry = tk.Entry(self.answer_frame, width=10)
        self.entry.pack(side='left')

        self.check_button = tk.Button(self.answer_frame, text="Check Answer", command=self.check_answer)
        self.check_button.pack(side='left')

        self.new_question_button = tk.Button(self.bottom_frame, text="New Question", command=self.generate_new_question)
        self.new_question_button.pack(side='right')

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.generate_new_question()

    def generate_random_numbers(self): # Generates a point on the fretboard
        self.string_number = random.randint(1, 6)
        self.fret_number = random.randint(0, 19)
        return self.string_number, self.fret_number

    def get_note(self): # Gets the note the user us trying to guess
        string_notes = ['E', 'B', 'G', 'D', 'A', 'E']
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        open_string_note = string_notes[self.string_number - 1]
        fretted_note_index = (note_names.index(open_string_note) + self.fret_number) % 12
        fretted_note = note_names[fretted_note_index]
        return fretted_note

    def get_string_name(self): # Gets the name of the selected string
        string_names = ['E1', 'B2', 'G3', 'D4', 'A5', 'E6']
        return string_names[self.string_number-1]

    def draw_guitar(self):  # Draw the guitar body and the position to answer
        self.canvas.delete("all")
        string_colors = ['black', 'black', 'black', 'black', 'black', 'black']

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

        selected_string_position = 20 + self.string_number * 30
        selected_fret_position = 50 + self.fret_number * 35
        self.canvas.create_oval(selected_fret_position - 5, selected_string_position - 5, selected_fret_position + 5, selected_string_position + 5, fill='red')

    def generate_note_labels(self):  # Peak functionality (display notes on guitar)
        if self.show_labels:
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
                self.canvas.delete(label)
        self.show_labels = not self.show_labels

    def check_answer(self): # Checks the users response to the question
        user_input = self.entry.get().upper()
        correct_note = self.get_note()

        if user_input == correct_note:
            self.result_label.config(text="Correct!")
        else:
            self.result_label.config(text=f"Wrong. The correct note is {correct_note}")

    def generate_new_question(self):
        if not self.show_labels:
            self.show_labels = not self.show_labels
        self.generate_random_numbers()
        self.string_label.config(text=f"String: {self.get_string_name()}, Fret: {self.fret_number}")
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.draw_guitar()
        self.note_labels = []

if __name__ == "__main__":
    root = tk.Tk()
    app = GuitarNoteQuiz(root)
    root.mainloop()