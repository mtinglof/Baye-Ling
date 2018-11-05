import nltk
from nltk import FreqDist 
from nltk import word_tokenize

class processor: 

    def __init__(self): 
        self.callwords = ['you',  'bitch', 'ur', 'your', 'fucking', 'fuck', 'u', 'stop', 'asshole', 'crusty', 'roommate', 'hate', 'cares', 'left', 'shoutout', 'shut', 'trust', 'need', 'dear', 'stupid', 'aztec', 'cunt', 'dumbass', 'needs', 'sincerely', 'sorority', 'yourself', 'bunk', 'stealing', 'stole']
        self.paths = [r'C:\Users\mting\Documents\Baye Ling\Baye-Ling\Callout.txt', 
         r'C:\Users\mting\Documents\Baye Ling\Baye-Ling\personals.txt', 
         r'C:\Users\mting\Documents\Baye Ling\Baye-Ling\meme.txt', 
         r'C:\Users\mting\Documents\Baye Ling\Baye-Ling\seeking.txt']
        self.tokens = {}
        self.titles = ("callout", "personals", "meme", "seeking")

    def token(self): 
        for index, path in enumerate(self.paths):
            tokens = word_tokenize(open(path).read())
            self.tokens[self.titles[index]] = FreqDist([tokens.lower() for tokens in tokens])

    def freq(self): 
        self.token()
        pos = {}
        calldist = self.tokens['callout']
        personaldist = self.tokens['personals']
        memedist = self.tokens['meme']
        seekingdist = self.tokens['seeking']
        for word in self.callwords: 
            pos[word] = list((calldist[word], (personaldist[word]+memedist[word]+seekingdist[word])))
        return pos 

           
test = processor()
items = test.freq()
for item in items: 
    print(str(item) + ' ' + str(items[item]))