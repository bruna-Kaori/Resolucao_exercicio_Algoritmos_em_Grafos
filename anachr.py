
import sys

INFINITO = 10**12

def solve_instance(n_cida, estradas, adj, entregas, inst_num):
    out_lines = []
    out_lines.append(f"Instancia {inst_num}")
    first_q = True
    for (cidade, destino, temp_max) in entregas:
        dp = [ [INFINITO] * (n_cida+1) for _ in range(temp_max+1) ]
        nos_finitos = [ [] for _ in range(temp_max+1) ]

        dp[0][cidade] = 0
        nos_finitos[0].append(cidade)

        for t in range(0, temp_max+1):
            if not nos_finitos[t]:
                continue
            for u in nos_finitos[t]:
                du = dp[t][u]
                if du == INFINITO:
                    continue
                for (v, c, tau) in adj[u]:
                    nt = t + tau
                    if nt > temp_max:
                        continue
                    newd = du + c
                    if newd < dp[nt][v]:
                        if dp[nt][v] == INFINITO:
                            nos_finitos[nt].append(v)
                        dp[nt][v] = newd
        melhor_distancia = INFINITO
        melhor_tempo = -1
        for T in range(0, temp_max+1):
            d = dp[T][destino]
            if d < melhor_distancia:
                melhor_distancia = d
                melhor_tempo = T

        if melhor_distancia == INFINITO:
            out_lines.append("Impossivel")
        else:
            out_lines.append(f"Possivel - {melhor_distancia} km, {melhor_tempo} min")

    return out_lines

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    out = []
    inst_num = 1
    try:
        while True:
            n = int(next(it))
            m = int(next(it))
            if n == 0 and m == 0:
                break
            nos_de = [[] for _ in range(n+1)]
            for _ in range(m):
                x = int(next(it)); y = int(next(it)); c = int(next(it)); t = int(next(it))
                if 1 <= x <= n and 1 <= y <= n:
                    nos_de[x].append( (y, c, t) )
            k = int(next(it))
            entregas = []
            for _ in range(k):
                s = int(next(it)); destino = int(next(it)); temp_max = int(next(it))
                entregas.append((s, destino, temp_max))
            inst_out = solve_instance(n, m, nos_de, entregas, inst_num)
            out.extend(inst_out)
            out.append("")  
            inst_num += 1
    except StopIteration:
        pass

    if len(out) > 0 and out[-1] == "":
        out = out[:-1]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()



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

