from animal import Animal




class Gato(Animal):
    """Classe que representa um gato."""


    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)
        self.__cor = cor


    @property
    def cor(self):
        return self.__cor


    def informacao_especifica(self):
        """Mostra a cor do gato."""
        return f"Cor: {self.cor}"


    def subir(self):
        """Representa o gato subindo nos móveis."""
        return f"{self.nome} gosta de subir nos móveis."


    def __str__(self):
        """Mostra os dados do gato."""
        return f"{super().__str__()} | Cor: {self.cor}"