#==============================
#CAJERO ELECTRONICO
#==============================

saldo = 0
pin_guardado = int(input("Cree un PIN: \n"))

def menu ():
    print("\n |||CAJERO ELECTRONICO|||")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    
    
#==========
#LOGIN
#==========
    
intentos = 0
acceso=False
    
while intentos < 3:
    pin = int(input("Ingrese su pin: "))
        
    if pin== pin_guardado:
            acceso = True
            break
    else:
            print("PIN incorrecto")
            intentos+=1
    
if not acceso:
        print("Tarjeta bloqueada")
        
else:
    
#==============
#MENU PRINCIPAL
#==============     
    
    while True:
        menu() 
        opcion =int(input("Seleccione una opcion: "))
        
        if opcion == 1:
            
            print("Su saldos es: ",saldo)
        
        elif opcion == 2:
            Deposita = float(input("Ingrese la cantidad: \n"))
            
            if Deposita > 0:
                
                saldo +=Deposita
                
                print("Deposito exitoso")
                
            
            else:
                print("Monto invalido")
                
        elif opcion == 3:
            retira = float(input("Ingrese la cantidad para retirar: \n"))
            
            if retira <= saldo and retira > 0:
                saldo-=retira
                print("Retiro Exitoso")
            else:
                print("Saldo insuficiente")
                
        elif opcion == 4:
            print("Gracias por usar el cajero")
            break
        
        else:
            print("Opcion no valida")
                                                   