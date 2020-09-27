import Pyro5.api
import os

from Crypto.Cipher import AES

IV_SIZE = 16    # 128 bit, fixed for the AES algorithm
KEY_SIZE = 32   # 256 bit meaning AES-256, can also be 128 or 192 bits
SALT_SIZE = 16  # This size is arbitrary

cleartext = b'Lorem ipsum'
password = b'highly secure encryption password'
salt = os.urandom(SALT_SIZE)
derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000,
                              dklen=IV_SIZE + KEY_SIZE)
iv = derived[0:IV_SIZE]
key = derived[IV_SIZE:]

encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(cleartext)



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