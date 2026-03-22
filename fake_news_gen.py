# import the random module :
import random

subjects =[
    "shahrukh khan",
    "salman khan",
    "amir khan",
    "rohit sharma",
    "virat kohli",
    "KCR",
    "modi",
    "yogi adityanath",
    "samantha",
    "karthikeya",
    "vijay ",
    "ajith kumar",
    "ntr",
    "auto driver",
    "politician",
]


actions =[
    "eats",
    "drinks",
    "sleeps with",
    "jumping  with  ",
    "celebrates ",
    "hugs",
    "kisses",
    "blowing"
]

places_things =[
    "at red fort",
    "in taj mahal",
    "caught in a hotel",
    "bitch ",
    "in a restaurant",
    "wild party in a hotel",
    "holding ass!!"
    "and hiting!!!!!!"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_thing = random.choice(places_things)
    print(f"BREAKING NEWS: {subject} {action} {place_thing}")
    user_in=input("want to generate another fake news? (y/n): ").strip()
    if user_in.lower() != "y":
        break

print("thank you for using fake news generator!")