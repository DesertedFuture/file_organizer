import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from organizer.file_organizer import FileOrganizer
import os
from config.config_handler import ConfigHandler


class GUIHandler:
    def __init__(self, master):
        self.root = master
        self.root.title("File Organizer")
        self.config_handler = ConfigHandler()

        # Create a Notebook for organizing tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Instantiate FileOrganizer
        self.file_organizer = FileOrganizer()

        main_tab = self.create_main_tab()
        new_project_tab = self.create_new_project_tab()
        settings_tab = self.create_settings_tab()

        self.directory_folder = tk.StringVar()

    def create_main_tab(self):
        main_tab = ttk.Frame(self.notebook)
        self.notebook.add(main_tab, text='Main')

        # Initialize attributes
        self.source_file = tk.StringVar()
        self.destination_folder = tk.StringVar()
        self.rename_file_text = tk.StringVar()

        # Entry for re-naming
        self.set_folder_entry(main_tab, self.source_file, "Source File:", self.browse_and_set_file)
        self.set_folder_entry(main_tab, self.destination_folder, "Destination Folder:", self.browse_and_set_folder)

        # Entry for renaming the file
        tk.Label(main_tab, text="Rename File:").pack(pady=5)
        tk.Entry(main_tab, textvariable=self.rename_file_text, width=40).pack(pady=5)

        # Confirmation buttn
        tk.Button(main_tab, text="Confirm", command=self.show_confirmation).pack(pady=10)
    
    def create_new_project_tab(self):
        new_project_tab = ttk.Frame(self.notebook)
        self.notebook.add(new_project_tab, text='New Project')

        # Entry for renaming the file
        tk.Label(new_project_tab, text="Create New Project?").pack(pady=5)
        # Confirmation button
        tk.Button(new_project_tab, text="Confirm", command=self.create_new_project).pack(pady=10)

    def create_settings_tab(self):
        settings_tab = ttk.Frame(self.notebook)
        self.project_directory = tk.StringVar()
        self.notebook.add(settings_tab, text='Settings')

        tk.Label(settings_tab, text="Configuration").pack(pady=5)
        tk.Button(settings_tab, text="Set Project Directory", command=self.browse_and_config_d).pack(pady=10)
        tk.Label(settings_tab, text="Currently set directory:").pack(pady=5)
        self.current_directory_label = tk.Label(settings_tab, text=self.config_handler.load_directory)
        self.current_directory_label.pack(pady=5)
    
    def browse_and_config_d(self):
        folder = filedialog.askdirectory()
        self.config_handler.update_d(folder)
        self.directory = folder
        self.current_directory_label.config(text=folder)

    def create_new_project(self):
        return    


    
    def set_folder_entry(self, tab, entry_var, label_text, browse_command):
        frame = tk.Frame(tab)
        frame.pack(pady=5)

        tk.Label(frame, text=label_text).pack(side=tk.LEFT, padx=5)
        tk.Entry(frame, textvariable=entry_var, width=40).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Browse", command=browse_command).pack(side=tk.LEFT, padx=5)

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

    def set_and_update(self):
            #get folder name
            folder = filedialog.askdirectory()
            self.project_directory.set(folder)
            self.config.set('Settings', 'project_directory',self.project_directory.get())
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)


    def browse_and_set_file(self):
        file = filedialog.askopenfilename()
        self.source_file.set(file)

    def browse_and_set_folder(self):
        folder = filedialog.askdirectory()
        self.destination_folder.set(folder)


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

if __name__ == "__main__":
    root = TkinterDnD.Tk()  # Use TkinterDnD for drag and drop
    gui_handler = GUIHandler(root)

    root.mainloop()

