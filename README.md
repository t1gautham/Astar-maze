# A* Pathfinding Engine 

A pure Python implementation of the A* Pathfinding algorithm. Designed as a standalone logic engine that calculates the optimal path through any 2D grid using Manhattan Distance heuristics.

## Features
* **Zero Dependencies:** Built entirely with standard Python. No external libraries (like OpenCV or NumPy) are required for the core engine.
* **Heuristic-Driven:** Uses Manhattan Distance ($F = G + H$) to optimize search time and guarantee the shortest path.
* **Dynamic Grids:** Adapts to any matrix size or configuration.

## How it Works
The algorithm evaluates nodes based on two costs:
1. **G-Cost:** The exact distance from the starting node.
2. **H-Cost:** The estimated heuristic distance to the target node.
It prioritizes nodes with the lowest total $F$ cost, avoiding the exhaustive "flood fill" search of older algorithms like Dijkstra's.

## The Logic
Give the engine a 2D grid where `0` is a walkable path and `1` is a solid wall, and it will return the optimal coordinate path from Start to End.
