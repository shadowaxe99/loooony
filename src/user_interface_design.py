import tkinter as tk
from tkinter import ttk

class UserInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Loom-Like Mac App with Live Reactions")
        self.create_widgets()

    def create_widgets(self):
        self.create_account_button = ttk.Button(self.root, text="Create Account")
        self.create_account_button.grid(column=0, row=0)

        self.email_input = ttk.Entry(self.root)
        self.email_input.grid(column=1, row=0)

        self.password_input = ttk.Entry(self.root, show="*")
        self.password_input.grid(column=2, row=0)

        self.record_button = ttk.Button(self.root, text="Record")
        self.record_button.grid(column=0, row=1)

        self.video_audio_settings = ttk.Button(self.root, text="Settings")
        self.video_audio_settings.grid(column=1, row=1)

        self.recipient_selection = ttk.Combobox(self.root)
        self.recipient_selection.grid(column=2, row=1)

        self.digital_gifts_selection = ttk.Combobox(self.root)
        self.digital_gifts_selection.grid(column=0, row=2)

        self.live_reactions_button = ttk.Button(self.root, text="Live Reactions")
        self.live_reactions_button.grid(column=1, row=2)

        self.message_input = ttk.Entry(self.root)
        self.message_input.grid(column=2, row=2)

        self.notification_button = ttk.Button(self.root, text="Notifications")
        self.notification_button.grid(column=0, row=3)

        self.privacy_settings_button = ttk.Button(self.root, text="Privacy & Security")
        self.privacy_settings_button.grid(column=1, row=3)

def main():
    root = tk.Tk()
    UserInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()