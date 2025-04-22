n = int(input("informe o numero: "))
if n % 2 ==0 and n > 0:
    print(f"o numero {n} é par e positivo.")
elif n % 2 ==0 and n < 0:
    print(f"o numero {n} é par e negativo.")
elif n % 2 !=0 and n > 0:
    print(f"o numero {n} é impar e positivo")
else:
    print(f"o numero {n} impar e negativo.")