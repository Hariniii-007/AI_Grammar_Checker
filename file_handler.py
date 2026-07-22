from tkinter import filedialog, messagebox
import os


def open_file():
    """
    Opens a text file and returns its contents.
    """

    file_path = filedialog.askopenfilename(
        title="Open Text File",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return None

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        return text

    except Exception as e:
        messagebox.showerror("Error", f"Unable to open file.\n\n{e}")
        return None


def save_file(text):
    """
    Saves corrected text into the output folder.
    """

    os.makedirs("output", exist_ok=True)

    file_path = filedialog.asksaveasfilename(
        initialdir="output",
        initialfile="corrected_text.txt",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

        messagebox.showinfo(
            "Success",
            "Corrected text saved successfully!"
        )

    except Exception as e:
        messagebox.showerror("Error", f"Unable to save file.\n\n{e}")