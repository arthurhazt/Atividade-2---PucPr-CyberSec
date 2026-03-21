print("Você está me uma floresta...")
caminho = input("Escolha um caminho: (e/d)")

if caminho == "e":
    print("Você achou um rio.")
    acao = input("Você deseja atravesssar ou voltar? (a/v)")
    if acao == "a":
        print("Você chegou em uma vila segura!!")
    elif acao == "v":
        print("Você CONTINUA na floresta...")
    else:
        print("Não existe essa opção!!")
elif caminho == "d":
    print("Você achou uma montanha.")
    acao = input("Você deseja subir ou voltar? (s/v)")
    if acao == "s":
        print("Você achou um tesouro!!")
    elif acao == "v":
        print("Você CONTINUA na floresta...")
    else:
        print("Não existe essa opção!!")
else:
    print("Não existe essa opção!!")
