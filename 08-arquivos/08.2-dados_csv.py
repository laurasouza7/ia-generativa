import csv

dados_tabela = [
    ["Nome","Cargo","Idade"],
    ["Carlos","Administrador",43],
    ["Laura","Logistica",32],
    ["Maria","Estagiária", 20],
    ["Ester", "Professora",25]
]

with open("08.2-funcionarios.csv","w",encoding="utf-8",newline="") as arquivo_csv:
    escrever = csv.writer(arquivo_csv)
    escrever.writerows(dados_tabela)
