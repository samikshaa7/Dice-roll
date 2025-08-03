import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("🎲 Dice Roller Simulator 🎲")
    while True:
        input("Press Enter to roll the dice...")
        print(f"You rolled a {roll_dice()}")
        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()