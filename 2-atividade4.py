class Cabeça:
    def __init__(self, cabelo, olho, boca):
        self.cabelo = cabelo
        self.olho = olho
        self.boca = boca

    def __str__(self):
        return f"cabelos {self.cabelo}, com os olhos {self.olho} e com a boca {self.boca}"


class Boneco:
    def __init__(self, nome, altura, peso, cabelo, olho, boca):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.cabeça = Cabeça(cabelo, olho, boca)

    def destruir(self):
        del self.cabeça 
    
    def __str__(self):
        return f"Boneco com o nome {self.nome} com {self.altura}cm e {self.peso}kg com os{self.cabeça}"

boneco1 = Boneco("Josias", 5, 0.99, "liso", "azuis", "boca alegre")
print(boneco1)  


boneco1.destruir()
