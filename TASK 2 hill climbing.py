grid = [
    [2, 4, 7, 5, 3],
    [3, 6, 9, 8, 4],
    [1, 5, 7, 10, 6],
    [2, 4, 6, 8, 5]
]

rows = len(grid)
cols = len(grid[0])


current_row = 0
current_col = 0

print("TREASURE HUNT - HILL CLIMBING")
print("--------------------------------")

print("Starting position:",
      (current_row, current_col))
print("Initial value:",
      grid[current_row][current_col])

while True:

    current_value = grid[current_row][current_col]

    
    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    best_row = current_row
    best_col = current_col
    best_value = current_value


    for dr, dc in moves:

        new_row = current_row + dr
        new_col = current_col + dc

        if 0 <= new_row < rows and 0 <= new_col < cols:

            value = grid[new_row][new_col]

            if value > best_value:
                best_value = value
                best_row = new_row
                best_col = new_col

   
    if best_value <= current_value:
        print("\nNo better neighboring state found.")
        print("Hill Climbing stopped.")
        break

    
    current_row = best_row
    current_col = best_col

    print("Moved to:",
          (current_row, current_col),
          "Value:", best_value)

print("\nFinal Position:",
      (current_row, current_col))

print("Maximum Treasure Found:",
      grid[current_row][current_col])


output

TREASURE HUNT - HILL CLIMBING
--------------------------------
Starting position: (0, 0)
Initial value: 2
Moved to: (0, 1) Value: 4
Moved to: (0, 2) Value: 7
Moved to: (1, 2) Value: 9

No better neighboring state found.
Hill Climbing stopped.

Final Position: (1, 2)
Maximum Treasure Found: 9
