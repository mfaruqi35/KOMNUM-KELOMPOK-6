from tkinter import messagebox

def validate_input(fungsi, batas_bawah, batas_atas, toleransi_error, iterasi):
    try:
        # Periksa apakah input yang diterima valid
        batas_bawah = float(batas_bawah)
        batas_atas = float(batas_atas)
        toleransi_error = float(toleransi_error)
        iterasi = int(iterasi)
