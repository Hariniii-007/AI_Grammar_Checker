import customtkinter as ctk

# Stores the current theme
current_theme = "Light"


def toggle_theme():
    """
    Toggle between Light Mode and Dark Mode.
    """
    global current_theme

    if current_theme == "Light":
        ctk.set_appearance_mode("Dark")
        current_theme = "Dark"
    else:
        ctk.set_appearance_mode("Light")
        current_theme = "Light"