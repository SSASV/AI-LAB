environment = [1, 0, 1, 1, 0]
vacuum_pos = 0

def vacuum_cleaner(env, pos):
    print(f"{'Percept':<10} | {'Action':<10} | {'Status':<15}")
    print("-"*40)

    while True:
        percept = "DIRTY" if env[pos] == 1 else "CLEAN"
        print(f"Vacuum at position {pos} → Current tile is {percept}")
        command = input("Enter action [s=SUCK, r=RIGHT, q=QUIT]: ").lower()

        if command == "s":
            if env[pos] == 1:
                action = "SUCK"
                env[pos] = 0
                status = "CLEANED"
            else:
                action = "SUCK"
                status = "NO DIRT"

        elif command == "r":
            if pos < len(env) - 1:
                pos += 1
                action = "RIGHT"
                status = f"Moved to {pos}"
            else:
                action = "RIGHT"
                status = "End of grid"

        elif command == "q":
            print("Exiting...")
            break

        else:
            action = "INVALID"
            status = "Try again"

        print(f"{percept:<10} | {action:<10} | {status:<15}")
        print("-"*40)

    print("\nFinal Environment State:", env)

vacuum_cleaner(environment, vacuum_pos)

