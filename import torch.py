import torch
import pyro

class Boleto_Espectaculo:
	"""docstring for Boleto_Espectaculo"""
	def __init__(self, datosDelComprador, datosDelEvento, datosDeAsientos, precio, isep, total, selloDigital):
		super(Boleto_Espectaculo, self).__init__()
		self._datosDelComprador = datosDelComprador
		self._datosDelEvento = datosDelEvento
		self._datosDeAsientos = datosDeAsientos
		self._precio = precio
		self._isep = isep
		self._total = total
		self._selloDigital = selloDigital

	