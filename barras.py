import matplotlib.pyplot as plt
import acessarDados as data

def dataFilter(atletas, qtdEsportes):

  def tirarRepetidos(atletas):
    result = []
    for atleta in atletas:
      if atleta not in result:
        result.append(atleta)
    return result

  def NumDeAtletasPorEsporte(atletas):
    conts = dict()
    result = []
    for atleta in atletas:
      conts[atleta[1]] = conts.get(atleta[1], 0) + 1
    for i in conts:
      result.append(conts[i])
    return result

  def gerarEixoY(atletasPorEsporte, qtdEsportes):
    result = []
    atletasPorEsporte.sort(reverse=True)
    for numDeAtleta in range(qtdEsportes):
      result.append(atletasPorEsporte[numDeAtleta])
    return result
  
  x = range(qtdEsportes)
  y = gerarEixoY(NumDeAtletasPorEsporte(tirarRepetidos(atletas)), qtdEsportes)
  
  return (x, y)

# Função de geração de gráfico usando a biblioteca matplotlib 
def creatGraph(x, y):
  plt.bar(x, y)
  plt.title('Esportes com maior número de atletas')
  plt.xlabel('Olimpíadas')
  plt.ylabel('Quantidade de atletas')
  plt.savefig('./graficosGerados/barras/barras.png')
  plt.close()

# Função que será chamada no arquivo main
def presentLineGraph(year, olympicsType, qtdEsportes):
  tuplaDados = dataFilter(data.dadosGraficoBarras(year, olympicsType), int(qtdEsportes))
  creatGraph(tuplaDados[0], tuplaDados[1])

""" colocar os nomes dos esportes abaixo """