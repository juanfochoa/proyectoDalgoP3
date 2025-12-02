# ProblemaP3.py
# Autores:
#   (Juan Felipe Hortúa
#    Juan Felipe Ochoa)


import sys

def construir_horizontales(points):
    """
    Construye las trayectorias horizontales agrupando focos por coordenada Y.
    Retorna una lista de tuplas (x1, y1, x2, y2) que representan cada trayectoria.
    """
    focos_por_y = {}
    for x, y in points:
        if y not in focos_por_y:
            focos_por_y[y] = []
        focos_por_y[y].append(x)

    horizontales = []

    for y in sorted(focos_por_y.keys()):
        lista_x = focos_por_y[y]
        min_x = min(lista_x)
        max_x = max(lista_x)
        trayectoria = (min_x, y, max_x, y)
        horizontales.append(trayectoria)
    
    return horizontales

def construir_verticales(points):
    """
    Construye las trayectorias verticales agrupando focos por coordenada X.
    Retorna una lista de tuplas (x1, y1, x2, y2) que representan cada trayectoria.
    """
    focos_por_x = {}
    for x, y in points:
        if x not in focos_por_x:
            focos_por_x[x] = []
        focos_por_x[x].append(y)

    verticales = []

    for x in sorted(focos_por_x.keys()):
        lista_y = focos_por_x[x]
        min_y = min(lista_y)
        max_y = max(lista_y)
        trayectoria = (x, min_y, x, max_y)
        verticales.append(trayectoria)
    
    return verticales

def formatear_linea(trayectorias):
    """
    Formatea una lista de trayectorias en una línea de salida.
    retorna una cadena con el formato: "cantidad x1 y1 x2 y2 ..."
    """
    cantidad = len(trayectorias)
    if cantidad == 0:
        return "0"
    
    partes = [str(cantidad)]

    for x1, y1, x2, y2 in trayectorias:
        partes.append(str(x1))
        partes.append(str(y1))
        partes.append(str(x2))
        partes.append(str(y2)) 

    return " ".join(partes)


def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    t = int(data[0])
    index = 1
    out_lines = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        points = []

        for _ in range(n):
            x = int(data[index])
            y = int(data[index + 1])
            idx +=2
            points.append((x, y))
        
        horizontales = construir_horizontales(points)
        verticales = construir_verticales(points)

        out_lines.append(formatear_linea(horizontales))
        out_lines.append(formatear_linea(verticales))   
    
    sys.stdout.write("\n".join(out_lines) + "\n")
      

if __name__ == "__main__":
    # Para pruebas locales con archivo, descomentar las siguientes líneas:
    # sys.stdin = open('input.txt', 'r')
    solve()
