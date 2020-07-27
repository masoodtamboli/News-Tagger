import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QProgressBar
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
from threading import Thread
import time

import csv
# from nltk.stem import WordNetLemmatizer
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
import nltk
from sklearn.naive_bayes import MultinomialNB

class App(QMainWindow):
	data = []
	type_ = []
	Lemmatizer = WordNetLemmatizer()

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('News Classifier')
		self.setGeometry(480,150,400,400)

		self.setAutoFillBackground(True)
		p = self.palette()
		p.setColor(self.backgroundRole(), Qt.black)
		self.setPalette(p)

		self.lab1 = QLabel(self)
		self.lab1.setText("News Classifier")
		self.lab1.move(100,30)
		self.lab1.resize(400,20)
		self.font = QFont('Open Sans',15,QFont.Bold)
		self.lab1.setFont(self.font)

		self.lab3 = QLabel(self)
		self.lab3.setText("1) Enter news")
		self.lab3.move(30,150)
		self.lab3.resize(400,20)

		self.lab4 = QLabel(self)
		self.lab4.setText("2) Press Submit Button")
		self.lab4.move(30,180)
		self.lab4.resize(400,20)

		self.lab5 = QLabel(self)
		self.lab5.setText("3) Wait for Algorithm to Predict type of news")
		self.lab5.move(30,210)
		self.lab5.resize(400,20)

		self.textbox = QLineEdit(self)
		self.textbox.move(20,80)
		self.textbox.resize(250,40)
		self.textbox.setPlaceholderText('Type your News')

		self.pbar = QProgressBar(self)
		self.pbar.setGeometry(20, 300, 350, 35)
		self.pbar.setValue(0)

		self.button = QPushButton('Submit',self)
		self.button.move(285,85)
		self.button.clicked.connect(self.test)

		self.show()	
	
	def test(self):
		Thread(target = self.main_method).start()
		Thread(target = self.handleTimer).start()


	def handleTimer(self):
		self.pbar.setValue(0)
		for i in range(11):
			value = self.pbar.value()
			if value < 100:
				value = value + 10
				self.pbar.setValue(value)
				self.pbar.setFormat("Processing ...")
			else:
				QMessageBox.about(self, 'Prediction','News Belongs to %s' % self.pred_class[0])
			time.sleep(2)

	def remove_stop_words(self,word_tokens):
	    s = stopwords.words('english')
	    stop_words = set(s)
	    filtered_sentence = [w for w in word_tokens if not w in stop_words]

	    return filtered_sentence   


	def process_sentence(self,sent):
	    # Word tokens
	    word_tokens = nltk.word_tokenize( sent )
	    # Remove Stop Words
	    word_tokens =   self.remove_stop_words( word_tokens )
	    # Lemmatize the whole sentence
	    for index in range( len(word_tokens) ):
	       word_tokens[index] = self.Lemmatizer.lemmatize( word_tokens[index] )
	    # Join the words of token
	    sent = " ".join(word_tokens)

	    return sent
	
	def main_method(self):
		with open('final_dataset.csv','r') as f:
		    r = csv.reader(f, delimiter=",")
		    for row in r:
		        self.data.append( self.process_sentence( row[0] ) )
		        self.type_.append(row[1])
		
		s = set(self.type_)
		# Vectorize the sentence
		count_vect = CountVectorizer()
		x_train = count_vect.fit_transform(self.data)

		tfidf_transformer = TfidfTransformer()
		x_train_tfd = tfidf_transformer.fit_transform(x_train)

		nb = MultinomialNB()
		nb.fit(x_train_tfd,self.type_)

		sent = self.process_sentence(self.textbox.text())

		cv = count_vect.transform([sent])
		tf_vect = tfidf_transformer.transform(cv)

		self.pred_class = nb.predict(tf_vect)

		print("Prediction: ",self.pred_class[0])


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())