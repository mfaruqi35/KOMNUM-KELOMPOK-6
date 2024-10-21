import input as it
import interface as ui
import fungsiregulafalsi as rf
import errorMassage as em

def main():
    em.handle_error(run_program)

def run_program():
    # Ambil input dari pengguna
    func, a, b, tol = it.get_input()

    # Hitung akar dengan metode regula falsi
    root, iterations = rf.regula_falsi(func, a, b, tol)

    # Tampilkan hasil
    ui.show_result(root, iterations)

if __name__ == "__main__":
    main()
