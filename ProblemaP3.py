# ProblemaP3.py
# Autores:
#   Juan Felipe Hortúa
#   Juan Felipe Ochoa

import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    t = int(data[0])
    idx = 1
    out_lines = []

    for _ in range(t):
        n = int(data[idx])
        idx += 1

        focos = []
        for _ in range(n):
            x = int(data[idx])
            y = int(data[idx + 1])
            idx += 2
            focos.append((x, y))

        # Obtener coordenadas únicas
        x_coords = sorted(set(x for x, y in focos))
        y_coords = sorted(set(y for x, y in focos))
        
        # Crear grafo bipartito
        # Cada foco (x,y) crea una arista entre coordenada-x y coordenada-y
        grafo_x = {}
        for x in x_coords:
            grafo_x[x] = []
        
        for x, y in focos:
            if y not in grafo_x[x]:
                grafo_x[x].append(y)
        
        # Matching usando DFS
        pareja_y = {}
        for y in y_coords:
            pareja_y[y] = None
        
        def dfs(x, visitado):
            for y in grafo_x[x]:
                if y in visitado:
                    continue
                visitado.add(y)
                if pareja_y[y] is None or dfs(pareja_y[y], visitado):
                    pareja_y[y] = x
                    return True
            return False
        
        # Encontrar matching máximo
        for x in x_coords:
            visitado = set()
            dfs(x, visitado)
        
        # Crear pareja_x inversa
        pareja_x = {}
        for x in x_coords:
            pareja_x[x] = None
        for y, x in pareja_y.items():
            if x is not None:
                pareja_x[x] = y
        
        # König: encontrar vertex cover mínimo
        visitado_x = set()
        visitado_y = set()
        
        # BFS desde X no emparejados
        cola = []
        for x in x_coords:
            if pareja_x[x] is None:
                cola.append(('x', x))
                visitado_x.add(x)
        
        idx_cola = 0
        while idx_cola < len(cola):
            tipo, nodo = cola[idx_cola]
            idx_cola += 1
            
            if tipo == 'x':
                for y in grafo_x[nodo]:
                    if y not in visitado_y and pareja_y[y] != nodo:
                        visitado_y.add(y)
                        cola.append(('y', y))
            else:
                x = pareja_y[nodo]
                if x is not None and x not in visitado_x:
                    visitado_x.add(x)
                    cola.append(('x', x))
        
        # Cover: X no visitados + Y visitados
        cover_x = [x for x in x_coords if x not in visitado_x]
        cover_y = [y for y in y_coords if y in visitado_y]
        
        # Construir horizontales (para cada Y en cover)
        horizontales = []
        for y in sorted(cover_y):
            x_list = [x for x, yy in focos if yy == y]
            min_x = min(x_list)
            max_x = max(x_list)
            horizontales.append((min_x, y, max_x, y))
        
        # Construir verticales (para cada X en cover)
        verticales = []
        for x in sorted(cover_x):
            y_list = [y for xx, y in focos if xx == x]
            min_y = min(y_list)
            max_y = max(y_list)
            verticales.append((x, min_y, x, max_y))
        
        out_lines.append(formatear_linea(horizontales))
        out_lines.append(formatear_linea(verticales))

    for line in out_lines:
        print(line)


def formatear_linea(trayectorias):
    if len(trayectorias) == 0:
        return "0"
    
    partes = [str(len(trayectorias))]
    for x1, y1, x2, y2 in trayectorias:
        partes.append(str(x1))
        partes.append(str(y1))
        partes.append(str(x2))
        partes.append(str(y2))
    
    return " ".join(partes)


if __name__ == "__main__":
    sys.stdin = open('input.txt', 'r')
    solve()