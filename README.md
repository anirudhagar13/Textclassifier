# Textclassifier
A simple interface for three underlying implementations to classify labelled text via supervised learning.

# Dependencies:
	- Spacy
	- En model of spacy
	- Scipy, Numpy

# Interface details:
	- Refer to client.py file so as how to use the module
	- There are three implementations that can be passed into Seggregator as classifier option; (cosine, naive, svm)
	- SVM parameters can be altered in svm_classify.py file
	- While instantiating Seggregator, can also pass (token='unique value') as an optional named argument, to create separate models and revoke them using the same unique value while testing.
	- In train() function can pass (init=False) as an optional named argument to add onto previous existing training set, rather than aggregating a new training set everytime.