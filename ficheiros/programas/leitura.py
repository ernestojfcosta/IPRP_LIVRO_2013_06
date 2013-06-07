def leitura():
	nome_f= input("\n Nome absoluto do ficheiro:\t")
	fich_ent=open(nome_f,'r')
	bytes=fich_ent.read(8)
	print(Bytes: ", bytes")
	linha= fich_ent.readline()
	print("Linha: ", linha)
	linhas=fich_ent.readlines()
	print("Linhas: ", linhas)
	fich_ent.close()
	return "Fim"
	
if __name__ == '__main__':
	leitura()