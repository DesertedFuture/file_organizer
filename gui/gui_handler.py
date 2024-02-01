import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from organizer.file_organizer import FileOrganizer
from config.config_handler import ConfigHandler

class GUIHandler:
    def __init__(self, master):
        self.root = master
        self.root.title("File Organizer")
        self.config_handler = ConfigHandler()
        self.file_organizer = FileOrganizer()

        self.root.geometry("800x300")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        self.source_file = tk.StringVar()
        self.destination_folder = tk.StringVar()
        self.rename_file_text = tk.StringVar()
        self.new_project_name = tk.StringVar()
        self.project_directory = tk.StringVar()


        main_tab = self.create_tab("Main", [
            ("Source File:", self.source_file, self.browse_and_set_file),
            ("Destination Folder:", self.destination_folder, self.browse_and_set_folder),
            ("Rename File:", self.rename_file_text, None),
        ], self.show_confirmation)

        new_project_tab = self.create_tab("New Project", [
            ("Project Name:", self.new_project_name, None),
        ], self.create_new_project)

        settings_tab = self.create_tab("Settings", [
            ("Set Project Directory", self.project_directory, self.browse_and_config_d),
        ])


        #Display current directory
        self.current_directory_label = tk.Label(settings_tab, text="")
        self.current_directory_label.pack(pady=5)
        current_directory = self.config_handler.load_directory()
        self.current_directory_label.config(text=f"Currently set Directory: {current_directory}")



    def create_tab(self, tab_name, entries_info, button_command=None):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=tab_name)

        for entry_info in entries_info:
            self.set_folder_entry(tab, *entry_info)

        if button_command:
            tk.Button(tab, text="Confirm", command=button_command).pack(pady=10)

        return tab

    def set_folder_entry(self, tab, label_text, entry_var, browse_command):
        frame = tk.Frame(tab)
        frame.pack(pady=5)

        tk.Label(frame, text=label_text).pack(side=tk.LEFT, padx=5)
        tk.Entry(frame, textvariable=entry_var, width=40).pack(side=tk.LEFT, padx=5)

        if browse_command:
            tk.Button(frame, text="Browse", command=browse_command).pack(side=tk.LEFT, padx=5)

    def browse_and_config_d(self):
        folder = filedialog.askdirectory()
        if folder:
            self.config_handler.update_d(folder)
            self.project_directory.set(folder)

    def create_new_project(self):
        new_project_name = self.new_project_name.get()

        if new_project_name:
            try:
                dest_path = self.config_handler.load_directory()
                templ_path = self.config_handler.get_project_template()
                self.file_organizer.create_new_project(dest_path, templ_path, new_project_name)
                messagebox.showinfo("Success", f"Project: {new_project_name} created at \n{dest_path}")
            except FileExistsError:
                messagebox.showerror("Error", f"A project with the same name already exists.")
            except Exception as e:
                messagebox.showerror("Error", f"Error creating project: {e}")

    def template_copy(self):
        folder = filedialog.askdirectory()
        self.config_handler.update_template(folder)
        self.current_template_label.config(text=f"Currently set Template: {folder}")

    def show_confirmation(self):
        source_file = self.source_file.get()
        destination_folder = self.destination_folder.get()
        new_name = self.get_new_file_name()

        confirmation_message = (
            f"Confirm you would like to rename and replace file"
        )

        user_response = messagebox.askokcancel("Confirmation", confirmation_message)

        if user_response:
            try:
                self.file_organizer.rename_and_move_file(
                    source_file, destination_folder, new_name, self.config_handler.load_directory()
                )
                messagebox.showinfo("Success", "Files organized successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Error moving the file: {str(e)}")

    
    def get_new_file_name(self):
        # Customize this method to generate the new file name based on your requirements
        return self.rename_file_text.get()

    def browse_and_set_file(self):
        #init_directory = self.config_handler.load_directory()
        #creat new settings for this
        file = filedialog.askopenfilename()
        self.source_file.set(file)

    def browse_and_set_folder(self):
        init_directory = self.config_handler.load_directory()
        folder = filedialog.askdirectory(initialdir=init_directory)
        print(folder)
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

