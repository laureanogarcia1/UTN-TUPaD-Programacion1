
#EJERCICIO 1
#Pedimos el nombre al cliente
nombre = input("cliente: ").strip()
#creamos un bucle para revisar  que no use numeros ni signos
while nombre == " " or not nombre.isalpha():
    print("Error: ingrese un nombre no vacio y solo con letras")
    nombre = input("cliente: ").strip()
#pedimos la cantidad de productos
cantidad_producto_str = input("Cantidad de productos: ").strip()
#creamos bucle para revisar que use solo numeros enteros
while not cantidad_producto_str.isdigit() or int(cantidad_producto_str) == 0:
    print("Error: ingrese un numero entero positivo mayor a 0 ") 
    cantidad_producto_str= input("Cantidad de productos: ").strip()
cantidad_producto_int = int(cantidad_producto_str)
#definimos variables para los totales
total_sin_descuento = 0
total_con_descuento = 0
#creamos bucle para preguntar precios y saber si tienen descuento
for i in range (1,cantidad_producto_int+1):
    precio_str = input(f"producto {i} - precio: ").strip()
#nos aseguramos que el precio sea positivo y mayor a 0 
    while not precio_str.isdigit() or int(precio_str) == 0:
        print("Error: el precio debe ser un numero entero positivo mayor a 0 ")
        precio_str = input(f"producto {i} - precio: ").strip()
# preguntamos si tiene descuento y nos aseguramos quesolo ponga s para si y n para no
    precio_int = int(precio_str)
    descuento = input("Descuento S/N: ").strip().lower()
    while not descuento in ("s", "n"):
        print("Error: introduce s para si y n para no")
        descuento = input("Descuento S/N: ").strip().lower()
    total_sin_descuento += precio_int
#sacamos los precios segun si tienen descuento o no lo tiene
    if descuento == "s":
        precio_final = precio_int * 0.9
    else:
        precio_final = precio_int

    total_con_descuento += precio_final
# sacamos el ahorro y el promedio 
ahorro_total = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_producto_int
#Mostramos los resultados 
print(f"Total sin descuento: $ {total_sin_descuento}")
print(f"Total con descuento: $ {total_con_descuento}")
print(f"ahorro total: $ {ahorro_total}")
print(f"promedio: $ {promedio:.2f} ")


#EJERCICIO 2
# definimos la variables de usuiaro y contraseña correcta
usuario_correcto = "alumno"
clave_correcta = "python123"
entro = False
#creamos un bucle  para permitir maximo 3 intentos 
for i in range(1,4):
    usuario = input(f"intentos {i}/3 - usuario: ").strip()
    clave = input("clave: ").strip()
# si el usuario y la contraseña son correctas le permitimos acceso y salimos del bucle 
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido")
        #entro = True
        break
#si no es correcto el usuario o la contraeña denegamos el acceso 
    else:
        print ("Error: credencial invalida") 
# despues de 3 intentos bloqueamos cuenta 
else:
    print("cuenta bloqueda") 
# si el usuario y la contraseña es correcta mostramos el menu con las opciones 
if usuario == usuario_correcto and clave == clave_correcta:
    opcion = ""
    while opcion != "4":
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opcion: ").strip()
# si la  opcion es distinta a un numero le pedimos que ingrese un numero valido
        if not opcion.isdigit():
            print("Error: ingrese un numero valido")
            continue
# convertimos la variable opcion a enteros ya que no puede comparar strings con enteros 
        opcion_int = int(opcion)
# si la opcion es un numero fuera de rango le decimos 
        if opcion_int < 1 or opcion_int > 4:
            print("Error: opcion fuera de rango ")
            continue
# si opcion puesta es igual a 1 mostramos inscripto
        if opcion_int == 1:
            print("Inscripto")
# si la opcion es igual a dos pedimos que ingrese una nueva clave y la confirme            
        elif opcion_int == 2:
            nueva_clave = input("Ingrese nueva clave: ").strip()
            confirmacion = input("Confirme su nueva clave: ").strip()
# si la clave es menor de 6 o no coinciden al confirmar, se le marca el error            
            if len(nueva_clave) < 6:
                print("Error: la clave debe tener al menos 6 caracteres.")
            elif nueva_clave != confirmacion:
                print("Error: las claves no coinciden.")
