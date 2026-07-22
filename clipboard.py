from tkinter import messagebox


def copy_text(root, text):
    """
    Copies the given text to the system clipboard.
    """

    if text.strip() == "":
        messagebox.showwarning(
            "Warning",
            "Nothing to copy!"
        )
        return

    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

    messagebox.showinfo(
        "Copied",
        "Corrected text copied to clipboard successfully!"
    )