# Word Search

A Web App that shows autocomplete suggestions.
This app is buit on Django and uses a corpus of 333,333,3333 English words to show users autocomplete suggestions as they type.
This app is live on : https://wordsearchapp.herokuapp.com/search/index

This HTTP Service provides a single endpoint:
GET https://wordsearchapp.herokuapp.com/search?<input>
where input is the (partial) word that the user has typed so far. For example, if the user is looking
up procrastination, the service might receive this sequence of requests:

GET https://wordsearchapp.herokuapp.com/search?word=pro

GET https://wordsearchapp.herokuapp.com/search?word=procr

GET https://wordsearchapp.herokuapp.com/search?word=procra

The response is a JSON array containing upto 25 results, ranked by the following criteria:
Matches occurs anywhere in the string, not just at the beginning. For example, eryx matches archaeopteryx (among others). Matches at the start of a word ranks higher, For example, for the input pract, the result practical ranks higher than impractical. Common words (those with a higher usage count) ranks higher than rare words. Short words ranks higher than long words. An exact match is always ranked as the first result.
