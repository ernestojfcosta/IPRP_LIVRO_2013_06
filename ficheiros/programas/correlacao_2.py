import pylab
import random

if __name__ == '__main__':
    random_a1 = [ random.randint(1,12) for i in range(12)]
    random_b1 = [ random.randint(1,12) for i in range(12)]
    
    lista_a2 = [1,2,3,4,5,6,7,8,9,10,11,12]
    lista_b2 = [1.1,2.2,3.1,4,5.1,6.2,7,8.2,9.1,10,11,12]
    
    lista_a3 = [1,2,3,4,5,6,7,8,9,10,11,12]
    lista_b3 = [12,11,10,9,8,7,6,5,4,3,2,1]
    
    lista_a4 = [1,2,3,4,5,6,7,8,9,10,11,12]
    lista_b4 = [1,4,2,6,2,4,9,6,11,8,10,11]
    
    pylab.figure(1)
    
    pylab.subplot(221)
    pylab.plot(random_a1,random_b1,'ro', label='Sem')
    #pylab.xlabel('Chuva')
    #pylab.ylabel('X')
    pylab.title('Pearson')
    pylab.axis([1,15,1,15])
    pylab.legend(loc=1)
    
    pylab.subplot(222)    
    pylab.plot(lista_a2,lista_b2,'bo', label='Forte +')
    #pylab.xlabel('Chuva')
    #pylab.ylabel('X')
    pylab.title('Pearson')
    pylab.axis([1,15,1,15])
    pylab.legend(loc=1)
    
    pylab.subplot(223)    
    pylab.plot(lista_a3,lista_b3,'go', label='Forte -')
    #pylab.xlabel('Chuva')
    #pylab.ylabel('X')
    #pylab.title('Pearson')
    pylab.axis([1,15,1,15])
    pylab.legend(loc=1)
  
    
    pylab.subplot(224)    
    pylab.plot(lista_a4,lista_b4,'yo', label='Medio +')
    #pylab.xlabel('Chuva')
    #pylab.ylabel('X')
    #pylab.title('Pearson')
    pylab.axis([1,15,1,15])
    pylab.legend(loc=1)

    pylab.show()
    