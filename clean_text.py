#!/usr/bin/env python
# coding: utf-8
# -*- coding: utf-8 -*-

import re, string


emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

# Regex_str is used to GET text from CSV file
regex_str = [

    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-signs
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)'  # other words
]
# These Regex are used to EXCLUDE items from the text AFTER IMPORTING from csv with regex_str

numbers = r'(?:(?:\d+,?)+(?:\.?\d+)?)'
URL = r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+'
html_tag = r'<[^>]+>'
hash_tag = r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)"
at_sign = r'(?:@[\w_]+)'
dash_quote = r"(?:[a-z][a-z'\-_]+[a-z])"
other_word = r'(?:[\w_]+)'
other_stuff = r'(?:\S)'  # anything else - NOT USED
start_pound = r"([#?])(\w+)"  # Start with #
start_quest_pound = r"(?:^|\s)([#?])(\w+)"  # Start with ? or with #
cont_number = r'(\w*\d\w*)'  # Words containing numbers
# Removes all words of 3 characters or less *****************************************************
short_words = r'\W*\b\w{1,3}\b'  # Short words of 3 character or less
short_wordsC = re.compile(short_words, re.VERBOSE | re.IGNORECASE)
# REGEX remove all words with \ and / combinations
slash_back = r'\s*(?:[\w_]*\\(?:[\w_]*\\)*[\w_]*)'
slash_fwd = r'\s*(?:[\w_]*/(?:[\w_]*/)*[\w_]*)'
slash_all = r'\s*(?:[\w_]*[/\\](?:[\w_]*[/\\])*[\w_]*)'
# Master REGEX to INCLUDE from the original tweets ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
list_regex = r'(' + '|'.join(regex_str) + ')'
master_regex = re.compile(list_regex, re.VERBOSE | re.IGNORECASE)  # TAKE from tweets INITIALLY
def filterPick(list, filter):
    return [(l, m.group(1)) for l in list for m in (filter(l),) if m]
search_regex = re.compile(list_regex, re.VERBOSE | re.IGNORECASE).search
# Use tweetList -  that is a list from DF (using .tolist())
outlist_init = filterPick(tweet_list_org, search_regex)  # It is a tuple: initial list from all tweets
with open('outlist_init.txt', 'a',encoding="utf-8") as f:
    print(outlist_init, file=f)
char_remove = [']', '[', '(', ')', '{', '}']  # characters to be removed
words_keep = ['old', 'new', 'age', 'lot', 'bag', 'top', 'cat', 'bat', 'sap', 'jda', 'tea', 'dog', 'lie', 'law', 'lab',
              'mob', 'map', 'car', 'fat', 'sea', 'saw', 'raw', 'rob', 'win', 'can', 'get', 'fan', 'fun', 'big', 'use',
              'pea', 'pit', 'pot', 'pat', 'ear', 'eye', 'kit', 'pot', 'pen', 'bud', 'bet', 'god', 'tax', 'won', 'run',
              'lid', 'log', 'pr', 'pd', 'cop', 'nyc', 'ny', 'la', 'toy', 'war', 'law', 'lax', 'jfk', 'fed', 'cry',
              'ceo', 'pay', 'pet', 'fan', 'fun', 'usd', 'rio']

emotion_list = [':)', ';)', '(:', '(;', '}', '{', '}']
word_garb = ['here', 'there', 'where', 'when', 'would', 'should', 'could', 'thats', 'youre', 'thanks', 'hasn', 'thank',
             'https', 'since', 'wanna', 'gonna', 'aint', 'http', 'unto', 'onto', 'into', 'havent', 'dont', 'done',
             'cant', 'werent', 'https', 'u', 'isnt', 'go', 'theyre', 'each', 'every', 'shes', 'youve', 'youll', 'weve',
             'theyve','twitter']

# Dictionary with Replacement Pairs ******************************************************************************
repl_dict = {'googleele': 'google', 'lyin': 'lie', 'googles': 'google', 'aapl': 'apple', 'msft': 'microsoft',
             'google': 'google', 'googl': 'google'}

exclude = list(string.punctuation) + emotion_list + word_garb




