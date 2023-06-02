class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def alterar_canal(self, muda_canal):
        self.canal = muda_canal
        return self.canal
    
    def aumenta(self, aumenta_vol):
        if aumenta_vol <= 100:
            self.volume += aumenta_vol
        else:
            self.volume = 100
        return self.volume
    
    def abaixa(self, abaixa_vol):
        if abaixa_vol >= 0:
            self.volume -= abaixa_vol
        else:
            self.volume = 0
        return self.volume
    
canal = int(input("Numero do canal: "))
volume = int(input("Volume do canal: "))
        
tv1 = Tv(canal, volume)
        
print(tv1.alterar_canal(3))
print(tv1.aumenta(23))
print(tv1.abaixa(3))








# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário 
# deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se 
# de que o número do canal e o nível do volume permanecem dentro de faixas válidas.