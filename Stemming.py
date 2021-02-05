import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


paragraph="""The only person for whom the house was in any way special was Arthur Dent, and that was only because it happened
 to be the one he lived in. He had lived in it for about three years, ever since he had moved out of London because it made
 him nervous and irritable. He was about thirty as well, tall, dark-haired and never quite at ease with himself. The thing
 that used to worry him most was the fact that people always used to ask him what he was looking so worried about. He worked 
 in local radio which he always used to tell his friends was a lot more interesting than they probably thought. It was,
 too most of his friends worked in advertising."""
 
sentences=nltk.sent_tokenize(paragraph)

#initializing

stemmer=PorterStemmer()

#stemming

for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    words=[stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words)

sentences


