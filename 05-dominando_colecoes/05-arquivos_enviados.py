#Lista de arquivos encontrados no diretório

arquivos_enviados = ["manual.pdf", "foto.png","contrato.PDF", "virus.exe","relatorio.pdf","anotacoes.txt"]

#lista de arquivos pdf(vazia)
pdfs_validos = []

for arquivo in arquivos_enviados: 
    if arquivo.lower().endswith(".pdf"): 
        #final do arquivo 
        pdfs_validos.append(arquivo)
print("Lista Completa", arquivos_enviados)
print("Arquivos de PDF",pdfs_validos)