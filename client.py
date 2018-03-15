#==============================================================================
# Benchmarking Classifiers
#==============================================================================

import numpy as np
from TextClassifier import Seggregator
from sklearn.datasets import fetch_20newsgroups
from mongowrapper import MongoWrapper  

# Import testing and training data
# twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

# Instantiating Text Seggregator
# txt_seg = Seggregator(classifier='cosine')

# Training
# txt_seg.train(twenty_train.data[:10000], [str(x) for x in twenty_train.target[:10000]])

# Testing
# predicted = txt_seg.predict(twenty_train.data[10001:10020])
# target = [str(x) for x in twenty_train.target[10001:10020]]
# print ('Predicted : ', predicted)
# print ('Target : ', target)
# print ('Efficiency : ', np.mean(np.asarray(predicted) == np.asarray(target))*100)

#==============================================================================
# Pending Issues:
# 	- Increase efficiency by using RandomUnderSampler, having ngrams in tf-idf
# 	or tuning parameters.
# 	- Remove deprecation warning from SVM.
#==============================================================================