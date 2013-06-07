"""Ficheiros."""

"""
import urllib.request

meu_sitio = urllib.request.urlopen("http://ernesto.dei.uc.pt")
meus_bytes = meu_sitio.read()

minha_cadeia = meus_bytes.decode("utf8")
meu_sitio.close()

novo_fich = open('/Users/ernestojfcosta/tmp/urlteste.html', 'w')
novo_fich.write(minha_cadeia)
novo_fich.close()
print(minha_cadeia)
"""
# Apanhar a codificação de uma página web


import urllib.request

def extract(text, sub1, sub2):
    """ Retira o texto entre duas subcadeias."""
    return text.split(sub1, 1)[-1].split(sub2, 1)[0]

if __name__ == '__main__':
    
    fp = urllib.request.urlopen("http://www.python.org")
    mybytes = fp.read()
    encoding = extract(str(mybytes).lower(), 'charset=', '"')
    
    print('-'*50)
    print( "Encoding type = %s" % encoding )
    print('-'*50)
    if encoding:
        mystr = mybytes.decode(encoding)
        print(mystr)
    else:
        print("Encoding type not found!")
    fp.close()