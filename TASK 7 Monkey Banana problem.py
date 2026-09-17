 Monkey and Banana Problem using Goal Stack Planning
Write a Python program to solve the Monkey and Banana Problem using a planning approach. The monkey starts on the floor at the center of the room, while the box is near the window. The monkey must walk to the window, push the box to the center, climb onto the box, and finally grasp the banana. Display the initial state, goal, actions executed, final plan, and final state.
class MonkeyBananaPlanner:
    def __init__(self):
        self.state = {
            "on_floor(Monkey)",
            "at(Monkey, Center)",
            "at(Box, Window)"
        }

        self.goal = "has(Monkey, Banana)"

        self.operators = {
            "Walk(Center, Window)": {
                "preconds": {
                    "on_floor(Monkey)",
                    "at(Monkey, Center)"
                },
                "add": {
                    "at(Monkey, Window)"
                },
                "del": {
                    "at(Monkey, Center)"
                }
            },

            "Push(Box, Window, Center)": {
                "preconds": {
                    "on_floor(Monkey)",
                    "at(Monkey, Window)",
                    "at(Box, Window)"
                },
                "add": {
                    "at(Monkey, Center)",
                    "at(Box, Center)"
                },
                "del": {
                    "at(Monkey, Window)",
                    "at(Box, Window)"
                }
            },

            "Climb(Box)": {
                "preconds": {
                    "on_floor(Monkey)",
                    "at(Monkey, Center)",
                    "at(Box, Center)"
                },
                "add": {
                    "on_box(Monkey)"
                },
                "del": {
                    "on_floor(Monkey)"
                }
            },

            "Grasp(Banana)": {
                "preconds": {
                    "on_box(Monkey)",
                    "at(Monkey, Center)",
                    "at(Box, Center)"
                },
                "add": {
                    "has(Monkey, Banana)"
                },
                "del": set()
            }
        }

        self.plan = []

    def can_execute(self, action):
        preconditions = self.operators[action]["preconds"]
        return preconditions.issubset(self.state)

    def execute(self, action):
        operator = self.operators[action]

        self.state -= operator["del"]
        self.state |= operator["add"]

        self.plan.append(action)

        print("\nExecuting:", action)
        print("Current State:", self.state)

    def solve(self):
        print("========== MONKEY BANANA PROBLEM ==========")

        print("\nInitial State:")
        for item in sorted(self.state):
            print("-", item)

        print("\nGoal:")
        print("-", self.goal)

        goal_stack = [
            "Walk(Center, Window)",
            "Push(Box, Window, Center)",
            "Climb(Box)",
            "Grasp(Banana)"
        ]

        print("\n========== PLANNING STARTED ==========")

        for action in goal_stack:
            if self.can_execute(action):
                self.execute(action)
            else:
                print("\nCannot execute:", action)
                print("Preconditions not satisfied!")
                return

        print("\n========== GOAL ACHIEVED ==========")

        print("\nFinal Plan:")

        for i, action in enumerate(self.plan, start=1):
            print(f"{i}. {action}")

        print("\nFinal State:")

        for item in sorted(self.state):
            print("-", item)


planner = MonkeyBananaPlanner()
planner.solve

output

========== MONKEY BANANA PROBLEM ==========

Initial State:
- at(Box, Window)
- at(Monkey, Center)
- on_floor(Monkey)

Goal:
- has(Monkey, Banana)

========== PLANNING STARTED ==========

Executing: Walk(Center, Window)
Current State: {'on_floor(Monkey)', 'at(Box, Window)', 'at(Monkey, Window)'}

Executing: Push(Box, Window, Center)
Current State: {'on_floor(Monkey)', 'at(Box, Center)', 'at(Monkey, Center)'}

Executing: Climb(Box)
Current State: {'on_box(Monkey)', 'at(Box, Center)', 'at(Monkey, Center)'}

Executing: Grasp(Banana)
Current State: {'on_box(Monkey)', 'at(Box, Center)', 'at(Monkey, Center)', 'has(Monkey, Banana)'}

========== GOAL ACHIEVED ==========

Final Plan:
1. Walk(Center, Window)
2. Push(Box, Window, Center)
3. Climb(Box)
4. Grasp(Banana)

Final State:
- at(Box, Center)
- at(Monkey, Center)
- has(Monkey, Banana)
- on_box(Monkey)
