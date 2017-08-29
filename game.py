import Room

#init variables
x=0
y=0

#add rooms to map
Room.create_room("Big room", "A big room", 0,0)
Room.create_room("Small room", "A small room", -1,0)
Room.create_room("Southern Room", "a room in the south", 0,1)
#init first starting room
currentRoom = Room.rooms[0]

#main game loop
while(True):
	#print room's name and description
	print(currentRoom.name)
	print(currentRoom.description)
	#prompt for user input
	cmd = input("Enter command:  ")
	process_command(cmd)
	
#this method reads a string which if it is a vallid command, executes the input command
def process_command(cmd):
	if cmd == "North" or cmd == "north" or cmd == "n":
		y-=1
		get_room(x, y)
	elif cmd == "West" or cmd == "west" or cmd == "w":
		x-=1
		get_room(x,y)
	if cmd == "East" or cmd == "east" or cmd == "e":
		x+=1
		get_room(x, y)
	if cmd == "South" or cmd == "south" or cmd == "s":
		y+=1
		get_room(x, y)
	
#this method loops through all rooms in the rooms array until it finds the room at the player's x and y position 
def get_room(x, y):
	for i in range(len(Room.rooms)):
		r = Room.rooms[i]
		if r.x == x and r.y == y:
			currentRoom = Room.rooms[i]
			break
			