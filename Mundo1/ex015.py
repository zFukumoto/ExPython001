# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dia = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
pago = dia*60 + km*0.15
print('O total a pagar é de R${:.2f}'
      .format(pago))