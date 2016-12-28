import sys
import tweet_sentiment
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def computerNewTerm(tweet_file, dict):
    for line in tweet_file:
        jsn = json.loads(line)
        tweet = jsn['text'].split()
        scores = []
        unknowns = {}

        for word in tweet:
            if word in dict:
                scores.append(dict[word])
            else:
                unknowns[word] = None

        if len(scores) == 0:
            avg = 0.0
        else:
            avg = float(sum(scores)) / float(len(scores))

        for key in unknowns:
            unknowns[key] = avg
            print key + " " +  str(unknowns[key])

    tweet_file.seek(0)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentiments = tweet_sentiment.buildDict(sent_file)

    computerNewTerm(tweet_file, sentiments)

if __name__ == '__main__':
    main()
