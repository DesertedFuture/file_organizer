import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")

        self.constant_directory = tk.StringVar()
        self.source_folder = tk.StringVar()
        self.spec_directory = tk.StringVar()

        tk.Label(root, text="Constant Directory:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Entry(root, textvariable=self.constant_directory, width=40).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(root, text="Browse", command=self.browse_constant_directory).grid(row=0, column=2, padx=5, pady=5)

        tk.Label(root, text="Source Folder:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Entry(root, textvariable=self.source_folder, width=40).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(root, text="Browse", command=self.browse_source_folder).grid(row=1, column=2, padx=5, pady=5)

        tk.Label(root, text="Specification Directory:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Entry(root, textvariable=self.spec_directory, width=40).grid(row=2, column=1, padx=5, pady=5)
        tk.Button(root, text="Browse", command=self.browse_spec_directory).grid(row=2, column=2, padx=5, pady=5)

        tk.Button(root, text="Organize Files", command=self.organize_files).grid(row=3, column=1, pady=10)

        # Bind drag-and-drop events
        root.drop_target_register(DND_FILES)
        root.dnd_bind('<<Drop>>', self.drop)

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

    def organize_files(self):
        constant_directory = self.constant_directory.get()
        source_folder = self.source_folder.get()
        spec_directory = self.spec_directory.get()

        if constant_directory and source_folder and spec_directory:
            spec_files = [f for f in os.listdir(spec_directory) if f.lower().endswith('.txt')]
            for spec_file in spec_files:
                spec_file_path = os.path.join(spec_directory, spec_file)
                create_folders_from_spec(constant_directory, spec_file_path)
                move_and_rename_files(source_folder, spec_file_path)
            tk.messagebox.showinfo("Success", "Files organized successfully!")
        else:
            tk.messagebox.showerror("Error", "Please select constant directory, source folder, and specification directory.")

    def drop(self, event):
        if event.data:
            file_path = event.data
            if os.path.isdir(file_path):
                self.source_folder.set(file_path)
            elif os.path.isdir(file_path) and any(f.lower().endswith('.txt') for f in os.listdir(file_path)):
                self.spec_directory.set(file_path)

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()

