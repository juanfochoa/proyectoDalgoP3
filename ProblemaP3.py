# ProblemaP3.py
# Autores:
#   (Juan Felipe Hortúa
#    Juan Felipe Ochoa)


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

        points = []
        for _ in range(n):
            x = int(data[idx])
            y = int(data[idx + 1])
            idx += 2
            points.append((x, y))

        horizontales = []
        verticales = []

        # Para cada foco (x, y) creamos:
        for (x, y) in points:
            X = 2 * x
            Y = 2 * y

            # Horizontal real
            horizontales.append((X - 1, Y, X + 1, Y))

            # Vertical real
            verticales.append((X, Y - 1, X, Y + 1))

        # No debería haber duplicados, pero por si acaso:
        horizontales = sorted(set(horizontales), key=lambda t: (t[1], t[0], t[2], t[3]))
        verticales  = sorted(set(verticales),  key=lambda t: (t[0], t[1], t[2], t[3]))

        # Formatear salida
        # Línea 1: horizontales
        out_lines.append(
            f"{len(horizontales)} " +
            " ".join(f"{x1} {y1} {x2} {y2}" for x1, y1, x2, y2 in horizontales)
        )
        # Línea 2: verticales
        out_lines.append(
            f"{len(verticales)} " +
            " ".join(f"{x1} {y1} {x2} {y2}" for x1, y1, x2, y2 in verticales)
        )

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
