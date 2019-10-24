import math

# rank weight for the input being at the start of the word
w1 = 0.2
# rank weight for word length
w2 = 0.1
# rank weight for words with higher frequency
w3 = -1
# upper bound on the maximum number of word suggestions to be sent as response
limit = 25
# index of word to be used as key during sorting of tuples
m = 1


def last(n):
    return n[m]


# function to sort the tuple with required keys
def sort(tuples):
    # user defined function last is passed as a parameter
    return sorted(tuples, key=last)


def getData(sub_string):
    # loading the data into data frame.
    wordFreqTuple = []
    meanFreq = 0
    with open('word_search.tsv') as datafile:  # opening the tab sepearted value file
        for row in datafile:
            word, frequency = row.split('\t')
            if sub_string in word:  # matching words which contain the substring
                wordFreqTuple.append((word, math.log(int(frequency), 2)))  # converting word frequency into logarithm for more meaningful evaluation
                meanFreq = meanFreq + int(frequency)
    meanFreq = meanFreq/len(wordFreqTuple)
    return wordFreqTuple, meanFreq


def getWordsWith(sub_string):
    wordFreqTuple, meanFreq = getData(sub_string)
    finallist = []
    # for handling errors if the input value is not part of any words
    if len(wordFreqTuple) != 0:
        wordRankList = []
        meanFreq = meanFreq / len(wordFreqTuple)
        for tupl in wordFreqTuple:
            substrIndex = tupl[0].index(sub_string)
            rank = (substrIndex * w1) + (len(tupl[0]) * w2) + ((math.log(tupl[1], 2) / meanFreq) * w3)
            wordRankList.append((tupl[0], rank))
        wordRankList = sort(wordRankList)
        for tupl in wordRankList:
            finallist.append(tupl[0])
            if len(finallist) == limit:
                break
    return finallist