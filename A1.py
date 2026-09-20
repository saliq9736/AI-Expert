
print("Hello! I am AI bot. what your name??")
name=input()
print("nice to meet you",name)
print("how are you feeling today??(good/bad):")
mood=input().lower()
if mood =="good":
    print("i am glad to hear  that")
elif mood=="bad":
    print("i am sorry to hear that, i hope things get better soon.")
else:
    print("yeah i know sometimes its hard to describe your feelings")
print("It was nice talking to you",name)
print("\n Goodbye")