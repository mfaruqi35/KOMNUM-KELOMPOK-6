from tkinter import messagebox

# Fungsi untuk memvalidasi input yang diberikan
def validate_input(fungsi, batas_bawah, batas_atas, toleransi_error, iterasi):
    try:
        # Periksa apakah input yang diterima valid
        # Mengubah batas_bawah, batas_atas, dan toleransi_error menjadi float
        # Mengubah iterasi menjadi integer
        batas_bawah = float(batas_bawah)
        batas_atas = float(batas_atas)
        toleransi_error = float(toleransi_error)
        iterasi = int(iterasi)

     # Memeriksa apakah batas_bawah lebih kecil dari batas_atas
     if batas_bawah >= batas_atas:
            raise ValueError("Batas bawah harus lebih kecil dari batas atas!")

     # Memeriksa apakah toleransi_error lebih besar dari 0
     if toleransi_error <= 0:
            raise ValueError("Toleransi error harus lebih besar dari 0!")

     # Memeriksa apakah jumlah iterasi lebih besar dari 0
     if iterasi <= 0:
            raise ValueError("Jumlah iterasi harus lebih besar dari 0!")

     # Jika semua validasi berhasil
            return True
         
     # Menangani kesalahan input
     except ValueError as e:
            # Jika ada kesalahan, tampilkan pesan error menggunakan messagebox
            messagebox.showerror("Input Error", str(e))
            return False
