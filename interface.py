import tkinter as tk
from tkinter import ttk
from validator import validate_inputs
from converter import convert_function
from regula_falsi import regula_falsi

def show_frame(frame):
    frame.tkraise()

def build_interface(root, calculate_callback):
    container = tk.Frame(root)
    container.pack(fill='both', expand=True)

    container.grid_rowconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)

    frame_home = tk.Frame(container, bg='#395487')
    frame_home.grid(row=0, column=0, sticky="nsew")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    frame_home.grid_rowconfigure(0, weight=2)  # Untuk membuat tulisan agak ke atas
    frame_home.grid_rowconfigure(1, weight=1)  # Tombol mulai berada di tengah
    frame_home.grid_rowconfigure(2, weight=1)  # Tombol info di bawah
    frame_home.grid_columnconfigure(0, weight=1)

    label_title = tk.Label(frame_home, text="KALKULATOR REGULA FALSI", font=("Poppins Bold", 40), bg='#395487', fg='white')
    label_title.pack(pady=(100,0))

    label_subtitle = tk.Label(frame_home, text='by Kelompok 3', font=("Poppins SemiBold", 24), bg='#395487', fg='white')
    label_subtitle.pack(pady=10)

    btn_start = tk.Button(frame_home, text="Mulai Menghitung", font=("Poppins SemiBold", 20), command=lambda: show_frame(frame_hitung), relief="ridge", borderwidth=2, bg='#918ba0', fg='white')
    btn_start.pack(pady=50)
    # Membuat dan mengatur komponen-komponen GUI
    
    frame_hitung = tk.Frame(container)
    frame_hitung.grid(row=0, column=0, sticky="nsew")

    label_func = tk.Label(frame_hitung, text="Masukkan fungsi f(x):")
    label_func.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    entry_func = tk.Entry(frame_hitung, width=90)
    entry_func.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    label_a = tk.Label(frame_hitung, text="Masukkan batas bawah (a):")
    label_a.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    entry_a = tk.Entry(frame_hitung, width=90)
    entry_a.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    label_b = tk.Label(frame_hitung, text="Masukkan batas atas (b):")
    label_b.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    entry_b = tk.Entry(frame_hitung, width=90)
    entry_b.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    label_tol = tk.Label(frame_hitung, text="Masukkan toleransi (e):")
    label_tol.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    entry_tol = tk.Entry(frame_hitung, width=90)
    entry_tol.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    label_max_iter = tk.Label(frame_hitung, text="Masukkan iterasi maksimum (N):")
    label_max_iter.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    entry_max_iter = tk.Entry(frame_hitung, width=90)
    entry_max_iter.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    button_calculate = tk.Button(frame_hitung, text="Mulai Hitung", command=calculate_callback, relief="ridge")
    button_calculate.grid(row=5, column=1, padx=(1,0), pady=5)

    label_result = tk.Label(frame_hitung, text="Hasil:")
    label_result.grid(row=8, column=0, padx=1, pady=5)

    # Membuat tabel Treeview untuk menampilkan hasil iterasi
    columns = ("Iteration", "a", "b", "f(a)", "f(b)", "x", "f(x)", "f(x)*f(a)<0")
    treeview = ttk.Treeview(frame_hitung, columns=columns, show='headings', height=10)

    for col in columns:
        treeview.heading(col, text=col)

    treeview.column("Iteration", width=80, anchor="center")
    treeview.column("a", width=100, anchor="center")
    treeview.column("b", width=100, anchor="center")
    treeview.column("f(a)", width=100, anchor="center")
    treeview.column("f(b)", width=100, anchor="center")
    treeview.column("x", width=100, anchor="center")
    treeview.column("f(x)", width=100, anchor="center")
    treeview.column("f(x)*f(a)<0", width=108, anchor="center")

    treeview.grid(row=7, column=0, columnspan=2, padx=5, pady=10)

    treeview.tag_configure('highlight', background='#d9ead3')
    show_frame(frame_home)
    return entry_func, entry_a, entry_b, entry_tol, entry_max_iter, label_result, treeview
