import random
import time


# 🎲 Map of dice numbers to emojis
DICE_FACES = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}


def roll():
    """Roll a six-sided die and return the value."""
    return random.randint(1, 6)


def print_scores(player_scores, max_score):
    """Display scores with progress bars."""
    print("\n📊 Current Scores:")
    for idx, score in enumerate(player_scores):
        progress = int((score / max_score) * 20)
        bar = "█" * progress + "-" * (20 - progress)
        print(f"Player {idx + 1}: {score:>3} pts |{bar}|")
    print("-" * 40)


# 🔢 Get number of players
while True:
    players = input("Enter number of players (2–4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Number of players must be between 2 and 4.")
    else:
        print("Invalid input, try again.")

# 🏁 Get custom winning score
while True:
    max_score = input("Enter the winning score (e.g., 50 or 100): ")
    if max_score.isdigit():
        max_score = int(max_score)
        if max_score > 0:
            break
        else:
            print("Winning score must be greater than 0.")
    else:
        print("Invalid input, please enter a number.")

# Initialize game state
player_scores = [0 for _ in range(players)]
previous_rolls = [-1 for _ in range(players)]

print(f"\n🎯 First player to reach {max_score} points wins!\n")
time.sleep(1)

# 🎮 Game loop
while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\n==============================")
        print(f"🎲 Player {player_idx + 1}'s Turn 🎲")
        print(f"Current Total: {player_scores[player_idx]} points")
        print("==============================\n")

        current_score = 0
        bonus_turn = False
        penalty_applied = False

        while True:
            should_roll = input("Roll the die? (y/n): ").lower()
            if should_roll != "y":
                break

            value = roll()
            print(f"\nRolling...", end="", flush=True)
            time.sleep(0.8)
            print(f" You rolled {DICE_FACES[value]} ({value})!")

            # If player rolls a 1 → lose turn
            if value == 1:
                print("😢 You rolled a 1! Turn over, no points added.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"💰 Current turn score: {current_score}")

                # Bonus roll for rolling a 6
                if value == 6:
                    print("✨ Lucky! You rolled a 6. You get a bonus roll!")
                    bonus_turn = True
                else:
                    bonus_turn = False

                # Penalty for two 1s in a row
                if previous_rolls[player_idx] == 1 and value == 1:
                    print("🚨 Two 1s in a row! You lose 5 points!")
                    player_scores[player_idx] = max(
                        0, player_scores[player_idx] - 5)
                    penalty_applied = True

            previous_rolls[player_idx] = value

            if not bonus_turn or penalty_applied:
                break

        # Update total score
        player_scores[player_idx] += current_score

        # 🎁 Bonus for multiples of 10
        if player_scores[player_idx] % 10 == 0 and player_scores[player_idx] != 0:
            print("🎁 Wow! Your total is a multiple of 10! +5 bonus points!")
            player_scores[player_idx] += 5

        print(f"\nYour total score is now: {player_scores[player_idx]}")

        # 🏆 Win check
        if player_scores[player_idx] >= max_score:
            print(
                f"\n🏆🎉 Player {player_idx + 1} wins with {player_scores[player_idx]} points! 🎉🏆"
            )
            break

        time.sleep(1)

    print_scores(player_scores, max_score)

    if max(player_scores) >= max_score:
        break

print("\n🎯 Game Over! Thanks for playing! 🎲")
