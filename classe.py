# Super Classe
class veiculo:
    pass
    # Atribudo - São as caracteristicas da classe
    # cor = 'preto'
    # ano = 2021
    # portas = 4
    # atributos de classe
    modelo = 'x6'
    # método construtor com atributos de instância
    # def __init__(self, cor, ano, portas, marca):
    def __init__(self):
        pass
        # self.cor = cor
        # self.ano = ano
        # self.portas = portas
        print('Nome da classe: ' + __class__.__name__)

    # Metodos - São as ações da classe
    # def acelerar():
    #     print('Acelerou')

    def acelerar(self,velocidade):
        print('Acelerou a ' + str(velocidade))

    def frear(self):
        print('Freou')

    # Métodos de classe
    @classmethod
    def metodoDeClasse(cls, parametro1, parametro2):
        print('EU sou um método de classe')
        print(f'Valor do parâmetro 1: {parametro1}')
        print(f'Valor do parâmetro 2: {parametro2}')

# Classe herdeira
class carro(veiculo):
    pass
    # método construtor da classe herdeira
    def __init__(self,modelo):
        print('Classe herdeira: ' + __class__.__name__)

    def obtemModelo(self):
        print('Eu sou o modelo do carro')

class classA:
    pass

class classB:
    pass

class classC:
    pass