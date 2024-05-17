from classe import veiculo, carro

# objeto = minhaClasse
# objeto.atributo = 'Valor do atributo'
# print(objeto.atributo)

# v1 = veiculo
# print(v1.cor)
# print(v1.ano)
# v1.acelerar(v1, 50)

# v1 = veiculo('Preto', 2021, 4)
# print(v1.cor)
# print(v1.ano)
# print(v1.portas)
# v1.acelerar(65)
# print(v1.modelo)

# Este é um método de instância
v1 = veiculo()
# v1.acelerar(50)
# v1.frear()

# veiculo.metodoDeClasse('parametro1', 'parametro2')

v2 = carro('Gol')
v2.obtemModelo()

# a classe herdeira consegue acessar aos metodos da super classe.
# ao contrário não é permitido

