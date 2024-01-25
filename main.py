#!/usr/bin/env python
# main.py
from gui.gui_handler import GUIHandler
from tkinterdnd2 import TkinterDnD

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    gui_handler = GUIHandler(root)
    root.mainloop()
