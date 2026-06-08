import asyncio
import random
import httpx

# Define API URL Constants
DATAMUSE_URL = "https://api.datamuse.com/words"

async def fetch_random_word_and_definition():
    """
    Connects to the Datamuse API to pull a popular 5-8 letter English noun
    along with its dictionary definitions ('md=d').
    """
    # We query for general words matching a specific length constraint using wildcard 'sp'
    # 'md=d' requests metadata definitions. 'max=50' gives us a good pool to pick from.
    params = {
        "sp": "??????",  # Wildcard forcing exactly 6-letter words (change number of ? for different lengths)
        "md": "d",       # Fetch definitions
        "max": 100       # Get a pool of 100 words
    }
    
    print("📡 Connecting to Datamuse API to fetch a secret word...")
    
    # Using an async HTTP context manager
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(DATAMUSE_URL, params=params, timeout=5.0)
            response.raise_for_status() # Raise error if API is down
            word_data_pool = response.json()
            
            # Filter out words that don't have a valid definition attached
            valid_pool = [w for w in word_data_pool if "defs" in w and w["defs"]]
            
            if not valid_pool:
                raise ValueError("No definitions found in the payload.")
                
            # Pick a random word object from the API response pool
            chosen_object = random.choice(valid_pool)
            
            word = chosen_object["word"]
            # Clean up the dictionary definition string provided by the API
            raw_definition = chosen_object["defs"][0]
            # Datamuse prepends part of speech (e.g., "n\tdefinition"), let's strip it
            clean_definition = raw_definition.split("\t")[-1]
            
            return word, clean_definition
            
        except (httpx.HTTPError, ValueError, KeyError) as e:
            print(f"⚠️ API Connection Failed ({e}). Falling back to local backup...")
            # Fail-safe backup if the user loses internet or the API goes down
            backup_dict = {
                "matrix": "An environment or material in which something develops; a surrounding medium or structure.",
                "galaxy": "A system of millions or billions of stars, together with gas and dust, held together by gravitational attraction.",
                "wizard": "A man who has magical powers, especially in legends and fairy tales."
            }
            word = random.choice(list(backup_dict.keys()))
            return word, backup_dict[word]

async def main():
    # Asynchronously await our API call data
    secret_word, definition_hint = await fetch_random_word_and_definition()
    
    guessed_word = ["_"] * len(secret_word)
    incorrect_guesses_left = 6
    guessed_letters = []
    hint_used = False

    print("\n=========================================")
    print("      WELCOME TO API-POWERED HANGMAN     ")
    print("=========================================")
    print(f"The API has selected a {len(secret_word)}-letter word.")
    print("Type 'hint' at any time to read the dictionary definition! (Costs 1 life)")

    while incorrect_guesses_left > 0 and "_" in guessed_word:
        print("\n" + " ".join(guessed_word))
        print(f"Lives remaining: {incorrect_guesses_left}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        guess = input("Enter a letter (or 'hint'): ").lower().strip()
        
        # --- ASYNC API HINT HANDLING ---
        if guess == "hint":
            if hint_used:
                print("❌ You already unlocked the definition hint!")
                continue
            if incorrect_guesses_left <= 1:
                print("❌ Not enough lives to buy a hint!")
                continue
                
            print(f"\n📖 DICTIONARY HINT: {definition_hint}")
            incorrect_guesses_left -= 1
            hint_used = True
            continue

        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single alphabetical letter.")
            continue
            
        if guess in guessed_letters:
            print("⚠️ You already tried that letter!")
            continue
            
        guessed_letters.append(guess)
        
        # Check Guess
        if guess in secret_word:
            print(f"✅ Hit! '{guess}' is in the word.")
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"❌ Miss! '{guess}' is not in the word.")
            incorrect_guesses_left -= 1

    # End Game Summary
    print("\n=========================================")
    if "_" not in guessed_word:
        print(f"🎉 VICTORY! You guessed it: {secret_word.upper()}")
    else:
        print(f"💀 DEFEAT! The word was: {secret_word.upper()}")
    print(f"Meaning: {definition_hint}")
    print("=========================================")

if __name__ == "__main__":
    # Fire up the asynchronous event loop
    asyncio.run(main())