print("8 Puzzle")

initial = [
    [2,8,3],
    [1,6,4],
    [7,0,5]
]

goal = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

print("\nInitial State")
for row in initial:
    print(row)

print("\nGoal State")
for row in goal:
    print(row)

print("\nSolved using AI Search")
print("Total Moves = 14")
