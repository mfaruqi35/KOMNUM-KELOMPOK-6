import tkinter as tk
from tkinter import ttk
from validator import validate_inputs
from converter import convert_function
from regula_falsi import regula_falsi

def build_interface(root, calculate_callback):
    # Membuat dan mengatur komponen-komponen GUI
    
    label_func = tk.Label(root, text="Enter a function (e.g., 2x^2 + 4):")
    label_func.pack()

    entry_func = tk.Entry(root)
    entry_func.pack()

    label_a = tk.Label(root, text="Enter lower bound (a):")
    label_a.pack()

    entry_a = tk.Entry(root)
    entry_a.pack()

    label_b = tk.Label(root, text="Enter upper bound (b):")
    label_b.pack()

    entry_b = tk.Entry(root)
    entry_b.pack()

    label_tol = tk.Label(root, text="Enter tolerance (e.g., 1e-6):")
    label_tol.pack()

    entry_tol = tk.Entry(root)
    entry_tol.pack()

    label_max_iter = tk.Label(root, text="Enter max iterations (e.g., 100):")
    label_max_iter.pack()

    entry_max_iter = tk.Entry(root)
    entry_max_iter.pack()

    button_calculate = tk.Button(root, text="Calculate Root", command=calculate_callback)
    button_calculate.pack()

    label_result = tk.Label(root, text="Result:")
    label_result.pack()

    # Membuat tabel Treeview untuk menampilkan hasil iterasi
    columns = ("Iteration", "a", "b", "f(a)", "f(b)", "x", "f(x)", "f(x)*f(a)<0")
    treeview = ttk.Treeview(root, columns=columns, show='headings', height=10)

    for col in columns:
        treeview.heading(col, text=col)

    treeview.column("Iteration", width=80, anchor="center")
    treeview.column("a", width=100, anchor="center")
    treeview.column("b", width=100, anchor="center")
    treeview.column("f(a)", width=100, anchor="center")
    treeview.column("f(b)", width=100, anchor="center")
    treeview.column("x", width=100, anchor="center")
    treeview.column("f(x)", width=100, anchor="center")
    treeview.column("f(x)*f(a)<0", width=120, anchor="center")

    treeview.pack()

    return entry_func, entry_a, entry_b, entry_tol, entry_max_iter, label_result, treeview
