lista = []
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://docs.google.com/forms/d/e/1FAIpQLSdlVlF0uyP-TawAnGK90CoVrRDGRfSmfikVMkZWl665wn3gpw/formResponse')
except urllib.error.URLError:
    print('o site pudim não esta acessivel no momento')
else:
    print('consegui acessar o site pudim com sucesso')
    print(site.read())
#http://pudim.com.br
