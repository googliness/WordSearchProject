import math

# rank weight for the input being at the start of the word
w1 = 0.2
# rank weight for word length
w2 = 0.1
# rank weight for words with higher frequency
w3 = -0.25
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
    
    with open('word_search.tsv') as datafile:  # opening the tab sepearted value file
        for row in datafile:
            word, frequency = row.split('\t')
            if sub_string in word:  # matching words which contain the substring
                wordFreqTuple.append((word, math.log(int(frequency), 2)))  # converting word frequency into logarithm for more meaningful evaluation
    minFreq = 0
    maxFreq = 0
    if wordFreqTuple != []:
        freqList = [tupl[1] for tupl in wordFreqTuple]
        minFreq = min(freqList)
        maxFreq = max(freqList)
    medianFreq = (minFreq + maxFreq) / 2
    return wordFreqTuple, medianFreq


def getWordsWith(sub_string):
    wordFreqTuple, medianFreq = getData(sub_string)
    finallist = []
    # for handling errors if the input value is not part of any words
    if len(wordFreqTuple) != 0:
        wordRankList = []
        for tupl in wordFreqTuple:
            substrIndex = tupl[0].index(sub_string)
            rank = (substrIndex * w1) + (len(tupl[0]) * w2) + ((tupl[1] / medianFreq) * w3)  # aggregate rank for a word
            wordRankList.append((tupl[0], rank))
        wordRankList = sort(wordRankList)  # sorting words according to rank
        for tupl in wordRankList:
            finallist.append(tupl[0])
            if len(finallist) == limit:
                break
    return finallist