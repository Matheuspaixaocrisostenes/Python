sexo = str(input('Informe seu sexo [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('dados invalidos. Por favor informe seu sexo novamente [M/F]')).strip().upper()[0]
print('sexo {} cadastrado com sucesso'.format(sexo))