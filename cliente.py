import Pyro5.client

servidor = Pyro5.client.Proxy("")
print(servidor)