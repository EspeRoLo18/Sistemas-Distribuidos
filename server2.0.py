
import Pyro5
import Pyro5.core

@Pyro5.server.expose
class Boleto_Espectaculo:
    """docstring for Boleto_Espectaculo"""
    espectaculo = {
        "name_espectaculo": "",
        "fecha_espectaculo": "",
        "tipo_espectaculo": "",
        "seccion": "",
        "numero_asiento": "",
        "precio": 0,
        "total": 0
    }
    sello_digital = ""
    comprador = {
        "edad": 0,
        "genero": "",
        "nombre": ""
    }

    def Generar_Boleto(self, nombre, name_espectaculo, fecha_espectaculo, tipo_espectaculo, seccion,numero_asiento, precio, cantidad, **kwargs):
        self.comprador["nombre"] = nombre
        self.comprador["edad"] = kwargs.get("edad", 0)
        self.comprador["genero"] = kwargs.get("genero","Indefinido")
        self.espectaculo["name_espectaculo"] = name_espectaculo
        self.espectaculo["fecha_espectaculo"] = fecha_espectaculo
        self.espectaculo["tipo_espectaculo"] = tipo_espectaculo
        self.espectaculo["seccion"] = seccion
        self.espectaculo["numero_asiento"] = numero_asiento
        self.espectaculo["precio"] = precio
        self.espectaculo["total"] = self.Calcular_Impuesto(precio, cantidad)

        #Se pasa directo
        return {
            "espectaculo": self.espectaculo,
            "comprador": self.comprador
        }


    def Ver_documento(self):
        """
            Muestra cada atributo de la clase
        """
        # print("Datos del Comprador: \nNombre: " + str(self._nombre) + " \nEdad: " + str(self._edad) + "\nGenero: " + str(self._genero) ) #se concatena para no tener problema con el tipo de dato   
        # print("Nombre del espectaculo:  " + str(self._name_espectaculo) )
        # print("Fecha_espectaculo  " + str(self._fecha_espectaculo) )
        # print("Tipo del espectaculo:  " + str(self._tipo_espectaculo) )
        # print("Datos_Asientos: \nSeccion: " + str(self._seccion) + "\nNumero: " + str(self._numero_asiento) )
        # print("Precio:  " + str(self._precio) )
        # print("Isep:  " + str(self._isep) )
        # print("Total:  " + str(self._total) )
        # print("sello_Digital:  " + str(self._sello_Digital) )

        #
        return {
            "espectaculo": self.espectaculo,
            "comprador": self.comprador
        }
        
        
    
    def Calcular_Impuesto(self, precio, cantidad):
        """
            12 ---- 100%
            x  ---- 8%
            (12 * 8) / 100 = cantidad a sumar al total
            Suma el ISEP al total del costo del boleto.
        """
        precio_total = precio * cantidad
        porcentaje_isep = 8
        cantidad_a_sumar = (precio_total * porcentaje_isep) / 100
        total_con_isep = total + cantidad_a_sumar
        return total_con_isep
        

    def Establece_Sello_Digital(self):
        pass
    


    def Modifica_Comprador(self, nombre, edad, genero):
        """
            Modifica los datos del comprador.
        """
        self.comprador["nombre"] = nombre
        self.comprador["edad"] = kwargs.get("edad", 0)
        self.comprador["genero"] = kwargs.get("genero","Indefinido")


    def Modifica_Evento(self, name_espectaculo, fecha_espectaculo, tipo_espectaculo):
        """
            Modifica los datos del evento.
        """
        self.espectaculo["name_espectaculo"] = name_espectaculo
        self.espectaculo["fecha_espectaculo"] = fecha_espectaculo
        self.espectaculo["tipo_espectaculo"] = tipo_espectaculo

    def Modifica_Asientos(self, seccion, numero_asiento):
        """
            Modificar los datos del asiento.
        """
        self.espectaculo["seccion"] = seccion
        self.espectaculo["numero_asiento"] = numero_asiento
        

    def Modifica_Precio(self, precio):
        """
            Modificar el precio
        """
        self.espectaculo["precio"] = precio



print('Iniciando servidor...')
Pyro5.server.serve(
		{
			Boleto_Espectaculo: "servidor2.0"
		},
		use_ns=False, verbose=True, host="locahost" 
	)