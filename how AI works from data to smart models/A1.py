
from textblob import TextBlob
print ("sentiment spy")
history = []
while True:
    text=input("/nEnter a sentece(history/exit/reset):")
    if text.lower()=="exit":
        print("goodbye")
        break
    elif text.lower()=="history":
        history.clear()
        print("History cleared.")
        continue
    elif text.lower()=="reset":
        history.clear()
        print("History reset.")
        continue
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        sentiment ="positive"
    elif polarity < 0:
        sentiment ="negative"
    else:
        sentiment ="neutral"
    history.append((text, sentiment))
    print(f"Sentiment|polarity: {sentiment}|{polarity:.2f}")
