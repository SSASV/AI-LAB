class MonkeyBanana:
    def __init__(self, monkey_pos, box_pos, banana_pos):
        self.monkey_position = monkey_pos
        self.box_position = box_pos
        self.banana_position = banana_pos
        self.monkey_on_box = False
        self.has_banana = False

    def walk(self, position):
        if not self.monkey_on_box:
            self.monkey_position = position
            print(f"Monkey walks to {position}")
        else:
            print("Monkey cannot walk while on the box.")

    def push(self, position):
        if self.monkey_position == self.box_position and not self.monkey_on_box:
            self.box_position = position
            self.monkey_position = position
            print(f"Monkey pushes the box to {position}")
        else:
            print("Monkey must be at the box to push it.")

    def climb(self):
        if self.monkey_position == self.box_position:
            self.monkey_on_box = True
            print("Monkey climbs the box.")
        else:
            print("Monkey is not near the box.")

    def grab(self):
        if self.monkey_on_box and self.box_position == self.banana_position:
            self.has_banana = True
            print("Monkey grabbed the banana!")
        else:
            print("Monkey cannot reach the banana.")

    def status(self):
        print("\nCurrent Status:")
        print("Monkey Position:", self.monkey_position)
        print("Box Position:", self.box_position)
        print("Banana Position:", self.banana_position)
        print("Monkey on Box:", self.monkey_on_box)
        print("Has Banana:", self.has_banana)
        print("-" * 30)


monkey_pos = input("Enter monkey position (door/window/middle): ")
box_pos = input("Enter box position (door/window/middle): ")
banana_pos = input("Enter banana position (door/window/middle): ")

game = MonkeyBanana(monkey_pos, box_pos, banana_pos)

while not game.has_banana:
    game.status()
    print("\nChoose Action:")
    print("1. Walk")
    print("2. Push Box")
    print("3. Climb Box")
    print("4. Grab Banana")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pos = input("Enter position to walk to: ")
        game.walk(pos)
    elif choice == "2":
        pos = input("Enter position to push box to: ")
        game.push(pos)
    elif choice == "3":
        game.climb()
    elif choice == "4":
        game.grab()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")

print("\nGame Over.")
