if None:
    print('None')
else:
    print('Hei!')
    
# Dá erro: não ter dois estatutos diferentes    
def toto():
    if y == 'Hei!': # não local
        print('Hei!')
    y = 'Haoi!' # local
    print(y)
    
if __name__ == '__main__':
    y = 'Hei!'
    toto()
    y = 'Bah!!'
    toto()        
