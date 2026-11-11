class Animal:
   """Classe principal dos animais."""


   def __init__(self, nome, idade):
       self.__nome = nome
       self.__idade = idade


   @property
   def nome(self):
       return self.__nome


   @nome.setter
   def nome(self, valor):
       if valor == "":
           raise ValueError("O nome não pode ficar vazio!")
       self.__nome = valor


   @property
   def idade(self):
       return self.__idade


   @idade.setter
   def idade(self, valor):
       if valor < 0:
           raise ValueError("A idade não pode ser negativa!")
       self.__idade = valor


   def informacao_especifica(self):
       """Retorna uma informação do animal."""
       return "Animal sem informação específica."


   def __str__(self):
       """Mostra os dados do animal."""
       return f"Nome: {self.nome} | Idade: {self.idade}"

