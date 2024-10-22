import re
import math

# fungsi konversi
def convert_function(func):
    # Mengubah tanda '^' menjadi '**' untuk eksponen
    func = func.replace('^', '**')  
    # Mengubah angka dan variabel menjadi format perkalian (misal 2x -> 2*x)
    func = re.sub(r"(\d)(x)", r"\1*x", func)  

    final_func = func.lstrip("*")
    return final_func
