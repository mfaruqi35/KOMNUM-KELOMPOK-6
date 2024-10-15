import tkinter as tk
from tkinter import messagebox

class RegulaFalsiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Regula Falsi")
        self.geometry("800x600")
