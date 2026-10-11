
import pandas as pd
from textblob import TextBlob
from colorama import init,Fore
init(autoreset =True)
url = "https://huggingface.co/datasets/drossi/EDA_on_IMDB_Movies_Dataset/resolve/main/imdb_top_1000.csv"
df = pd.read_csv(url)
print(Fore.GREEN + "Movie recommendation system")
name=input("Enter your name: ")
print("welcome",name)
genre = input("enter genre(Action, Adventure, Animation,  Comedy, Crime, Drama,   History, Horror, Mystery, Romance, Sci-Fi, Sport, Thriller, War): ")
mood = input ("how are you feeling today?")
polarity = TextBlob(mood).sentiment.polarity
print("your mood:","positive"if polarity > 0 else "negative" if polarity < 0 else "neutral")
rating = float(input("enter minimum IMDb rating(0-10): "))
movies = df[
    df['Genre'].str.contains(genre, case=False,na=False) & (df['IMDB_Rating'] >= rating)
].head(5)
if movies.empty:
    print(Fore.RED + "No movies found matching your criteria.")
else:
    print(Fore.YELLOW+"\nTop 5 recommended movies based on your preferences:")
    for movie in movies["Series_Title"]:
        print(Fore.CYAN + movie)
print(Fore.GREEN + "\n Enjoy your movies,",name)

