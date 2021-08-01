import csv

def dadosGraficoLinhas(genero):
  result = []
  with open('./baseDeDados/athlete_events.csv') as csvfile:
    reader = csv.DictReader(csvfile) 
    for atleta in reader:
      if atleta['Medal'] != 'NA' and atleta['Sex'] == genero and atleta['Age'] != 'NA':
        result.append([atleta['ID'], int(atleta['Age']), int(atleta['Year'])])
  return result

def dadosGraficoBarras(ano, tipoOlimpiada):
  result = []
  with open('./dados/athlete_events.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for atleta in reader:
      if atleta['Year'] == ano and atleta['Season'] == tipoOlimpiada:
        result.append([atleta['ID'], atleta['Sport']])
  return result

def dadosGraficoBoxplot(evento,tipoDeOlimpia):
  result = []
  with open('./dados/athlete_events.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for atleta in reader:
      if atleta['Event'] == evento and atleta['Season'] == tipoDeOlimpia:
        result.append([atleta['Height'], atleta['Year'], atleta['Season']])
  return result

def dadosTextual(tipoMedalha):
  result = []
  with open('./dados/athlete_events.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for atleta in reader:
      if atleta['Medal'] == tipoMedalha:
        result.append([atleta['Name'], atleta['Event']])
  return result

def dadosExtra(year, medal, sex):
  result = []
  with open('./dados/athlete_events.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for atleta in reader:
      if (atleta['Year'] == year and atleta['Medal'] == medal and atleta['Sex'] == sex):
        result.append((atleta['ID'],atleta['Sport']))
  return result

def listaEventos():
  result = []
  with open('./dados/athlete_events.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for atleta in reader:
      if atleta['Event'] not in result:
        result.append(atleta['Event'])
  return result

def listaAnos():
  result = []
  with open('./dados/athlete_events.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for atleta in reader:
      if atleta['Year'] not in result:
        result.append(atleta['Year'])
  return result

def listaEsportes():
  result = []
  with open('./dados/athlete_events.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for atleta in reader:
      if atleta['Sport'] not in result:
        result.append(atleta['Sport'])
  return result

def listaJogos():
  result = []
  with open('./dados/athlete_events.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for atleta in reader:
      if atleta['Games'] not in result:
        result.append(atleta['Games'])
  return result

def listaTemporadaEvento():
  result = []
  with open('./dados/athlete_events.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for atleta in reader:
      if (atleta['Season'],atleta['Event']) not in result:
        result.append((atleta['Season'],atleta['Event']))
  return result

