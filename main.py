import tkinter as tk
from converter import convert_function
from validator import validate_inputs
from regula_falsi import regula_falsi
from interface import build_interface

def main():
    root = tk.Tk()
    root.title("Kalkulator Regula Falsi")
    root.geometry("800x600")

    def calculate():
        func = entry_func.get()
        a = entry_a.get()
        b = entry_b.get()
        tol = entry_tol.get()
        max_iter = entry_max_iter.get()

        # Validasi input
        if validate_inputs(func, a, b, tol, max_iter):
            converted_func = convert_function(func)
            root_result, iterations = regula_falsi(converted_func, float(a), float(b), float(tol), int(max_iter))
            
            if root_result is None:
                label_result.config(text="No root found in the interval.")
            else:
                label_result.config(text=f"Root: {root_result}")
                
            # Clear Treeview sebelumnya
            for row in treeview.get_children():
                treeview.delete(row)
            
            # Masukkan hasil iterasi ke dalam Treeview
            for i, (a_val, b_val, fa_val, fb_val, x_val, fx_val, fx_fa_cond) in enumerate(iterations):
                treeview.insert("", "end", values=(i+1, round(a_val, 6), round(b_val, 6),
                                                   round(fa_val, 6), round(fb_val, 6),
                                                   round(x_val, 6), round(fx_val, 6), f"{fx_fa_cond:.6f}"))

    # Bangun antarmuka
    entry_func, entry_a, entry_b, entry_tol, entry_max_iter, label_result, treeview = build_interface(root, calculate)

    root.mainloop()

if __name__ == "__main__":
    main()
