                                 #      DESCRIÇÃO      #

#     para esse exercício, como descrito na DICA, utilizei um código baseado no BELLMAN-FORD-MOORE.                

#                                                    
#   ___________________                                                                 / \
#   |              |   \                              _____        _____     __________/ o \/\_________      _________
#   |  ENTREGAS    |____\_____                       |o o o|_______|    |___|               | | # # #  |____|o o o o  | /\
#   | _____        |    |_o__ |                      |o o o|  * * *|: ::|. .|     CIDADES   |o| # # #  |. . |o o o o  |//\\
#   [/ ___ \       |   / ___ \|     --------->       |o o o|* * *  |::  |. .| []  []  []  []|o| # # #  |. . |o o o o  |((|))        
#  []_/.-.\_\______|__/_/.-.\_[]                     |o o o|**  ** |:  :|. .| []  []  []    |o| # # #  |. . |o o o o  |((|))
#     |(O)|             |(O)|                        |_[]__|__[]___|_||_|__<|____________;;_|_|___/\___|_.|_|____[]___|  |
#      '-'               '-'



                                 #      DESCRIÇÃO DO CÓDIGO      #


#     (linha 4) INFINITO = 10**12   ---> representa o " dist[v] := INFINITO" do pseudo código do bellman.

#     (linha 6) n_cida ----> representa o número de cidades
#     (linha 6) estradas ---> é o numero de estradas.
#     (linha 6) adj ---> é a lista de vértices adjacentes.
#     (linha 6) entregas ---> é a lista de entregas que vai ser verificada.
#     (linha 6) inst_num ---> são as intâncias.

#     (linha 8) out_lines.append(f"Instancia {inst_num}") --> impriime a instânia i 

#     (linha 10) temp_max --> tempo máximo (6000 minutos).

#     (linha 11)  dp = [ [INFINITO] * (n_cida+1) for _ in range(temp_max+1) ]
#      ---> cria a tabela com a menor distância para alcançar v em tantos minutos.
#      ---> utilizando a lógica da busca em largura para as menores distâncias.

#     (linha 12)  nos_finitos ---> guarda os nós

#     (linha 14)  dp[0][cidade] = 0 --->  dist[s] := 0  (referente ao pseudo código)
#      começa na distancia 0

#     (linha 17)  for t in range(0, temp_max+1): ---> vai processando os tempos

#     (linha 18)  if not nos_finitos[t]: ---> se nenhum nó é alcançável nos tempo máximo, não há nada para melhorar.

#     (linha 20 - 32)  for u in nos_finitos[t]: ---> cada aresta u -> v
#                                                    tau = tempo

#     (linha 35 - 39)  melhor_tempo = T ---> encontra a melhor distancia                                               

#     (linha 42)  out_lines.append("Impossivel") ---> imprime "impossivel" para os impossíveis

#     (linha 44)  out_lines.append(f"Possivel - {melhor_distancia} km, {melhor_tempo} min") 
#                 ---> imprime "Possivel - <d> km, <t> min, onde <d>"

#     (linha 49)   data = sys.stdin.read().strip().split() ---> le as entradas

#     (linha 50)   it = iter(data) ---> vai consumindo um por um 

#     (linha 59)   nos_de = [[] for _ in range(n+1)] ---> lista de adjacências

#     (linha 61)   x = int(next(it)); y = int(next(it)); c = int(next(it)); t = int(next(it))
#                 ---> estrada percorrida x→y com comprimento c e tempo t

#     (linha 59)   sys.stdout.write("\n".join(out)) ---> imprme  resultado final

