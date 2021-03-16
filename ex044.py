pc = float(input('qual o valor da compra: R$'))
print('''formas de pagamento
[1] A vista no dinheiro/cheque
[2] A vista no cartão 
[3] 2x no cartão
[4] 3x ou mais no cartão''')
desd = pc - (pc * 10 / 100)
desc = pc - (pc * 5 / 100)
p3 = pc + (pc ** 20 / 100)
par2 = pc / 2
par3 = pc / 3 + p3
op = int(input('qual sua opção: '))
if op == 1:
    print('valor total da compra: R${}'.format(desd))
elif op == 2:
    print('o valor total da compra foi de R${:.2f}'.format(desc))
elif op == 3:
    print('o valor total da compra foi de R${:.2f} e cada parcela vai custar {:.2f}'.format(pc, par2))
elif op == 4 :
    total = pc = (pc * 20 /100)
    p = int(input('quantas parcelas: '))
    p4 = total / p
    print('o valor total da compra foi de R${:.2f} e cada parcela vai custar {:.2f}'.format(pc,p4 ))
else:
    print('opção invalida tente novamente!')