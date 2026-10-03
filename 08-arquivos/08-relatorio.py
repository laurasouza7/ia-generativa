# O modo w cria o arquivo "relatorio.txt" na pasta raiz do projeto

with open("08-relatorio.txt", "w",encoding="utf-8") as arquivos:
    arquivos.write("Primeira linha: atenção a primeira linha foi escrita")