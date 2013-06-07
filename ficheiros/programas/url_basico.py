import urllib.request

meu_sitio = urllib.request.urlopen("http://ernesto.dei.uc.pt")
meus_bytes = meu_sitio.read()
# note that Python3 does not read the html code as string
# but as html code bytearray, convert to string with
minha_cadeia = meus_bytes.decode("utf8")
meu_sitio.close()
print(minha_cadeia)