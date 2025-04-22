salariominimo = float(input("Informe o salario minimo: "))
salariousuario = float(input("Informe o salario do usuario: "))
calc= salariominimo-salariousuario
if salariominimo > salariousuario:
    print(f"O usuario recebe {calc} a menos que um salario minimo.")
else:
    print(f"o usuario recebe {calc} a mais que o salario minimo.")