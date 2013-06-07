import matplotlib as mpl
import matplotlib.pyplot as plt


def le_cidade(f_ent):
    """
    Lê os dados de uma cidade.Devolve -1 se alcançou o fim de ficheiro
    """
    # procura primeira linha significativa 
    linha = f_ent.readline()

    while (linha !='') and (linha == '\n'):
        linha = f_ent.readline()
    
    if linha == '':
        return -1
    else:
        # extrai dados 
        cidade = linha[:-1]
        pluviosidade = [float(dado) for dado in f_ent.readline()[:-1].split('\t')[1:]]
        temperatura = [float(dado) for dado in f_ent.readline()[:-1].split('\t')[1:]]
        return (cidade,pluviosidade,temperatura)

def dados_portugal(fich):
    """
    Extrai os dados relativos a Portugal.
    """
    f_ent = open(fich,'r')
    portugal = dict()
    
    ficha = le_cidade(f_ent)
    while ficha != -1:
        cidade,pluviosidade,temperatura = ficha
        portugal.update({cidade:{'pluviosidade':pluviosidade,'temperatura':temperatura}})

        ficha = le_cidade(f_ent)
    f_ent.close()
    return portugal




def main(fich):
    dicio = dados_portugal(fich)
    mostra(dicio)
    
    
def mostra(dados):
    """
    dados é um dicionáro. A chave é o nome da cidade, o valor é outro dicionário
    de chaves 'pluviosidade' e 'temperatura'
    """
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio','Junho','Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    chuva = []
    cidades = []
    temp = []
    for c,v in list(dados.items()):
        chuva.append(v['pluviosidade'])
        temp.append(v['temperatura'])
        cidades.append(c)
    
    figura = plt.figure()
    fig_1 = figura.add_subplot(211)
    plt.title('Cidades de Portugal')
    fig_2 = figura.add_subplot(212)
    

    for indice in range(len(cidades)):
        fig_1.plot(chuva[indice])
        fig_2.plot(temp[indice])
    
    fig_1.set_ylabel('Pluviosidade (mm)')
    fig_2.set_ylabel('Temperatura (C)')
    plt.xticks(list(range(0,12)),meses, rotation=17)
    plt.legend(cidades, loc=0)
   
    plt.show()    
    
    
    
if __name__ == '__main__':
    """
    ficheiro = open('/tempo/data/tempo_portugal.txt','r')
    ficha = le_cidade(ficheiro)
    if ficha != -1:
        cidade, pluviosidade,temperatura = ficha
        print cidade
        print pluviosidade
        print temperatura
    else:
        print 'fim de ficheiro'
    """
    #print dados_portugal('/data/tempo_portugal.txt')
    main('/data/tempo_portugal.txt')

    