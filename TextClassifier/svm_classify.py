# Support Vector Machine Text Classifier
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

class SupportVecMachine:
	def __init__(self):
		'''
		To initialize the pipeline
		'''
		self.text_clf = Pipeline([('tfidf', TfidfVectorizer()),
                     			('clf-svm', SGDClassifier(loss='hinge',
                     			penalty='l2', alpha=1e-3, random_state=42,
                     			max_iter=15, tol=1e-4)),])

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
		To make SupportVecMachine instance printable
		'''
		return 'Support Vector Machine Text Classifier'