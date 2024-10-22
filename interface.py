import tkinter as tk
from tkinter import ttk
from validator import validate_inputs
from converter import convert_function
from regula_falsi import regula_falsi

def show_frame(frame):
    frame.tkraise()

def build_interface(root, calculate_callback):
    # Frame utama untuk kontainer
    container = tk.Frame(root)
    container.pack(fill='both', expand=True)

    container.grid_rowconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)

    # Frame Home
    frame_home = tk.Frame(container, bg='#395487')  # Warna latar lebih modern
    frame_home.grid(row=0, column=0, sticky="nsew")

    # Mengatur tampilan root
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    frame_home.grid_rowconfigure(0, weight=2)
    frame_home.grid_rowconfigure(1, weight=1)
    frame_home.grid_rowconfigure(2, weight=1)
    frame_home.grid_columnconfigure(0, weight=1)

    # Judul aplikasi
    label_title = tk.Label(frame_home, text="KALKULATOR REGULA FALSI", font=("Poppins Bold", 40), bg='#395487', fg='white')
    label_title.pack(pady=(100, 0))

    # Subjudul aplikasi
    label_subtitle = tk.Label(frame_home, text='by Kelompok 3', font=("Poppins SemiBold", 24), bg='#395487', fg='white')
    label_subtitle.pack(pady=10)

    # Tombol Mulai Menghitung
    btn_start = tk.Button(frame_home, text="Mulai Menghitung", font=("Poppins SemiBold", 20), command=lambda: show_frame(frame_hitung),
                          relief="flat", borderwidth=2, bg='#918ba0', fg='white')
    btn_start.pack(pady=50)

    def on_enter_start(e):
        btn_start['background'] = "#708f53"

    def on_leave_start(e):
        btn_start['background'] = "#918ba0"

    btn_start.bind("<Enter>", on_enter_start)
    btn_start.bind("<Leave>", on_leave_start)

    # Frame untuk perhitungan
    frame_hitung = tk.Frame(container, bg='#f6ecea')  # Warna latar yang cerah dan bersih
    frame_hitung.grid(row=0, column=0, sticky="nsew")

    # Label dan input untuk fungsi
    label_func = tk.Label(frame_hitung, text="Masukkan fungsi f(x):", font=("Segoe UI", 12), bg='#f6ecea')
    label_func.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    entry_func = tk.Entry(frame_hitung, width=60, font=("Segoe UI", 12), relief="groove", borderwidth=2)
    entry_func.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    # Label dan input untuk batas bawah
    label_a = tk.Label(frame_hitung, text="Masukkan batas bawah (a):", font=("Segoe UI", 12), bg='#f6ecea')
    label_a.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    entry_a = tk.Entry(frame_hitung, width=60, font=("Segoe UI", 12), relief="groove", borderwidth=2)
    entry_a.grid(row=1, column=1, padx=5, pady=5, sticky="w")

    # Label dan input untuk batas atas
    label_b = tk.Label(frame_hitung, text="Masukkan batas atas (b):", font=("Segoe UI", 12), bg='#f6ecea')
    label_b.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    entry_b = tk.Entry(frame_hitung, width=60, font=("Segoe UI", 12), relief="groove", borderwidth=2)
    entry_b.grid(row=2, column=1, padx=5, pady=5, sticky="w")

    # Label dan input untuk toleransi
    label_tol = tk.Label(frame_hitung, text="Masukkan toleransi (e):", font=("Segoe UI", 12), bg='#f6ecea')
    label_tol.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    entry_tol = tk.Entry(frame_hitung, width=60, font=("Segoe UI", 12), relief="groove", borderwidth=2)
    entry_tol.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    # Label dan input untuk iterasi maksimum
    label_max_iter = tk.Label(frame_hitung, text="Masukkan iterasi maksimum (N):", font=("Segoe UI", 12), bg='#f6ecea')
    label_max_iter.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    entry_max_iter = tk.Entry(frame_hitung, width=60, font=("Segoe UI", 12), relief="groove", borderwidth=2)
    entry_max_iter.grid(row=4, column=1, padx=5, pady=5, sticky="w")

    # Tombol untuk mulai perhitungan
    button_calculate = tk.Button(frame_hitung, text="Mulai Hitung", command=calculate_callback, relief="flat", borderwidth=2, 
                                 bg="#4CAF50", fg="white", font=("Segoe UI", 12))
    button_calculate.grid(row=5, column=1, padx=(1,0), pady=5)

    def on_enter_calc(e):
        button_calculate['background'] = "#708f53"

    def on_leave_calc(e):
        button_calculate['background'] = "#4CAF50"

    button_calculate.bind("<Enter>", on_enter_calc)
    button_calculate.bind("<Leave>", on_leave_calc)

    # Label untuk menampilkan hasil perhitungan
    label_result = tk.Label(frame_hitung, text="Hasil: ", font=("Segoe UI", 12), bg='#f6ecea')
    label_result.grid(row=8, column=0, padx=1, pady=5)

    # Tabel Treeview untuk menampilkan hasil iterasi
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

    # Menambah tag striping untuk setiap baris di Treeview agar terlihat lebih menarik
    treeview.tag_configure('oddrow', background='#f2f2f2')
    treeview.tag_configure('evenrow', background='#ffffff')

    # Menampilkan frame utama
    show_frame(frame_home)
    
    return entry_func, entry_a, entry_b, entry_tol, entry_max_iter, label_result, treeview
