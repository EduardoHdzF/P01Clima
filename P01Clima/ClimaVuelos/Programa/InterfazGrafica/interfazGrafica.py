import tkinter as Climas
from Solicitud.SolicitaAPI import SolicitaApi

class interfazGrafica:
    
    seleccion = ['']

    def __init__(self, viajes, coordenadas):        
        self.viajes = viajes
        self.coordenadas = coordenadas

    def desplega_ventana(self):

        altura = 1000
        ancho = 10000
        coordenadas = self.coordenadas

        raiz = Climas.Tk()

        ventana = Climas.Canvas(raiz, height = altura, width = ancho, bg= '#F58E1F')
        ventana.pack()

        marco = Climas.Frame(raiz, bg= 'blue')
        marco.place(relx=.25, rely=.15, relheight=.25, relwidth=.5)

        titulo = Climas.Label(raiz, text=' - Informe del clima - ', font= ('Modern',40), bg= '#F58E1F')
        titulo.place(relx= .01, rely= .01)

        subtitulo = Climas.Label(raiz, text='Viajes disponibles', font= ('Modern',35), bg= '#F58E1F')
        subtitulo.place(relx= .4, rely= .075)        

        comentario = Climas.Label(raiz, text='Selecciona una \nopción:', font= ('Modern',15), bg= '#F58E1F')
        comentario.place(relx= .02, rely= .15)

        barra = Climas.Scrollbar(marco)
        barra.pack(side= Climas.RIGHT, fill= Climas.Y)
        #barra.place(relx= .1, rely= .1)

        '''
        lista_viajes = Climas.Listbox(raiz, height=10, width=10, yscrollcommand= barra.set(), cursor = 'hand2',bg= 'green', selectmode= 'single')
        
        for viajes_disponibles in range(len(self.viajes)):
            lista_viajes.insert(viajes_disponibles + 1, self.viajes[viajes_disponibles])
        
        #lista_viajes.place(height= 300, width= 500)        
        lista_viajes.place(relx= .25, rely= .125, relheight= .5, relwidth= .5)        
        '''    
        lista_viajes = Climas.Listbox(marco, yscrollcommand= barra.set, width= 125, font= 'Modern')
        
        for viajes_disponibles in range(len(self.viajes)):
            lista_viajes.insert(Climas.END, self.viajes[viajes_disponibles][0] + " ---> " + self.viajes[viajes_disponibles][1])
        
        #lista_viajes.place(height= 300, width= 500)        
        #lista_viajes.place(relx= .25, rely= .125, relheight= .5, relwidth= .5)        
        lista_viajes.pack(side= Climas.LEFT, fill= Climas.BOTH)

        barra.config(command= lista_viajes.yview)        

        def opcion_seleccionada():                        

            clima_cd_origen = Climas.Label(raiz, text='Ciudad de origen', font= ('Modern',20), bg= '#F58E1F')
            clima_cd_origen.place(x= 100, y= 410)

            clima_cd_destino = Climas.Label(raiz, text='Ciudad de destino', font= ('Modern',20), bg= '#F58E1F')
            clima_cd_destino.place(x= 1100, y= 410)

            self.seleccion = lista_viajes.get(lista_viajes.curselection())            

            eti_seleccion = Climas.Label(raiz, text= self.seleccion, bg= 'red', font= ('Modern', 15))
            eti_seleccion.place(x= 1600, y= 150,height= 250, width=250)          

            ind = 0
            
            while self.seleccion.count(self.viajes[ind][0]) == 0 or self.seleccion.count(self.viajes[ind][1]) == 0:            
                ind = ind + 1
            
            print(ind)

            solicitud = SolicitaApi(self.coordenadas, ind)
            
            solicitud.preguntaApi(self.coordenadas, ind)
            
            clima_ciudad_origen = Climas.Label(raiz, text= solicitud.clima_ciudad_origen, bg= '#43C01B', font= ('Modern', 20), justify= 'left')
            clima_ciudad_origen.place(x= 100, y= 450,height= 500, width=700)

            clima_ciudad_destino = Climas.Label(raiz, text= solicitud.clima_ciudad_destino, bg= '#39D2E7', font= ('Modern', 20), justify= 'left')
            clima_ciudad_destino.place(x= 1100, y= 450,height= 500, width=700)
            
        '''
        entrada = Climas.Entry(raiz, text= 'Selecciona la opción disponible')
        entrada.place(relx=.5, rely=.5, height= 100 , width=100)
        '''        

        boton = Climas.Button(raiz, text= 'Buscar', font= 'Modern', command= opcion_seleccionada)
        boton.place(relx= .75, rely= 0.15,height= 100, width=100)                
        
        raiz.mainloop()