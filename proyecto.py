import numpy as np

class persona(object):
    def __init__(self):
        pass

class contexto(persona):
    # nombre
    # sentimiento
    # horas de sueño noche anterior
    # comida
    # vasos de agua
    # metas del día
    # actividad física
    # recreación
    def __init__(self, nombre, sentimiento, hobbie):
        super().__init__()
        self.nombre = nombre # name of the person
        self.sentimiento = sentimiento
        self.sueño = 0
        self.comida = 0
        self.agua = 0
        self.metas = 0
        self.fisica = 0
        self.recreacion = 0
        self.hobbie = hobbie

    def Sueño(sueño):
        # int = horas de sueño
        # si sueño <= 8, recomendar cuidar hábitos de sueño
        # si sueño <= 6, recomendar tomar una siesta
        self.sueño = sueño
    
    def Comida(comida):
        # bool = has comido bien hoy?
        # si es False, recomendar comer
        self.comida = comida

    def Agua(agua):
        # bool = has tomado suficiente agua hoy?
        # si es False, recomendar tomar agua
        self.agua = agua

    def Metas(metas):
        # bool = vas al día con tus metas de trabajo?
        # si es False, recomendar tomarse un momento para re-organizar el día
        self.metas = metas

    def Fisica(fisica):
        # bool = has hecho actividad física hoy?
        # si es False, recomendar salir a caminar
        self.fisica = fisica

    def Hobbie(hobbie):
        # input hobbie
        # qué te gusta hacer en tu tiempo libre?
        self.hobbie = hobbie

    def Recreacion(recreacion):
        # bool = has tenido recreación hoy?
        # si es False, hacer segunda pregunta
        # bool = tienes planificado un tiempo de recreación hoy?
        # si es False, recomendar hacer hobbie
        self.recreacion = recreacion


def inputs():
    '''runs the code to display the interacticve 
       messages and create the card'''
    nombre = input('¿Cómo te llamas?')
    sentimiento = input('¿Cómo te sientes hoy? (feliz, triste, cansad@, enojad@, tranquil@, ansios@) ')
    hobbie = input('¿Qué te gusta hacer en tu tiempo libre?')
    persona = contexto(nombre, sentimiento, hobbie)

    print('Responde la siguiente pregunta con un número entero')

    f_sueño = input('¿Cuántas horas dormiste anoche aproximadamente?')

    persona.horas_sueño = f_sueño

    f_comida = input('¿Has comido bien hoy? (si, no)')
    persona.ha_comido = f_comida

    f_agua = input('¿Has tomado suficiente agua hoy? (si, no)')
    persona.toma_agua = f_agua

    f_fisica = input('¿Has hecho actividad física hoy? (si, no)')
    persona.act_fisica = f_fisica

    f_recreacion = input('¿Has hecho alguna actividad recreativa hoy? (si, no)')
    persona.act_fisica = f_fisica
  
inputs()