# si la nueva clave y su confirmacion son iguales mostramos clave cambiada 
            else:
                clave_correcta = nueva_clave
                print("Clave cambiada con éxito.")
# si opcione elegida es igual a 3 mostramos una frase motivacional               
        elif opcion_int == 3:
            print("El esfuerzo de hoy es el exito de mañana")
# si elige opcion 4 terminamos el ejercicio saliendo          
        elif opcion_int == 4:
            break

# ejercicio 3 
#pedimos que ingrese su nombre y verificamos que no ingrese ningun numero sino solo letras 
nombre_3 = input(" ingrese su nombre por favor: ").strip().lower()
while not nombre_3.isalpha():
     print("error: ingrese solo letras")
     nombre_3 = input(" ingrese su nombre por favor: ").strip().lower()
#definimos las variables de los dias y opcion que tiene para elegir
opcion_1 = ""

lunes_1 = ""
lunes_2 = ""
lunes_3 = ""
lunes_4 = ""

martes_1 = ""
martes_2 = ""
martes_3 = ""
#creamos un bucle mientras sea distinto de 5 muestra las opciones del menu, si es igual a 5 finaliza 
while opcion_1 != "5":
    print ("1- Reservar turno  2-Cancelar turno  3- Ver agenda del dia  4- Ver resumen general  5-Cerrar sistema ")
    opcion_1 = input("opcion: ").strip()
#verificamos que ingrese una opcion validas de las que hay en el menu     
    if not opcion_1.isdigit():
        print("error: ingrese una opcion valida")
        continue
    opcion_1_int = int(opcion_1)
    if opcion_1_int < 1 or opcion_1_int > 5 :
        print("error: ingrese una numero valido")
        continue
#si la opcion es igual a 1 damos a elejir dia entre lunes opcion 1 y martes opcion 2
    if opcion_1_int == 1:
        print("1=Lunes  2=Martes")
        dia = input("opcion: ")
#verificamos que elija una opcion correcta         
        if not dia.isdigit():
            print("error: ingrese un caracter valido")
            continue
#convertimos la variable string dia a enteros
        dia_int = int(dia)

        if dia_int < 1 or dia_int > 2:
            print("error: ingrese un numero valido")
            continue
# si elije opcion de dia 1 (lunes) pedimos nombre del paciente y verificamos que solo use letras y no otro caracter         
        if dia_int == 1:
            print("Nombre del paciente: ")
            nombre_paciente = input("").strip().lower()
            if not nombre_paciente.isalpha():
                print("solo se perimten letras")
                continue
# si el nombre ingresado ya se encuentra con turno mostramos "ya existe este paciente"            
            elif nombre_paciente == lunes_1 or nombre_paciente == lunes_2 or nombre_paciente == lunes_3 or nombre_paciente == lunes_4:
                print("Ya existe ese paciente")
# si el nombre no se encuentra lo vamos guardando en el primer lugar vacio                
            elif lunes_1 == "":    
                lunes_1 = nombre_paciente 
                print("turno guardado")
            elif lunes_2 == "":
                lunes_2 = nombre_paciente 
                print("turno guardado")
            elif lunes_3 == "":    
                lunes_3 = nombre_paciente 
                print("turno guardado")
            elif lunes_4 == "":
                lunes_4 = nombre_paciente 
                print("turno guardado")
#si ya no hay lugar para guardar turnos se lo notificamos 
            else: 
                print("ya no hay mas turnos disponible para el lunes")
##
# en caso que la opcion elegida sea 2(martes) los procedimientos son los mismos 
        if dia_int == 2:
            print("Nombre del paciente: ")
            nombre_paciente = input("").strip().lower()
            if not nombre_paciente.isalpha():
                print("solo se perimten letras")
                continue
            elif nombre_paciente == martes_1 or nombre_paciente == martes_2 or nombre_paciente == martes_3:
                print("Ya existe ese paciente")
            elif martes_1 == "":    
                martes_1 = nombre_paciente 
                print("turno guardado")
            elif martes_2 == "":
                martes_2 = nombre_paciente 
                print("turno guardado")
            elif martes_3 == "":    
                martes_3 = nombre_paciente 
                print("turno guardado")

            else: 
                print("ya no hay mas turnos disponible para el martes")
