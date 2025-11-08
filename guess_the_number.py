import random

def display_welcome():
    """Display welcome message and game instructions."""
    print("=" * 50)
    print("🎮 WELCOME TO THE NUMBER GUESSING GAME! 🎮")
    print("=" * 50)
    print("\nHow to Play:")
    print("1. I will think of a number between 1 and 100")
    print("2. You try to guess the number")
    print("3. I'll give you hints (higher/lower)")
    print("4. Try to guess in as few attempts as possible!")
    print("\nType 'quit' at any time to exit the game.")
    print("=" * 50)

def get_difficulty():
    """Let user choose difficulty level."""
    print("\n📊 Choose Difficulty Level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice == '1':
            return 50, "Easy"
        elif choice == '2':
            return 100, "Medium"
        elif choice == '3':
            return 200, "Hard"
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

def get_user_guess():
    """Get and validate user's guess."""
    while True:
        user_input = input("\nEnter your guess: ").strip()
        
        if user_input.lower() == 'quit':
            return None
        
        try:
            guess = int(user_input)
            return guess
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def play_game():
    """Main game logic."""
    # Get difficulty level
    max_number, difficulty = get_difficulty()
    
    # Generate random number
    secret_number = random.randint(1, max_number)
    attempts = 0
    
    print(f"\n🎯 Great! I've picked a number between 1 and {max_number}.")
    print(f"Difficulty: {difficulty}")
    print("Let's start guessing!\n")
    
    # Game loop
    while True:
        guess = get_user_guess()
        
        # Check if user wants to quit
        if guess is None:
            print(f"\n👋 Thanks for playing! The number was {secret_number}.")
            print(f"You made {attempts} attempt(s).")
            break
        
        attempts += 1
        
        # Check if guess is in valid range
        if guess < 1 or guess > max_number:
            print(f"⚠️  Please guess a number between 1 and {max_number}!")
            continue
        
        # Check the guess
        if guess < secret_number:
            print(f"📈 Too low! Try a higher number.")
            print(f"   Attempts so far: {attempts}")
        elif guess > secret_number:
            print(f"📉 Too high! Try a lower number.")
            print(f"   Attempts so far: {attempts}")
        else:
            # Correct guess!
            print("\n" + "=" * 50)
            print("🎉 CONGRATULATIONS! 🎉")
            print(f"You guessed the number {secret_number} correctly!")
            print(f"Total attempts: {attempts}")
            print("=" * 50)
            
            # Performance feedback
            if attempts == 1:
                print("🏆 AMAZING! First try! Are you a mind reader?")
            elif attempts <= 5:
                print("⭐ EXCELLENT! You're really good at this!")
            elif attempts <= 10:
                print("👍 GOOD JOB! Nice guessing skills!")
            else:
                print("✅ WELL DONE! You got it!")
            
            break

def main():
    """Main function to run the game."""
    display_welcome()
    
    while True:
        play_game()
        
        # Ask if user wants to play again
        print("\n" + "-" * 50)
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        
        if play_again in ['yes', 'y']:
            print("\n" + "=" * 50)
            print("Starting a new game...")
            print("=" * 50)
        else:
            print("\n" + "=" * 50)
            print("Thanks for playing! Goodbye! 👋")
            print("=" * 50)
            break

if __name__ == "__main__":
    main()
