# Autômato Finito Determinísitico
Trabalho realizado para a disciplina de Linguagens Formais e Autômatos

# Compilar # 
```
  python3 afd.py
```
## Função de Transição ##
Para criar sua função de transição basta informar o estado atual, o símbolo lido e o estado final(após o símbolo ser lido). Após informar, digite 1 para adicionar mais um passo a função ou 0 para finalizar o processo.
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

  
