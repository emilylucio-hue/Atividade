from animal import Animal

class Passaro(Animal):
    """Classe que representa um pássaro."""


    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade)
        self.__especie = especie


    @property
    def especie(self):
        return self.__especie


    def informacao_especifica(self):
        """Mostra a espécie do pássaro."""
        return f"Espécie: {self.especie}"


    def voar(self):
        """Representa o pássaro voando."""
        return f"{self.nome} está voando."


    def __str__(self):
        """Mostra os dados do pássaro."""
        return f"{super().__str__()} | Espécie: {self.especie}"