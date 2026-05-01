




#===============================================================================================================
# DATA BASE
users = [
    {"name_user" : "joao", "password" : "1234", "profile" : "reader"},
    {"name_user" : "Roco", "password" : "1234", "profile" : "librarian"},
    {"name_user" : "Zuan", "password" : "1234", "profile" : "reader"},
]

books = [
    {"name_book" : "Dune", "category" : "Fiction", "available" : True},
    {"name_book" : "Star wars", "category" : "Fiction", "available" : False},
    {"name_book" : "Sons of Dune", "category" : "Fiction", "available" : False},
]

loans = [
    {"user" : "joao", "book" : "Star wars", "returned" : True},
    {"user" : "Zuan", "book" : "Sons of Dune", "returned" : False},
]

#===============================================================================================================
# Cadastro de usuários
def users_register():

    print("qual é o seu nome?")
    name_user = input()
    
    for i in users:
        if i["name_user"] == name_user:
            print("xxxxxx Essa conta já existe! xxxxxx")
            return
        
    password = input("digite sua senha")
    
    print("tipo de conta:")
    print("1 = leitor")
    print("0 = bibliotecario")
    option = input("Escolha: ")
    
    if option == "1":
        cont_type = "reader"
    elif option == "0":
        cont_type = "librarian"    
    else: 
        print("Opcao invalida")
        return
 
    new_user = {"name_user" : name_user, "password" : password, "profile" : cont_type}
    users.append(new_user)
    print(f"Usuario '{name_user}', cadastrado com sucesso!")
    
#===============================================================================================================
# Login
def do_login():
    print("=== LOGIN ===")
    name = input("Digite seu nome: ").strip()
    password1 = input("Digite sua senha ").strip()
    
    for i in users:
        if i["name_user"] == name and i["password"] == password1:
            print(f"Bem-vindo, {i['name_user']}!")
            return i
    
    print("Nome ou senha incorretos")


#===============================================================================================================
# Login

users_register()

print(f"Usuários cadastrados: {users}")

