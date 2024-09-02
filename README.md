# Algoritmo-Ruta

Este proyecto contiene un algoritmo que busca la ruta de menor y mayor costo desde un punto de inicio (`I`) hasta un punto final (`F`) en una matriz de costos. No utiliza Dijkstra, sino una variante de Búsqueda en Anchura (BFS).

## Descripción

El script utiliza BFS para encontrar dos rutas:
- **Ruta de menor costo**: Encuentra el camino con el costo acumulado más bajo desde `I` hasta `F`.
- **Ruta de mayor costo**: Encuentra el camino con el costo acumulado más alto desde `I` hasta `F`.

## Estructura de la Matriz
La matriz es una cuadrícula de 13x13 que contiene valores numéricos que representan el costo de cada celda. Los puntos `I` y `F` están definidos por sus coordenadas dentro de la matriz.