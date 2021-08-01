import matplotlib.pyplot as plt
import acessarDados as data

def filtrarAlturas(olimpiada, atletas):

  def gerarAlturasDesse(ano): #(PERGUNTE AO PROFESSOR) poderia remover essas variaveis passadas como parametro ja que a função vai buscar variaveis em um escopo mais abrangente?
    alturasDoAno = []
    for atleta in atletas:
      if ano == int(atleta[1]):
         if atleta[0] != 'NA':
          alturasDoAno.append(int(atleta[0]))
    return alturasDoAno

  def gerarEixoy():
    y = []
    for ano in olimpiada:
      if gerarAlturasDesse(ano) != []:
        y.append(gerarAlturasDesse(ano))
    return y
    
  return gerarEixoy()

def pegarUltimosAnos(atletas, tipoDeOlimpia, ultimasOlimpiadas):
  def todosOsAnos():
    result = []
    for atleta in atletas:
      if tipoDeOlimpia == atleta[2]:
        if int(atleta[1]) not in result:
          result.append(int(atleta[1]))
    result.sort()
    return result

  def pegarUltimosAnos(ultimosAnos):
    return ultimosAnos[-int(ultimasOlimpiadas):]

  return pegarUltimosAnos(todosOsAnos())

def plotarBox(x, y):
  plt.boxplot(y, labels = x)
  plt.title('Altura dos atletas no decorrer das olimpíadas')
  plt.xlabel('Olimpíadas')
  plt.ylabel('Altura dos atletas (em cm)')
  plt.savefig('./graficosGerados/boxplot/boxplot.png')
  plt.close()

def apresentarGraficoBoxplot(evento, ultimasOlimpiadas, tipoDeOlimpia):
  atletas = data.dadosGraficoBoxplot(evento, tipoDeOlimpia)
  anos = pegarUltimosAnos(atletas, tipoDeOlimpia, ultimasOlimpiadas)
  alturas = filtrarAlturas(anos, atletas)
  plotarBox(anos, alturas) 
