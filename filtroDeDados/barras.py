import matplotlib.pyplot as plt
import acessarDados as data

def dataFilter(athletes, amountSports):

  def removeRepeated(athletes):
    result = []
    for athlete in athletes:
      if athlete not in result:
        result.append(athlete)
    return result

  def athletesBySport(athletes):
    conts = dict()
    result = []
    for athlete in athletes:
      conts[athlete[1]] = conts.get(athlete[1], 0) + 1
    for i in conts.items():
      result.append(i)
    return result

  def creatAxes(athletes, amountSports):
    amountAthletes = []
    sports = []
    athletes.sort(reverse=True,key=lambda item : item[1])
    for athlete in range(amountSports):
      sports.append(athletes[athlete][0])
      amountAthletes.append(athletes[athlete][1])
    return (sports, amountAthletes)
  
     
  axes = creatAxes(athletesBySport(removeRepeated(athletes)), amountSports)
  
  return (axes[0], axes[1])

# Função de geração de gráfico usando a biblioteca matplotlib 
def creatGraph(x, y):
  plt.bar(x, y)
  plt.title('Esportes com maior número de atletas')
  plt.xlabel('Olimpíadas')
  plt.ylabel('Quantidade de atletas')
  plt.savefig('./graficosGerados/barras/barras.png')
  plt.close()

# Função que será chamada no arquivo main
def presentLineGraph(year, olympicsType, amountOfSports):
  tuplaDados = dataFilter(data.dadosGraficoBarras(year, olympicsType), int(amountOfSports))
  creatGraph(tuplaDados[0], tuplaDados[1])

""" colocar os nomes dos esportes abaixo """