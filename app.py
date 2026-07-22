import customtkinter as ctk
from tkinter import messagebox

from grammar import check_grammar
from file_handler import open_file, save_file
from clipboard import copy_text
from theme import toggle_theme
from utils import get_statistics, export_report

# ---------------- Appearance ----------------

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

# ---------------- Main Window ----------------

root = ctk.CTk()
root.title("AI Grammar Checker")
root.geometry("1000x780")
root.resizable(False, False)

status_var = ctk.StringVar(value="Ready")

# ---------------- Functions ----------------

def check_text():

    text = input_box.get("1.0", "end").strip()

    if text == "":
        messagebox.showwarning(
            "Warning",
            "Please enter some text."
        )
        return

    corrected_text, total_errors, suggestions = check_grammar(text)

    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    output_box.insert("1.0", corrected_text)
    output_box.configure(state="disabled")

    error_label.configure(
        text=f"Errors Found : {total_errors}"
    )

    stats = get_statistics(text)

    char_count.configure(
        text=f"Characters : {stats['characters']}"
    )

    word_count.configure(
        text=f"Words : {stats['words']}"
    )

    sentence_count.configure(
        text=f"Sentences : {stats['sentences']}"
    )

    unique_word_count.configure(
        text=f"Unique Words : {stats['unique_words']}"
    )

    reading_time.configure(
        text=f"Reading Time : {stats['reading_time']} min"
    )

    suggestion_box.configure(state="normal")
    suggestion_box.delete("1.0", "end")

    if len(suggestions) == 0:
        suggestion_box.insert(
            "end",
            "No grammar mistakes found."
        )
    else:
        for item in suggestions:
            suggestion_box.insert(
                "end",
                item + "\n\n"
            )

    suggestion_box.configure(state="disabled")

    status_var.set("Grammar Checked Successfully")


def clear_all():

    input_box.delete("1.0", "end")

    output_box.configure(state="normal")
    output_box.delete("1.0", "end")
    output_box.configure(state="disabled")

    suggestion_box.configure(state="normal")
    suggestion_box.delete("1.0", "end")
    suggestion_box.configure(state="disabled")

    error_label.configure(
        text="Errors Found : 0"
    )

    char_count.configure(
        text="Characters : 0"
    )

    word_count.configure(
        text="Words : 0"
    )

    sentence_count.configure(
        text="Sentences : 0"
    )

    unique_word_count.configure(
        text="Unique Words : 0"
    )

    reading_time.configure(
        text="Reading Time : 0 min"
    )

    status_var.set("Ready")


def open_text():

    text = open_file()

    if text:

        input_box.delete("1.0", "end")
        input_box.insert("1.0", text)

        status_var.set("File Opened")


def save_text():

    text = output_box.get("1.0", "end")

    save_file(text)

    status_var.set("File Saved")


def copy_output():

    text = output_box.get("1.0", "end")

    copy_text(root, text)

    status_var.set("Copied")


def export_statistics():

    text = input_box.get("1.0", "end").strip()

    if text == "":
        messagebox.showwarning(
            "Warning",
            "Nothing to export."
        )
        return

    stats = get_statistics(text)

    export_report(stats)

    status_var.set("Report Exported")
    # ---------------- Title ----------------

title = ctk.CTkLabel(
    root,
    text="AI Grammar Checker",
    font=("Arial", 30, "bold")
)
title.pack(pady=20)

# ---------------- Input ----------------

input_label = ctk.CTkLabel(
    root,
    text="Enter Text",
    font=("Arial", 18)
)
input_label.pack()

input_box = ctk.CTkTextbox(
    root,
    width=900,
    height=150
)
input_box.pack(pady=10)

# ---------------- Buttons ----------------

button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=10)

check_btn = ctk.CTkButton(
    button_frame,
    text="✅ Check Grammar",
    width=150,
    command=check_text
)
check_btn.grid(row=0, column=0, padx=5)

open_btn = ctk.CTkButton(
    button_frame,
    text="📂 Open",
    width=100,
    command=open_text
)
open_btn.grid(row=0, column=1, padx=5)

save_btn = ctk.CTkButton(
    button_frame,
    text="💾 Save",
    width=100,
    command=save_text
)
save_btn.grid(row=0, column=2, padx=5)

copy_btn = ctk.CTkButton(
    button_frame,
    text="📋 Copy",
    width=100,
    command=copy_output
)
copy_btn.grid(row=0, column=3, padx=5)

theme_btn = ctk.CTkButton(
    button_frame,
    text="🌙 Dark Mode",
    width=120,
    command=toggle_theme
)
theme_btn.grid(row=0, column=4, padx=5)

