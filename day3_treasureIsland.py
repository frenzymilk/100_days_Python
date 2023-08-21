direction = None
travel = None
door = None

print("Welcome to Sweetness Island. Your mission is to find the honey pot!")

direction = input("You are at a crossroad. Do you want to go left or right? Type 'left' or 'right' ").lower()
if direction == "left":
	travel = input("You arrive at a lake.Do you want to swim accross or swing on ropes like Tarzan to reach the other side? Type 'swim' or 'swing' ").lower()
	if travel == "swing":
		door = input("You arrive at a village with 3 houses. Do you want to open house with the red door, the blue door or the yellow door? Type 'blue', 'red' or 'yellow' ").lower()
		if door=="yellow":
			print("Congratulations! You found the honey pot, you win!!!")
		else:
			print("Sorry, a vicious villager was waiting for you. Game Over!!!")
	else:
		print("Sorry, the other side was too far away, you drowned. Game Over!!!")
else:
	print("Sorry, you fell in a hole with spikes in the bottom. Game Over!!!")
