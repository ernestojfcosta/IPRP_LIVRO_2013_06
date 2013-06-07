import matplotlib
import pylab

def le_cidade(f_ent):
    """
    Lê os dados de uma cidade.
    Devolve -1 se alcançou o fim de ficheiro
    """
    # procura primeira linha significativa 
    linha = f_ent.readline()

    while (linha !='') and (linha == '\n'):
        linha = f_ent.readline()
    
    if linha == '':
        return -1
    else:
        # extrai dados -- pode-se simplificar o código
        cidade = linha[:-1]
        pluviosidade = f_ent.readline().split()[1:-1]
        pluviosidade = [ float(dado) for dado in pluviosidade]
        temperatura = f_ent.readline().split()[1:-1]
        temperatura = [ float(dado) for dado in temperatura]

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
        #print 'Dicio',portugal
        ficha = le_cidade(f_ent)
    f_ent.close()
    return portugal
    
def main(fich):
    dicio = dados_portugal(fich)

    chuva = list()
    cidades = list()
    for c,v in list(dicio.items()):
        pluviosidade = v['pluviosidade']
        chuva.append(pluviosidade)
        cidades.append(c)

    for indice in range(len(chuva)):
        pylab.plot(chuva[indice])
        pylab.legend(cidades[indice])
    pylab.show()
    
    
    
    
    
    
    
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
    #print dados_portugal('/tempo/data/tempo_portugal.txt')
    main('/tempo/data/tempo_portugal.txt')

    