# Monkey Banana Problem

monkey_position = "door"
box_position = "window"
banana_position = "middle"
monkey_on_box = False

print("Initial State")
print("Monkey at:", monkey_position)
print("Box at:", box_position)
print("Banana at:", banana_position)

# Monkey moves to box
monkey_position = box_position
print("Monkey moves to box")

# Monkey pushes box to banana
box_position = banana_position
monkey_position = banana_position
print("Monkey pushes box to banana")

# Monkey climbs box
monkey_on_box = True
print("Monkey climbs on box")

# Monkey gets banana
print("Monkey grabs the banana 🍌")
