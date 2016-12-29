import sys
import json

def termFreq(tweet_file):
    tweets = ""
    termDict = {}
    totalOccurence = 0

    for line in tweet_file:
        jsn = json.loads(line)
        tweets += jsn['text']

    terms = tweets.split()

    for word in terms:
        if word not in termDict:
            termDict[word] = terms.count(word)
            totalOccurence += termDict[word]

    for word in termDict:
        print word + " " + str(float(termDict[word]) / float(totalOccurence)) 

def main():
    tweet_file = open(sys.argv[1])

    termFreq(tweet_file)

if __name__ == '__main__':
    main()
