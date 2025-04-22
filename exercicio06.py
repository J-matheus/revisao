salariominimo = float(input("Informe o salario minimo: "))
while True:
    salariousuario = float(input("Informe o salario do usuario: "))
    if salariousuario==0:
        print("Programa terminado")
        break
    calc = salariominimo - salariousuario
    if salariominimo > salariousuario:
        print(f"O usuario recebe {calc} a menos que um salario minimo.")
    else:
        print(f"o usuario recebe {calc} a mais que o salario minimo.")
    salariousuario=(input(f"deseja informar um novo salario ? se não, informe 0, se sim informa seu salario."))
    break