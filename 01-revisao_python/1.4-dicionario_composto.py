funcionarios = {
    101: {
        "nome" : "Ester",
        "cargo" : "Desenvolvedor",
        "habilidades" : ["Python","C##","Java"]
    },
    102: {
         "nome" : "Lavynia",
        "cargo" : "Analista",
        "habilidades" : ["Comunicação,Agilidade"]

            
    }

}

print(funcionarios[101]["cargo"])
print(funcionarios.get(102,{}).get("nome","Funcionário não encontrado"))