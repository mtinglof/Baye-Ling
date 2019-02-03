# This project was created for my computational linguistics class. 
# Three methods are included within the program, each can be called separately to achieve different tasks. 
# Class Sentiment complies a dictionary of word sentiments based off the site https://hedonometer.org/ using web scraping techniques. 
# Token finds most common ngrams and words within text file. Stat complies certain stats of strings passed. 

import nltk
from nltk import bigrams 
from nltk import collocations
from nltk import FreqDist 
from nltk import word_tokenize
from nltk import ngrams
from bs4 import BeautifulSoup as soup
import itertools
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

class lingpersonal: 
    def __init__(self): 
        self.paths = []
        self.starting_url = 'https://hedonometer.org/words.html' 
        self.sentdic = {}
        self.browser = webdriver.Chrome(executable_path=r'') 
    
    # Class removes punctuation and simultaneously creates a dictionary of word sentiment while assigning sentence sentiment score. 
    # Optimization of sentiment class is needed for future projects.  
    def sentiment(self):
        self.browser.create_options()
        self.browser.get(self.starting_url)
        punctuation = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', 
        '=', '[', ']', '{', '}', '\\', '|', ';', ':', ',', '.', 
        '<', '>', '?', '/', '`', '~', "''", '``', '--', "'", '"'] 
        f = open("results.txt", "a")
        for path in self.paths: 
            tfile = open(path, "r") 
            for line in tfile:
                sentscore = 0 
                line = word_tokenize(line)
                for word in line: 
                    word = word.lower()
                    if word not in punctuation and word not in self.sentdic.keys():
                        search_bar = self.browser.find_element_by_id("wordsearch")
                        search_bar.send_keys(word)
                        search_bar.send_keys(Keys.RETURN)
                        innerHTML = self.browser.execute_script("return document.body.innerHTML")
                        page_soup = soup(innerHTML)            
                        g_data = page_soup.find_all("i")
                        try: 
                            score = str(g_data[1])
                            score = float(score[3:-4])
                        except IndexError: 
                            score = 5
                        self.sentdic[word] = score
                        self.browser.find_element_by_id('wordsearch').clear()
                        if score > 6 or score < 4:
                            sentscore = sentscore + score
                    else: 
                        if (score > 6 or score < 4) and word not in punctuation:
                            sentscore = sentscore + self.sentdic[word]
                f.write(str(sentscore)+'\n')


    def token(self): 
        for path in self.paths: 
            tokens = word_tokenize(open(path).read())
            tester = FreqDist(list(ngrams(tokens, 3)))
            f = open("results.txt", "a")
            f.write(str(tester.most_common(60)))

    def stat(self):
        punctuation = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', 
        '=', '[', ']', '{', '}', '\\', '|', ';', ':', ',', '.', 
        '<', '>', '?', '/', '`', '~', "''", '``', '--', "'", '"'] 
        f = open("results.txt", "a")
        for path in self.paths: 
            tfile = open(path, "r") 
            for line in tfile:
                line = word_tokenize(line)
                count = 0 
                for word in line: 
                    if word not in punctuation:
                        count = count + 1
                f.write(str(count)+'\n')
                

test = lingpersonal()
test.token()