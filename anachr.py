
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



