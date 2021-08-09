def afd(delta, q0, F, cadeia):
    qA = q0
    for s in cadeia:
        qA = delta[(qA, s)]
    return qA in F

delta = {}
print("[Função de Transição]\n")

i = 1
while i != 0:
    inic = input("Informe o estado inicial:")
    simb =input("Informe o simbolo lido:")
    fim = input("Informe o estado final:")
    delta[(inic,simb)] = fim
    i = int(input("[1] - Continuar a função\n[0] - Finalizar\n"))
    if(i == 0):
        break

print("Sua Função de transição:\n")
print(delta)

F = input("Informe o conjunto de Estados Finais:") #caso tenha mais de um estado final, separe-os com uma vírgula. Ex: q1,q2
F = F.split(',')

P = input("Informe a Palavra:")

res = afd(delta, 'q0', F, P)
if res == True:
    print("Aceita!")
elif res == False:
    print("Rejeita!")
