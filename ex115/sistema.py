from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *
arq = 'cursoemvideo.txt'

if not arquivoexite(arq):
    criararquivo(arq)

while True:
    resposta = menu(['ver pessoas cadastradas', 'cadastrar nova pessoa','sair do programa'])
    if resposta == 1:
        # opção de listar o conteudo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #opção de criar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
       cabeçalho('\033[35mSaindo do sistema... volte sempre\033[m')
       break
    else:
        print('\033[31mERRO ,digite uma opção valida\033[m')
    sleep(2)
