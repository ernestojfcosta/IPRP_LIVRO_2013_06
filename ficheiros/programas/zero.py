
def teste(fich):
    f_ent = open(fich,'r')
    ent = f_ent.readline()
    print f_ent
    if ent:
        print True
    else:
        print False
        
if __name__ =='__main__':
    teste('/tempo/data/zero.txt')