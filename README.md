# Computational Linguistics
> A couple projects I created for Ling 571 with Dr. Rob Malouf

My first project, processor.py was an introduction for myself into using a Naïve Bayes text classifier. The classifier was an experimentation with key word probability and complete word probability. 
The second project, lingpersonal.py, was used to compile several stats on passed .txt files, including sentiment analysis, word counts, and popular phrase comparisons. 

## Installing / Getting started

Both programs were developed in Python 3.7 
In addition to running the most updated version of Python, several packages must also be installed before running these programs.  

```
pip install beautifulsoup4
pip install nltk 
pip install selenium
```

### Initial Configuration

Both projects require that paths be set to existing .txt files that you wish to analyze. In addition, lingpersonal.py runs a Chrome extension to scrap sentiment data. Make sure you have the Chrome driver saved to your local machine and have the path properly set. See here for more details here http://chromedriver.chromium.org/getting-started 

## Developing

lingpersonal.py currently needs development to optimize sentiment collecting. The current web scrapping method, although effective, takes a significant portion of time to create an entire dictionary. 
Future development may include importing an already created corpa of sentiment data. 

In addition, processor.py needs to be edited since much of the work done to the program was left unfinished once it was determined that the datasets initially being used were too complex for a simple Naïve Bayes application to deliver acceptable classification results. 

## Features

processor.py 
* Main functionality is based in Naïve Bayes text classification 
* Uses key word probability instead of complete word probability  

lingpersonal.py
* Sentiment word analysis 
* Word and phrase frequency output 

## Contributing

Pull requests are gladly welcomed, just fork the repository and create a feature branch. 

## Links

- Professor Homepage: https://malouf.sdsu.edu/
- Repository: https://github.com/mtinglof/Computational-Ling-Class
- Chrome Driver: http://chromedriver.chromium.org/getting-started
- Natural Language Toolkit: https://www.nltk.org/ 
- Hedonometer Team: https://hedonometer.org
- My Homepage: https://github.com/mtinglof

## Licensing

This project is licensed under Unlicense license. This license does not require you to take the license with you to your project.
