# Função para adicionar dois números
def adicionar(a, b):
    return a + b

# Função para subtrair dois números
def subtrair(a, b):
    return a - b

# Função para multiplicar dois números
def multiplicar(a, b):
    return a * b

# Função para dividir dois números
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

# Exibição do menu
print("Selecione uma operação:")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

# Entrada da escolha do usuário
escolha = input("Digite sua opção (1/2/3/4): ")

# Entrada dos números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realização da operação selecionada
if escolha == '1':
    resultado = adicionar(num1, num2)
elif escolha == '2':
    resultado = subtrair(num1, num2)
elif escolha == '3':
    resultado = multiplicar(num1, num2)
elif escolha == '4':
    resultado = dividir(num1, num2)
else:
    resultado = "Escolha inválida"

# Exibição do resultado
print("O resultado da operação é:", resultado)
