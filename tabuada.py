#!/usr/bin/python

tabuada=int(input("Digite um numero para exibir a tabuada:" ))
print("Tabuada dop numero" , tabuada)
for valor in range(1,11,1):
    print(str(tabuada) + "X" +  str(valor) + "=" + str((tabuada*valor)))
