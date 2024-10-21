def evaluate_function(func, x):
    # Mengevaluasi fungsi di titik x
    return eval(func.replace('x', str(x)))

def regula_falsi(func, a, b, tol=1e-6, max_iter=100):
    # Evaluasi nilai fungsi di batas bawah dan atas
    fa = evaluate_function(func, a)
    fb = evaluate_function(func, b)

    if fa * fb > 0:
        return None, []  # Tidak ditemukan akar di interval ini

    iterations = []
    
    for _ in range(max_iter):
        x = b - (fb * (a - b)) / (fa - fb)  # Formula Regula Falsi
        fx = evaluate_function(func, x)

        # Simpan data iterasi saat ini
        fa_fx_condition = fa * fx
        iterations.append((a, b, fa, fb, x, fx, fa_fx_condition))

        if abs(fx) < tol:  # Akar ditemukan
            return x, iterations

        if fa * fx < 0:  # Akar ada di subinterval kiri
            b = x
            fb = fx
        else:  # Akar ada di subinterval kanan
            a = x
            fa = fx

    return x, iterations  # Kembalikan hasil akhir jika akar tidak ditemukan dalam max_iter
