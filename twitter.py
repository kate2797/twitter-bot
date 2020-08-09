import tweepy
import random
from nltk.corpus import wordnet

from secrets import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline(count=1)
mention = str(mentions[0].text).lower().replace("@bitemybot ", "")
word_type = wordnet.synsets(mention)[0].pos()

noun = [
    f"Let me execute this {mention} for you",
    f"The Big O notation of {mention} is n^2",
    f"The {mention} replies back: 'Darling, I am a programmer'",
    f"10 reasons why you should know how to program in {mention}",
    f"{mention.title()}Script",
    f"Programmer to his son: 'Here, I brought you a new {mention}'",
    f"Programmer {mention} fixes 10 of the bugs"
    f"I really {mention} React",
    f"Binary {mention} is used to perform a very efficient search on sorted dataset",
    f"{mention.title()} is one of the best places to learn to code for free"
]

verb = [
    f"To {mention} a coding interview you need to know algorithms and data structures",
    f"$ git {mention} documentation.txt",
    f"The system can’t {mention} it",
    f"Let us {mention} needless data on your system",
    f"A computer program will always do what you {mention} it to do",
    f"Real software engineers don't {mention} their code",
    f"{mention.title()} defines the meaning and structure of web content"

]

adjective = [
    f"All programmers are playwrights, and all computers are {mention} actors",
    f"{mention.title()} loop: n., see loop, {mention}",
    f"Have you heard about the object-oriented way to become {mention}?",
    f"Lots of {mention} semicolons and parentheses",
    f"Programmer produces code they believe is {mention}",
    f"I'm so {mention} at programming I don't even need to test before I ship code",
    f"For Programmers, a good day starts with a {mention} blend of coffee"

]

if word_type == "n":
    api.update_status(random.choice(noun))
elif word_type == "v":
    api.update_status(random.choice(verb))
elif word_type == "a":
    api.update_status(random.choice(adjective))
