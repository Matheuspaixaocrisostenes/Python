def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'com {idade} anos. NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 65:
        return f'com {idade} anos . VOTO OPCIONAL!'
    else:
        return f'com {idade} anos . VOTO OBRIGATORIO!'


# programa principal
print('-'*30)
nasc = int(input('Ano de nascimento: '))
print(voto(nasc))