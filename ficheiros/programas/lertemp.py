def ler_1(ficheiro):
    with open(ficheiro,'r') as f_ent:
        dados_car = f_ent.read().split()
        dados = [float(elem) for elem in dados_car]
    return dados

def ler_2(ficheiro):
    with open(ficheiro,'r') as f_ent:
        dados = [float(elem) for elem in f_ent.read().split()]
    return dados

def ler_3(ficheiro):
    with open(ficheiro,'r') as f_ent:
        return [float(elem) for elem in f_ent.read().split()]
    
