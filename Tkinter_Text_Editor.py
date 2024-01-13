import tkinter as tk
from tkinter import filedialog, font, Scale

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Text Editor")
        self.initialize_gui()

    def initialize_gui(self):
        self.text_widget = tk.Text(self.root, wrap='word', undo=True, autoseparators=True)
        self.text_widget.pack(expand='yes', fill='both')

        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)

        format_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Format", menu=format_menu)
        format_menu.add_command(label="Font", command=self.choose_font)
        format_menu.add_command(label="Font Size", command=self.choose_font_size)

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)

    def open_file(self):
        try:
            file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, 'r') as file:
                    content = file.read()
                    self.text_widget.delete(1.0, tk.END)
                    self.text_widget.insert(tk.END, content)
        except Exception as e:
            print(f"Error opening file: {e}")

    def save_file(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, 'w') as file:
                    content = self.text_widget.get(1.0, tk.END)
                    file.write(content)
        except Exception as e:
            print(f"Error saving file: {e}")

    def save_as_file(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, 'w') as file:
                    content = self.text_widget.get(1.0, tk.END)
                    file.write(content)
        except Exception as e:
            print(f"Error saving file: {e}")

    def choose_font(self):
        try:
            font_path = filedialog.askopenfilename(title="Select Font File", filetypes=[("Font Files", "*.ttf;*.otf"), ("All Files", "*.*")])

            if font_path:
                new_font = font.Font(self.text_widget, self.text_widget.cget("font"))
                new_font.configure(family=font.Font(file=font_path).actual("family"))
                self.text_widget.configure(font=new_font)
        except Exception as e:
            print(f"Error choosing font: {e}")

    def choose_font_size(self):
        try:
            font_size_window = tk.Toplevel(self.root)
            font_size_window.title("Choose Font Size")

            current_font = font.Font(font=self.text_widget['font'])

            font_size_scale = Scale(font_size_window, from_=8, to=48, orient='horizontal', label='Font Size', length=200)
            font_size_scale.set(int(current_font.actual('size')))
            font_size_scale.pack(padx=20, pady=10)

            ok_button = tk.Button(font_size_window, text="OK", command=lambda: self.apply_font_size(font_size_scale.get(), font_size_window))
            ok_button.pack(pady=10)
        except Exception as e:
            print(f"Error choosing font size: {e}")

    def apply_font_size(self, new_size, window):
        try:
            current_font = font.Font(font=self.text_widget['font'])
            current_font.configure(size=int(new_size))
            font_str = "{family} {size} {weight} {slant}".format(**current_font.actual())
            self.text_widget.configure(font=font_str)
            window.destroy()
        except Exception as e:
            print(f"Error applying font size: {e}")
    

    def undo(self):
        try:
            self.text_widget.event_generate("<<Undo>>")
        except tk.TclError:
            print("Nothing left to undo")

    def redo(self):
        try:
            self.text_widget.event_generate("<<Redo>>")
        except tk.TclError:
            print("Nothing left to redo")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
