import tweepy
import random
import requests
import nltk

from secrets import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# POS tagging
pos_nouns_pl = ["NNS", "NNPS"]
pos_nouns_sg = ["NN", "NNP"]
pos_verbs = ["VB"]
pos_adjectives = ["JJ"]

previous_tweet = None

# TODO:
# ADD TYPES
# NEVER RETURN THE SAME SENTECE AS PREVIOUSLY


def authorise():
    """ Twitter authorisation. """

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    try:
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        return api
    except tweepy.TweepError:
        print('Error! Failed to get access token.')


def get_random_word():
    """ Get random word from randoword API. """

    word_type = None
    word = None
    while word_type not in pos_nouns_pl + pos_nouns_sg + pos_verbs + pos_adjectives:
        get_word = requests.get(
            'https://random-word-api.herokuapp.com/word?number=1').json()
        word_type = nltk.pos_tag(get_word)[0][-1]
        word = get_word
    return word, word_type


def get_random_sentence(random_word, word_type, pos_adjectives, pos_nouns_sg, pos_nouns_pl, pos_verbs):
    """ Get a random sentence from these predefined options. """

    noun_pl_sentences = [
        f"10 reasons why you should know how to program in {random_word[0].title()}",
        f"Why do software developers always say 'it works on my {random_word[0]}'?",
        f"My friend quit their job as a programmer because they didn't like {random_word[0]}",
        f"console.log('{random_word[0]}')",
        f"A major skill in computer programming is understanding how to work with {random_word[0]}",
    ]

    noun_sg_sentences = [
        f"Hey, I'm working as software {random_word[0]}. What about you?",
        f"My friend quit their job as a programmer because they didn't like {random_word[0]}",
        f"{random_word[0].title()} is one of the best places to learn to code for free",
        "Binary {random_word[0]} is used to perform a very efficient search on sorted dataset",
        f"{random_word[0].title()} automatically fixes every bug present in your code",
        f"Programmer to his son: 'Here, I brought you a new {random_word[0]}'",
        f"{random_word[0].title()} defines the meaning and structure of web content",
        f"I said to my computer science professor that my {random_word[0]} ate my homework",
        f"Let me execute this {random_word[0]} for you",
        f"{random_word[0].title()}Script is the new JavaScript",
        f"Why do software developers always say 'it works on my {random_word[0]}'?",
        f"The Big O notation of {random_word[0]} is n^2",
        f"The {random_word[0]} replies back: 'Darling, I am a programmer'",
        f"10 reasons why you should know how to program in {random_word[0]}",
        f"console.log('{random_word[0]}')",
    ]

    verb_sentences = [
        f"I really {random_word[0]} React",
        f"To {random_word[0]} a coding interview you need to know algorithms and data structures",
        f"$ git {random_word[0]} documentation.txt",
        f"The system can’t {random_word[0]} it",
        f"Let us {random_word[0]} needless data on your system",
        f"A computer program will always do what you {random_word[0]} it to do",
        f"Real software engineers don't {random_word[0]} their code",
        f"One programmer says to another. How well can you {random_word[0]}?",
        f"What does a coder do when a recursion program fails to {random_word[0]} after several attempts?",
        f"console.log('{random_word[0]}')",
        f"They desperately needed another progammer since the current one only knew how to {random_word[0]} in C++",
    ]

    adjective_sentences = [
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
        f"I tried to write a code for {random_word[0]} robots but it didn’t work",
        f"console.log('{random_word[0]}')",
    ]

    if word_type in pos_nouns_pl:
        return random.choice(noun_pl_sentences)

    elif word_type in pos_nouns_sg:
        return random.choice(noun_sg_sentences)

    elif word_type in pos_verbs:
        return random.choice(verb_sentences)

    elif word_type in pos_adjectives:
        return random.choice(adjective_sentences)


def tweet(tweepy_api, sentence):
    """ Tweet. """

    try:
        tweet = tweepy_api.update_status(sentence)
        return tweet
    except tweepy.TweepError as e:
        print(e)


def main():
    api = authorise()
    random_word, word_type = get_random_word()
    sentence = get_random_sentence(random_word, word_type, pos_adjectives,
                                   pos_nouns_sg, pos_nouns_pl, pos_verbs)
    tweeted = tweet(api, sentence)
    return tweeted


main()
