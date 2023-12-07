from heapq import heappush, heappop
from collections import deque

class HanoiTower:
    def __init__(self, disks):
        """Initialization with given number of disks."""
        self.start = (tuple(i for i in range(disks, 0, -1)), tuple(), tuple())
        self.goal = (tuple(), tuple(), tuple(i for i in range(disks, 0, -1)))

    def is_valid(self, src, dest):
        """Check if it's a valid move: non-empty source and smaller disk on top."""
        return src and (not dest or src[-1] < dest[-1])

    def get_next_states(self, state):
        """Generate all valid next states from the current state."""
        next_states = []
        for i in range(3):
            for j in range(3):
                if i != j and self.is_valid(state[i], state[j]):
                    new_state = list(map(list, state))
                    new_state[j].append(new_state[i].pop())
                    next_states.append(tuple(map(tuple, new_state)))
        return next_states

    def h(self, state):
        """Heuristic function: number of disks not in the goal position."""
        return len(self.goal[2]) - len(state[2])

    def dfs(self):
        """Depth-First Search: recursive search through the state space."""
        visited = set()
        stack = [(self.start, [])]

        while stack:
            state, steps = stack.pop()

            if state == self.goal:
                for step in steps:
                    print(step)
                return len(steps)

            if state not in visited:
                visited.add(state)
                for next_state in self.get_next_states(state):
                    stack.append((next_state, steps + [next_state]))

    def bfs(self):
        """Breadth-First Search: search through the state space."""
        queue = deque([(self.start, [])])
        visited = set()

        while queue:
            state, steps = queue.popleft()

            if state == self.goal:
                for step in steps:
                    print(step)
                return len(steps)

            if state not in visited:
                visited.add(state)
                for next_state in self.get_next_states(state):
                    queue.append((next_state, steps + [next_state]))

    def ucs(self):
        """Uniform Cost Search: cost-based search through the state space."""
        heap = [(len(steps), steps[-1], steps) for steps in [[self.start]]]
        visited = set()

        while heap:
            cost, state, steps = heappop(heap)

            if state == self.goal:
                for step in steps:
                    print(step)
                return len(steps)

            if state not in visited:
                visited.add(state)
                for next_state in self.get_next_states(state):
                    heappush(heap, (cost + 1, next_state, steps + [next_state]))

    def greedy_best_first(self):
        """Greedy Best-First Search: heuristic-based search through the state space."""
        heap = [(self.h(self.start), self.start, [])]
        visited = set()

        while heap:
            priority, state, steps = heappop(heap)

            if state == self.goal:
                for step in steps:
                    print(step)
                return len(steps)

            if state not in visited:
                visited.add(state)
                for next_state in self.get_next_states(state):
                    heappush(heap, (self.h(next_state), next_state, steps + [next_state]))

    def a_star(self):
        """A* Search: heuristic-based search through the state space."""
        heap = [(self.h(self.start), self.start, [])]
        visited = set()

        while heap:
            priority, state, steps = heappop(heap)

            if state == self.goal:
                for step in steps:
                    print(step)
                return len(steps)

            if state not in visited:
                visited.add(state)
                for next_state in self.get_next_states(state):
                    heappush(heap, (len(steps) + 1 + self.h(next_state), next_state, steps + [next_state]))

print('Welcome to the solution to Tower of Hanoi problem by Muhammad Irtiza')

search_methods = {
    "1": ("Depth-First Search (Blind-Search)", "dfs"),
    "2": ("A* Search (Heuristic)", "a_star"),
    "3": ("Breadth-First Search (Blind-Search)", "bfs"),
    "4": ("Uniform Cost Search (Blind-Search)", "ucs"),
    "5": ("Greedy Best-First Search (Heuristic)", "greedy_best_first"),
    "6": ("Exit the program", "exit")
}

while True:
    print("\nSelect the search method:")
    for option, (description, _) in sorted(search_methods.items()):
        print(f"{option}: {description}")

    choice = input("Enter the number of your choice: ")

    if choice not in search_methods:
        print("Invalid choice. Please choose a valid option.")
        continue

    method = search_methods[choice][1]
    if method == "exit":
        print("Exiting the program.")
        break

    hanoi = HanoiTower(5)
    steps = getattr(hanoi, method)()
    print(f"Total steps: {steps}")
