def milhas_quilo(inf, sup):
    """Converte emtre milhas e quilómetros entre os dois intervalos."""
    print(('{0}\t\t{1}'.format('Milhas','Quilómetros')))
    print((27*'-'))
    for i in range(inf, sup+1):
        print(('{0:4.2f}\t\t{1:>11.2f}'.format(i, 1.609*i)))
        
if __name__ == '__main__':
    milhas_quilo(10,20)