#si la opcion del menu es iugal a 2(cancelar turnos) verificamos que elija un dia y verificamos que solo use digitos 
    if opcion_1_int == 2:
        print("1=Lunes  2=Martes")
        dia = input("opcion: ")
        if not dia.isdigit():
            print("error: ingrese un caracter valido")
            continue  
#convertimos la variable string dia a enteros
        dia_int = int(dia)

        if dia_int < 1 or dia_int > 2:
            print("error: ingrese un numero valido")
            continue
# si el dia elejido es igual a 1(lunes) pedimos nombre del paciente y verificamos que soo use letras        
        if dia_int == 1:
            print("Nombre del paciente: ")
            nombre_paciente = input("").strip().lower()
            if not nombre_paciente.isalpha():
                print("solo se permiten letras")
                continue  
# si el nombre del paciente ya se encuentra cancelamos el turno y dejamos el lugar vacio             
            elif lunes_1 == nombre_paciente:    
                lunes_1 = ""
                print("turno cancelado")
            elif lunes_2 == nombre_paciente: 
                lunes_2 = "" 
                print("turno cancelado")
            elif lunes_3 == nombre_paciente:    
                lunes_3 = ""
                print("turno cancelado")
            elif lunes_4 == nombre_paciente: 
                lunes_4 = "" 
                print("turno cancelado")
# si el nombre del paciente no esta le decimos que no hay ningun turno para ese paciente                
            else: 
                print(f"no hay ningun turno para {nombre_paciente}")

# si la opcion elegida es 2(martes) repetimos los pasos
        if dia_int == 2:
            print("Nombre del paciente: ")
            nombre_paciente = input("").strip().lower()
            if not nombre_paciente.isalpha():
                print("solo se perimten letras")
                continue        
            elif martes_1 == nombre_paciente:    
                martes_1 = ""
                print("turno cancelado")
            elif martes_2 == nombre_paciente: 
                martes_2 = "" 
                print("turno cancelado")
            elif martes_3 == nombre_paciente:    
                martes_3 = ""
                print("turno cancelado")

            else: 
                print(f"no hay ningun turno para {nombre_paciente}")
# opcion elegida del menu es igual a 3(ver agenda del dia)
# mostramos ordenadamente los turnos, si lunes es distinto "" mostramos el nombre que esta asignado, por lo contrario mostramos "(libre)" 
    if opcion_1_int == 3:
        print("LUNES")
        print(f"Turno 1: {lunes_1 if lunes_1 != "" else "(libre)"}")
        print(f"Turno 2: {lunes_2 if lunes_2 != "" else "(libre)"}")
        print(f"Turno 3: {lunes_3 if lunes_3 != "" else "(libre)"}")
        print(f"Turno 4: {lunes_4 if lunes_4 != "" else "(libre)"}")
        print("MARTES")
        print(f"Turno 1: {martes_1 if martes_1 != "" else "(libre)"}")
        print(f"Turno 2: {martes_2 if martes_2 != "" else "(libre)"}")
        print(f"Turno 3: {martes_3 if martes_3 != "" else "(libre)"}")
# opcion del menu es iugla a 4(ver resumen general)
    if opcion_1_int == 4:
# asignamos a la variable turnos_ocupados_lunes el valor de 0, si lunes_1 es distinto de ""(espacio vacio) la variable turnos_ocupados_lunes suma uno y asi sucesivamente con los otros dias
        turnos_ocupados_lunes = 0
        if lunes_1 != "": turnos_ocupados_lunes += 1
        if lunes_2 != "": turnos_ocupados_lunes += 1
        if lunes_3 != "": turnos_ocupados_lunes += 1
        if lunes_4 != "": turnos_ocupados_lunes += 1
# asignamos a la variable turnos_ocupados_martes el valor de 0, si martes_1 es distinto de ""(espacio vacio) la variable turnos_ocupados_martes suma uno y asi sucesivamente con los otros dias
        turnos_ocupados_martes = 0
        if martes_1 != "": turnos_ocupados_martes += 1
        if martes_2 != "": turnos_ocupados_martes += 1
        if martes_3 != "": turnos_ocupados_martes += 1
