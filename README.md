                         # 🚚 Sistema de Entregas com Restrição de Tempo

##  Descrição
Neste projeto foi implementada uma solução para um problema de **entregas entre cidades**, considerando **distância mínima** e **tempo máximo permitido**.  
A abordagem utilizada é baseada no algoritmo **Bellman-Ford-Moore**, conforme sugerido na dica do exercício, adaptado para trabalhar com restrição de tempo.

A solução utiliza **programação dinâmica** para calcular a menor distância possível para alcançar uma cidade em um determinado intervalo de tempo.

---

## Abordagem Utilizada
- Algoritmo inspirado no **Bellman-Ford-Moore**
- Uso de **Programação Dinâmica**
- Controle de estados por **tempo máximo (6000 minutos)**
- Busca pelo menor custo (distância) dentro do tempo permitido

---

## Descrição do Código

### Constantes e Estruturas
- **INFINITO = 10¹²**  
  Representa o valor inicial de distância infinita (`dist[v] := INFINITO` no pseudocódigo do Bellman-Ford).

- **n_cida** → número de cidades  
- **estradas** → número de estradas  
- **adj** → lista de vértices adjacentes  
- **entregas** → lista de entregas a serem verificadas  
- **inst_num** → número da instância do problema  

---

### Processamento das Instâncias
- Impressão do cabeçalho:
  ```python
  out_lines.append(f"Instancia {inst_num}")

