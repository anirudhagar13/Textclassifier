# Contains various language related operations
# Its dependency is spacywrapper.py and nltk

from .spacywrapper import SWrapper
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
Stopwords = set(stopwords.words('english'))

def basic_preprocessing(document):
	'''
	Performs the following operations and returns a cleansed document
	1. Reduces to lower case
	2. Removes certain symbols
	3. Replace certain symbols
	4. Removes stop words and small words
	'''

	# Reduce to lower case
	document = document.lower()

	# Removing forbidden items
	forbidden_list = ["'s","-"]
	for x in forbidden_list:
		if x in document:
			document = document.replace(x,'')

	# Replace items(keys) with their respective values
	replace_dict = {"_":" ", "n't":" not"}
	for rep, equi in replace_dict.items():
		if rep in document:
			document = document.replace(rep, equi)

	# Removing stopwords
	document = ' '.join([x for x in word_tokenize(document) if x not in Stopwords])
	
	return document 

def advance_preprocessing(document):
	'''
	Performs the following operations and returns a cleansed document
	1. Removes non-alphanumerics and small words
	2. Lemmatizes words into basic form
	'''

	# Delegating to basic preprocessing
	document = basic_preprocessing(document)

	cleaned_words = list()

	sentences = sent_tokenize(document)
	for inp_sent in sentences:
		temp = list()
		spacy_obj = SWrapper(inp_sent)

		# Remove non-alphanumerics and words less than length 2
		temp = [x[0] for x in spacy_obj.is_alpha() if x[1] == True and len(x[0]) > 2]

		# Reduce to lemma
		cleaned_words.extend([x[1] for x in spacy_obj.get_lemmas() if x[0] in temp])

	# Accumulating document
	document = ' '.join(cleaned_words) 

	return document

if __name__ == '__main__':
	inp_sent = input('Enter Input Sentence for Preprocessing : \n >> ')

	print ('Basic Preprocessing : ',basic_preprocessing(inp_sent))
	print ('Advance Preprocessing : ',advance_preprocessing(inp_sent))