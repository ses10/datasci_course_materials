import sys
import json

def buildDict(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    sent_file.seek(0)
    return scores

def sentimentScore(word, dict):
    if word in dict:
        return dict[word];
    return 0

#read each line in tweets file and computer total
#sentiment score for each tweet
def computeSentiments(tweet_file, dict):
    for line in tweet_file:
        jsn = json.loads(line)
        tweet = jsn['text'].split()
        score = 0

        for word in tweet:
            score += sentimentScore(word, dict)

        print(score)

    tweet_file.seek(0)

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    fp.seek(0)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentiments = buildDict(sent_file)

    computeSentiments(tweet_file, sentiments)


if __name__ == '__main__':
    main()
