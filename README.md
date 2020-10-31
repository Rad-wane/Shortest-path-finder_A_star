# Shortest path finder with Python
## Using the A* algorithm & with visualization tool 

Dev. by : **Radwane Ait Ouhani**.


In this repo. you can find 3 files :
* `Shortest_path_finder.py` : Where all the magic happen, when runing, you get the visualization tool where you can draw, delete and launch the A* algo. 
* `A_star_algo.py` : A module with the 1* algo. that is imported into the `Shortest_path_finder.py`
* `colors.py` : A module with the colors in RGB format, that I used for the visualization tool. Also imported into `Shortest_path_finder.py`

I used `Pygame` for visualization and `tkinter` for the pop-up message in case a path is impossible. There are some comments alongside the code for clarification.
All the distances between spots are = 1.    

## Using the code : 

First run the `Shortest_path_finder.py`, a 800x800 window with a grid will pop-up. Your first click is the **start position**, you second is the **end position**, 
and if you click more, you can create a barrier (as many as you want, the more the merrier). Then you can press the `spacebar` key to start the A* search algo. You
can then see it as it evolve, with the color green as open position, and red as closed one. When it reaches the end spot, the shortest path is drawn in purple. 
You can the press `c` on your keybord to clear all and restart. If you the path is impossible to find, a message pops-up. 

## The A* algorithm :
Source : [A* search algorithm, wiki](https://en.wikipedia.org/wiki/A*_search_algorithm)

A* is an informed search algorithm, or a best-first search, meaning that it is formulated in terms of weighted graphs: starting from a specific starting node 
of a graph, it aims to find a path to the given goal node having the smallest cost (least distance travelled, shortest time, etc.). It does this by maintaining
a tree of paths originating at the start node and extending those paths one edge at a time until its termination criterion is satisfied.

At each iteration of its main loop, A* needs to determine which of its paths to extend. It does so based on the cost of the path and an estimate of the cost 
required to extend the path all the way to the goal. Specifically, A* selects the path that minimizes **f(n)=g(n)+h(n)** where **n** is the next node 
on the path, **g(n)** is the cost of the path from the start node to n, and **h(n)** is a heuristic function that estimates the cost of the 
cheapest path from n to the goal (for my code, I used `L distance` or `Manhattan distance` as h(n)) . A* terminates when the path it chooses to extend is a path
from start to goal or if there are no paths eligible to be extended. The heuristic function is problem-specific. If the heuristic function is admissible, meaning 
that it never overestimates the actual cost to get to the goal, A* is guaranteed to return a least-cost path from start to goal.

A* use a priority queue to perform the repeated selection of minimum (estimated) cost nodes to expand. This priority queue is known
as the open set or fringe. At each step of the algorithm, the node with the lowest f(x) value is removed from the queue, the f and g values of its neighbors 
are updated accordingly, and these neighbors are added to the queue. The algorithm continues until a removed node (thus the node with the lowest f value out
of all fringe nodes) is a goal node. The f value of that goal is then also the cost of the shortest path, since h at the goal is zero in an admissible
heuristic.

The algorithm described so far gives us only the length of the shortest path. To find the actual sequence of steps, the algorithm is revised so 
that each node on the path keeps track of its predecessor. After this algorithm is run, the ending node will point to its predecessor, and so on, until some
node's predecessor is the start node.

