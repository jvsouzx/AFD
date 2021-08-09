# Autômato Finito Determinísitico
Trabalho realizado para a disciplina de Linguagens Formais e Autômatos

# Compilar # 
```
  python3 afd.py
```
## Função de Transição ##
```
i = 1
while i != 0:
    inic = input("Informe o estado inicial:")
    simb =input("Informe o simbolo lido:")
    fim = input("Informe o estado final:")
    delta[(inic,simb)] = fim
    i = int(input("[1] - Continuar a função\n[0] - Finalizar\n"))
    if(i == 0):
        break
```

  
