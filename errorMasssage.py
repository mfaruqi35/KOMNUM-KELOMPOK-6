from tkinter import messagebox

def validate_input(fungsi, batas_bawah, batas_atas, toleransi_error, iterasi):
    try:
        # Periksa apakah input yang diterima valid
        batas_bawah = float(batas_bawah)
        batas_atas = float(batas_atas)
        toleransi_error = float(toleransi_error)
        iterasi = int(iterasi)

     if batas_bawah >= batas_atas:
            raise ValueError("Batas bawah harus lebih kecil dari batas atas!")
        
        if toleransi_error <= 0:
            raise ValueError("Toleransi error harus lebih besar dari 0!")
        
        if iterasi <= 0:
            raise ValueError("Jumlah iterasi harus lebih besar dari 0!")

