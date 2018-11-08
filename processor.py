import nltk
from nltk import FreqDist 
from nltk import word_tokenize
class processor: 

    def __init__(self): 
        self.keywords = []
        self.keyphrases = []
        self.wordscount = 133
        self.callcount = 0
        self.seekcount = 0
        self.paths = [r'C:\Users\mting\Documents\Baye Ling\Baye-Ling\Callout.txt',   
         r'C:\Users\mting\Documents\Baye Ling\Baye-Ling\seeking.txt']
        self.tokens = {}
        self.calldic = {}
        self.seekdic = {}
        self.titles = ("callout", "seeking")

    def token(self): 
        for index, path in enumerate(self.paths):
            tokens = word_tokenize(open(path).read())
            self.tokens[self.titles[index]] = FreqDist([tokens.lower() for tokens in tokens])

    def freq(self): 
        self.token()
        calldist = self.tokens['callout']
        seekingdist = self.tokens['seeking']
        for word in self.keywords: 
            # self.calldic[word] = len(list(term for term in calldist if word in term))
            # self.seekdic[word] = len(list(term for term in seekingdist if word in term))
            # self.callcount = len(list(term for term in calldist if word in term)) + self.callcount
            # self.seekcount = len(list(term for term in seekingdist if word in term)) + self.seekcount
            self.calldic[word] = calldist[word]
            self.seekdic[word] = seekingdist[word]
            self.callcount = calldist[word] + self.callcount
            self.seekcount = seekingdist[word] + self.seekcount
        
    def prob(self, submit): 
        for word in submit:
            subtoken = word_tokenize(submit)
        samewords = []
        seekwordtotal = self.seekcount + self.wordscount
        callwordtotal = self.callcount + self.wordscount
        for word in subtoken: 
            for keyword in self.keywords: 
                if word.lower() == keyword: 
                    samewords.append(word.lower())
        probseek = 96/400
        probcall = 190/400
        for word in samewords: 
            probseek = ((self.seekdic[word]+1)/seekwordtotal)*probseek
            probcall = ((self.calldic[word]+1)/callwordtotal)*probcall
        percall = probcall/(probcall+probseek)
        perseek = probseek/(probcall+probseek)
        f = open("results.txt", "a")
        if percall <.75 and perseek <.75: 
            f.write("Personal " + str(perseek) + " " + str(percall) + "\n")
        elif percall > perseek: 
            f.write("Callout " + str(perseek) + " " + str(percall) + "\n")
        else: 
            f.write("Seeking " + str(perseek) + " " + str(percall) + "\n")


           
test = processor()
items = test.freq()
tfile = open(r'C:\Users\mting\Documents\Baye Ling\Baye-Ling\personals.txt', "r")
for line in tfile:
    test.prob(line)
tfile.close()