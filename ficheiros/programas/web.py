import urllib

def processa_pagina_web(url):
    """Opera›es b‡sicas com uma p‡gina web.
    """
    pagina = urllib.urlopen(url)
    num_linhas_cabeca = 0
    
    linha = pagina.readline()
    while '<head>' not in linha:
        linha = pagina.readline()
        
    while '</head>' not in linha:
        num_linhas_cabeca = num_linhas_cabeca + 1
        linha = pagina.readline()
        
    while '<body>' not in linha:
        linha = pagina.readline()
        
    while ('</body>' not in linha) and (linha != ''):
        print linha[:-1]
        linha = pagina.readline()
    
    print 'Nœmero de linhas do cabealho= %d' % num_linhas_cabeca
    
    pagina.close()
    
if __name__ == '__main__':
    processa_pagina_web('/tempo/html/teste.html')
    
        
            
        