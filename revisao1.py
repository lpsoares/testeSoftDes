
time = {}
time["nome"] = "X"
time["JG"] = 5
time["PT"] = 10
time["VIT"] = 5

time2 = {}
time2["nome"] = "Y"
time2["JG"] = 4
time2["PT"] = 8
time2["VIT"] = 4

lista = []
lista.append(time)
lista.append(time2)

with open("arquivo.txt","w") as arquivo:
    for l in lista:
        conteudo = "Time {0}, fez {1} jogos, com {2} pontos e {3} vitórias\n".format(l["nome"],l["JG"],l["PT"],l["VIT"])
        arquivo.write(conteudo)