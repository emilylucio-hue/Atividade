class Clinica:
    """Classe que gerencia os animais."""


    def __init__(self):
        self.__animais = []


    def cadastrar_animal(self, animal):
        """Adiciona um animal à lista."""
        self.__animais.append(animal)
        print("Animal cadastrado!")


    def listar_animais(self):
        """Mostra todos os animais cadastrados."""
        if not self.__animais:
            print("Nenhum animal cadastrado.")
            return


        for animal in self.__animais:
            print(animal)


    def buscar_animal(self, nome):
        """Busca um animal pelo nome."""
        for animal in self.__animais:
            if animal.nome.lower() == nome.lower():
                return animal


        return None


    def mostrar_informacoes(self):
        """Mostra informações específicas dos animais."""
        if not self.__animais:
            print("Nenhum animal cadastrado.")
            return


        for animal in self.__animais:
            print(animal.informacao_especifica())


    def __str__(self):
        """Mostra a quantidade de animais."""
        return f"Total de animais: {len(self.__animais)}"
