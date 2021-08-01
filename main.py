import time
import timeit
import linhas
import barras
import textual
import boxplot
import extra
import acessarDados as data

def interface():
  
  def gerarGraficoLinhas():
    genero = input("Por favor digite o genero requisitado(M/F)\n")
    if genero == 'M' or genero == 'F':
      linhas.presentLineGraph(genero)
    else:
      print('erro: Genero indisponivel')
  
  def gerarGraficoBarras():
    listaDeEspotes = data.listaEsportes()
    espotes = input("Por favor digite o numero de esportes requisitados\n")
    if int(espotes) <= len(listaDeEspotes):
      anos = data.listaAnos()
      ano = input("Por favor digite o ano da olimpiada requisitada\n")
      if ano in anos:
        tipoDeOlimpia = input("Por favor digite o tipo de olimpiada(Summer/Winter)\n")
        if tipoDeOlimpia == 'Summer' or tipoDeOlimpia == 'Winter':
          olimpiadas = data.listaJogos()
          if ano + ' ' + tipoDeOlimpia in olimpiadas:
            barras.apresentarGraficoDeBarras(ano, tipoDeOlimpia, espotes)
          else:
            print('erro: Tipo de Olimpiada invalido para o ano requisitado')
        else:
          print('erro: Tipo de olimpiada indisponivel')
      else:
        print('erro: Ano indisponivel')
    else:
      print('erro: Numero de esportes invalido')

  def gerarGraficoBoxplot():

    eventos = data.listaEventos() 
    evento = input("Por favor digite o evento requisitado\n")
    if evento in eventos:
      anos = data.listaAnos()
      ultimasOlimpiadas = input("Por favor digite a quantidade de olimpiadas requisitadas\n")
      if int(ultimasOlimpiadas) <= len(anos):
        tipoDeOlimpia = input("Por favor digite o tipo de olimpiada(Summer/Winter)\n")
        if tipoDeOlimpia == 'Summer' or tipoDeOlimpia == 'Winter':
          teste = data.listaTemporadaEvento()
          if (tipoDeOlimpia,evento) in teste:
            boxplot.apresentarGraficoBoxplot(evento, ultimasOlimpiadas, tipoDeOlimpia)
          else:
            print('erro: Evento indisponivel para o tipo de olimpiada requisitado')
        else:
          print('erro: Tipo de olimpiada indisponivel')
      else:
        print('erro: Quantidade de anos indisponivel.')
    else:
      print('erro: Evento indisponivel')
  
  def gerarTextual():
      tipoMedalha = input("Digite o tipo de medalha requisitado(Bronze/Silver/Gold)\n")
      if tipoMedalha == 'Bronze' or tipoMedalha == 'Silver' or tipoMedalha == 'Gold':
        textual.apresentartextual(tipoMedalha)
      else:
        print('erro: Tipo de medalha indisponivel')

  def gerarExtra():
      esportes = data.listaEsportes()
      numEsportes = input('Digite a quantidade de esportes desejada\n')
      if int(numEsportes) <= len(esportes):
        tipoDeMedalha = input("Digite o tipo de medalha requisitado(Bronze/Silver/Gold)\n")
        if tipoDeMedalha == 'Bronze' or tipoDeMedalha == 'Silver' or tipoDeMedalha == 'Gold':
            anos = data.listaAnos()
            ano = input('Digite o ano desejado\n')
            if ano in anos:
              genero = input("Por favor digite o genero requisitado(M/F)\n")
              if genero == 'M' or genero == 'F':
                extra.apresentarExtra(numEsportes,tipoDeMedalha,ano,genero)
              else:
                print('erro: Genero invalido')  
            else:
              print('erro: Ano invalido')    
        else:
            print('erro: Tipo de medalha invalido.')
      else:
            print('erro: Quantidade de esportes invalida.')

  print("Caso deseje um grafico que represente a evolução da idade média dos atletas do <Gênero> que ganharam medalhas em alguma das Olimpíadas digite 'linhas'\n")
  print("Caso deseje um grafico que represente a quantidade de atletas dos <X> esportes com maior número de atletas na olimpíada de <Ano> de <Tipo de Olimpíada> digite 'barras'\n")
  print("Caso deseje um grafico que represente a altura dos atletas do <Evento> nas últimas <X> olimpíadas de <Tipo de Olimpíada> digite 'boxplot'\n")
  print("Caso deseje saber o maior vencedor (Atleta) de <Tipo de Medalha> num mesmo evento digite 'textual'\n")
  print('Caso deseje saber os (x) esportes com mais medalhas de (tipo de medalha) ganhas na olimpiada do (ano) por atletas diferentes do (genero). Digite "extra"\n')
  tipo = input("Por favor digite o tipo de grafico/resposta desejada (linhas/barras/boxplot/textual/extra)\n")
  
      
  if tipo == "linhas":
    gerarGraficoLinhas()
  elif tipo == "barras":
    gerarGraficoBarras()
  elif tipo == "boxplot":
    gerarGraficoBoxplot()
  elif tipo == "textual":
    gerarTextual()
  elif tipo == "extra":
    gerarExtra()
  else:
    print('erro: Consulta inválida.')

inicio = timeit.default_timer()
interface()
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))