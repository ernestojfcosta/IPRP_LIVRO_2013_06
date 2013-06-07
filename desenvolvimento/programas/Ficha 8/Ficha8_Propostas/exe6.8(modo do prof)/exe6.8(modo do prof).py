import pylab

def temp_max_min(f_ent):
  """
  L� temperaturas mensais de v�rias cidades, calcula valores m�ximos e m�nimos.
  Mostra o resultado num gr�fico.
  """
  # l� dados
  f_in = open(f_ent)
  dados = []
  cidade = f_in.readline()
  while cidade != '':
    dados.append([float(valor) for valor in cidade[:-1].split()])
    cidade = f_in.readline()
  # calcula m�ximo e m�nimo
  print 'here'
  lista_valores_mes = zip(*dados)
  maximos = [max(mes) for mes in lista_valores_mes]
  minimos = [min(mes) for mes in lista_valores_mes]
  # mostra resultados
  pylab.figure(1)
  absissa = range(1,13)
  pylab.xlabel('Meses')
  pylab.ylabel('Temperaturas')
  pylab.title(r'$\mathrm{M\acute aximo\,e\,M\acute inimo}$')
  pylab.text(8,22,'Max')
  pylab.text(8,18,'Min')
  pylab.plot(absissa,maximos,'r-o',absissa, minimos,'b-^')
  pylab.show()

temp_max_min('temperaturas.txt')