import torch
import pyro

class Boleto_Espectaculo:
	"""docstring for Boleto_Espectaculo"""
	def __init__(self, datosDelComprador, datosDelEvento, datosDeAsientos, precio, isep, total, selloDigital):
		#super(Boleto_Espectaculo, self).__init__()
		self._datosDelComprador = datosDelComprador
		self._datosDelEvento = datosDelEvento
		self._datosDeAsientos = datosDeAsientos
		self._precio = precio
		self._isep = isep
		self._total = total
		self._selloDigital = selloDigital


	def generar_boleto(self, datosDelComprador, datosDelEvento, datosDeAsientos, precio, isep, total):
		self._datosDelComprador = datosDelComprador
		self._datosDelEvento = datosDelEvento
		self._datosDeAsientos = datosDeAsientos
		self._precio = precio
		self._isep = isep
		self._total = total

	def Ver_documento(self):
        print("Ver documento")    
        resultado = self.Modifica_Comprador("Esperanza")
        print(self._comprador)
        print(resultado)

	