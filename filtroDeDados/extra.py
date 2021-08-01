import acessarDados as data

def filtrarEntrada(atletas, qtdEsportes):

  def tirarRepetidos(atletas):
    esportes = []
    for atleta in atletas:
      if atleta not in esportes:
        esportes.append(atleta[1])
    return esportes

  def contarEsportes(esportes):
    conts = dict()
    result = []
    for esporte in esportes:
      conts[esporte] = conts.get(esporte, 0) + 1
    for i in conts.items():
      result.append(i)
    return result

  def gerarResposta(esportes, qtdEsportes):
    result = []
    esportesOrdenados = sorted(esportes, key=lambda esporte: esporte[1], reverse=True)
    for i in range(qtdEsportes):
      result.append(esportesOrdenados[i])
    return result
  
  listaDeEsportes = tirarRepetidos(atletas)
  medalhasPorEsporte = contarEsportes(listaDeEsportes)
  esportesComMaisMedalha = gerarResposta(medalhasPorEsporte, qtdEsportes)  
  return(esportesComMaisMedalha)

def apresentarExtra(numEsportes,tipoDeMedalha,ano,genero):
  esportes = filtrarEntrada(data.dadosExtra(ano, tipoDeMedalha, genero), int(numEsportes))
  for esporte in esportes:
    print('Esporte:',esporte[0],'com',esporte[1],'medalhas.')