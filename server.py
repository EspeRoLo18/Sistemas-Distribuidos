import Pyro5.api


@Pyro5.api.expose
class Boleto_Espectaculo:
	"""docstring for Boleto_Espectaculo"""
	#constructor  
	def __init__(self, nombre, edad, genero, name_espectaculo, fecha_espectaculo, tipo_espectaculo, seccion, numero_asiento, precio, isep, total, sello_Digital):
		"""
			Datos del espectaculo se descompone  en tres parametros nombre, fecha y tipo.
		"""
		self._nombre = nombre
		self._edad = edad
		self._genero = genero
		self._name_espectaculo = name_espectaculo
		self._fecha_espectaculo = fecha_espectaculo
		self._tipo_espectaculo = tipo_espectaculo
		self._seccion = seccion
		self._numero_asiento = numero_asiento
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
			"""
				Muestra cada atributo de la clase
			"""
			print("Datos del Comprador: \nNombre: " + str(self._nombre) + " \nEdad: " + str(self._edad) + "\nGenero: " + str(self._genero) ) #se concatena para no tener problema con el tipo de dato   
			print("Nombre del espectaculo:  " + str(self._name_espectaculo) )
			print("Fecha_espectaculo  " + str(self._fecha_espectaculo) )
			print("Tipo del espectaculo:  " + str(self._tipo_espectaculo) )
			print("Datos_Asientos: \nSeccion: " + str(self._seccion) + "\nNumero: " + str(self._numero_asiento) )
			print("Precio:  " + str(self._precio) )
			print("Isep:  " + str(self._isep) )
			print("Total:  " + str(self._total) )
			print("sello_Digital:  " + str(self._sello_Digital) )
			
			
		
		def Calcular_Impuesto(self):
			"""
				12 ---- 100%
				x  ---- 8%
				(12 * 8) / 100 = cantidad a sumar al total
				Suma el ISEP al total del costo del boleto.
			"""
			total = self._total
			porcentaje_isep = 8
			cantidad_a_sumar = (total * porcentaje_isep) / 100
			total_con_isep = total + cantidad_a_sumar
			return total_con_isep
			

		def Establece_Sello_Digital(self):


		def Modifica_Comprador(self, nombre, edad, genero):
			"""
				Modifica los datos del comprador.
			"""
			self._nombre = nombre
			self._edad = edad
			self._genero = genero


		def Modifica_Evento(self, name_espectaculo, fecha_espectaculo, tipo_espectaculo):
			"""
				Modifica los datos del evento.
			"""
			self._name_espectaculo = name_espectaculo
			self._fecha_espectaculo = fecha_espectaculo
			self._tipo_espectaculo = tipo_espectaculo

		def Modifica_Asientos(self, seccion, numero_asiento):
			"""
				Modificar los datos del asiento.
			"""
			self._seccion = seccion
			self._numero_asiento = numero_asiento

		def Modifica_Precio(self, precio):
			"""
				Modificar el precio
			"""
			self._precio = precio
		
class Valida_Boleto(Boleto_Espectaculo):
	"""
		Boleto_Espectaculo contine a Valida_Boleto
		Esto para aprovechar los metodos de Boleto_Espectaculo en 
		los metodos de Valida_Boleto, es decir, podremos invocar 
		los metodos de Boleto_Espectaculo.
	"""

	def __init__(self, llave_simetrica, mensaje_autenticacion):
		"""
			Constructor
		"""
		self._llave_simetrica = llave_simetrica
		self._mensaje_autenticacion = mensaje_autenticacion

	def Genera_SelloDigital(self, boleto)
		"""
			#Paso 1. Agrupar informacion.
			#Paso 2. Enviar al servidor.
			#Paso 3. Recibir informacion e interpretarla.
			#Paso 4. Regresar sello digital o en caso de una falla, notificar.
			Genera el sello digital a traves del servidor.
		"""
		#pyro("127.1.1.1", boleto)




#     def Modifica_Comprador(self, name):
#         self._comprador = name
#         return self._comprador


