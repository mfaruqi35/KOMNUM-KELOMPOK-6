# fungsi konversi
def konversi(user_input):
    user_input = user_input.replace("^", "**").replace("x", "*x")
    final = user_input.lstrip("*")
    return final


# fungsi evaluasi ekspresi matematika
def eval_funct(user_input, x):
    func = konversi(user_input)
    try:
        result = eval(func)
    except Exception as ex:
        print("Terjadi Error: ", ex)
        result = None
    return result
