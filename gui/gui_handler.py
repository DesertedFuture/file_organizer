# gui/gui_handler.py
import tkinter.filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from organizer.file_organizer import FileOrganizer

class GUIHandler:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")

        # Create a Notebook for organizing tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        # Initialize attributes
        self.source_file = tk.StringVar()
        self.destination_folder = tk.StringVar()
        self.rename_file_text = tk.StringVar()

        # Create tabs
        self.create_main_tab()
        self.create_settings_tab()
        self.create_new_project_tab()

        # Instantiate FileOrganizer
        self.file_organizer = FileOrganizer()  



    def create_main_tab(self):
        main_tab = ttk.Frame(self.notebook)
        self.notebook.add(main_tab, text='Main')

        # Entry for source file
        tk.Label(main_tab, text="Source File:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(main_tab, textvariable=self.source_file, width=40).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(main_tab, text="Browse", command=self.browse_and_set_source_file).grid(row=0, column=2, padx=5, pady=5)

        # Entry for destination folder
        tk.Label(main_tab, text="Destination Folder:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(main_tab, textvariable=self.destination_folder, width=40).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(main_tab, text="Browse", command=self.browse_and_set_destination_folder).grid(row=1, column=2, padx=5, pady=5)

        # Entry for renaming the file
        tk.Label(main_tab, text="Rename File:").grid(row=2, column=0, padx=5, pady=5)
        self.rename_file_text = tk.StringVar()
        tk.Entry(main_tab, textvariable=self.rename_file_text, width=40).grid(row=2, column=1, padx=5, pady=5)

        # Confirmation button
        tk.Button(main_tab, text="Confirm", command=self.show_confirmation).grid(row=3, column=0, columnspan=3, pady=10)

    def show_confirmation(self):
        source_file = self.source_file.get()
        destination_folder = self.destination_folder.get()
        new_name = self.get_new_file_name()

        confirmation_message = (
            f"Source File: {source_file}\n"
            f"Destination Folder: {destination_folder}\n"
            f"New File Name: {new_name}"
        )

        messagebox.showinfo("Confirmation", confirmation_message)

    def get_new_file_name(self):
        # Customize this method to generate the new file name based on your requirements
        return self.rename_file_text.get()

    def create_settings_tab(self):
        settings_tab = ttk.Frame(self.notebook)
        self.notebook.add(settings_tab, text='Settings')

        # Entry for source project folder
        tk.Label(settings_tab, text="Source Project Folder:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(settings_tab, textvariable=self.destination_folder, width=40).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(settings_tab, text="Browse", command=self.browse_and_set_source_project_folder).grid(row=0, column=2, padx=5, pady=5)

    def create_new_project_tab(self):
        new_project_tab = ttk.Frame(self.notebook)
        self.notebook.add(new_project_tab, text='New Project')

        tk.Label(new_project_tab, text="Project Name:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Entry(new_project_tab).grid(row=0, column=1, padx=5, pady=5)

    def browse_file(self):
            file = tk.filedialog.askopenfilename()
            return file

    def browse_folder(self):
        folder = tk.filedialog.askdirectory()
        return folder

    def browse_and_set_source_file(self):
            file = self.browse_file()
            self.set_source_file(file)
            
    def set_source_folder(self, folder):
        if folder:
            self.destination_folder.set(folder)

    def set_source_file(self, file):
        if file:
            self.source_file.set(file)

    def browse_and_set_source_folder(self):
        folder = self.browse_folder()
        self.set_source_folder(folder)

    def browse_and_set_source_project_folder(self):
        folder = self.browse_folder()
        if folder:
            self.destination_folder.set(folder)
            # Include logic to set source project folder in FileOrganizer
   
    def browse_and_set_destination_folder(self):
        folder = self.browse_folder()
        self.set_destination_folder(folder)

    def set_destination_folder(self, folder):
        if folder:
            self.destination_folder.set(folder)
    
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
            # Call the corresponding method in the existing FileOrganizer instance
            self.file_organizer.rename_and_move_file(source_file, destination_folder, user_input)

            messagebox.showinfo("Success", "Files organized successfully!")
        else:
            messagebox.showwarning("Warning", "Please provide both source file and destination folder.")

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    gui_handler = GUIHandler(root)
    root.mainloop()
