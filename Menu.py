from Funciones import*

quien=("1.Coordinador", "2.Trainer", "3.Camper", "4.Salir")
menu_coordinador=("1.Crear Ruta", "2.Modificar Estado de Camper", "3.Asignar Cursos", "4.Camper en Riesgo", "5.Asignar Camper Curso", "6.Aprobar Camper", "7.Inscritos", "8.Salir")
Menu_Trainer=("1.Registrarse", "2.Asignar Notas", "3.Salir")

def Menu_Principal():
    while True:    
        try:
            print("************************************************")
            print("      Bienvenido a la Plataforma Campus")
            print("************************************************")
            print("¿Quien es usted en Campus?")
            for i in quien:
                print(i)
            opc=int(input("--> "))
            if opc == 4:
                print("Saliendo....")
                print("*************************************************")
            elif opc==1:
                print(" *-* BIENVENIDO COORDINADOR *-* ")
                print("¿Que desea hacer hoy?")
                for i in menu_coordinador:
                    print(i)
                opc1=int(input("--> "))
                if opc1== 8:
                    print("Saliendo....")
                    print("************************************************")
                    return
                elif opc1 ==1:
                    Crear_Ruta()
                elif opc1==2:
                    Cambiar_Estado()
                elif opc1==3:
                    Registro_Cursos()
                elif opc1==4:
                    camper_evaluado = Evaluar_Riesgo() 
                elif opc1==5:
                    Asignar_Camper_Curso()
                elif opc1==6:
                    Aprobar_Camper()
                elif opc1==7:
                    Mostrar_Inscritos()
                else:
                    print("ERROR de digitacion")
                    print("************************************************")
                    continue
            elif opc==2:
                print("**BIENVENIDO TRAINER**")
                print("¿Que desea hacer hoy?")
                for i in Menu_Trainer:
                    print(i)
                opc2=int(input("Escoja la opcion: --> "))
                if opc2==3:
                    print("Saliendo....")
                    print("************************************************")
                    return
                elif opc2==1:
                    Registrar_profesor()
                elif opc2==2:
                    Registrar_notas()
                else:
                    print("ERROR de digitacion")
                    print("************************************************")
                    continue
            elif opc==3:
                print("**BIENVENIDO CAMPER**")
                print("Vamos a Registrarnos")
                Registrar_Campers() 
                continue
            else:
                print("ERROR de digitacion")
                print("************************************************")
                continue
        except ValueError:
            print("Por favor, ingrese información válida.")
            print("**************************************************") 
            continue    


# Menu_Principal()
