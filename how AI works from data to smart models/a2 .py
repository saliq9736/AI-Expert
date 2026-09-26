
from textblob import TextBlob

print(" Sentiment Spy AI")
print("Analyze your sentences and discover their mood!")

history = []

while True:

    text = input("\nEnter a sentence (history/stats/exit/reset): ")

    if text.lower() == "exit":
        print("Goodbye! ")
        break

    elif text.lower() == "history":
        if history:
            print("\n--- Sentiment History ---")
            for number, item in enumerate(history, 1):
                print(f"{number}. {item[0]} -> {item[1]}")
        else:
            print("History is empty.")
        continue

    elif text.lower() == "reset":
        history.clear()
        print("History reset.")
        continue

    elif text.lower() == "stats":
        positive = sum(1 for item in history if item[1] == "positive")
        negative = sum(1 for item in history if item[1] == "negative")
        neutral = sum(1 for item in history if item[1] == "neutral")

        print("\n--- Statistics ---")
        print(f" Positive: {positive}")
        print(f" Negative: {negative}")
        print(f" Neutral: {neutral}")
        print(f"Total: {len(history)}")
        continue

    if text.strip() == "":
        print("Please enter a sentence.")
        continue

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0:
        sentiment = "positive "
    elif polarity < 0:
        sentiment = "negative "
    else:
        sentiment = "neutral "

    history.append((text, sentiment))

    words = len(text.split())
    characters = len(text)

    if abs(polarity) < 0.3:
        strength = "Weak"
    elif abs(polarity) < 0.7:
        strength = "Moderate"
    else:
        strength = "Strong"

    print("\n--- Analysis Result ---")
    print(f"Sentiment: {sentiment}")
    print(f"Polarity: {polarity:.2f}")
    print(f"Strength: {strength}")
    print(f"Words: {words}")
    print(f"Characters: {characters}")