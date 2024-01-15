# gui/gui_handler.py
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
        self.constant_directory = tk.StringVar()
        self.source_folder = tk.StringVar()
        self.spec_directory = tk.StringVar()
        self.subfolder_option = tk.StringVar()  # Add this line to initialize subfolder_option

        
        # Create tabs
        self.create_main_tab()
        self.create_settings_tab()
        self.create_new_project_tab()

        # Bind drag-and-drop events
        #root.drop_target_register(DND_FILES)
        #root.dnd_bind('<<Drop>>', self.drop)

    def create_main_tab(self):
        main_tab = ttk.Frame(self.notebook)
        self.notebook.add(main_tab, text='Main')

        # Entry for source folder
        tk.Label(main_tab, text="Source Folder:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(main_tab, textvariable=self.source_folder, width=40).grid(row=0, column=1, padx=5, pady=5)

        # Button to browse source folder
        tk.Button(main_tab, text="Browse", command=self.browse_source_folder).grid(row=0, column=2, padx=5, pady=5)

    def create_settings_tab(self):
        settings_tab = ttk.Frame(self.notebook)
        self.notebook.add(settings_tab, text='Settings')

        # Add options for subfolders
        subfolder_options = ["Option 1", "Option 2", "Option 3"]
        self.subfolder_option.set(subfolder_options[0])  # Set default option

        # Dropdown for subfolders
        subfolder_dropdown = tk.OptionMenu(settings_tab, self.subfolder_option, *subfolder_options)
        subfolder_dropdown.grid(row=0, column=1, padx=5, pady=5)

    def create_new_project_tab(self):
        new_project_tab = ttk.Frame(self.notebook)
        self.notebook.add(new_project_tab, text='New Project')

        tk.Label(new_project_tab, text="Project Name:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        project_name_entry = tk.Entry(new_project_tab)
        project_name_entry.grid(row=0, column=1, padx=5, pady=5)

    def drop(self, event):
        # Handle file drop logic
        pass

    def browse_source_folder(self):
        folder = tk.filedialog.askdirectory()
        if folder:
            self.source_folder.set(folder)

    def browse_spec_directory(self):
        folder = tk.filedialog.askdirectory()
        if folder:
            self.source_folder.set(folder)
            
    def browse_constant_directory(self):
        folder = tk.filedialog.askdirectory()
        if folder:
            self.source_folder.set(folder)

    def run_file_organizer(self):
        # Initialize FileOrganizer
        file_organizer = FileOrganizer()
        
        # Perform other necessary actions before running FileOrganizer

        # Run the FileOrganizer logic
        file_organizer.run()

        messagebox.showinfo("Success", "Files organized successfully!")

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    gui_handler = GUIHandler(root)
    root.mainloop()
