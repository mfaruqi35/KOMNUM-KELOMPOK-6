import tkinter as tk
from tkinter import messagebox

def validate_inputs(func, a, b, tol, max_iter):
    # Cek apakah fungsi sudah diisi
    if not func:
        messagebox.showerror("Input Error", "Please enter a valid function.")
        return False
    
    try:
        a = float(a)
        b = float(b)
        tol = float(tol)
        max_iter = int(max_iter)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for a, b, tolerance, and max iterations.")
        return False

    # Cek apakah batas bawah lebih kecil dari batas atas
    if a >= b:
        messagebox.showerror("Input Error", "Lower bound 'a' must be less than upper bound 'b'.")
        return False

    # Cek apakah toleransi lebih besar dari 0
    if tol <= 0:
        messagebox.showerror("Input Error", "Tolerance must be greater than zero.")
        return False

    # Cek apakah iterasi maksimum adalah bilangan positif
    if max_iter <= 0:
        messagebox.showerror("Input Error", "Maximum iterations must be greater than zero.")
        return False

    return True
