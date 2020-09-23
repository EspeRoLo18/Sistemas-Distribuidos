import Pyro5.api


# Pyro5.config.COMPRESSION = True
# Pyro5.config.SERVERTYPE = "multiplex"
# Pyro5.config.NS_PORT = "localhost"
# Pyro5.config.NS_PORT = 8181

# name = input("What is your name? ").strip()

print("initial")

uri = "PYRO:obj_6b66e7ea57f84d9988b9116064fad025@localhost:51729"

boleto_espectaculo = Pyro5.api.Proxy(uri)     # get a Pyro proxy to the greeting object
try:
    x = boleto_espectaculo.Generar_Boleto()
    print(x)
except Exception as e:
    print(e)