export_btn = ctk.CTkButton(
    button_frame,
    text="📄 Export",
    width=120,
    command=export_statistics
)
export_btn.grid(row=0, column=5, padx=5)

clear_btn = ctk.CTkButton(
    button_frame,
    text="🗑 Clear",
    width=100,
    command=clear_all
)
clear_btn.grid(row=0, column=6, padx=5)

# ---------------- Error Label ----------------

error_label = ctk.CTkLabel(
    root,
    text="Errors Found : 0",
    font=("Arial", 18, "bold"),
    text_color="red"
)
error_label.pack(pady=10)

# ---------------- Output ----------------

output_label = ctk.CTkLabel(
    root,
    text="Corrected Text",
    font=("Arial", 18)
)
output_label.pack()

output_box = ctk.CTkTextbox(
    root,
    width=900,
    height=150
)
output_box.pack(pady=10)

output_box.configure(state="disabled")

# ---------------- Suggestions ----------------

suggestion_title = ctk.CTkLabel(
    root,
    text="Grammar Suggestions",
    font=("Arial", 18)
)
suggestion_title.pack()

suggestion_box = ctk.CTkTextbox(
    root,
    width=900,
    height=120
)
suggestion_box.pack(pady=10)

suggestion_box.configure(state="disabled")

# ---------------- Statistics ----------------

stats_frame = ctk.CTkFrame(root)
stats_frame.pack(pady=15)

char_count = ctk.CTkLabel(
    stats_frame,
    text="Characters : 0",
    width=150
)
char_count.grid(row=0, column=0, padx=10)

word_count = ctk.CTkLabel(
    stats_frame,
    text="Words : 0",
    width=120
)
word_count.grid(row=0, column=1, padx=10)

sentence_count = ctk.CTkLabel(
    stats_frame,
    text="Sentences : 0",
    width=140
)
sentence_count.grid(row=0, column=2, padx=10)

unique_word_count = ctk.CTkLabel(
    stats_frame,
    text="Unique Words : 0",
    width=150
)
unique_word_count.grid(row=0, column=3, padx=10)

reading_time = ctk.CTkLabel(
    stats_frame,
    text="Reading Time : 0 min",
    width=150
)
reading_time.grid(row=0, column=4, padx=10)
# ---------------- Status Bar ----------------

status_label = ctk.CTkLabel(
    root,
    textvariable=status_var,
    font=("Arial", 14)
)

status_label.pack(pady=10)


# ---------------- Keyboard Shortcuts ----------------

root.bind("<Control-o>", lambda event: open_text())

root.bind("<Control-s>", lambda event: save_text())

root.bind("<Control-c>", lambda event: copy_output())

root.bind("<Control-e>", lambda event: export_statistics())

root.bind("<Control-l>", lambda event: clear_all())

root.bind("<Control-q>", lambda event: root.destroy())


# ---------------- About Window ----------------

def show_about():

    about = ctk.CTkToplevel(root)

    about.title("About")

    about.geometry("420x300")

    about.resizable(False, False)

    ctk.CTkLabel(
        about,
        text="AI Grammar Checker",
        font=("Arial", 24, "bold")
    ).pack(pady=20)

    ctk.CTkLabel(
        about,
        text="Version 1.0",
        font=("Arial", 16)
    ).pack()

    ctk.CTkLabel(
        about,
        text="Developed by\nHarini S",
        font=("Arial", 16)
    ).pack(pady=15)

    ctk.CTkLabel(
        about,
        text="B.Tech Information Technology",
        font=("Arial", 15)
    ).pack()

    ctk.CTkButton(
        about,
        text="Close",
        command=about.destroy
    ).pack(pady=20)


# ---------------- Menu Bar ----------------

menu_frame = ctk.CTkFrame(root)

menu_frame.pack(fill="x", padx=10, pady=5)

ctk.CTkButton(
    menu_frame,
    text="📂 Open",
    width=90,
    command=open_text
).pack(side="left", padx=5)

ctk.CTkButton(
    menu_frame,
    text="💾 Save",
    width=90,
    command=save_text
).pack(side="left", padx=5)

ctk.CTkButton(
    menu_frame,
    text="📋 Copy",
    width=90,
    command=copy_output
).pack(side="left", padx=5)

ctk.CTkButton(
    menu_frame,
    text="📄 Export",
    width=90,
    command=export_statistics
).pack(side="left", padx=5)

ctk.CTkButton(
    menu_frame,
    text="🗑 Clear",
    width=90,
    command=clear_all
).pack(side="left", padx=5)

ctk.CTkButton(
    menu_frame,
    text="ℹ About",
    width=90,
    command=show_about
).pack(side="right", padx=5)


# ---------------- Start Application ----------------

status_var.set("Application Ready")

root.mainloop()