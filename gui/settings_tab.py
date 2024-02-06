# gui/settings_tab.py
import tkinter as tk
from tkinter import filedialog
from gui.tab_base import TabBase
from config.config_handler import ConfigHandler

class SettingsTab(TabBase):
    def __init__(self, notebook, gui_handler):
        super().__init__(notebook, "Settings")
        self.gui_handler = gui_handler

        # Your variables
        self.project_directory = tk.StringVar()
        self.current_project_path = tk.StringVar()
        self.template_path = tk.StringVar()

        self.load_ui()

    def load_ui(self):
        # Display current project directory
        project_directory_label = tk.Label(self, text="Project Directory:")
        project_directory_label.pack(pady=5)
        project_directory = self.gui_handler.config_handler.load_project_directory()
        project_directory_label.config(text=f"Currently set Project Directory: {project_directory}")

        # Display current project path
        current_project_path_label = tk.Label(self, text="Current Project Path:")
        current_project_path_label.pack(pady=5)
        current_project_path = self.gui_handler.config_handler.load_current_project_path()
        current_project_path_label.config(text=f"Currently set Current Project Path: {current_project_path}")

        # Display current template path
        template_path_label = tk.Label(self, text="Template Path:")
        template_path_label.pack(pady=5)
        template_path = self.gui_handler.config_handler.load_template_path()
        template_path_label.config(text=f"Currently set Template Path: {template_path}")

        # Buttons to update paths
        update_project_button = tk.Button(self, text="Update Project Directory", command=self.browse_and_update_project)
        update_project_button.pack(pady=5)

        update_current_project_button = tk.Button(self, text="Update Current Project Path", command=self.browse_and_update_current_project)
        update_current_project_button.pack(pady=5)

        update_template_button = tk.Button(self, text="Update Template Path", command=self.browse_and_update_template)
        update_template_button.pack(pady=10)

    def browse_and_update_project(self):
        folder = filedialog.askdirectory()
        if folder:
            # Update the project directory and display the updated path
            self.gui_handler.config_handler.update_project_directory(folder)
            project_directory_label = self.children['!label']  # Assumes the label is the first child
            project_directory_label.config(text=f"Currently set Project Directory: {folder}")

    def browse_and_update_current_project(self):
        folder = filedialog.askdirectory()
        if folder:
            # Update the current project path and display the updated path
            self.gui_handler.config_handler.update_current_project_path(folder)
            current_project_path_label = self.children['!label2']  # Assumes the label is the second child
            current_project_path_label.config(text=f"Currently set Current Project Path: {folder}")

    def browse_and_update_template(self):
        folder = filedialog.askdirectory()
        if folder:
            # Update the template path and display the updated path
            self.gui_handler.config_handler.update_template_path(folder)
            template_path_label = self.children['!label3']  # Assumes the label is the third child
            template_path_label.config(text=f"Currently set Template Path: {folder}")
