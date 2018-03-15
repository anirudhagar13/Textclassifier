# Vector Space Cosine Text Classifier
from .files import write_to_json, read_from_json
from sklearn.feature_extraction.text import TfidfVectorizer

class VectorSpace:
	def __init__(self, token):
		'''
		To initialize the pipeline
		'''
		self.train_file = 'data/' + token + '_vs_data.json'
		self.text_clf =  TfidfVectorizer()                     				

	def train(self, train_data, train_target):
		'''
		To train model
		'''
		# As interface is similar to other classifiers, accumulate docs of one class together
		training_set = {'data':list(), 'target':list()}

		for data, target in zip(train_data, train_target):
			if target in training_set['target']:
				tgt_index = training_set['target'].index(target)
				
				# Append doc with a space
				training_set['data'][tgt_index] += ' ' + data
			else:
				# Append both as new entries
				training_set['data'].append(data)
				training_set['target'].append(target)

		# Storing classes and docs for transformation later
		write_to_json(training_set, self.train_file)

		model = self.text_clf.fit(training_set['data'])
		return model

	def predict(self, trained_model, test_data):
		'''
		To predict as per trained model
		'''
		# load training set
		training_set = read_from_json(self.train_file)

		# Transforming training set and testing set. In this case, trained model is a vectorizer
		train_tfidf = trained_model.transform(training_set['data'])
		test_tfidf = trained_model.transform(test_data)

		# Converting model into array
		train_tfidf = train_tfidf.toarray()
		test_tfidf = test_tfidf.toarray()

		predicted = list()

		# Calculating cosine similarity between each training and test doc
		for test_doc in test_tfidf:
			sim_class = ''
			max_cos = -1

			for index, train_doc in enumerate(train_tfidf):
				cos_score = self.unit_cosine_calc(test_doc, train_doc)

				# Recording highest score
				if cos_score > max_cos:
					max_cos = cos_score
					sim_class = training_set['target'][index]

			predicted.append(sim_class)

		return predicted

	def unit_cosine_calc(self, v1, v2):
		'''
		Calculates cosine between two unit vectors
		'''
		cos = 0
		for x,y in zip(v1, v2):
			cos += (x*y)

		return cos

	def __str__(self):
		'''
		To make VectorSpace instance printable
		'''
		return 'Cosine Similarity Text Classifier'