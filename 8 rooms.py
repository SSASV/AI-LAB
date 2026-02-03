environment=[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1][1,1,1,1]
vaccum_pos=[0]
before_cleaning=[1,0,1,0],[0,0,0,0],[1,0,0,0],[0,0,0,1],[1,1,1,1],[0,1,0,1]

import random

# Step 1: Initialize environment with 0=clean, 1=dirty, 'P'=pending
choices = [0, 1, 'P']
rooms = [[random.choice(choices) for _ in range(4)] for _ in range(6)]

def calculate_percentage(section):
    total = len(section)
    clean = section.count(0)
    pending = section.count('P')
    # Treat pending as half credit
    percent = ((clean + 0.5 * pending) / total) * 100
    return percent

def clean_room(room):
    # Divide into centre, left, right
    centre = room[1:3]
    left = [room[0]] * 4
    right = [room[3]] * 4

    # Calculate percentages
    left_percent = calculate_percentage(left)
    right_percent = calculate_percentage(right)
    centre_percent = calculate_percentage(centre)

    # Overall cleaning status
    overall = (left_percent + right_percent + centre_percent) / 3

    return left_percent, right_percent, centre_percent, overall

# Step 2: Run cleaning simulation
print(f"{'Room':<6} | {'Left%':<8} | {'Right%':<8} | {'Centre%':<8} | {'Overall%':<8}")
print("-"*50)

for i, room in enumerate(rooms):
    left_p, right_p, centre_p, overall_p = clean_room(room)
    print(f"{i+1:<6} | {left_p:<8.2f} | {right_p:<8.2f} | {centre_p:<8.2f} | {overall_p:<8.2f}")
