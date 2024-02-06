# gui/tab_base.py
import tkinter as tk
from tkinter import ttk

class TabBase(ttk.Frame):
    def __init__(self, notebook, tab_name):
        super().__init__(notebook)
        self.notebook = notebook
        self.tab_name = tab_name
        self.pack(expand=True, fill='both')

    def set_folder_entry(self, label_text, entry_var, browse_command):
        frame = tk.Frame(self)
        frame.pack(pady=5)

        tk.Label(frame, text=label_text).pack(side=tk.LEFT, padx=5)
        tk.Entry(frame, textvariable=entry_var, width=40).pack(side=tk.LEFT, padx=5)

        if browse_command:
            tk.Button(frame, text="Browse", command=browse_command).pack(side=tk.LEFT, padx=5)
