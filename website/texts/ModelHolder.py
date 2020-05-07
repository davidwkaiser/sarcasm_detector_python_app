import pickle
import sklearn

class ModelHolder:
	def __init__(self):
		self.bayes = None
		self.lr = None
		self.cvec = None

	def load_the_model(self, filename):
		infile = open(filename,'rb')
		output_file = pickle.load(infile)
		infile.close()
		print ("loaded "+ filename)
		return output_file

	def load_models(self):	
		self.bayes = self.load_the_model("bayes_finalized_model.sav")
		self.lr = self.load_the_model("lr_finalized_model.sav")
		self.cvec = self.load_the_model("vectorizer.sav")


