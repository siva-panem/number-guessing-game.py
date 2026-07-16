import random

print("---------------------------Welcome to SYNTECXHUB NUMBER GUESSING GAME---------------------------")

best_score = None  # tracks lowest attempts across all games

while True:
    # --- Difficulty selection ---
    print("\nChoose difficulty level:")
    print("1. Easy   (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard   (1-200)")

    level = input("Enter your choice (1/2/3): ").strip()
    if level == "1":
        low, high = 1, 50
    elif level == "3":
        low, high = 1, 200
    else:
        low, high = 1, 100  # default = Medium

    system = random.randint(low, high)
    choice = 0
    print(f"\nThe system has picked a number between {low} and {high}. Now it's your turn to find it!")

    while True:
        try:
            user = int(input(f"Enter your guess ({low}-{high}): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        choice += 1

        if user < system:
            print(f"You need something greater than {user}.")
        elif user > system:
            print(f"You need something less than {user}.")
        else:
            print(f"Hurrah! You got it in {choice} attempts!")
            break

    # --- Update best score ---
    if best_score is None or choice < best_score:
        best_score = choice
        print(f"🎉 New best score: {best_score} attempts!")
    else:
        print(f"Your best score so far is {best_score} attempts.")

    # --- Replay option ---
    chance = input("\nDo you want to play again? (yes/no): ").lower()
    if chance != "yes":
        print(f"\nThanks for playing! Your best score this session was {best_score} attempts.")
        break