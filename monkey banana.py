# Monkey and Banana Problem

def monkey_banana():
    monkey = "door"
    box = "window"
    banana = "center"

    print("Initial State")
    print("Monkey is at:", monkey)
    print("Box is at:", box)
    print("Banana is at:", banana)

    print("\nSteps to get the banana:")

    # Step 1: Monkey goes to the box
    monkey = box
    print("1. Monkey moves to the box.")

    # Step 2: Monkey pushes the box to the banana
    box = banana
    monkey = banana
    print("2. Monkey pushes the box under the banana.")

    # Step 3: Monkey climbs the box
    print("3. Monkey climbs onto the box.")

    # Step 4: Monkey takes the banana
    print("4. Monkey grabs the banana.")

    print("\nGoal Achieved: Monkey has the banana!")

# Main Program
monkey_banana()
