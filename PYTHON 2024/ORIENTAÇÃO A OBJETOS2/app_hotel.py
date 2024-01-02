from hotel import Hotel
import os
os.system('cls')

cliente1=Hotel('Antonio',4,40,9)
cliente2=Hotel('Francisca',3,15,2,100)
cliente3=Hotel('Luana',10,100,200)
cliente4=Hotel('Lucas',4)

clientes=[cliente1,cliente2,cliente3]
# print(cliente1)
# print(cliente2)
# print(cliente3)

# for i in clientes:
#     print(i)


def main():
   
    Hotel.mostrar()
    # print(Hotel.lista_clientes)

if __name__ == '__main__':
    main()
