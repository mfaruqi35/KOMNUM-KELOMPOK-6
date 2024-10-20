def konversi(user_input):
    user_input = user_input.replace("^", "**").replace("x", "*x")
    final = user_input.lstrip("*")
    return final
