from animal import Animal

class Cachorro(Animal):
    """Classe que representa um cachorro."""


    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca = raca


    @property
    def raca(self):
        return self.__raca


    def informacao_especifica(self):
        """Mostra a raça do cachorro."""
        return f"Raça: {self.raca}"


    def brincar(self):
        """Representa o cachorro brincando."""
        return f"{self.nome} está brincando."


    def __str__(self):
        """Mostra os dados do cachorro."""
        return f"{super().__str__()} | Raça: {self.raca}"