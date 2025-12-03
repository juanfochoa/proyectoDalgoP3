# Autores: Juan Felipe Ochoa, Juan Felipe Hortúa 
# ISIS 1105 - Proyecto Parte 3
# Problema de cobertura mínima de focos de infección
# Solución usando algoritmo de aproximación para Vertex Cover

import sys

def aproximacion_por_aristas(focos):
    """
    Aproximación 2-aproximado: por cada foco sin cubrir,
    agrega ambas líneas que lo cubren.
    """
    if not focos:
        return set(), set()
    
    lineas_x = set()
    lineas_y = set()
    
    focos_cubiertos = set()
    
    for x, y in sorted(focos):
        if (x, y) in focos_cubiertos:
            continue
        
        lineas_x.add(x)
        lineas_y.add(y)
        
        for fx, fy in focos:
            if fx == x or fy == y:
                focos_cubiertos.add((fx, fy))
    
    return lineas_x, lineas_y


def remover_lineas_innecesarias(focos, lineas_x, lineas_y):
    """
    Elimina líneas redundantes que no son necesarias
    porque sus focos ya están cubiertos por otras líneas.
    """
    lineas_x = set(lineas_x)
    lineas_y = set(lineas_y)
    
    cambio = True
    while cambio:
        cambio = False
        
        for y in list(lineas_y):
            focos_en_y = [(x, cy) for x, cy in focos if cy == y]
            todos_cubiertos = all(x in lineas_x for x, cy in focos_en_y)
            
            if todos_cubiertos:
                lineas_y.remove(y)
                cambio = True
                break
        
        for x in list(lineas_x):
            focos_en_x = [(cx, y) for cx, y in focos if cx == x]
            todos_cubiertos = all(y in lineas_y for cx, y in focos_en_x)
            
            if todos_cubiertos:
                lineas_x.remove(x)
                cambio = True
                break
    
    return lineas_x, lineas_y


def elegir_mejor_linea(focos):
    """
    Algoritmo greedy: siempre elige la línea que cubre
    más focos sin cubrir.
    """
    focos_restantes = set(focos)
    lineas_x_usadas = set()
    lineas_y_usadas = set()
    
    while focos_restantes:
        mejor_linea = None
        mejor_tipo = None
        maxima_cobertura = 0

        ys_posibles = set(y for x, y in focos_restantes)
        for y in ys_posibles:
            cobertura = sum(1 for x, cy in focos_restantes if cy == y)
            if cobertura > maxima_cobertura:
                maxima_cobertura = cobertura
                mejor_linea = y
                mejor_tipo = 'H'
        
        xs_posibles = set(x for x, y in focos_restantes)
        for x in xs_posibles:
            cobertura = sum(1 for cx, y in focos_restantes if cx == x)
            if cobertura > maxima_cobertura:
                maxima_cobertura = cobertura
                mejor_linea = x
                mejor_tipo = 'V'
        
        if mejor_tipo == 'H':
            lineas_y_usadas.add(mejor_linea)
            focos_restantes = {(x, y) for x, y in focos_restantes if y != mejor_linea}
        else:  # 'V'
            lineas_x_usadas.add(mejor_linea)
            focos_restantes = {(x, y) for x, y in focos_restantes if x != mejor_linea}
    
    return lineas_x_usadas, lineas_y_usadas


def resolver_cobertura(focos):
    if not focos:
        return [], []
    
    x1, y1 = aproximacion_por_aristas(focos)
    x1, y1 = remover_lineas_innecesarias(focos, x1, y1)

    x2, y2 = elegir_mejor_linea(focos)
    x2, y2 = remover_lineas_innecesarias(focos, x2, y2)
    
    if len(x1) + len(y1) <= len(x2) + len(y2):
        lineas_x, lineas_y = x1, y1
    else:
        lineas_x, lineas_y = x2, y2
    
    lineas_horizontales = []
    for y in sorted(lineas_y):
        xs = [x for x, cy in focos if cy == y]
        lineas_horizontales.append((y, min(xs), max(xs)))
    
    lineas_verticales = []
    for x in sorted(lineas_x):
        ys = [y for cx, y in focos if cx == x]
        lineas_verticales.append((x, min(ys), max(ys)))
    
    return lineas_horizontales, lineas_verticales


def main():
    # Para pruebas locales: descomenta la siguiente línea
    #sys.stdin = open('input.txt', 'r')
    
    entrada = sys.stdin.read().strip().split('\n')
    num_casos = int(entrada[0])
    
    for i in range(1, num_casos + 1):
        datos = list(map(int, entrada[i].split()))
        n = datos[0]
        
        focos = []
        for j in range(n):
            x = datos[1 + j * 2]
            y = datos[1 + j * 2 + 1]
            focos.append((x, y))
        
        horizontales, verticales = resolver_cobertura(focos)
        
        print(len(horizontales), end='')
        for y, x_min, x_max in horizontales:
            print(f" {x_min} {y} {x_max} {y}", end='')
        print()

        print(len(verticales), end='')
        for x, y_min, y_max in verticales:
            print(f" {x} {y_min} {x} {y_max}", end='')
        print()


if __name__ == "__main__":
    main()