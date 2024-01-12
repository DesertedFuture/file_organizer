import os
import shutil
import tkinter as tk
from tkinter import ttk, filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES  # Import TkinterDnD
import tkinter.messagebox

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")

        # Variables for paths
        self.constant_directory = tk.StringVar()
        self.source_folder = tk.StringVar()
        self.spec_directory = tk.StringVar()

        # Variable for subfolder naming
        self.subfolder_option = tk.StringVar()
        self.subfolder_option.set("No Subfolder")  # Default option

        # Create a Notebook for organizing tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')

        # Create tabs
        self.create_main_tab()
        self.create_new_project_tab()
        self.create_settings_tab()
        

        # Bind drag-and-drop events
        #root.drop_target_register(tk.DND_FILES)
        #root.dnd_bind('<<Drop>>', self.drop)

    def create_main_tab(self):
        main_tab = ttk.Frame(self.notebook)
        self.notebook.add(main_tab, text='Main')

        tk.Label(main_tab, text="Source Folder:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Entry(main_tab, textvariable=self.source_folder, width=40).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(main_tab, text="Browse", command=self.browse_source_folder).grid(row=0, column=2, padx=5, pady=5)

        tk.Label(main_tab, text="Specification Directory:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Entry(main_tab, textvariable=self.spec_directory, width=40).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(main_tab, text="Browse", command=self.browse_spec_directory).grid(row=1, column=2, padx=5, pady=5)

    def create_settings_tab(self):
        settings_tab = ttk.Frame(self.notebook)
        self.notebook.add(settings_tab, text='Settings')

        tk.Label(settings_tab, text="Constant Directory:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Entry(settings_tab, textvariable=self.constant_directory, width=40).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(settings_tab, text="Browse", command=self.browse_constant_directory).grid(row=0, column=2, padx=5, pady=5)

        tk.Label(settings_tab, text="Subfolder Naming:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        subfolder_options = ["No Subfolder", "Use Source Folder Name", "Use Specification Folder Name"]
        subfolder_dropdown = tk.OptionMenu(settings_tab, self.subfolder_option, *subfolder_options)
        subfolder_dropdown.grid(row=1, column=1, padx=5, pady=5)

    def create_new_project_tab(self):
        new_project_tab = ttk.Frame(self.notebook)
        self.notebook.add(new_project_tab, text='New Project')

        tk.Label(new_project_tab, text="Project Name:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        project_name_entry = tk.Entry(new_project_tab)
        project_name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Add more entry fields as needed for other project information

        tk.Button(new_project_tab, text="Create Project", command=lambda: self.create_project_callback(project_name_entry.get(), description_entry.get())).grid(row=2, column=0, columnspan=2, pady=10)

    def create_project_callback(self, project_name, description):
        # Ensure that the Projects folder exists
        projects_folder = "Projects"
        if not os.path.exists(projects_folder):
            os.makedirs(projects_folder)

        # Create a new folder for the project
        project_folder = os.path.join(projects_folder, project_name)
        os.makedirs(project_folder)

        # Create subfolders within the project folder (customize as needed)
        subfolders = {
            "Documents": ["Text", "Spreadsheets"],
            "Images": ["JPEG", "PNG"],
            "Data": ["Raw", "Processed"]
        }
        
        for subfolder in subfolders:
            subfolder_path = os.path.join(project_folder, subfolder)
            os.makedirs(subfolder_path)

        # Display a message box with the provided information
        message = f"Project '{project_name}' created in '{projects_folder}'.\nDescription: {description}"
        tk.messagebox.showinfo("New Project Created", message)

    def browse_constant_directory(self):
        folder = filedialog.askdirectory()
        if folder:
            self.constant_directory.set(folder)

    def browse_source_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.source_folder.set(folder)

    def browse_spec_directory(self):
        folder = filedialog.askdirectory()
        if folder:
            self.spec_directory.set(folder)

    def drop(self, event):
        if event.data:
            file_path = event.data
            if os.path.isdir(file_path):
                self.source_folder.set(file_path)
            elif os.path.isdir(file_path) and any(f.lower().endswith('.txt') for f in os.listdir(file_path)):
                self.spec_directory.set(file_path)

        constant_directory = self.constant_directory.get()
        source_folder = self.source_folder.get()
        spec_directory = self.spec_directory.get()
        subfolder_option = self.subfolder_option.get()

        if constant_directory and source_folder and spec_directory:
            spec_files = [f for f in os.listdir(spec_directory) if f.lower().endswith('.txt')]
            for spec_file in spec_files:
                spec_file_path = os.path.join(spec_directory, spec_file)
                subfolder_name = self.get_subfolder_name(subfolder_option, source_folder, spec_directory)
                create_folders_from_spec(constant_directory, spec_file_path, subfolder_name)
                move_and_rename_files(source_folder, spec_file_path, subfolder_name)
            tk.messagebox.showinfo("Success", "Files organized successfully!")
        else:
            tk.messagebox.showerror("Error", "Please select constant directory, source folder, and specification directory.")

    def get_subfolder_name(self, option, source_folder, spec_directory):
        if option == "Use Source Folder Name":
            return os.path.basename(os.path.normpath(source_folder))
        elif option == "Use Specification Folder Name":
            return os.path.basename(os.path.normpath(spec_directory))
        else:
            return ""

if __name__ == "__main__":
    root = TkinterDnD.Tk()  # Use TkinterDnD to create the Tkinter window
    app = FileOrganizerApp(root)
    root.mainloop()