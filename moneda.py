dinero=[200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05]

vuelto=float(input("Ingrese el vuelto :")) 

print("Se le devuelve :") 
for v in dinero: 
    cantidad=vuelto//v 
    if cantidad>0: 
        vuelto=vuelto-(cantidad*v) +0.00000000001
        print(f"S/{v}: {cantidad}")

print(vuelto)