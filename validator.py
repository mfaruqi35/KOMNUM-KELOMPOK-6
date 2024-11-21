import tkinter as tk
from tkinter import messagebox

def validate_inputs(func, a, b, tol, max_iter):
    # Memeriksa apakah fungsi sudah diisi
    if not func:
        messagebox.showerror("Kesalahan Input", "Silakan masukkan fungsi yang valid.")
        return False
        
    try:
        a = float(a)
        b = float(b)
        tol = float(tol)
        max_iter = int(max_iter)
        
    except ValueError:
        messagebox.showerror("Kesalahan Input", "Silakan masukkan nilai numerik yang valid untuk a, b, toleransi, dan jumlah iterasi maksimum.")
        return False
        
    # Memeriksa apakah batas bawah lebih kecil dari batas atas
    if a >= b:
        messagebox.showerror("Kesalahan Input", "Batas bawah 'a' harus lebih kecil dari batas atas 'b'.")
        return False
        
    # Memeriksa apakah toleransi lebih besar dari 0
    if tol <= 0:
        messagebox.showerror("Kesalahan Input", "Toleransi harus lebih besar dari nol.")
        return False
        
    # Memeriksa apakah iterasi maksimum adalah bilangan positif
    if max_iter <= 0:
        messagebox.showerror("Kesalahan Input", "Jumlah iterasi maksimum harus lebih besar dari nol.")
        return False
    return True
