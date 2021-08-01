import acessarDados as data

def filtrarEntrada(data):
  conts = dict()
  for atleta in data:
    conts[key(atleta)] = conts.get(key(atleta), 0) + 1
  maxKey = max(conts, key=conts.get)
  print('O atleta que mais ganhou medalhas foi:',maxKey.split('/')[0], 'no evento',maxKey.split('/')[1], 'com',conts[maxKey], 'medalhas.')

def key(atleta):
  return atleta[0] +'/'+ atleta[1]

def apresentartextual(tipoMedalha):
  filtrarEntrada(data.dadosTextual(tipoMedalha))

  