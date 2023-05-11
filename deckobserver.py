def fileIntoList(nome):
    lista = []
    file = open(nome, "r")

    for i in file:
        flag = True
        linha = i.split(" ")
        try:
            int(linha[0])
        except:
            flag = False
        if flag:
            if i[-1] == "\n":
                trat = linha[:-1]
                trat.append(linha[-1][:-1])
                lin = ""
                for k in trat[1:]:
                    lin += k + " "
                lista.append([trat[0], lin[:-1]])
            else:
                lista.append(i)

    file.close()
    return lista

def compararListaDif(l1, l2):
    for i in l1:
        flag = False
        for j in l2:
            if i == j:
                flag = True
        if not flag:
            print(i)

def compararListaIg(l1, l2):
    listaIguais = []
    first = True
    for i in l1:
        flag = False
        for j in l2:
            if i == j:
                flag = True
        if flag:
            if first:
                listaIguais.append(i)
            else:
                for k in listaIguais:
                    if k == i:
                        break
                    else:
                        listaIguais.append(i)

    for i in listaIguais:
        if int(i[0]) > 1: 
            print(i[0] + " " + i[1])
        else:
            print(i[1])

    if len(l1) != 0 and len(l2) != 0:    
        print(f"Porcentagem de linhas iguais no arquivo 1: {retornarPorcentagem(len(listaIguais), len(l1)):.2f}%. Porcentagem no arquivo 2: {retornarPorcentagem(len(listaIguais), len(l2)):.2f}%.")
        #print(f"{len(l1)}, {len(l2)}, {len(listaIguais)}")

def retornarPorcentagem(n1, n2):
    return (n1*100)/n2


lista1 = fileIntoList("deck1.txt")
lista2 = fileIntoList("deck2.txt")

#print("Linha(s) diferente(s) no arquivo 1: ")
#compararListaDif(lista1, lista2)
#print("Linha(s) diferente(s) no arquivo 2: ")
#compararListaDif(lista2, lista1)

print("Linhas iguais: ")
compararListaIg(lista1, lista2)