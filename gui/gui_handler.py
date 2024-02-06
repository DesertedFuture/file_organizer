# gui/gui_handler.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from gui.main_tab import MainTab
from gui.new_project_tab import NewProjectTab
from gui.settings_tab import SettingsTab
from config.config_handler import ConfigHandler
from organizer.file_organizer import FileOrganizer

class GUIHandler:
    def __init__(self, master):
        self.root = master
        self.root.title("File Organizer")
        self.config_handler = ConfigHandler()
        self.file_organizer = FileOrganizer()

        self.root.geometry("800x400")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        self.load_main_tab()
        self.load_new_project_tab()
        self.load_settings_tab()

    def load_main_tab(self):
        main_tab = MainTab(self.notebook)
        self.notebook.add(main_tab, text="Main")

    def load_new_project_tab(self):
        new_project_tab = NewProjectTab(self.notebook, self.create_new_project)
        self.notebook.add(new_project_tab, text="New Project")

    def create_new_project(self, new_project_name):
        # Implement the logic to create a new project here
        # You can use the provided project name and take necessary actions
        # For now, let's just print the project name
        print(f"Creating a new project: {new_project_name}")

    def load_settings_tab(self):
        settings_tab = SettingsTab(self.notebook, self)
        self.notebook.add(settings_tab, text="Settings")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    gui_handler = GUIHandler(root)
    gui_handler.run()
