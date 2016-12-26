import sys

def buildDict(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    sent_file.seek(0)
    return scores

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    fp.seek(0)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentiments = buildDict(sent_file)

    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
