




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
# Cadastro de usuários 1

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
    
    global current_user
    current_user = new_user
    
    Menu()

#===============================================================================================================
# Login 2

def Do_login():
    print("=== LOGIN ===")
    name1 = input("Digite seu nome: ").strip()
    password1 = input("Digite sua senha ").strip()
    
    for i in users:
        if i["name_user"] == name1 and i["password"] == password1:
            print(f"Bem-vindo, {i['name_user']}!")
            
            global current_user
            current_user = i
            Menu()
            return 
            
    print("xxx Nome de usuário ou senha incorretos! xxx")
            

#===============================================================================================================
# Registrar livro 1

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
    
    return Menu()

#===============================================================================================================
# Pesquisar Livro e pesquisar categoria 2

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
            
    return Menu()

#===============================================================================================================
# Registrar emprestimo 3

def Loan_register():
    print("=== Empretimos de livros===")
    print("Digite o nome do livro que vc quer pegar empretado")    
    loan_book = input(" ")
    
    for i in books:
        if i["name_book"] == loan_book:
            i["available"] = False
            new_loan = {"user" : current_user["name_user"], "book" : loan_book, "returned" : False}
            loans.append(new_loan)
            print(f"Livro '{loan_book}' emprestado com sucesso para {current_user['name_user']}!")
            return
            
    print("xxx Desculpe, esse livro não está disponível no momento. xxx")
    return Menu()
     
#===============================================================================================================
# Devolver livro 

def Return_book():
    print("=== Devolução de livros ===")
    print("Digite o nome do livro que vc quer devolver")
    return_book = input(" ")
    
    for i in loans:
        if i["user"] == current_user["name_user"] and i["book"] == return_book and not i["returned"]:
            i["returned"] = True
            for j in books:
                if j["name_book"] == return_book:
                    j["available"] = True
                    print(f"Livro '{return_book}' devolvido com sucesso por {current_user['name_user']}!")
                    return
    print("xxx Você não tem esse livro emprestado ou já o devolveu. xxx")
    return Menu()
    
#===============================================================================================================
#Main
def Menu():
    if current_user["profile"] == "reader":
        while True:
            print(" === BIBLIOTECA SIMPLES ===")
            print("1 - Pesquisar livro")
            print("2 - Pesquisar categoria")
            print("3 - Registrar empréstimo")
            print("4 - Registrar devolução")
            print("5 - Sair")
            
            option = input("Escolha: ")
            if option == "1":
                Search_book()   
            elif option == "2":
                Search_category()
            elif option == "3":
                Loan_register()
            elif option == "4":
                Return_book()
            elif option == "5":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    elif current_user["profile"] == "librarian":
        while True:
            print(" === BIBLIOTECA SIMPLES ===")
            print("1 - Registrar livro")
            print("2 - ")
            print("3 - ")
            print("4 - Sair")

#===============================================================================================================
#Main

def main():
    while True:
        print("=== BIBLIOTECA SIMPLES ===")
        print("1 - Registrar usuário")
        print("2 - Login")
        print("3 - Sair")
        
        option = input("Escolha: ")
        
        if option == "1":
            Users_register()
        elif option == "2":
            Do_login()
            Menu()
        elif option == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
main()