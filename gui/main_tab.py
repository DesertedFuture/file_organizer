# gui/main_tab.py
import tkinter as tk
from tkinter import filedialog, messagebox
from gui.tab_base import TabBase
from organizer.file_organizer import FileOrganizer

class MainTab(TabBase):
    def __init__(self, notebook):
        super().__init__(notebook, "Main")

        # Your variables
        self.source_file = tk.StringVar()
        self.destination_folder = tk.StringVar()
        self.rename_file_text = tk.StringVar()

        # File organizer instance
        self.file_organizer = FileOrganizer()

        self.load_ui()

    def load_ui(self):
        self.set_folder_entry("Source File:", self.source_file, self.browse_and_set_file)
        self.set_folder_entry("Destination Folder:", self.destination_folder, self.browse_and_set_folder)
        self.set_folder_entry("Rename File:", self.rename_file_text, None)

        # Button to move and rename the file
        move_rename_button = tk.Button(self, text="Move and Rename File", command=self.move_and_rename_file)
        move_rename_button.pack(pady=10)

    def browse_and_set_file(self):
        file = filedialog.askopenfilename()
        self.source_file.set(file)

    def browse_and_set_folder(self):
        folder = filedialog.askdirectory()
        self.destination_folder.set(folder)

    def move_and_rename_file(self):
        source_file_path = self.source_file.get()
        destination_folder = self.destination_folder.get()
        rename_text = self.rename_file_text.get()

        if not source_file_path or not destination_folder or not rename_text:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        success, message = self.file_organizer.move_and_rename_file(source_file_path, destination_folder, rename_text)

        if success:
            messagebox.showinfo("Success", f"File moved and renamed to:\n{message}")
        else:
            messagebox.showerror("Error", f"Failed to move and rename file:\n{message}")
