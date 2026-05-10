




#===============================================================================================================
# DATA BASE

users = [
    {"name_user" : "joao", "password" : "1234", "profile" : "reader"},
    {"name_user" : "Roco", "password" : "1234", "profile" : "librarian"},
    {"name_user" : "Zuan", "password" : "1234", "profile" : "reader"},
]

books = [
    {"name_book" : "Dune", "category" : "Fiction", "available" : True},
    {"name_book" : "Star wars", "category" : "Fiction", "available" : True},
    {"name_book" : "Sons of Dune", "category" : "Fiction", "available" : False},
]

loans = [
    {"user" : "joao", "book" : "Star wars", "returned" : True},
    {"user" : "Zuan", "book" : "Sons of Dune", "returned" : False},
    {"user" : "joao", "book" : "Dune", "returned" : True}
]

#===============================================================================================================
# Cadastro de usuários

def Users_register():
    
    print("=== Regitre sua Conta ===")
    print("qual é o seu nome?")
    name_user = input()
    
    for i in users:
        if i["name_user"] == name_user:
            print("xxxxxx Essa conta já existe! xxxxxx")
            return
    
    print("Digite sua senha: ")    
    password = input(" ")
    
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

def Do_login():
    print("=== LOGIN ===")
    name = input("Digite seu nome: ").strip()
    password1 = input("Digite sua senha ").strip()
    
    for i in users:
        if i["name_user"] == name and i["password"] == password1:
            print(f"Bem-vindo, {i['name_user']}!")
            return i
    
    print("Nome ou senha incorretos")


#===============================================================================================================
# Registrar livro

def Book_register():
    
    print("=== Registro de Livros ===")
    print("=== Digite o nome do livro ===")
    Name_book = input(" ")
    
    for i in books:
        if i ["name_book"] == Name_book:
            print("xxx Esse livro já existe na nossa biblioteca")
            return
        
    print("Digite a categoria do livro ")    
    Book_category = input(" ")
    
    New_Book = {"name_book" : Name_book, "category" : Book_category, "available" : True}
    books.append(New_Book)
    print(f"Livro '{Name_book}', cadastrado com sucesso!")

#===============================================================================================================
# Pesquisar Livro e pesquisar categoria

def Search_book():
    print("=== Pesquisa de livros ===")
    print("Digite o nome do livro que vc quer pesquisar")
    Search = input(" ")
    
    for i in books:
        if i["name_book"] == Search:
            print(f"Livro Disponível: {i['name_book']} - Categoria: {i['category']} - Disponível: {'Sim' if i['available'] else 'Não'}")
            return
        
def Search_category():
    print("=== Pesquisar categoria ===")
    print("Digite a categoria do livro que vc quer pesquisar")
    Search = input(" ")
    
    for i in books:
        if i["category"] == Search:
            print(f"{i['name_book']} - Categoria: {i['category']} - Disponível: {'Sim' if i['available'] else 'Não'}")

#===============================================================================================================
# Registrar emprestimo

#def Loan_register():
#    print("=== Empretimos de livros===")
#    print("Digite o nome do livro que vc quer pegar empretado")
#    loan_book = input(" ")
#    
#    for i in books and i["available"] == True:
#        if i["name_book"] == loan_book:
#            print()(f"Livro '{i['name_book']}' emprestado com sucesso!")
#        else:
#            print("xxx Livro indisponível para empréstimo xxx")
#            return
#            