import random
import tkinter as tk

class GuitarScaleLearn:
    def __init__(self, master):
        self.master = master
        master.title("Guitar Note Quiz")

        self.string_label = tk.Label(master, text="")
        self.string_label.pack()

        self.new_question_button = tk.Button(master, text="New Question", command=self.generate_new_question)
        self.new_question_button.pack()

        self.canvas = tk.Canvas(master, width=750, height=270)
        self.canvas.pack()

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
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        open_string_note = string_notes[self.string_number - 1]
        fretted_note_index = (note_names.index(open_string_note) + self.fret_number) % 12
        fretted_note = note_names[fretted_note_index]
        return fretted_note

    def get_string_name(self):
        string_names = ['E1', 'B2', 'G3', 'D4', 'A5', 'E6']
        return string_names[self.string_number-1]

    def draw_guitar(self):
        self.canvas.delete("all")
        string_colors = ['black', 'black', 'black', 'black', 'black', 'black']

        # Draw the guitar body
        body_coords = [470, 50, 715, 50, 715, 200, 470, 200, 1000, 300, 850, 125, 1000, -50]
        self.canvas.create_polygon(body_coords, fill='brown', outline='black')

        # Draw the guitar neck
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

    def check_answer(self):
        user_input = self.entry.get().upper()
        correct_note = self.get_note()

        if user_input == correct_note:
            self.result_label.config(text="Correct!")
        else:
            self.result_label.config(text=f"Wrong. The correct note is {correct_note}")

    def generate_new_question(self):
        self.generate_random_numbers()
        self.string_label.config(text=f"String: {self.get_string_name()}, Fret: {self.fret_number}")
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.draw_guitar()

if __name__ == "__main__":
    root = tk.Tk()
    app = GuitarScaleLearn(root)
    root.mainloop()