class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        
    def alterar_nome(self, new_name):
        self.nome = new_name
        return self.nome

    def alterar_nome(self, new_fome):
        self.fome = new_fome
        return self.fome

    def alterar_nome(self, new_saude):
        self.saude = new_saude
        return self.saude

    def alterar_nome(self, new_idade):
        self.idade = new_idade
        return self.idade

    def result(self):
        print(f"Nome: {self.nome}")
        if self.fome:
            print(f"Com fome")
        elif self.fome == False:
            print(f"Sem fome")
        print(f"Saude: {self.saude}")
        print(f"Idade: {self.idade}")
        
        
# Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

# Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar 
# Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, 
# o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, 
# um campo calculado, então não devemos criar um atributo para armazenar esta informação por que 
# ela pode ser calculada a qualquer momento.