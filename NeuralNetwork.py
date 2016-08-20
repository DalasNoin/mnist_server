from PIL import Image
import sys
import os
import numpy

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.models import load_model

def convert(image):
	image = image.resize((28,28))
	img = numpy.array(image.getdata(),numpy.float32)
	img /= 3
	img = numpy.sum(img,axis=1)
	img = img.reshape(1,1,28,28)
	return img / 255

def execute(path):
	try:
		image = Image.open(path)
	except IOError:
		os.remove(path)
	prediction = numpy.argmax(model.predict_on_batch([convert(image)])[0])+1
	os.rename(path,path+str(prediction))
	

model = load_model(os.path.expanduser('~/mnist_server/mnist_model.h5'))

