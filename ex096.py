def area(lag,com):
    print(f'a area de um tereno de {lag}X{com} é de {lag*com:.1f}m².')


print('COMTROLE DE TERRENO')
print('-='*30)

l = float(input('LARGURA EM (M): '))
c = float(input('COMPRIMENTO EM (M): '))


area(l,c)
