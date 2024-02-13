# gui/new_project_tab.py
import tkinter as tk
from gui.tab_base import TabBase
import os


class NewProjectTab(TabBase):
    def __init__(self, notebook, gui_handler):
        super().__init__(notebook, "New Project")

        # Your variables
        self.new_project_name = tk.StringVar()
        self.template_path = tk.StringVar()
        self.gui_handler = gui_handler
        self.load_ui()

    def load_ui(self):
        self.set_folder_entry("Project Name:", self.new_project_name, None)

        create_project_button = tk.Button(self, text="Create Project",
                                          command=self.create_project)

        create_project_button.pack(pady=10)

        template_label = tk.Label(self, text="Template File Structure:")
        template_label.pack()

        self.template_text = tk.Text(self, height=10, width=50)
        self.template_text.pack()

        initial_content = self.load_template_structure()
        self.template_text.insert(tk.END, initial_content)
        self.template_text.pack()

        # Button to update template path
        update_template_button = tk.Button(self, text="Update Template Path",
                                           command=self.
                                           browse_and_update_template)

        update_template_button.pack(pady=10)

    def create_project(self):
        # Get the project name from the entry
        new_project_name = self.new_project_name.get()

        # Check if the project name is not empty
        if new_project_name:
            # Get the project directory
            project_directory = \
                    self.gui_handler.config_handler.load_project_directory()

            # Call the create_new_project method of FileOrganizer
            success, message = self. \
                gui_handler.file_organizer.\
                create_new_project(new_project_name, project_directory)

            if success:
                tk.messagebox.showinfo("Success", message)
            else:
                tk.messagebox.showerror("Error", message)
        else:
            tk.messagebox.showerror("Error", "Please enter a project name.")

    def browse_and_update_template(self):
        template_path = tk.filedialog.askdirectory()
        if template_path:
            self.gui_handler.config_handler.update_template_path(template_path)
            self.template_text.delete(1.0, tk.END)
            file_structure = self.load_template_structure()
            self.template_text.insert(tk.END, file_structure)

    def load_template_structure(self, folder=None, indent=""):
        if folder is None:
            folder = self.gui_handler.config_handler.load_template_path()
        file_structure = f"{indent}{os.path.basename(folder)}/\n"
        for item in os.listdir(folder):
            item_path = os.path.join(folder, item)
            if os.path.isfile(item_path):
                file_structure += f"{indent}  - {item}\n"
            elif os.path.isdir(item_path):
                file_structure += self.\
                        load_template_structure(item_path, f"{indent}  | ")
        return file_structure
