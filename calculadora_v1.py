# Calculadora em Python

print("\n******************* Calculadora em Python *******************")

def adicao (x,y):
    return x + y
def subtracao (x,y):
    return x - y
def multiplicacao (x,y):
    return x * y
def divisao (x,y):
    return x / y

print("""Selecione o numero da opção desejada

1- adição
2- subtração
3- multiplicação
4- divisão""")

operacao =input("\nDigite a opção desejada: 1/2/3/4 \n")

num1 = int(input("digite o primeiro valor: "))
num2 = int(input("digite o segundo valor: "))

if operacao == "1":
    print("\n")
    print(num1, "+",num2,"=",adicao(num1,num2))
elif operacao =="2":
    print("\n")
    print(num1, "-",num2,"=",subtracao(num1,num2))
elif operacao =="3":
    print("\n")
    print(num1, "*",num2,"=",multiplicacao(num1,num2))
elif operacao =="4":
    print("\n")
    print(num1, "/",num2,"=",divisao(num1,num2))
else:
    print("\n")
    print("opção invalida")