class Player:#Clase para los jugadores. Define sus dimensiones y como se van a desplazar
    
    up_or_down1 = (4.2,4.5,5.5,6)#cambio de dirección 1 (para las secciones laterales)
    up_or_down2 = (2.5,3,3.5,3.8)#cambio de dirección 2 (para las secciones intermedias)
    up_or_down3 = (-2,-1.5,0,1.5,2)#cambio de dirección 3 (para la sección ubicada en la mitad del bloque)
    color = (255,255,255)#color del bloques
    longitude = 60#longitud del bloque
    
    def __init__(self,x_pos,y1_pos,broad,contact_zone):
        
        self.x_pos = x_pos#posición horizontal fija del jugador
        self.y1_pos = y1_pos#1era posición vertical variable del jugador (1er punto de la linea)
        self.y2_pos = self.y1_pos + Player.longitude#2da posición vertical variable del jugador (2do punto de la linea)
        self.broad = broad#grosor de la linea
        self.contact_zone = contact_zone#zona de contacto (donde la pelota rebotará)
        self.speed = 0#velocidad de movimiento (inicializada como cero)
        self.mouse_act = False#activación del raton para controlar el bloque
        
        #secciones del bloque:
        self.cz_y1 = self.y1_pos + 7.5
        self.cz_y2 = self.cz_y1 + 15
        self.cz_y4 = self.y2_pos - 7.5
        self.cz_y3 = self.cz_y4 - 15
        
    def drawPlayer(self,screen,draw):#para dibujar el bloque
        draw(screen,Player.color,[self.x_pos,self.y1_pos],[self.x_pos,self.y2_pos],self.broad)
        
    def movePlayer_conf1(self,event,py):#para controlar el bloque con las teclas w y s
        
        if event.type == py.KEYDOWN:#si presiono la tecla tecla
            
            if event.key == py.K_w:#si presiono w
                self.speed = -9
            elif event.key == py.K_s:#si presiono s
                self.speed = 9
            
        elif event.type == py.KEYUP:#si suelto la tecla
            
            if event.key == py.K_w:#si suelto w
                self.speed = 0
            elif event.key == py.K_s:#si suelto s
                self.speed = 0   
                
    def movePlayer_conf2(self,event,py):#para controlar el bloque con las flechas     
        
        if event.type == py.KEYDOWN:
            
            if event.key == py.K_UP:#si presiono flecha arriba
                self.speed = -9
            elif event.key == py.K_DOWN:#si presiono flecha abajo
                self.speed = 9
                
        elif event.type == py.KEYUP:
            
            if event.key == py.K_UP:#si suelto flecha arriba
                self.speed = 0
            elif event.key == py.K_DOWN:#si presiono flecha abajo
                self.speed = 0 
                
    def movePlayer_conf3(self):#para controlar el bloque con el mouse
        
        self.mouse_act = True#ahora se puede usar el raton

    def movingPlayer(self,py):#desplazando el bloque
        
        if self.mouse_act == True:
            
            mouse_pos = py.mouse.get_pos()#posición del mouse (horizontal,vertical)
            
            self.y1_pos = mouse_pos[1]#posicion vertical del raton
            
        else:
            
            self.y1_pos += self.speed

        self.y2_pos = self.y1_pos + Player.longitude
        
        if self.y1_pos <= 0:#si se sube demasiado el bloque
            
            self.y1_pos = 0
            self.y2_pos = self.y1_pos + Player.longitude
            
        elif self.y2_pos >= 600:#si se baja demasiado el bloque
            
            self.y2_pos = 600
            self.y1_pos = self.y2_pos - Player.longitude
            
        self.cz_y1 = self.y1_pos + 7.5
        self.cz_y2 = self.cz_y1 + 15
        self.cz_y4 = self.y2_pos - 7.5
        self.cz_y3 = self.cz_y4 - 15