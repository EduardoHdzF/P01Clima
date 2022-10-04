import tkinter as tk
from Solicitud.SolicitaAPI import SolicitaApi
from threading import Timer

class interfazGrafica:
    
    seleccion = ['']
    Cache = open("ClimaVuelos/Programa/Solicitud/Cache/Cache.txt","r+")

    def __init__(self, viajes, coordenadas):        
        self.viajes = viajes
        self.coordenadas = coordenadas

    def solicitud_Datos(self, ind):
        self.solicitud = SolicitaApi(self.coordenadas)            
        self.solicitud.preguntaApi(self.coordenadas, ind)

    def tempo(self):
        self.t = Timer(300, self.borraCache)
        self.t.start()       

    def borraCache(self):         
        self.Cache.truncate(0)
        self.Cache.close()                

    def desplega_ventana(self):
        
        altura = 1000
        ancho = 10000

        raiz = tk.Tk()
        raiz.title("Climas de Aeropuertos")        

        ventana = tk.Canvas(raiz, height = altura, width = ancho, bg= '#F58E1F')
        ventana.pack(anchor= tk.CENTER, expand=True)

        marco = tk.Frame(raiz, bg= 'blue')     
        marco.place(relx=.25, rely=.15, relheight=.25, relwidth=.5)

        titulo = tk.Label(raiz, text=' - Informe del clima - ', font= ('Modern',40), bg= '#F58E1F')
        titulo.place(relx= .01, rely= .01)

        subtitulo = tk.Label(raiz, text='Viajes disponibles', font= ('Modern',35), bg= '#F58E1F')
        subtitulo.place(relx= .4, rely= .075)        

        comentario = tk.Label(raiz, text='Selecciona una \nopción:', font= ('Modern',15), bg= '#F58E1F')
        comentario.place(relx= .02, rely= .15)

        barra = tk.Scrollbar(marco)
        barra.pack(side= tk.RIGHT, fill= tk.Y)
        lista_viajes = tk.Listbox(marco, yscrollcommand= barra.set, width= 125, font= 'Modern')
        
        for viajes_disponibles in range(len(self.viajes)):
            lista_viajes.insert(tk.END, self.viajes[viajes_disponibles][0] + " ---> " + self.viajes[viajes_disponibles][1])
        
        lista_viajes.pack(side= tk.LEFT, fill= tk.BOTH)

        barra.config(command= lista_viajes.yview)                      


        def opcion_seleccionada(): 

            self.Cache = open("ClimaVuelos/Programa/Solicitud/Cache/Cache.txt","r+")                       
            
            if self.Cache.readline() == '' and raiz.winfo_viewable() == 1:
                self.tempo()

            self.seleccion = lista_viajes.get(lista_viajes.curselection())   

            origen = self.seleccion[0:3]
            destino = self.seleccion[9:12]         

            eti_seleccion = tk.Label(raiz, text= self.seleccion, bg= 'red', font= ('Modern', 15))
            eti_seleccion.place(relx= 0.82, rely= 0.15,height= 250, width=250)          
            
            clima_cd_origen = tk.Label(raiz, text= 'Origen', font= ('Modern',20), bg= '#F58E1F')            
            clima_cd_origen.place(relx= 0.11, rely= 0.42)

            clima_cd_destino = tk.Label(raiz, text= 'Destino', font= ('Modern',20), bg= '#F58E1F')
            clima_cd_destino.place(relx= 0.56, rely= 0.42)                                    
            
            ind = 0
            
            while origen.count(self.viajes[ind][0]) == 0 or destino.count(self.viajes[ind][1]) == 0:            
                ind = ind + 1
            
            self.solicitud_Datos(ind)

            clima_ciudad_origen = tk.Label(raiz, text= self.solicitud.clima_ciudad_origen, bg= '#43C01B', font= ('Modern', 20), justify= 'left')
            clima_ciudad_origen.place(relx= 0.1, rely= 0.48,height= 500, width=700)

            clima_ciudad_destino = tk.Label(raiz, text= self.solicitud.clima_ciudad_destino, bg= '#39D2E7', font= ('Modern', 20), justify= 'left')
            clima_ciudad_destino.place(relx= 0.55, rely= 0.48,height= 500, width=700)            

        self.solicitud = SolicitaApi(self.coordenadas)

        boton = tk.Button(raiz, text= 'Buscar', font= 'Modern', command= opcion_seleccionada)
        boton.place(relx= .75, rely= 0.15,height= 100, width=100)                                        

        raiz.mainloop()        
        
        self.Cache.truncate(0)
        self.t.cancel()
        
