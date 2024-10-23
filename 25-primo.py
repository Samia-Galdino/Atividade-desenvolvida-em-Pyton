numero = int(input("Digite um número "))
divisiveis = 0

for i in range(1, numero +1):
    if numero % i ==0:
       divisiveis += 1

if divisiveis == 2:
    print(f"O número {numero} é primo")
else:
    print(f"O número {numero} não é primo")
