from clinica import Clinica
from cachorro import Cachorro
from gato import Gato
from passaro import Passaro




def main():
    """Executa o sistema da clínica."""


    clinica = Clinica()


    while True:
        print("\n===== CLÍNICA VETERINÁRIA =====")
        print("1 - Cadastrar animal")
        print("2 - Listar animais")
        print("3 - Buscar animal")
        print("4 - Mostrar informações")
        print("5 - Sair")


        opcao = input("Escolha uma opção: ")


        if opcao == "1":
            print("\n1 - Cachorro")
            print("2 - Gato")
            print("3 - Pássaro")


            tipo = input("Escolha o animal: ")


            if tipo not in ["1", "2", "3"]:
                print("Tipo inválido!")
                continue


            nome = input("Nome: ")


            try:
                idade = int(input("Idade: "))


                if tipo == "1":
                    raca = input("Raça: ")
                    animal = Cachorro(nome, idade, raca)


                elif tipo == "2":
                    cor = input("Cor: ")
                    animal = Gato(nome, idade, cor)


                else:
                    especie = input("Espécie: ")
                    animal = Passaro(nome, idade, especie)


                clinica.cadastrar_animal(animal)


            except ValueError as erro:
                print("Erro:", erro)


        elif opcao == "2":
            clinica.listar_animais()


        elif opcao == "3":
            nome = input("Digite o nome do animal: ")
            animal = clinica.buscar_animal(nome)


            if animal:
                print(animal)
            else:
                print("Animal não encontrado!")


        elif opcao == "4":
            clinica.mostrar_informacoes()


        elif opcao == "5":
            print("Sistema encerrado!")
            break


        else:
            print("Opção inválida!")




if __name__ == "__main__":
    main()
