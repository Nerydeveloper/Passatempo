#CALCULADORA QUE TRABALHA COM 2 NUMEROS 

def op(element, n1, n2):
    if element == '+':
        return n1 + n2
    elif element == '-':
        return n1 - n2
    elif element == '*':
        return n1 * n2
    elif element == '/':
        return n1 / n2
    elif element == '%':
        return n1 % n2
    elif element == '**':
        return n1 ** n2
    

while True:
    num1 = float(input("Digite o primeiro: "))
    num2 = float(input("Digite o segundo: "))

    operador  = str(input(("Selecione um operador entre ( +  |  -  |  *  |  /  |  %  |  **  ): ")))
    if operador in '+-*/%**':
        print(op(operador,num1,num2))
    else:
        print("Operador invalido!")

    

    escolha = input("Quer continuar? ").upper()
    if escolha == 'SIM' or escolha == 'S':
        continue
    elif escolha == 'NÃO' or escolha == 'N' or escolha == 'NAO':
        break
    else:
        print("Valor invalido!")
    