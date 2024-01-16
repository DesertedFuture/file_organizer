import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from organizer.file_organizer import FileOrganizer
import os
import configparser

class BaseGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create a Notebook for organizing tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # Instantiate FileOrganizer
        self.file_organizer = FileOrganizer()

        # Load configuration
        self.config = configparser.ConfigParser()
        self.load_config()

    def load_config(self):
        try:
            self.config.read('config.ini')
            self.project_folder = tk.StringVar(value=self.config.get('Settings', 'project_folder'))
        except configparser.Error:
            # Handle the case when the config file is not found or has an incorrect format
            self.project_folder = tk.StringVar()

    def save_config(self):
        try:
            if not self.config.has_section('Settings'):
                self.config.add_section('Settings')
            self.config.set('Settings', 'project_folder', self.project_folder.get())

            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
        except configparser.Error as e:
            # Handle the case when there is an error while saving the config
            print(f"Error saving configuration: {e}")

    def browse_file(self):
        file = filedialog.askopenfilename()
        return file

    def browse_folder(self):
        folder = filedialog.askdirectory()
        return folder

    def create_tab(self, title):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=title)
        return tab

    def set_folder_entry(self, entry_var, label_text, browse_command):
        tk.Label(self, text=label_text).grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=entry_var, width=40).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self, text="Browse", command=browse_command).grid(row=0, column=2, padx=5, pady=5)

class GUIHandler(BaseGUI):
    def __init__(self, root):
        super().__init__()

        self.root = root
        self.root.title("File Organizer")

        # Create main tab
        main_tab = self.create_tab('Main')

        # Initialize attributes
        self.source_file = tk.StringVar()
        self.destination_folder = tk.StringVar()
        self.rename_file_text = tk.StringVar()

        # Entry for source file
        self.set_folder_entry(self.source_file, "Source File:", self.browse_and_set_source_file)

        # Entry for destination folder
        self.set_folder_entry(self.destination_folder, "Destination Folder:", self.browse_and_set_destination_folder)

        # Entry for renaming the file
        tk.Label(main_tab, text="Rename File:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(main_tab, textvariable=self.rename_file_text, width=40).grid(row=2, column=1, padx=5, pady=5)

        # Confirmation button
        tk.Button(main_tab, text="Confirm", command=self.show_confirmation).grid(row=3, column=0, columnspan=3, pady=10)

        # Create settings tab
        settings_tab = self.create_tab('Settings')

        # Entry for source project folder
        self.set_folder_entry(self.destination_folder, "Source Project Folder:", self.browse_and_set_source_project_folder)

        # Create new project tab
        new_project_tab = self.create_tab('New Project')

        tk.Label(new_project_tab, text="Project Name:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Entry(new_project_tab).grid(row=0, column=1, padx=5, pady=5)

        # Button to select project folder
        tk.Button(new_project_tab, text="Select Project Folder", command=self.browse_and_set_project_folder).grid(row=1, column=0, columnspan=2, pady=10)

    def show_confirmation(self):
        source_file = self.source_file.get()
        destination_folder = self.destination_folder.get()
        new_name = self.get_new_file_name()

        confirmation_message = (
            f"Source File: {source_file}\n"
            f"Destination Folder: {destination_folder}\n"
            f"New File Name: {new_name}"
        )

        # Prompt the user with a confirmation dialog
        user_response = messagebox.askokcancel("Confirmation", confirmation_message)

        # If the user clicks "OK," proceed with file renaming and moving
        if user_response:
            try:
                # Perform the file relocation logic
                self.rename_and_move_file(source_file, destination_folder, new_name)

                messagebox.showinfo("Success", "Files organized successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error moving the file: {str(e)}")

    def get_new_file_name(self):
        # Customize this method to generate the new file name based on your requirements
        return self.rename_file_text.get()

    def rename_and_move_file(self, source_file, destination_folder, new_name):
        # Call the corresponding method in FileOrganizer
        self.file_organizer.rename_and_move_file(source_file, destination_folder, new_name)

    def run_file_organizer(self):
        # Get user input for renaming
        user_input = self.rename_file_text.get()

        # Get source file and destination folder
        source_file = self.source_file.get()
        destination_folder = self.destination_folder.get()

        if source_file and destination_folder:
            # Construct new file name based on the desired architecture
            new_file_name = f"{user_input}_{os.path.basename(source_file)}"

            # Construct the full path for the destination file
            destination_file = os.path.join(destination_folder, new_file_name)

            try:
                # Perform the file relocation logic
                shutil.move(source_file, destination_file)

                messagebox.showinfo("Success", "Files organized successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error moving the file: {str(e)}")
        else:
            messagebox.showwarning("Warning", "Please provide both source file and destination folder.")

    def browse_and_set_source_file(self):
        file = self.browse_file()
        self.set_source_file(file)

    def browse_and_set_destination_folder(self):
        folder = self.browse_folder()
        self.set_destination_folder(folder)

    def browse_and_set_source_project_folder(self):
        folder = self.browse_folder()
        if folder:
            self.destination_folder.set(folder)
            # Include logic to set source project folder in FileOrganizer

    def browse_and_set_project_folder(self):
        project_folder = self.browse_folder()
        self.set_project_folder(project_folder)

    def set_destination_folder(self, folder):
        if folder:
            self.destination_folder.set(folder)

    def set_project_folder(self, folder):
        if folder:
            self.project_folder.set(folder)
            self.save_config()

    def set_source_file(self, file):
        if file:
            self.source_file.set(file)

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    gui_handler = GUIHandler(root)
    root.mainloop()
