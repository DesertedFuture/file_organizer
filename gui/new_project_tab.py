# gui/new_project_tab.py
import tkinter as tk
from tkinter import ttk, messagebox
from gui.tab_base import TabBase

class NewProjectTab(TabBase):
    def __init__(self, notebook, gui_handler):
        super().__init__(notebook, "New Project")

        # Your variables
        self.new_project_name = tk.StringVar()
        self.gui_handler = gui_handler
        print(type(self.gui_handler))

        self.load_ui()

    def load_ui(self):
        self.set_folder_entry("Project Name:", self.new_project_name, None)

        # Button to create a new project
        create_project_button = tk.Button(self, text="Create Project", command=self.create_project)
        create_project_button.pack(pady=10)

        # Display template file structure (you can customize this part based on your needs)
        template_label = tk.Label(self, text="Template File Structure:")
        template_label.pack()

        template_text = tk.Text(self, height=10, width=50)
        template_text.insert(tk.END, "Your template file structure here")
        template_text.pack()

    def create_project(self):
        # Get the project name from the entry
        new_project_name = self.new_project_name.get()

        # Check if the project name is not empty
        if new_project_name:
            # Get the project directory
            project_directory = self.gui_handler.config_handler.load_project_directory()

            # Call the create_new_project method of FileOrganizer
            success, message = self.gui_handler.file_organizer.create_new_project(new_project_name, project_directory)

            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        else:
            messagebox.showerror("Error", "Please enter a project name.")
