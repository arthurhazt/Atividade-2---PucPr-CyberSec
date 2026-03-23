usuario = input("Digite um usuário: ")
senha = input("Digite uma senha: ")

if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
elif usuario == "convidado" and senha == "":
    print("Acesso restrito")
else:
    print("Acesso bloqueado")