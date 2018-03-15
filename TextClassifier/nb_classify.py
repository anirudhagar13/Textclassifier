# Naive Bayes Text Classifier
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

class NaiveBayes:
	def __init__(self):
		'''
		To initialize the pipeline
		'''
		self.text_clf = Pipeline([('tfidf', TfidfVectorizer()),
                     				('clf', MultinomialNB()),])

	def train(self, train_data, train_target):
		'''
		To train model
		'''
		model = self.text_clf.fit(train_data, train_target)
		return model

	def predict(self, trained_model, test_data):
		'''
		To predict as per trained model
		'''
		predicted = trained_model.predict(test_data)
		return predicted

	def __str__(self):
		'''
		To make NaiveBayes instance printable
		'''
		return 'Multinomial Naive Bayes Text Classifier'