from re import search
import tweepy
import random
import requests
import nltk

from secrets import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Handle creating funny sentences
"""
mentions = api.mentions_timeline(count=1)
mention = str(mentions[0].text).lower().replace("@bitemybot ", "")
"""

random_word = requests.get(
    'https://random-word-api.herokuapp.com/word?number=1').json()
word_type = nltk.pos_tag(random_word)[0][-1]

noun = [
    f"Let me execute this {random_word[0]} for you",
    f"The Big O notation of {random_word[0]} is n^2",
    f"The {random_word[0]} replies back: 'Darling, I am a programmer'",
    f"10 reasons why you should know how to program in {random_word[0]}",
    f"{random_word[0].title()}Script is the new JavaScript",
    f"Programmer to his son: 'Here, I brought you a new {random_word[0]}'",
    f"Programmer {random_word[0]} fixes 10 of the bugs"
    f"I really {random_word[0]} React",
    f"Binary {random_word[0]} is used to perform a very efficient search on sorted dataset",
    f"{random_word[0].title()} is one of the best places to learn to code for free",
    f"My friend quit their job as a programmer because they didn't like {random_word[0]}'",
    f"Why do software developers always say 'it works on my {random_word[0]}'?",
    f"Hey, I'm working as software {random_word[0]}. What about you?"
]

verb = [
    f"To {random_word[0]} a coding interview you need to know algorithms and data structures",
    f"$ git {random_word[0]} documentation.txt",
    f"The system can’t {random_word[0]} it",
    f"Let us {random_word[0]} needless data on your system",
    f"A computer program will always do what you {random_word[0]} it to do",
    f"Real software engineers don't {random_word[0]} their code",
    f"{random_word[0].title()} defines the meaning and structure of web content",
    f"One programmer says to another. How well can you {random_word[0]}?",
    f"What does a coder do when a recursion program fails to {random_word[0]} after several attempts?",
    f"I said to my computer science professor that my {random_word[0]} ate my homework."

]

adjective = [
    f"All programmers are playwrights, and all computers are {random_word[0]} actors",
    f"{random_word[0].title()} loop: n., see loop, {random_word[0]}",
    f"Have you heard about the object-oriented way to become {random_word[0]}?",
    f"Lots of {random_word[0]} semicolons and parentheses",
    f"Programmer produces code they believe is {random_word[0]}",
    f"I'm so {random_word[0]} at programming I don't even need to test before I ship code",
    f"For Programmers, a good day starts with a {random_word[0]} blend of coffee",
    f"Beware of the {random_word[0]} programmer, they may byte",
    f"A coworker who is writing documentation about some {random_word[0]} software was asking me 'What do you call that UI element? Is it a sidebar or a pane?'",
    f"I'm taking a forty-day break from {random_word[0]} software",
    f"I tried to write a code for {random_word[0]} robots but it didn’t work"

]

pos_nouns = ["NN", "NNS", "NNP", "NNPS"]
pos_verbs = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
pos_adjectives = ["JJ", "JJR", "JJS"]

if word_type in pos_nouns:
    api.update_status(random.choice(noun))
elif word_type in pos_verbs:
    api.update_status(random.choice(verb))
elif word_type in pos_adjectives:
    api.update_status(random.choice(adjective))
