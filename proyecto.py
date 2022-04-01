import numpy as np
import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors as mcolors
import os

class persona(object):
    def __init__(self):
        pass

class contexto(persona):
    def __init__(self, nombre, sentimiento, hobbie, color):
        super().__init__()
        self.nombre = nombre
        self.sentimiento = sentimiento
        self.hobbie = hobbie
        self.color = color
        self.sueño = -1.0  # horas de sueño noche anterior
        self.comida = 0
        self.agua = 0
        self.metas = 0  # metas del día
        self.fisica = 0  # actividad física
        self.recreacion = 0

    def Sueño(self, sueño):
        # int = horas de sueño
        # si sueño < 8, recomendar cuidar hábitos de sueño
        # si sueño < 6, recomendar tomar una siesta
        self.sueño = sueño
    
    def Comida(self, comida):
        # bool = has comido bien hoy?
        # si es False, recomendar comer
        self.comida = comida

    def Agua(self, agua):
        # bool = has tomado suficiente agua hoy?
        # si es False, recomendar tomar agua
        self.agua = agua

    def Metas(self, metas):
        # bool = vas al día con tus metas de trabajo?
        # si es False, recomendar tomarse un momento para re-organizar el día
        self.metas = metas

    def Fisica(self, fisica):
        # bool = has hecho actividad física hoy?
        # si es False, recomendar salir a caminar
        self.fisica = fisica

    def Recreacion(self, recreacion):
        # bool = has tenido recreación hoy?
        # si es False, hacer segunda pregunta
        # bool = tienes planificado un tiempo de recreación hoy?
        # si es False, recomendar hacer hobbie
        self.recreacion = recreacion

    def recomendacion(self):
        # si sueño < 8, recomendar cuidar hábitos de sueño
        # si sueño < 6, recomendar tomar una siesta

        recomendacion = ' '

        rec_sueño = str()
        if np.float64(self.sueño) < 8 and np.float64(self.sueño) > 0:
            assert type(self.sueño) == str
            rec_sueño = 'Considera cuidar tus hábitos de sueño \n'

        rec_comida = str()
        if self.comida == 'no':
            assert type(self.comida) == str
            rec_comida = 'Ve a comer algo rico para reponerte y continuar el día \n'

        rec_agua = str()
        if self.agua == 'no':
            rec_agua = str()
            rec_agua = 'Toma agüita (de uwu) para que estés hidratade \n'

        rec_metas = str()
        if self.metas == 'no':
            assert type(self.metas) == str
            rec_metas = 'Tómate un rato para reorganizar tu día, \nfija sólo una meta que quieras lograr hoy \n'

        rec_fisica = str()
        if self.fisica == 'no':
            assert type(self.fisica) == str
            rec_fisica = 'Ve a caminar un rato para estirar las piernas \n'

        rec_recreacion = str()
        if self.recreacion == 'no':
            assert type(self.recreacion) == str
            assert type(self.hobbie) == str
            rec_recreacion = 'Tómate un ratito para ' + self.hobbie + ' y disfrutar \n'

        recomendacion = rec_sueño + rec_agua + rec_comida + rec_fisica + rec_metas + rec_recreacion
        
        return recomendacion

    def imagenes(self, sentimiento):
        '''
        Entrega pandas.dataframe con links del sentimiento correspondiente
        columnas: link, sentimiento
        '''
        links = pd.read_table('imagenes.txt', sep = ' ')
        links = links[links['sentimiento'] == sentimiento]
        return links

    def plot(self, sentimiento):
        links = self.imagenes(sentimiento).links

        i = np.random.randint(len(links))

        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', 'whatever')
        path_hrb = './cute_images/'
        
        if (os.path.isdir(path_hrb)==False):
            os.mkdir(path_hrb)
            pass

        filename, headers = opener.retrieve(links.iloc[i],path_hrb + "cute_{}.jpg".format(i))

        img = mpimg.imread(path_hrb + "cute_{}.jpg".format(i))

        cute_img = plt.figure(figsize = (10, 15)) 
        ax = plt.subplot(111)
        plt.imshow(img)

        print('   ')
        print('-------------------')
        print('   ')
        print(self.recomendacion())

        t = plt.text(0.5, -0.1, self.recomendacion(), transform=ax.transAxes, fontsize=12, 
                        color=self.color, ha='center', va='center')
        t.set_bbox(dict(facecolor='white', alpha=0.8, edgecolor='white', boxstyle="round"))

        plt.axis('off')
        
        plt.show()


def inputs():

    nombre = input('¿Cómo te llamas?  ')
    sentimiento = input('¿Cómo te sientes hoy? (feliz, triste, cansade, tranquile, ansiose)  ')
    hobbie = input('¿Qué te gusta hacer en tu tiempo libre?  ')
    color = input('Cuál es tu color favorito? (blue, green, red, magenta, black)  ')
    persona = contexto(nombre, sentimiento, hobbie, color)

    f_sueño = input('¿Cuántas horas dormiste anoche aproximadamente?  ')

    persona.sueño = f_sueño

    f_comida = input('¿Has comido bien hoy? (si, no)  ')
    persona.comida = f_comida

    f_agua = input('¿Has tomado suficiente agua hoy? (si, no)  ')
    persona.agua = f_agua

    f_metas = input('¿Vas al día con tus metas de trabajo hoy? (si, no)  ')
    persona.metas = f_metas

    f_fisica = input('¿Has hecho actividad física hoy? (si, no)  ')
    persona.fisica = f_fisica

    f_recreacion = input('¿Has hecho alguna actividad recreativa hoy? (si, no)  ')
    persona.recreacion = f_recreacion

    persona.plot(sentimiento)

inputs()