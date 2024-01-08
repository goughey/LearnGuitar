import tkinter as tk

class GuitarNoteLearn:
    def __init__(self, master):
        self.master = master
        master.title("Guitar Note Learn")

        self.canvas = tk.Canvas(master, width=750, height=270)
        self.canvas.pack()

        self.note_labels = []
        self.draw_guitar()
        self.generate_note_labels()

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

    def generate_note_labels(self):
        string_notes = ['E', 'B', 'G', 'D', 'A', 'E']
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

        for string_num in range(6):
            for fret_num in range(20):  # You can adjust the number of frets as needed
                open_string_note = string_notes[string_num]
                fretted_note_index = (note_names.index(open_string_note) + fret_num) % 12
                fretted_note = note_names[fretted_note_index]

                x_position = 43 + fret_num * 35
                y_position = 43 + string_num * 30

                note_label = self.canvas.create_text(x_position, y_position, text=fretted_note, font=('Arial', 8))

                self.note_labels.append(note_label)

# Main execution block
if __name__ == "__main__":
    root = tk.Tk()
    app = GuitarNoteLearn(root)
    root.mainloop()
