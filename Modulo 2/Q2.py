import os
import platform
def limpar_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def imprimir(variaveis_selecao):
    print("Digite um numero para selecionar uma opção")
    for item in variaveis_selecao:
        print(f"{item} - {variaveis_selecao[item]}")
      

def menu():
    usuarios = []
    variaveis_selecao = {
         1:"Incluir usuário",
         2:"Excluir usuário",
         3:"Consultar usuário",
         4:"Alterar usuário",
         5:"Listar todos os usuários que estão cadastrados",
         9:"Sair"
    }

    numero = 0
    while(numero != 9):
        limpar_terminal()
        imprimir(variaveis_selecao)

        try:
            entrada = input("Digite um número: ")
            numero = int(entrada) 
        except ValueError:
            print("Erro: a entrada não é um número válido.")
            continue
        match numero:
            case 1:
                print("A opção selecinada foi :" )
                print (f"{numero}   - {variaveis_selecao[numero]}")
                usuario = input("Digite o nome do novo usuário:")
                usuarios.append(usuario)
            case 2:
                print("A opção selecinada foi :" )
                print (f"{numero}   - {variaveis_selecao[numero]}")
                usuario = input("Digite o nome do usuario que deseja excluir :")
                try:
                    usuarios.remove(usuario)
                except ValueError:
                    print("Erro: o nome não está presente na lista.")
                    input("\nPressione Enter para continuar...")
            
            case 3:
                print("A opção selecinada foi :" )
                print (f"{numero}   - {variaveis_selecao[numero]}")
                usuario = input("Digite o nome do usuario  procurar : ")
                try:
                    print(f"{usuarios.index(usuario)} - {usuario}")
                    input("\nPressione Enter para continuar...")
            
                except ValueError:
                    print("Erro: o nome não está presente na lista.")

            case 4:
                print("A opção selecinada foi :" )
                print (f"{numero}   - {variaveis_selecao[numero]}")
                usuario = input("Digite o nome do usuario que deseja alterar: ")
                usuario_novo =input("Digite o novo  nome do usuário:")
                try:
                    usuarios[usuarios.index(usuario)] = usuario_novo
                    
                except ValueError:
                    print("Erro: o nome não está presente na lista.")
            case 5:
                print("A opção selecinada foi :" )
                print (f"{numero}   - {variaveis_selecao[numero]}")
                print("\n")
                for user in usuarios:
                     print(user)
                input("\nPressione Enter para continuar...")
            case 9:
                print("A opção selecionada foi :" )
                print (f"{numero}   - {variaveis_selecao[numero]}")
            case _:
                print("numero inválido ")
    


if __name__ == "__main__":
    menu()