def ler_tudo():
	nome_f = input("Nome absoluto do ficheiro: ")
	fich_ent = open(nome_f,'r')
	dados = fich_ent.read()
	fich_ent.close()
	return dados	
	
if __name__ == '__main__':
	print(ler_tudo()) 