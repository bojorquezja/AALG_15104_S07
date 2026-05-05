class Caja:
    def __init__(self, pago, peso):
            self.pago : float = pago
            self.peso : float = peso
    def ratio(self) -> float:
        return self.pago / self.peso
    def __str__(self):
         return f"Caja paga S/{self.pago} y pesa {self.peso}Kg"
    def __repr__(self):
         return f"Caja paga S/{self.pago} y pesa {self.peso}Kg\n"

def ordenaBur(lst):
    n = len(lst)
    for pasada in range(n-1):
        for izqpar in range(n - 1 - pasada):
            print(lst[izqpar])
            derpar = izqpar + 1
            if lst[izqpar].ratio() < lst[derpar].ratio():
                lst[izqpar], lst[derpar] = lst[derpar], lst[izqpar]

     
lista = [Caja(3,3), Caja(1.8,2), Caja(3,4), Caja(2,3), Caja(3,7), Caja(2,5), Caja(4,10), Caja(1,3)]

print(lista)

mochila=float(input("Ingrese el peso que carga la mochila:")) 

ordenaBur(lista)

print("Se llevarán :") 
ganancia = 0.0
for c in lista: 
    if mochila +0.00000000001 >=c.peso: 
        mochila=mochila-c.peso 
        ganancia += c.pago
        print(c)
    elif mochila > 0:
        gan = c.pago / c.peso * mochila
        ganancia += gan
        print(f"Caja paga S/{gan} y pesa {mochila}Kg")
        break
print(f"Gano en total S/{ganancia}")