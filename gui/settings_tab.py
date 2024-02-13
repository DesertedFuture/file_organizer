# gui/settings_tab.py
import tkinter as tk
from tkinter import filedialog
from gui.tab_base import TabBase


class SettingsTab(TabBase):
    def __init__(self, notebook, gui_handler):
        super().__init__(notebook, "Settings")
        self.gui_handler = gui_handler

        # Your variables
        self.project_directory_label = tk.Label(self,
                                                text="Project Directory:")
        self.project_directory_label.pack(pady=5)

        self.current_project_path_label = tk.\
            Label(self,
                  text="Current Project Path:")
        self.current_project_path_label.pack(pady=5)

        self.load_ui()

    def load_ui(self):
        self.update_project_directory_label()
        self.update_current_project_path_label()

        project_directory_button = tk.\
            Button(self,
                   text="Update Project Directory",
                   command=self.browse_and_update_project)
        project_directory_button.pack(pady=5)

        update_current_project_button = tk. \
            Button(self,
                   text="Update Current Project Path",
                   command=self.browse_and_update_current_project)
        update_current_project_button.pack(pady=5)

    def update_project_directory_label(self):
        project_directory = self.\
                gui_handler.config_handler.load_project_directory()
        self.project_directory_label. \
            config(text=f"""Currently set Project Directory:\n
                   {project_directory}""")

    def update_current_project_path_label(self):
        current_project_path = self.\
                gui_handler.config_handler.\
                load_current_project_path()
        self.current_project_path_label. \
            config(text=f"""Currently set Current Project Path:\n
                   {current_project_path}""")

    def browse_and_update_project(self):
        folder = filedialog.askdirectory()
        if folder:
            # Update the project directory and display the updated path
            self.gui_handler.config_handler.update_project_directory(folder)
            self.update_project_directory_label()

    def browse_and_update_current_project(self):
        folder = filedialog.askdirectory()
        if folder:
            # Update the current project path and display the updated path
            self.gui_handler.config_handler.update_current_project_path(folder)
            self.update_current_project_path_label()

