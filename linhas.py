import matplotlib.pyplot as plt
import acessarDados as data

def dataFilter(dataOfAthletes):

  def getOlympicYears():
    result = []
    for athlete in dataOfAthletes:
      if athlete[2] not in result:
        result.append(athlete[2])
    result.sort()
    return result
    
  def removeRepeatAthletes():
    result = []
    for athlete in dataOfAthletes:
      if athlete not in result:
        result.append(athlete)
    return result
  
  def averageAgeOfAthletes(NoRepeatAthletes, x):
    result = []
    for year in x:
      sumOfOld = 0
      counter = 0
      average = 0
      for athlete in NoRepeatAthletes:
        if athlete[2] == year:
          sumOfOld = sumOfOld + athlete[1]
          counter = counter + 1
      average = sumOfOld/counter
      result.append(average)
    return result
  
  x = getOlympicYears()
  y = averageAgeOfAthletes(removeRepeatAthletes(), x)

  return (x, y)

def creatGraph(x, y):
  plt.plot(x, y, color = "k", linestyle = "-", linewidth = 2)
  plt.title('Evolução da idade média dos atletas')
  plt.xlabel('Olimpíadas')
  plt.ylabel('Idade')
  plt.scatter(x, y, label = "Idade média", color = "r", marker = ".", s = 50)
  plt.legend()
  plt.savefig('./graficosGerados/linhas/linhas.png')
  plt.close()

def presentLineGraph(sex):
  tupleData = dataFilter(data.dadosGraficoLinhas(sex))
  creatGraph(tupleData[0], tupleData[1])