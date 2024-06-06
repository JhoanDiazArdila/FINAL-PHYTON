

import json
from  Dicionarios import * 

aulas=("1.Apolo", "2.Sputnik","3.Artemis","4.salir")
horario=("1. 6am-10am", "2. 10am-2pm", "3. 2pm-6pm", "4. 6pm-10pm")
desicion=("1. Si", "2. No")
modificar=("1.Instructor","2.Cambiar Fechas", "3.Salir")
estados=("1.Graduado", "2.Expulsado", "3.Retirado")

def cargar_datos(Archivo,Tipo):
    global Diccionario
    try:
        with open(Archivo, "r") as file:
            Diccionario = json.load(file)
        print(Archivo, "huyó de la nube y aterrizo aqui.")
    except FileNotFoundError:
        if Tipo=="d":
            Diccionario = {}
        else:
            if Tipo=="l":
                Diccionario = []


def guardar_datos(Diccionario,Archivo):
    try:
        contenido = json.dumps(Diccionario, indent=4)
        with open(Archivo, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")


def cargar_dato(Archivo, Tipo):
    try:
        with open(Archivo, "r") as file:
            data = json.load(file)
        print(f"Datos cargados de {Archivo}")
    except FileNotFoundError:
        if Tipo == "d":
            data = {}
        elif Tipo == "l":
            data = []
    return data


def guardar_dato(data, Archivo):
    try:
        with open(Archivo, "w") as file:
            json.dump(data, file, indent=4)
        print("Datos guardados exitosamente!!")
    except Exception as e:
        print(f"Error al guardar datos: {e}")



def seleccion_Aula ():
    while True:
        try: 
            print("**************************************************")
            print("Estas son las Aulas disponibles")
            for i in aulas:
                print(i)
            opc=int(input("Cual salon desea asignar? --> "))
            if opc==4:
                print("Saliendo...")
                print("**************************************************")
                return
            elif opc ==1:
                salon= "Apolo"
            elif opc==2:    
                salon= "Sputnik"
            elif opc==3:    
                salon= "Artemis"
            else:
                print("Opcion no Valida \nIntente Nuevamente")
                print("**************************************************")
                continue  
            print("**************************************************")    
            print("Estas son los horarios del aula")
            hora=""
            for i in horario:
                print(i)
            opc1=int(input("Que horario desea verificar -> "))
            print("**************************************************") 
            if opc1 ==1:
                hora= "6am-10am"
            elif opc1==2:    
                hora= "10am-2pm"
            elif opc1==3:    
                hora= "2pm-6pm"
            elif opc1==4:   
                hora= "6pm-10pm"
            else:
                print("Opcion no Valida \nIntente Nuevamente")
                print("**************************************************")
                continue
            seleccion=salon+hora  
            print("Este es el nombre del curso --> ",seleccion)
            return seleccion
        except ValueError:
                print("Por favor, ingrese información válida.")
                print("**************************************************") 
                continue




def Registrar_Campers():
    while True:
        try:
            print("**************************************************")
            cargar_datos("Camper.json","d")
            Camper=Diccionario
            cargar_datos("Trainer.json","d")
            print("**************************************************")
            Trainer=Diccionario
            Campers = {}
            print("Vamos a empezar con el regustro!")
            doc = input("Ingrese el documento: ")
            if Camper.get(doc, None) == None and Trainer.get(doc, None) == None:
                Campers["Nombre"] = input("Ingrese los Nombres -> ")
                Campers["Apellido"]= input("Ingrese los Apellidos -> ")
                Campers["Telefono"] = int(input("Ingrese su telefono -> "))
                Campers["Direccion"] = input("Ingrese su direccion -> ")
                Campers["Jornada"] = input("Jornada- Diurna o Tarde ->")
                Campers["Estado"] = "En proceso"
                print("**************************************************")
                print(doc,Campers)
                print("¿Es la informacion correcta?")
                for a in desicion:
                    print(a)  
                opc2=int(input("--> "))
                if opc2==1:
                    Campers["Estado"] = "Inscrito"
                    Campers["Ruta"] = None
                    Campers["Modulo"] ={}
                    Campers["Riesgo"] = False
                    Camper[doc]=Campers
                    guardar_datos(Camper,"Camper.json")
                    print("Camper agregado con Exito")
                    print("Adios")
                    print("**************************************************")
                    break
                elif opc2==2:
                    continue
            else:
                    print("Documento ya fue registrado")  
                    print("Adios")
                    print("**************************************************")
                    break
        except ValueError:
            print("Por favor, ingrese información válida.")
            print("**************************************************") 
            continue




def Cambiar_Estado():
    while True:
        cargar_datos("Camper.json","d")
        Camper=Diccionario
        print("**************************************************")
        print("Va a modificar el Estado de un camper. \n Escriba el documento del camper")
        try:
            doc=input("--> ")
        except ValueError:
            print("Por favor, ingrese información válida.")
            print("**************************************************") 
            continue
        print(doc,", ",Camper[doc]["Nombre"],", ","Estado",Camper[doc]["Estado"])
        print("**************************************************")
        if doc in Camper:
            print("Escoja el estado para asignar al Camper")
            print("Estados Disponibles:")
            for i in estados:
                print(i)
            try:
                opc=int(input("--> "))
            except ValueError:
                print("Por favor, ingrese información válida.")
                print("**************************************************") 
                continue
            if opc==1:
                Camper[doc]["Estado"]="Graduado"
                print(doc,",",Camper[doc]["Nombre"],",","Estado",Camper[doc]["Estado"])
                print("¿Es la informacion correcta?")
                for a in desicion:
                    print(a)
                try:    
                    opc2=int(input("--> "))
                except ValueError:
                    print("Por favor, ingrese información válida.")
                    print("**************************************************") 
                    continue
                if opc2==1:
                    guardar_datos(Camper,"Camper.json")
                    print("Estado de Camper modificado con Exito")
                    print("Adios")
                    print("**************************************************")
                    break
                elif opc2==2:
                    continue
            elif opc==2:        
                Camper[doc]["Estado"]="Expulsado"
                print(doc,",",Camper[doc]["Nombre"],",","Estado",Camper[doc]["Estado"])
                print("¿Es la informacion correcta?")
                for a in desicion:
                    print(a)
                try:    
                    opc2=int(input("--> "))
                except ValueError:
                    print("Por favor, ingrese información válida.")
                    print("**************************************************") 
                    continue
                if opc2==1:
                    guardar_datos(Camper,"Camper.json")
                    print("Estado de Camper modificado con Exito y Fue Expulsado a patadas")
                    print("Adios")
                    print("**************************************************")
                    break
                elif opc2==2:
                    continue
            elif opc==3:
                Camper[doc]["Estado"]="Retirado"
                print(doc,",",Camper[doc]["Nombre"],",","Estado",Camper[doc]["Estado"])
                print("¿Es la informacion correcta?")
                for a in desicion:
                    print(a)
                try:    
                    opc2=int(input("--> "))
                except ValueError:
                    print("Por favor, ingrese información válida.")
                    print("**************************************************") 
                    continue
                if opc2==1:
                    guardar_datos(Camper,"Camper.json")
                    print("Estado de Camper modificado con Exito")
                    print("Adios")
                    print("**************************************************")
                    break
                elif opc2==2:
                    continue
            else:
                print("Opcion no valida \n Vuelve a leer")
                continue
        else:
            print("Camper no registrado")
            continue




def Aprobar_Camper():
    while True:
        cargar_datos("Camper.json","d")
        Camper=Diccionario
        print("**************************************************")
        print("¿Desea registrar las notas de un Camper Inscrito?")
        for i in desicion:
            print(i)
        try:
            opc=int(input("--> "))
        except ValueError:
            print("Por favor, ingrese información válida.")
            print("**************************************************") 
            continue
        if opc==2:
            print("Saliendo....")
            print("**************************************************")
            return
        elif opc==1:       
            try:
                doc=str(input("Ingrese el numero del documento:  "))
            except ValueError:
                print("Por favor, ingrese información válida.")
                print("**************************************************") 
                continue
            if doc in Camper:
                if Camper[doc]["Estado"]=="Aprobado":
                    print("Camper ya fue aprobado")
                    print("Ingrese otro documento")
                    print("**************************************************")
                    break
                else:
                    try:
                        valorT=int(input("Ingrese la nota del examen teorico de admision del Camper (0-100) -->  "))
                    except ValueError:
                        print("Por favor, ingrese información válida.")
                        print("**************************************************") 
                        continue
                    try:
                        valorP=int(input("Ingrese la nota del examen practico de admision del Camper (0-100) --> "))
                    except ValueError:
                        print("Por favor, ingrese información válida.")
                        print("**************************************************") 
                        continue
                    nota_promedio = (valorT + valorP)/2
                    if nota_promedio>=60:
                        Camper[doc]["Estado"]="Aprobado"
                        guardar_datos(Camper,"Camper.json")
                        print("Camper Aprobado con Exito")
                        print("**************************************************")
                        continue
                    else:
                        print("Camper Inscrito No Aprobado")
                        print("Adios")
                        print("**************************************************")
            else:
                print("Registro aun no realizado en Campus")
                print("Por favor, ingrese información válida.")
                print("**************************************************")
                continue
        else:
            print("Opcion no valida, Intente Nuevamente")
            print("**************************************************")
            continue




def Registrar_profesor():
    while True:
        print("**************************************************")
        cargar_datos("Trainer.json","d")
        Trainer=Diccionario
        cargar_datos("Camper.json","d")
        Camper=Diccionario 
        print("**************************************************")
        Intructor = {}
        try:
            print("Un gusto tenerlo en Campus \n Aqui podra ingresar sus datos para el sistema. \n Nuevamente un placer que trabaje con nosotros.")
            doc = str(input("Ingrese el documento: "))
            if Trainer.get(doc, None) == None and Camper.get(doc, None) == None:
                Intructor["Nombre"] = input("Ingrese los Nombres: ")
                Intructor["Apellido"]= input("Ingrese los Apellidos: ")
                Intructor["Telefono"] = int(input("Ingrese su telefono: "))
                Intructor["Direccion"] = input("Ingrese su direccion: ")
                print("**************************************************")            
                print(doc,Intructor)
                print("¿Es la informacion correcta?")
                for a in desicion:
                    print(a)
                opc2=int(input("--> "))   
                if opc2==1:
                    Trainer[doc]=Intructor
                    guardar_datos(Trainer,"Trainer.json")
                    print("Instructor agregado con Exito")
                    print("Adios")
                    print("**************************************************")
                    break
                elif opc2==2:
                    print("Vuelva a empezar")
                    continue
                else:
                    print("Opcion no valida `\n Si no sabe leer no creo que enseñar")
                    continue
            else:
                print("Documento ya fue registrado")
                print("Adios")  
                print("**************************************************")
                continue
        except ValueError:
            print("Por favor, ingrese información válida.")
            print("**************************************************") 
            continue        




def Registro_Cursos():
    while True:
        Aulas = cargar_dato("Aulas.json", "d")
        Trainer = cargar_dato("Trainer.json", "d")
        Materias = cargar_dato("Rutas_Modulos.json", "d")
        print("**************************************************")
        print("Estas son las Aulas disponibles")
        try:
            for i in aulas:
                print(i)
            opc=int(input("Cual salon desea asignar? --> "))
            if opc==4:
                print("Saliendo...")
                print("**************************************************")
                return
            elif opc ==1:
                salon= "Apolo"
            elif opc==2:    
                salon= "Sputnik"
            elif opc==3:    
                salon= "Artemis"
            else:
                print("Opcion no Valida \nIntente Nuevamente")
                print("**************************************************")
                continue  
            print("**************************************************")    
            print("Estas son los horarios del aula")
            hora=""
            for i in horario:
                print(i)
            opc1=int(input("Que horario desea verificar -> "))
            print("**************************************************") 
            if opc1 ==1:
                hora= "6am-10am"
            elif opc1==2:    
                hora= "10am-2pm"
            elif opc1==3:    
                hora= "2pm-06pm"
            elif opc1==4:   
                hora= "6pm-10pm"
            else:
                print("Opcion no Valida \nIntente Nuevamente")
                print("**************************************************")
                continue
            seleccion=salon+hora  
            print("Este es el nombre del curso --> ",seleccion)
            if seleccion in Aulas["Aulas"]:
                informacion_aula=Aulas["Aulas"][seleccion]
                for i in informacion_aula.items():
                    print(i)   
                print("**************************************************")
                print("¿Desea modificar toda la informacion?")
                for a in desicion:
                    print(a)
                opc2=int(input("--> "))
                print("**************************************************")
                if opc2== 1:
                    Aula={}
                    lista={}
                    doc= input("Ingrese el ID del trainer: ") 
                    for llave, valor in Aulas["Aulas"].items():
                        if valor["Trainer ID"] == doc and valor["Horario"] == hora and llave != informacion_aula:
                            print("El Trainer ya está asignado en otra Aula en la misma hora.")
                            print("Intentelo Nuevamente")
                            print("**************************************************")
                            break
                        else:
                            if doc in Trainer:
                                print("**************************************************")
                                Aula["Trainer ID"] = doc
                                Aula["Nombre"] = Trainer[doc]["Nombre"]
                                print("Ahora debemos asignar la Ruta. \n Para esta vamos a asignar los modulos de preferencia a la Ruta. \n Estas son las rutas creadas hasta el momento")
                                print("**************************************************")
                                print(Materias["Rutas"])
                                print("**************************************************")
                                ruta = str(input("Escriba la Ruta a la cual se le asignaran los Modulos. \n -->"))
                                print("**************************************************")
                                print("Estos son los modulos que se pueden agregar a la lista")
                                for llave, valor in Materias["Modulos"].items():
                                    print(llave,valor)
                                print("**************************************************")
                                cantidad=int(input("¿Cuantos modulos va agregar? \n -->"))
                                for i in range(0,cantidad):
                                    modulo=str(input("Escriba el modulo para agregar a la ruta \n --> "))
                                    lista.update({modulo:None})
                                print("Estos son los modulos ",lista, " de la Ruta", ruta)
                                Aula["Ruta"]= {ruta:lista}
                                Aula["Aula"] = salon            #Este es el diccionario en Json
                                Aula["Horario"] = hora          #Como que cambios debo hacer en este codigo para que guarde la informacion de esta manera
                                Aula["Cantidad de campers"] = 0
                                Aula["Camper"] = {}
                                print (Aula)
                                print("Ingrese la Fecha de Inicio con dia/mes/año *Ejemplo 06/06/2024")
                                Aula["Fecha Inicio"] = str(input("--> "))
                                print("Ingrese la Fecha de Finalizacion con dia/mes/año *Ejemplo 30/01/2025")
                                Aula["Fecha Finalizacion"] = str(input("-->"))
                                print(Aula)
                                print("¿Es la informacion correcta?")
                                for a in desicion:
                                    print(a)
                                opc2=int(input("--> "))
                                if opc2==1:
                                    Aulas["Aulas"][seleccion].update(Aula)
                                    guardar_datos(Aulas,"Aulas.json")
                                    print("Datos asignados al Aula con Exito!")
                                    print("Adios")
                                    print("**************************************************")
                                    break
                                elif opc2==2:
                                    print("Vuelva a empezar")
                                    print("**************************************************")
                                    continue
                                else:
                                    print("Opcion no Valida \n Intente Nuevamente")
                                    print("**************************************************")
                                    continue
                            else:    
                                print("Instructor no registrado")
                                print("Intentelo Nuevamente")
                                print("**************************************************") 
                                continue
                elif opc2==2:
                    print("Que informacion desea modificar")
                    for i in modificar:
                        print(i)
                    try:
                        opc1=int(input("----> "))
                    except ValueError:
                        print("Por favor, ingrese información válida.")
                        print("**************************************************") 
                        continue    
                    if opc1==3:
                        print("Saliendo...")
                        print("Adios")
                        print("**************************************************")
                        continue    
                    elif opc1==1:
                        Aula={}
                        try:
                            doc= str(input("Ingrese el ID del trainer para asignar: "))
                        except ValueError:
                            print("Por favor, ingrese información válida.")
                            print("**************************************************") 
                            continue
                        for llave, valor in Aulas.items():
                            if llave != seleccion and valor.get("Trainer ID") == doc and valor["Horario"] == hora :
                                print("El Trainer ya está asignado en otra Aula en la misma hora.")
                                print("Intentelo Nuevamente")
                                print("**************************************************")
                        else:
                            if Trainer.get(doc, None) != None:
                                Aula["Trainer ID"] = doc
                                Aula["Nombre"] = Trainer[doc]["Nombre"]
                                Aula["Aula"] = salon
                                Aula["Horario"] = hora
                                Aula["Cantidad de campers"] = Aulas["Aulas"][seleccion]["Cantidad de campers"]
                                Aula["Fecha Inicio"] = Aulas["Aulas"][seleccion]["Fecha Inicio"]
                                Aula["Fecha Finalizacion"] = Aulas["Aulas"][seleccion]["Fecha Finalizacion"]
                                print(Aula)
                                print("¿Es la informacion correcta?")
                                for a in desicion:
                                    print(a)
                                try:
                                    opc2=int(input("--> "))
                                except ValueError:
                                    print("Por favor, ingrese información válida.")
                                    print("**************************************************") 
                                    continue
                                if opc2==1:
                                    Aulas["Aulas"][seleccion].update(Aula)
                                    guardar_datos(Aulas,"Aulas.json")
                                    print("Trainer asignado al Aula con Exito")
                                    print("Adios")
                                    print("**************************************************")
                                    break
                                elif opc2==2:
                                    print("Vuelva a empezar")
                                    continue
                                else:
                                    print("Opcion no Valida \nIntente Nuevamente")
                                    print("**************************************************")
                                    continue
                            else:    
                                print("Instructor no registrado")
                                print("Intentelo Nuevamente")
                                print("**************************************************")   
                    elif opc1==2:
                        Aula={}
                        Aula["Trainer ID"] = Aulas["Aulas"][seleccion]["Trainer ID"]
                        Aula["Nombre"] = Aulas["Aulas"][seleccion]["Nombre"]
                        Aula["Ruta"] = Aulas["Aulas"][seleccion]["Ruta"]
                        Aula["Aula"] = salon
                        Aula["Horario"] = hora
                        Aula["Cantidad de campers"] = Aulas[seleccion]["Cantidad de campers"]
                        try:
                            print("Ingrese la Fecha de Inicio con dia/mes/año *Ejemplo 06/06/2024")
                            Aula["Fecha Inicio"] = str(input("--> "))
                        except ValueError:
                            print("Por favor, ingrese información válida.")
                            print("**************************************************") 
                            continue
                        try:
                            print("Ingrese la Fecha de Finalizacion con dia/mes/año *Ejemplo 30/01/2025")
                            Aula["Fecha Finalizacion"] = str(input("-->"))
                        except ValueError:
                            print("Por favor, ingrese información válida.")
                            print("**************************************************") 
                            continue
                        print(Aula)
                        print("¿Es la informacion correcta?")
                        for a in desicion:
                            print(a)
                        try:
                            opc2=int(input("--> "))
                        except ValueError:
                            print("Por favor, ingrese información válida.")
                            print("**************************************************") 
                            continue
                        if opc2==1:
                            Aulas["Aulas"][seleccion].update(Aula)
                            guardar_datos(Aulas,"Aulas.json")
                            print("Fechas asignadas con Exito")
                            print("Adios")
                            print("**************************************************")
                            break
                        elif opc2==2:
                            print("Vuelva a empezar")
                            continue
                        else:
                            print("Opcion no Valida \nIntente Nuevamente")
                            print("**************************************************")
                            continue
                    else:
                        print("Opcion no Valida \nIntente Nuevamente")
                        print("**************************************************")
                        continue
                else:
                    print("Opcion no Valida \nIntente Nuevamente")
                    print("**************************************************")
                    continue                      
            else:
                print("Hubo error")
        except ValueError:
            print("Por favor, ingrese información válida.")
            print("**************************************************") 
            continue        





def Evaluar_Riesgo():
    cargar_datos("Camper.json","d")
    Notas=Diccionario 
    camper_evaluado = {}
    for camper, cursos in Notas.items():
        bajo_rendimiento = []
        for curso, modulos in cursos["Modulo"].items():
            for modulo, calificaion in modulos.items():
                if calificaion < 60:
                    bajo_rendimiento.append(modulo)
        if bajo_rendimiento:
            camper_evaluado[camper] = bajo_rendimiento
    if camper_evaluado:
        print("**************************************************")
        print("Campers con alto riesgo:")
        for camper, modulos in camper_evaluado.items():
            print(f"{camper}: Módulos con bajo rendimiento: {', '.join(modulos)}")
            print("**************************************************")
    else:
        print("No hay Campers con alto riesgo")
        print("Adios")
        print("**************************************************")
    return camper_evaluado

Evaluar_Riesgo()


def Registrar_notas():
    while True:
        cargar_datos("Camper.json","d")
        Camper=Diccionario
        cargar_datos("Aulas.json","d")
        Aulas=Diccionario
        cargar_datos("Trainer.json","d")
        Trainer=Diccionario
        doc_trainer=input("Trainer, ¿Cual es su ID?")
        if doc_trainer in Trainer:
            print("Ingrese el ID del Camper para asignar las notas")
            doc_camper=int(input("--->  "))
            if doc_camper in Camper and Camper[doc_camper]["Estado"]=="Cursando":
                Not={}
                for llave, valor in Camper[doc_camper].items():
                    print(llave, valor)
                    

        for llave, valor in Camper.items():
            print(llave, valor)
        print("**************************************************")
        print("Ingrese el ID del Camper para asignar las notas")
        try:
            doc=int(input("--->  "))
        except ValueError:
            print("Por favor, ingrese información válida.")
            print("**************************************************") 
            continue
        if doc in Camper and Camper[doc]["Estado"]=="Cursando":
            for llave, valor in Aulas.items():
                if doc in valor.get("Camper", {}):
                    ruta = valor.get("Ruta")
                    nombre = Camper[doc]["Nombre"]
                    nota_teoria = float(input("Ingrese la nota de la prueba teórica: --> "))
                    nota_practica = float(input("Ingrese la nota de la prueba práctica: --> "))
                    nota_quiz = float(input("Ingrese la nota del quiz: -->"))
                    nota_trabajo = float(input("Ingrese la nota del trabajo: --> "))
                    nota_final = (nota_teoria * 0.3) + (nota_practica * 0.6) + (nota_quiz * 0.1) + (nota_trabajo * 0.1)
                    evaluacion = {
                        "nombre": nombre,
                        "evaluaciones": [
                            {"tipo": "teorica", "nota": nota_teoria},
                            {"tipo": "practica", "nota": nota_practica},
                            {"tipo": "quiz", "nota": nota_quiz},
                            {"tipo": "trabajo", "nota": nota_trabajo}
                        ],
                        "nota_final": nota_final
                    }
                    if doc in Notas:
                        Notas[doc]["evaluaciones"].append(evaluacion)
                    else:
                        Notas[doc] = {"evaluaciones": [evaluacion]}
                    guardar_datos("Nota.json", Notas, "w")
                    print("Evaluación ingresada exitosamente.")
                    break
            else:
                print("El camper no está asignado a ninguna ruta.")
        else:
            print("El ID del camper no existe o no está en estado cursando.")
        print("**************************************************")




def Asignar_Camper_Curso():
    while True:
        print("**************************************************")
        cargar_datos("Camper.json","d")
        Campers=Diccionario
        cargar_datos("Aulas.json","d")
        Aulas=Diccionario
        print("**************************************************")
        print("Vamos asignar un Camper a un Aula y sus modulos estaran ligados")
        print("Estas son las aulas para asignacion" )
        for i in aulas:
            print(i)
        try:
            opc=int(input("Cual salon desea asignar? --> "))
        except ValueError:
            print("Ingrese una Opcion válida.")
            print("**************************************************") 
            continue
        if opc==4:
            print("Saliendo...")
            print("**************************************************")
            return
        elif opc ==1:
            salon= "Apolo"
        elif opc==2:    
            salon= "Sputnik"
        elif opc==3:    
            salon= "Artemis"
        else:
            print("Opcion no Valida \nIntente Nuevamente")
            print("**************************************************")
            continue  
        print("**************************************************")    
        print("Estas son los horarios del aula")
        hora=""
        for i in horario:
            print(i)
        try:
            opc1=int(input("Que horario desea verificar -> "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            print("**************************************************") 
            continue
        print("**************************************************") 
        if opc1 ==1:
            hora= "6am-10am"
        elif opc1==2:    
            hora= "10am-2pm"
        elif opc1==3:    
            hora= "2pm-6pm"
        elif opc1==4:   
            hora= "6pm-10pm"
        else:
            print("Opcion no Valida \nIntente Nuevamente")
            print("**************************************************")
            continue
        seleccion=salon+hora
        print("Este es el nombre del curso --> ",seleccion)
        if seleccion in Aulas["Aulas"]:
            if seleccion in Aulas["Aulas"]:
                informacion_aula=Aulas["Aulas"][seleccion]
                for i in informacion_aula.items():
                    print(i)   
                print("**************************************************")
                print("¿Desea asignar un Camper a esta Aula?")
                for a in desicion:
                    print(a)
                try:
                    opc2=int(input("--> "))
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    print("**************************************************") 
                    continue
                print("**************************************************")
                if opc2== 1:
                    Camper={}
                    cantidad={}
                    try:
                        doc= input("Ingrese el ID del Camper: ")
                    except ValueError:
                        print("Por favor, ingrese información válida.")
                        print("**************************************************") 
                        continue    
                    if doc in Campers and Campers[doc]["Estado"] == "Aprobado":
                        if Aulas["Aulas"][seleccion]["Cantidad de campers"] <= 33:
                            Camper[doc]= Campers[doc]["Nombre"]
                            Aulas["Aulas"][seleccion]["Cantidad de campers"] += 1
                            Aulas["Aulas"][seleccion]["Camper"][doc]= Campers[doc]["Nombre"]
                            print(Camper)
                            guardar_datos(Aulas,"Aulas.json") 
                            Campers[doc]["Estado"]="Cursando"
                            guardar_datos(Campers,"Camper.json") 
                            print("Camper asignado con exito!")
                            print("Adios")
                            print("**************************************************")
                            continue
                        else:
                            print("Documento no puede ser asignado")
                            print("Vuelva a Intentar")
                            print("**************************************************")
                            continue
                    else:
                        print("Vuelva a empezar el proceso") 
                        print("Ya fue asignado a un Aula")
                        print("**************************************************")       
                        continue

#Asignar_Camper_Curso() Completado


def Mostrar_Inscritos():
    cargar_datos("Camper.json","d")
    Camper=Diccionario
    print("**************************************************")
    print("Los Campers que estan inscritos y no se han aprobado son")
    for llave, valor in Camper.items():
        if valor["Estado"] == "Inscrito":
            print(llave, valor)
            print("Que tenga buen dia")
            return

def Crear_Ruta():
    while True:
        print("**************************************************")
        cargar_datos("Rutas_Modulos.json","d")
        Rutas=Diccionario 
        print("**************************************************")
        print("Va a crear una Ruta para Campus y puede asignarla a las Aulas")
        print("**************************************************")
        print("**************************************************")
        print("Rutas creadas hasta el momento...")
        for ruta in Rutas.get("Rutas", []):
            print(ruta)
        rut=input("Ingrese el nombre de la Ruta para añadir: --> ")
        if "Rutas" not in Rutas:
            Rutas["Rutas"] = []
        if rut not in Rutas["Rutas"]:
            Rutas["Rutas"].append(rut)
            guardar_datos(Rutas,"Rutas_Modulos.json")
            print("Ruta Guardada con Exito!!!")
            print("**************************************************")
            print("**************************************************")
            break
        else:
            print("Ruta ya existe")
            continue


#Crear_Ruta()   
#Registrar_Campers()       
#Aprobar_Camper()   
#Registrar_profesor() 
#camper_evaluado = Evaluar_Riesgo()   
#Registro_Cursos()   
#Cambiar_Estado()
#Registrar_notas()
#Mostrar_Inscritos()



