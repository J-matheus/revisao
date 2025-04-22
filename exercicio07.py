altura = float(input("informe sua altura"))
peso  = float(input("informe seu peso"))
imc = peso / (altura*altura)

if imc <= 18.6:
    print(f"voce está com {imc}, portanto você está abaixo do peso.")
elif imc > 18.6 and imc <= 24.9:
    print(f"voce esta com {imc} este é seu peso ideal. Parabéns!")
elif imc >= 25.0 and imc <= 29.9:
    print(f"voce está com {imc}, portanto está levemente acima do peso.")
elif imc >= 30.0 and imc <= 34.9:
    print(f"voce está com {imc}, portanto está com obesidade de grau 1")
elif imc >= 35.0 and imc <= 39.9:
    print(f"voce está com {imc}, portanto está com obesidade de grau 2, obesidade severa")
else:
    print(f"voce está com {imc}, portanto está com obesidade de grau 3, obesidade morbida")