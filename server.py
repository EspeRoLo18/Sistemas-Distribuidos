import Pyro5.api


@Pyro5.api.expose
class Boleto_Espectaculo(object):
	"""docstring for Boleto_Espectaculo"""
	#constructor  
	def __init__(self, datos_Comprador, name_espectaculo, fecha_espectaculo, tipo_espectaculo, datos_Asientos, precio, isep, total, sello_Digital):
		""" datosDel espectaculo se descompone  en tres parametros nombre, fecha y tipo"""

		self._datos_Comprador = datos_Comprador
		self._name_espectaculo = name_espectaculo
		self._fecha_espectaculo = fecha_espectaculo
		self._tipo_espectaculo = tipo_espectaculo
		self._datos_Asientos = datos_Asientos
		self._precio = precio
		self._isep = isep
		self._total = total
		self._sello_Digital = sello_Digital

	def Generar_Boleto(self):
    """
	    Generar_Boleto:
	
	    datosDelComprador = {
			"name": string,
			"edad": integer
		}
	"""

		print("generar boleto")
		return "hello world!!!"

daemon = Pyro5.api.Daemon()             # make a Pyro daemon
uri = daemon.register(Boleto_Espectaculo)    # register the greeting maker as a Pyro object

print("Ready. Object uri =", uri)       # print the uri so we can use it in the client later
daemon.requestLoop()                    # start the event loop of the server to wait for calls


# daemon = Pyro5.server.Daemon()         # make a Pyro daemon
# ns = Pyro5.api.locate_ns(port=8181)             # find the name server
# uri = daemon.register(Boleto_Espectaculo)   # register the greeting maker as a Pyro object
# ns.register("erl.project", uri)   # register the object with a name in the name server

print("Ready.")
daemon.requestLoop()                   # start the event loop of the server to wait for calls




	# def generar_boleto(self, datosDelComprador, datosDelEvento, datosDeAsientos, precio, isep, total):
	# 	self._datosDelComprador = datosDelComprador
	# 	self._datosDelEvento = datosDelEvento
	# 	self._datosDeAsientos = datosDeAsientos
	# 	self._precio = precio
	# 	self._isep = isep
	# 	self._total = total

# class Boleto_Espectaculo:
#     def __init__(self):
#         self._comprador = ""
#         self._evento = ""

#     def Generar_Boleto(self, quantity):
#         print("hello world!!!")

#         print(self._comprador)
#         print(self._evento)


		def Ver_documento(self):
			#muestra cada atributo de la clase 
			print("Datos del Comprador:  "+ str(self._datos_Comprador)) #se concatena para no tener problema con el tipo de dato   
			#resultado = self.Modifica_Comprador("Esperanza")
			print("name del espectaculo:  "+ str(self._name_espectaculo))
			print("name del espectaculo:  "+ str(self._name_espectaculo))
			print("name del espectaculo:  "+ str(self._name_espectaculo))
			print("name del espectaculo:  "+ str(self._name_espectaculo))
			print("name del espectaculo:  "+ str(self._name_espectaculo))
			print("name del espectaculo:  "+ str(self._name_espectaculo))
			
			


#     def Modifica_Comprador(self, name):
#         self._comprador = name
#         return self._comprador


