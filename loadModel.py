import pandas as pd
import numpy as np
import cv2

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

MODELO = load_model('modelo_20_epocas.h5')

ROTULOS = {
	0: 'GUARITA',
	1: 'IPE_AMARELO',
	2: 'CLEAVERS'
}


def ler_imagem(image):
	imagem = cv2.resize(cv2.imread(image, cv2.IMREAD_COLOR), (180, 120), interpolation=cv2.INTER_CUBIC)
	return [imagem]


def analise(imagem):
	test_datagen = ImageDataGenerator(rescale=1. / 255)
	testeImagem = np.array(ler_imagem(imagem))
	ImagensParaAvaliar = len(testeImagem)
	i = 0
	mudaRetorno = ""
	for batch in test_datagen.flow(testeImagem, batch_size=1):
		predictions = MODELO.predict(batch, 16)
		pred = np.argmax(predictions, axis=1)
		print(pred)
		mudaRetorno = ROTULOS[int(pred)]
		i += 1
		if i % ImagensParaAvaliar == 0:
			break

	return mudaRetorno
