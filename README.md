# Tower of Hanoi Solver - CSE4AIF Assignment 2
### Developer: Muhammad Irtiza

## Introduction
This project is an implementation of various search algorithms to solve the Tower of Hanoi problem. The Tower of Hanoi, a classic problem in algorithm and puzzle solving, involves moving disks of different sizes from one peg to another, with the constraint that no larger disk can be placed on top of a smaller one.

## Algorithms Implemented
- **Blind-Search Algorithms**: Breadth-First, Depth-First, Uniform-Cost
- **Heuristic Algorithms**: Greedy Best-First, A*

The goal was to solve the problem for 5 disks, which theoretically requires a minimum of \(2^n - 1 = 31\) moves.

## Tools Used
- **Programming Language**: Python
- **IDE**: Microsoft Visual Studio Code
- **Python Modules**: `heapq`, `heappush`, `heappop`, `deque` for efficient queue management

## Features
- **User Input for Algorithm Selection**: Users can select which search algorithm to use.
- **Step Counter**: Displays the total number of steps each algorithm takes to reach the goal state.

## State Representation
The state is represented using tuples, with each tuple signifying a peg and the numbers representing the disks in decreasing order of size.

Example:
- Initial State: `((5, 4, 3, 2, 1), (), ())`

## Heuristic Evaluation Function Design

In the assignment, the heuristic functions for both A* and Greedy Best-First search algorithms were implemented. The heuristic function, denoted as `h`, is used exclusively within these heuristic searches. The function is defined in Python as follows:

```python
def h(self, state):
    """
    Heuristic function: number of disks not in the goal position.
    """
    return len(self.goal[2]) - len(state[2])

## Program Structure
- **Class Design**: The `HanoiTower` class encapsulates the entire problem-solving process.
- **Constructor**: Sets up initial and goal states.
- **Methods**: Includes methods for validating moves, generating next states, and applying heuristic evaluation.
- **Search Methods**: Implements different search algorithms like DFS, BFS, UCS, Greedy Best-First, and A*.
- **Main Loop**: A loop that allows users to choose a search method and view the solving process and steps taken.

## Result Evaluation and Conclusion
The program executes as programmed and the Tower of Hanoi problem is solved. However, some search algorithms were able to solve the problem in lesser steps than the other problems. 

| Search Algorithm               | Steps taken to solve the problem |
|--------------------------------|----------------------------------|
| Depth-First Search (Blind Search) | 121                              |
| A* Search (Heuristic)          | 31                               |
| Breadth-First Search (Blind Search) | 31                               |
| Uniform-Cost Search (Blind Search) | 32                               |
| Greedy Best-First Search (Heuristic) | 46                               |

Given that the minimum number of steps required to solve this problem are 31, the most efficient algorithms were A* and BFS. A* uses a heuristic and an estimated cost to reach the result, thus, it makes perfect sense that it was able to solve the problem efficiently. BFS was also able to solve the problem efficiently since the solution for this problem lay relatively shallow in the state space. On the flipside, DFS was the least efficient since it insisted on exploring the deeper levels of state space first.
Uniform-Cost search was also quite efficient at 32 steps, although not as efficient as BFS or A*. Since it explores path in accordance to costs, it can start exploring longer paths if they have lower relative cost. Finally, the Greedy-Best-First Search was in the middle with 46 steps, being only more efficient than DFS since it only uses heuristics to guide its search and with no regard to the cost to reach that goal.
In conclusion, the optimal search method to solve any particular problem depends highly on the design and nature of the problem. What works well for one problem may not work best for another problem, and we need to evaluate our options as per the requirements of the specific problem at hand.


## Acknowledgements
The implementation and problem-solving approach were designed considering the specific requirements and constraints of the Tower of Hanoi problem. The project demonstrates how different algorithms perform under various conditions and highlights the importance of choosing the right algorithm based on problem characteristics.

---

For further details, please refer to the code and comments within the attached project files.