# asignamos las variables turnos libres (lunes = 4), (martes=3) y le restamos la variable turnos ocupados 
        turnos_libre_lunes = 4 - turnos_ocupados_lunes
        turnos_libre_martes = 3 - turnos_ocupados_martes
# imprimimos los turnos libres y ocupados por dia usando las varibales turnos libres y turnos ocupados
        print("TURNOS LUNES")
        print(f"libres: {turnos_libre_lunes} ocupados: {turnos_ocupados_lunes}")
        print("TURNOS MARTES")
        print(f"libres: {turnos_libre_martes} ocupados: {turnos_ocupados_martes}")
# mostramos que dia tiene mas turnos 
        if turnos_ocupados_lunes > turnos_ocupados_martes:
             print("dia con mas turnos es: Lunes")
        elif turnos_ocupados_lunes < turnos_ocupados_martes:
             print("dia con mas turnos es: Martes")
# en caso que esten igualados mostramos que ambos tienen los mismo turnos
        else:
            print("tienen los mismo turnos ")

# ejercicio 4
# Historia
# Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados. Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás
# definimos las variables
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_cerradura = 0
# pedimos el nombre del agente y verificamos que solo ingrese letras 
print("ingrese nombre del agente")
nombre_agente = input("agente: ").strip().lower()
while not nombre_agente.isalpha():
    print("error: ingrese solo letras")
    nombre_agente = input("agente: ").strip().lower()


#creamos un ciclo que ande mientras energia sea mayor a cero, tiempo mayor a 0 y cerraduras abiertas menor a 3 
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
# en cada vuelta mostramos la energia, tiempo, cerraduras abiertas que va el agente y si la alarma esta activada 
# Mostramos la opciones del menu     
    print(f"""
          energia = {energia} 
          tiempo = {tiempo} 
          cerraduras abierta = {cerraduras_abiertas} 
          alarma = {alarma} """)
    print(f"""
          1) Forzar cerradura (costo: -20 energía, -2 tiempo)
          2) Hackear panel (costo: -10 energía, -3 tiempo)
          3) Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)""")
# definimos la variable opcion 
    opc = input("opcion: ").strip()
# y validamos que para continuar ingrese una opcion valida del menu
    while not opc.isdigit() or int(opc) < 1 or int(opc) > 3:
        print("Error: opcion invalida ingrese solo numeros entre los rangos solicitados")
        opc = input("opcion: ").strip()

    opc_int = int(opc)
# si la opcion es igual a 1, restamos la energia y el tiempo que corresponde
    if opc_int == 1:
        energia -=20
        tiempo -= 2
        forzar_cerradura += 1
# si energia es menor a 40 activamos un riesop de alarma
        if energia < 40:
            print("riesgo de alarma, elegir un numero (1-3)")
            riesgo = input("").strip()
#validamos que ingrese una opcion valida 
            while not riesgo.isdigit() and int(riesgo) != 1 or int(riesgo) !=3:
                print(" ingrese un numero pedido")
                print("riesgo de alarma, elegir un numero (1-3)")
                riesgo = input("").strip()
                riesgo_int = int(riesgo)
# si la opcion es igual a 3 activamos la alarma y le mostramos 
            if riesgo_int == 3:
                alarma = True
                print("activaste la alarma")
# si  ingresa 3 veces seguida a la opcion 1 del menu forzar cerradura, esta se traba y activa la alarma 
        if forzar_cerradura == 3 :
            alarma = True
            print("La cerradura se trabo, Alarma activada")
# si la alarma no se activa se desbloquea una cerradura 
        elif alarma == False:
            cerraduras_abiertas += 1
            print("abriste una cerradura")
# si opcion del menu es iugal a dos restamos energia y tiempo que corresponde
    elif opc_int == 2:
        energia -= 10
        tiempo -= 2
        forzar_cerradura = 0 #cortamos la racha
#creamos un ciclo donde en cada vuelta le pedimos al usuario que ingres 1 letras y validamos para que solo sea 1 
        for i in range(1,5):
            letra = input(f"{i}-ingrese solo 1 letra: ").strip().lower()
            while not letra.isalpha() or len(letra) != 1:
                print(" ingrese solo letra ")
                letra = input(f"{i}-ingrese solo 1 letra: ").strip().lower()
