from .models import Word
from django.http import JsonResponse
import math
import time

# rank weight for the input being at the start of the word
w1 = 0.2
# rank weight for word length
w2 = 0.1
# rank weight for words with higher frequency
w3 = -1
# index of word to be used as key during sorting of tuples
m = 1
# upper bound on the maximum number of word suggestions to be sent as response
limit = 25


def last(n):
    return n[m]


# function to sort the tuple with required keys
def sort(tuples):
    # user defined function last is passed as a parameter
    return sorted(tuples, key=last)


def search(request):
    prefix = request.GET.get('word', '')
    wordFreqTuple = []
    meanFreq = 0
    st = time.time()
    for word_tuple in Word.objects.raw('SELECT word, freq from word_search where word like %s ', ['%' + prefix + '%']):
        # converting word frequency into logarithm for more meaningful evaluation
        wordFreqTuple.append((word_tuple.word, math.log(word_tuple.freq, 2)))
        meanFreq = meanFreq + math.log(word_tuple.freq, 2)
    print(time.time()-st)
    finallist = []
    # for handling errors if the input value is not part of any words
    if len(wordFreqTuple) != 0:
        wordRankList = []
        meanFreq = meanFreq / len(wordFreqTuple)
        for tupl in wordFreqTuple:
            substrIndex = tupl[0].index(prefix)
            rank = (substrIndex * w1) + (len(tupl[0]) * w2) + ((math.log(tupl[1], 2) / meanFreq) * w3)
            wordRankList.append((tupl[0], rank))
        # sorting words in order of their aggregate weightage critera
        wordRankList = sort(wordRankList)
        for tupl in wordRankList:
            finallist.append(tupl[0])
            if len(finallist) == limit:
                break
    return JsonResponse({'word_suggestions': finallist})
