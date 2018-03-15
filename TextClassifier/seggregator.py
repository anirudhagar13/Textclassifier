# To seggregate text into classes

import sys
from .files import read_from_json, read_from_pkl, write_to_json, write_to_pkl
from .linguistics import basic_preprocessing, advance_preprocessing
from .nb_classify import NaiveBayes
from .vs_classify import VectorSpace
from .svm_classify import SupportVecMachine

class Seggregator():
	def __init__(self, classifier='naive', token='A9699K'):
		'''
		Interface for Text classification
		Maintains token to have multiple independent instances of trained seggregator
		'''
		self.token = token + '_' + classifier
		self.tagged_file = 'data/' + self.token +'_tagged_docs.json'
		self.model_file = 'data/' + self.token +'_trained_model.pkl'

		if classifier == 'naive':
			self.classifier = NaiveBayes()
		elif classifier == 'svm':
			self.classifier = SupportVecMachine()
		elif classifier == 'cosine':
			self.classifier = VectorSpace(self.token)
		else:
			raise Exception('Invalid Classifier type')

		# Loading trained model, if exists
		self.trained_model = read_from_pkl(self.model_file)

	def train(self, train_data, train_target, init=True):
		'''
		Reads existing data and append new data by default
		If init False, then systems starts accumulating data on previous training set
		'''
		tagged_docs = {'data':list(), 'target':list()}
		
		if not init:
			# Getting previously stored data
			temp = read_from_json(self.tagged_file)
			if temp:
				# If file exists and returns valid data
				tagged_docs = temp

		# Adding new data
		tagged_docs['data'].extend(train_data)
		tagged_docs['target'].extend(train_target)

		# Updating file
		write_to_json(tagged_docs, self.tagged_file)

		# Preparing training data
		tagged_docs['data'] = [advance_preprocessing(document) for document in tagged_docs['data']]

		# Delegation
		print ('Model Training Starts')
		trained_model = self.classifier.train(tagged_docs['data'], tagged_docs['target'])

		# Updating trained model
		self.trained_model = trained_model

		# Storing trained model on disk
		write_to_pkl(trained_model, self.model_file)

		# Nothing to return
		print ('Model Training Complete :)')

	def predict(self, test_data):
		'''
		To make predictions on the basis of learnt model
		'''
		predicted = list()

		# Preparing training data
		test_data = [basic_preprocessing(document) for document in test_data]

		# Delegation. Verifying if loaded model really exists
		if not isinstance(self.trained_model, str):
			predicted = self.classifier.predict(self.trained_model, test_data)
		else:
			print ('The model has not been trained yet :(')
			sys.exit(0)

		return predicted

	def __str__(self):
		'''
		To make Seggregator instance printable
		'''
		return 'Classifier : ' + self.token