# la variable codigo_parcial suma una letra por cada vez que el usuario ingresa
# si el codigo_parcial  es igual o mayor a 8 abrimos una cerradura        
            codigo_parcial += letra
            print(f"codigo: {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("abriste una cerradura")
# si la opcion es igual a 3 restamos el tiempo que corresponde 
    elif opc_int == 3:
        tiempo -= 1
        forzar_cerradura = 0 #cortamos la racha
# en caso que tenga 85 o menos sumamos 15 de energia     
        if energia < 86:
            energia += 15
# si la alarme es igual a false restamos 10 de energia  
        if alarma == False:
            energia -= 10
# en caso que la alarma este activada y el tiempo sea igual o menor a 3 y no se abrieron las 3 cerraduras,mostramos derrota 
    if alarma == True and tiempo <= 3  and cerraduras_abiertas < 3:
        print("bloqueo por alarma")
        print("DERROTA")
        break
# en caso que las cerraduras_abiertas sean igual a 3, imprimimos "victoria" y si nos quedamos sin energia o sin tiempo mostramos "derrota"
if cerraduras_abiertas == 3:
    print("VICTORIA")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA")



#ejercicio 5
# definimos variables
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
daño_base = 15
daño_base_enemigo = 12

print(" --BIENVENIDO A LA ARENA--")
# pedimos el nombre del gladiador
nombre_gladiador = input("ingrese el nombre del gladiador: ").strip().lower() 
# verificamos que solo use letras
while not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras")
    nombre_gladiador = input("ingrese el nombre del gladiador: ").strip().lower()
# mostramos inicio de combate 
print(" ===INICIO DEL COMBATE===")
# mientras el jugador y el enemigo tengan vida continua el bulce
while vida_gladiador > 0 and vida_enemigo > 0 :
# mostramos el nombre del jugador y su hp, el enemigo y su hp, la cantidad de pociones disponibles 
    print(f"\n{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_vida}")
# mostramos las opciones del menu 
    print("1)- ataque pesado")
    print("2)- rafaga veloz")
    print("3)- curar")
# hacemos que el jugador seleccione una opcion 
    opcion_ = input("opcion: ").strip()
# verificamos que puso solo un numero y entre 1 y 3 
    while not opcion_.isdigit() or int(opcion_) < 1 or int(opcion_) > 3:
        print("error: ingrese un numero que este dentro del rango del menu")
        opcion_ = input("opcion: ").strip()
    opcion_int_ = int(opcion_)
# si es igual a 1 continua con el daño base 
    if opcion_int_ == 1:
# si el enemigo tiene menos de 20 hacemos un golpe critico        
        if vida_enemigo < 20 :
            daño = daño_base* 1.5
            print("GOLPE CRITICO")
            print(f" ¡atacaste al enemigo por {daño} puntos de daño!")
            vida_enemigo -= daño
# si el enemigo tiene 20 o mas la vida del enemigo resta en la vida del enemigo lo que baja el daño base           
        else:
            vida_enemigo -= daño_base
            print("¡atacaste al enemigo por 15 puntos de daño!")
           
# si la opcion elegida es igual a 2, hacemos una rafa de 3 golpes que cada golpe quite 5 de vida enemiga 
    elif opcion_int_ == 2:
        for i in range(1,4):
            vida_enemigo -=5
            print("> Golpe conectado por 5 de daño")
# si la opcion es igual a 3 y las pociones son mayor a 0 restamos una pocion y curamos 30 de vida    
    elif opcion_int_ == 3:
        if pociones_vida > 0:
            pociones_vida -=1
            vida_gladiador +=30
# en caso que no haya pociones le decimos y perdemos el turno           
        else:
            print("¡No quedan pociones!")
# si el enemigo tiene mas de 0 de vida ataca con un daño base 
    if vida_enemigo > 0:
        print("¡El enemigo te atacó por 12 puntos de daño!")
        vida_gladiador -= daño_base_enemigo        
        
# si la vida del enemigo es menor o igual a cero mostramos victoria para el jugador     
if vida_enemigo <= 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
# si la vida del jugador es menor o igual a 0 mostramos derrota para el jugador.
if vida_gladiador <= 0:
    print("DERROTA. Has caído en combate.")

         
        




