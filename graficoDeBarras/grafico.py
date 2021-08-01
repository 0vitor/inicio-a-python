import matplotlib.pyplot as plt
import csv

dataList = []

with open('wealth-per-country.csv') as data:
  reader = csv.reader(data)
  for row in reader:
    dataList.append(row)

dataList.pop()

def getLabel(dataList):
  return dataList.pop(0)

def getCountry(dataList):
  result = []
  for n in dataList:
    result.append(n[0])
  return result

def getMediaWealth(dataList):
  result = []
  for n in dataList:
    result.append(n[1])
  return result

def getMeanWealth(dataList):
  result = []
  for n in dataList:
    result.append(n[2])
  return result

def getPopulation(dataList):
  result = []
  for n in dataList:
    result.append(n[3])
  return result

def parserFloat(floatList):
  result = []
  for n in floatList:
    nFloat = n.replace(",", ".", 1)
    result.append(float(nFloat))
  return result

def posicion(x, multiplier):
  result = []
  for n in x:
    result.append(n+multiplier)
  return result

label = getLabel(dataList)
country = getCountry(dataList)
mediaWealth = parserFloat(getMediaWealth(dataList))
meanWealth = parserFloat(getMeanWealth(dataList))
population = parserFloat(getPopulation(dataList))

width = 0.2
x = [0,1,2,3,4,5,6,7,8,9]

fig, ax = plt.subplots()
rects1 = ax.bar(posicion(x, -width), mediaWealth, width, color='#00BFFF',label=label[1])
rects2 = ax.bar(posicion(x, 0), meanWealth, width, color='#4169E1',label=label[2])
rects3 = ax.bar(posicion(x, width), population, width, color='#FF4040',label=label[3])

ax.set_ylabel(label[0])
ax.set_xticks(x)
ax.set_xticklabels(country)

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

ax.legend()
plt.savefig('grafico.png')
fig.tight_layout()

plt.show()