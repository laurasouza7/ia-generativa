tem_cartao = True
saldo = 70.0

if tem_cartao: 
    if saldo >= 100: 
        print("Compra aprovada, saldo suficiente")
    else:
        print("Compra aprovada, saldo insuficiente")
else: 
    print("Erro, cartão não inserido")
