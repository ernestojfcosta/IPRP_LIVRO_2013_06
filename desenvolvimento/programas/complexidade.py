

# Análise
import time
import matplotlib.pyplot as plt

def insere_1(n):
     lista = []
     for i in range(n):
          lista.insert(0,i)
     return lista

def insere_2(n):
     lista = []
     for i in range(n-1,0,-1):
          lista.append(i)
     return lista

def insere_3(n):
     lista = []
     for i in range(n):
          lista = [i] + lista
     return lista

def insere_4(n):
     lista = []
     for i in range(n):
          lista += [i]
     return lista

if __name__ == '__main__':
     """
     inicio_1 = time.time()
     insere_1(10**6)
     fim_1 = time.time()
     tempo_1 = fim_1 - inicio_1
     print('1: ',tempo_1)
     
     inicio_2 = time.time()
     insere_2(10**6)
     fim_2 = time.time()
     tempo_2 = fim_2 - inicio_2
     print('2: ',tempo_2)     
     
     inicio_3 = time.time()
     insere_3(10**6)
     fim_3 = time.time()
     tempo_3 = fim_3 - inicio_3
     print('3: ',tempo_3)  
     
     inicio_4 = time.time()
     insere_4(10**6)
     fim_4 = time.time()
     tempo_4 = fim_4 - inicio_4
     print('4: ',tempo_4) 
     """
     
     lista_1 = [4.6*10e-05,2.09*10e-05,6.38*10e-05,3.09*10e-05]
     
     lista_2 = [8.9*10e-03,1.6*10e-03,20.2*10e-03,2.7*10e-03]
     
     lista_3 = [6*10e-02,1.6*10e-03,26*10e-02,0.3*10e-02]
     
     lista_4 = [5.7,1.6*10e-03,34.1,0.02]
     
     # -----------------------------------------------------------
     
     compara_1 = [4.6*10e-05,8.9*10e-03,6*10e-02,5.7]
     
     compara_2 = [2.09*10e-05,1.6*10e-03,1.6*10e-03,1.6*10e-03]
                  
     compara_3 = [6.38*10e-05,20.2*10e-03,26*10e-02,34.1]
     
     compara_4 = [3.09*10e-05,2.7*10e-03,0.3*10e-02,0.02]
     
     #plt.plot(lista_1,'r-', label='insert')
     plt.plot(compara_1,label='insert')
     plt.plot(compara_2, label='append')
     plt.plot(compara_3, label='[i]+')
     plt.plot(compara_4, label='+=')
     
     plt.title('Complexidade Temporal')
     plt.legend(loc=0)
     plt.show()

