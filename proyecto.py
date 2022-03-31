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
        self.nombre = nombre  # name of the person
        self.sentimiento = sentimiento
        self.hobbie = hobbie
        self.sueño = -1.0
        self.comida = 0
        self.agua = 0
        self.metas = 0
        self.fisica = 0
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

        recomendacion = ''

        if self.sueño != -1.0:
            assert type(self.sueño) == float

            if self.sueño < 6:
                recomendacion = recomendacion + 'Ve a tomar una merecida siesta para reponer energías'
            elif self.sueño < 8:
                recomendacion = recomendacion + 'Considera cuidar tus hábitos de sueño'

        if self.comida != 0:
            assert type(self.comida) == str

            if self.comida == 'si':
                pass
            elif self.comida == 'no':
                recomendacion = recomendacion + 'Ve a comer algo rico para reponerte y continuar el día'

        if self.agua != 0:
            assert type(self.agua) == str

            if self.agua == 'si':
                pass
            elif self.agua == 'no':
                recomendacion = recomendacion + 'Toma agüita (de uwu) para que estés hidratade'

        if self.metas != 0:
            assert type(self.metas) == str

            if self.metas == 'si':
                pass
            elif self.metas == 'no':
                recomendacion = recomendacion + 'Tómate un rato para reorganizar tu día. Fija sólo una meta que quieras lograr hoy'

        if self.fisica != 0:
            assert type(self.fisica) == str

            if self.fisica == 'si':
                pass
            elif self.fisica == 'no':
                recomendacion = recomendacion + 'Ve a caminar un rato para estirar las piernas'

        if self.recreacion != 0:
            assert type(self.recreacion) == str
            assert type(self.hobbie) == str

            if self.recreacion == 'si':
                pass
            elif self.recreacion == 'no':
                recomendacion = recomendacion + 'Tómate un ratito para ' + self.hobbie + ' y disfrutar'
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
            
        cute_img = plt.figure(figsize = (15,15)) 
        ax = plt.subplot(111)
        plt.imshow(img)

        print(self.recomendacion())

        t = plt.text(0.5, 0.3, self.recomendacion(), transform=ax.transAxes, fontsize=25, 
                        color='black', ha='center', va='center')
        t.set_bbox(dict(facecolor='white', alpha=0.8, edgecolor='white', boxstyle="round"))
        plt.axis('off')
        plt.show()



def inputs():

    nombre = input('¿Cómo te llamas?')
    sentimiento = input('¿Cómo te sientes hoy? (feliz, triste, cansade, tranquile, ansiose) ')
    hobbie = input('¿Qué te gusta hacer en tu tiempo libre?')
    color = input('Cuál es tu color favorito? (blue, green, red, cyan, magenta, yellow, black)')
    persona = contexto(nombre, sentimiento, hobbie)

    print('Responde la siguiente pregunta con un número entero')

    f_sueño = input('¿Cuántas horas dormiste anoche aproximadamente?')

    persona.horas_sueño = f_sueño

    f_comida = input('¿Has comido bien hoy? (si, no)')
    persona.ha_comido = f_comida

    f_agua = input('¿Has tomado suficiente agua hoy? (si, no)')
    persona.toma_agua = f_agua

    f_metas = input('¿Vas al día con tus metas de trabajo hoy? (si, no)')
    persona.cumplido_metas = f_metas

    f_fisica = input('¿Has hecho actividad física hoy? (si, no)')
    persona.act_fisica = f_fisica

    f_recreacion = input('¿Has hecho alguna actividad recreativa hoy? (si, no)')
    persona.recreacion = f_recreacion

    #persona.
    persona.plot(sentimiento)

inputs()