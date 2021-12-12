tempo = float(input('informe horas de viagem: '))
velocidade = float(input('informe velocidade media: '))
gasolina = float(input('informe o valor da gasolina: (R$) '))
distancia = tempo * velocidade
litros_gastos = distancia / 14
dinheiro_gasto = litros_gastos * gasolina
print('a distancia é:{:.2f}' .format (distancia))
print('seu carro consumiu:{:.2f}' .format (litros_gastos))
print('seu dinheiro gasto foi:{:.2f}' .format (dinheiro_gasto))

print()

print('se beber nao dirija, preserve a sua vida e a da sua familia!!!')