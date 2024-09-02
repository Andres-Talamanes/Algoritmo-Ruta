from collections import deque

matriz = [
    [-3, -3, 2, -3, 3, -2, -2, 1, 2, 0, 2, 0, 1],
    [2, 3, -1, -1, 3, 2, 0, -3, -3, 2, 0, 1, 1],
    [1, -3, 2, 3, 1, 3, 3, 2, 1, -2, 2, -3, 3],
    [0, 0, 3, 3, -3, -2, -3, 0, 2, 1, 1, 0, 1],
    [2, -1, -1, -3, 3, 3, 0, -3, 1, -2, 0, 1, 0],
    [0, 3, -1, -1, -1, 2, -2, 2, -2, 1, -2, -3, 0],
    [0, 3, 2, 0, 1, 1, 2, 3, -1, 3, 0, -2, 0],
    [3, 3, -3, -2, 3, -3, -1, 3, 2, 2, -2, -2, -1],
    [-2, -1, 0, -1, 0, 3, 0, 0, 0, -2, -2, -3, -1],
    [-3, 3, 0, -1, -3, 1, -2, 3, -3, -3, 2, 2, 1],
    [-3, -3, -3, 3, -2, 0, -2, 3, 1, 0, 1, -1, 2],
    [-1, 0, 1, 2, 1, 0, -3, 3, 0, -3, 3, -2, 0],
    [1, 3, -1, 0, 1, 2, 3, 1, -2, 3, 0, 3, 0]
]

inicio = (1, 2)  # Punto 'I'
final = (11, 7)  # Punto 'F'

def bfs_min_cost(matriz, inicio, final):
    filas, columnas = len(matriz), len(matriz[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    queue = deque([(inicio, 0, [inicio])])  
    visitado = set([inicio])
    min_ruta = []

    while queue:
        (x, y), costo, ruta = queue.popleft()
        
        if (x, y) == final:
            min_ruta = ruta
            return costo, min_ruta

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < filas and 0 <= ny < columnas and (nx, ny) not in visitado:
                visitado.add((nx, ny))
                queue.append(((nx, ny), costo + matriz[nx][ny], ruta + [(nx, ny)]))

    return float('inf'), []  

def bfs_max_cost(matriz, inicio, final):
    filas, columnas = len(matriz), len(matriz[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    queue = deque([(inicio, 0, [inicio])])  
    visitado = set([inicio])
    max_cost = float('-inf')
    max_ruta = []

    while queue:
        (x, y), costo, ruta = queue.popleft()
        
        if (x, y) == final:
            if costo > max_cost:
                max_cost = costo
                max_ruta = ruta

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < filas and 0 <= ny < columnas and (nx, ny) not in visitado:
                visitado.add((nx, ny))
                queue.append(((nx, ny), costo + matriz[nx][ny], ruta + [(nx, ny)]))

    return max_cost, max_ruta

costo_min, ruta_min = bfs_min_cost(matriz, inicio, final)
costo_max, ruta_max = bfs_max_cost(matriz, inicio, final)

print(f"Costo de la ruta de menor costo: {costo_min}")
print(f"Ruta de menor costo: {ruta_min}")
print(f"Costo de la ruta de mayor costo: {costo_max}")
print(f"Ruta de mayor costo: {ruta_max}")