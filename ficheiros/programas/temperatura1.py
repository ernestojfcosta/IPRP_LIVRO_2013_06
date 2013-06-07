import matplotlib.pyplot
plt = matplotlib.pyplot

def ler(ficheiro):
    with open(ficheiro,'r') as f_ent:
        dados_car = f_ent.read().split()
        dados = []
        for elem in dados_car:
            dados.append(float(elem))
    return dados

def mostra(xetiq, yetiq,tit,x,y):
    plt.xlabel(xetiq)
    plt.ylabel(yetiq)
    plt.plot(x,y)


def main(ficheiro):
    dados = ler(ficheiro)
    mostra('Meses','Temperatura','',range(1,13),dados)
    plt.show()
 
    
if __name__ == '__main__':
    main('/data/dados_simples.txt')