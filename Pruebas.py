import json
from Funciones import*

aulas=("1.Apolo", "2.Sputnik","3.Artemis","4.salir")
horario=("1. 06am-10am", "2. 10am-02pm", "3. 02pm-6pm", "4. 06pm-10pm")
desicion=("1. Si", "2. No")
modificar=("1.Instructor","2.Cambiar Fechas", "3.Salir")
estados=("1.Graduado", "2.Expulsado", "3.Retirado")


def Evaluar_Riesgo():
    Notas=cargar_datos("Camper.json","d") 
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



camper_evaluado = Evaluar_Riesgo()  



    # 
    # if llave != seleccion: