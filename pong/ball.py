from random import choice

class Ball:#la clase de la bola
    
    color = (255,255,255)#color de la bola
    dim = 8#dimension de la bola
    speed_up = 10#en que momento aumentará su velocidad
    normal_speedx = 6#velocidad horizontal normal de la bola
    max_speedx = 12#velocidad horizontal máxima de la bola
    initial_moves = (-3,-2,-1,0)#movimientos iniciales
    count = 0#define a que direccion irá la bola cuando se reinicie la posición
    
    def __init__(self,xc,yc):
        
        self.xc = xc#pos.horizontal de la bola
        self.yc = yc#pos.vertical de la bola
        
        self.yc1 = self.yc + (self.dim/2)#mitad de la bola (pos.vertical)
        self.xc1 = self.xc + (self.dim/2)#mitad de la bola (pos.horizontal)
        self.xc2 = self.xc + self.dim#extremo derecho de la bola
        self.yc2 = self.yc + self.dim#extremo izquierdo de la bola
        self.touch1 = True#el bloque del jugador 1 puede tocar la bola
        self.touch2 = True#el bloque del jugador 2 puede tocar la bola
        self.contacts = 0#cantidad de contactos hecho de la bola con los bloques
        self.move_x = 2#velocidad horizontal inicial de la bola
        self.move_y = 2#velocidad vertical inicial de la bola
        
    def drawBall(self,screen,draw):
        draw(screen,self.color,(self.xc,self.yc,self.dim,Ball.dim))#dibujar la bola 
    
    def moveBall(self,player1,player2):#movimientos de la bola
        
        if self.yc <= 0 or self.yc2 >= 600:#si busca salirse de la ventana (por arriba o abajo), rebota
            self.move_y *= -1
            
        elif self.xc <= 0 or self.xc2 >= 800:#si sale de la ventana (por los lados)
            
            #los bloques no pueden hacer contacto con la bola
            self.touch1 = False
            self.touch2 = False
            
            if self.xc <= -1000 or self.xc2 >= 1900:#de pasar estos limites, la bola vuelve a la mitad de la pantalla
                
                self.touch1 = True
                self.touch2 = True
                self.contacts = 0
                
                self.count += 1
                
                if self.count%2:#si count es par, la bola se desplazará a la derecha (jugador 2)
                    
                    self.move_x = 2
                    self.move_y = choice(Ball.initial_moves)#eleccion aleatoria de una velocidad vertical inicial
                    
                else:#si count es impar, la bola se desplazará a la derecha (jugador 1)
                    self.move_x = -2
                    self.move_y = -1*choice(Ball.initial_moves)
                
                #mitad horizontal y vertical de la ventana
                self.xc = 400
                self.yc = 300
                
                self.xc2 = self.xc + Ball.dim
                self.yc2 = self.yc + Ball.dim
        
        #aqui se definen las zonas o secciones de contacto del bloque del jugador 1
        #en total son 5 zonas, dos ubicadas en los extremos, dos intermedias (una cerca de cada extremo) y dos ubicadas en el medio del bloque
        
        elif player1.contact_zone >= self.xc and self.touch1 == True:
            
            
            if (player1.y1_pos <= self.yc1 and player1.cz_y1 >= self.yc1) or (player1.y1_pos > self.yc1 and player1.y1_pos > self.yc and player1.y1_pos <= self.yc2):
                
                #zona del extremo superior
                
                self.contacts += 1#se cuenta el contacto
                self.touch1 = False#jugador 1 no puede tocar la bola
                self.touch2 = True#jugador 2 ya puede tocar la bola
                
                if self.contacts > self.speed_up:#si contacts es mayor a speed_up, la velocidad de la bola aumenta al doble (tanto vertical como horizontalmente)
                    
                    self.move_x = Ball.max_speedx
                    self.move_y = (-choice(player1.up_or_down1))*2
                
                else:
                    
                    self.move_x = Ball.normal_speedx
                    self.move_y = -choice(player1.up_or_down1)
                    
            elif player1.cz_y1 < self.yc1 and player1.cz_y2 >= self.yc1:
                
                #zona intermedia superior
                
                self.contacts += 1
                self.touch1 = False
                self.touch2 = True
                
                if self.contacts > Ball.speed_up:
                    self.move_x = Ball.max_speedx
                    self.move_y = (-choice(player1.up_or_down2))*2
                    
                else:  
                    self.move_x = Ball.normal_speedx
                    self.move_y = -choice(player1.up_or_down2)
                    
            elif player1.cz_y2 < self.yc1 and player1.cz_y3 >= self.yc1:
                
                #mitad del bloque
                
                self.contacts += 1
                self.touch1 = False
                self.touch2 = True
                
                if self.contacts > Ball.speed_up:
                    self.move_x = Ball.max_speedx
                    self.move_y = (choice(player1.up_or_down3))*2
                    
                else:
                    self.move_x = Ball.normal_speedx
                    self.move_y = choice(player1.up_or_down3)
            
            elif player1.cz_y3 < self.yc1 and player1.cz_y4 >= self.yc1:
                
                #zona intermedia inferior
                
                self.contacts += 1
                self.touch1 = False
                self.touch2 = True
                
                if self.contacts > Ball.speed_up:
                    self.move_x = Ball.max_speedx
                    self.move_y = (choice(player1.up_or_down2))*2
                    
                else:  
                    self.move_x *= -1
                    self.move_y = choice(player1.up_or_down2)
            
            elif (player1.cz_y4 < self.yc1 and player1.y2_pos >= self.yc1) or (player1.y2_pos < self.yc1 and player1.y2_pos < self.yc2 and player1.y2_pos >= self.yc):
                
                #zona intermedia superior
                
                self.contacts += 1
                self.touch1 = False
                self.touch2 = True
                
                if self.contacts > Ball.speed_up:
                    self.move_x = Ball.max_speedx
                    self.move_y = (choice(player1.up_or_down1))*2
                
                else:
                    self.move_x = Ball.normal_speedx
                    self.move_y = choice(player1.up_or_down1)
                    
        #en lo que respecta al jugador ocurre el mismo caso, pero ahora se toma en sentido contrario
                
        elif player2.contact_zone <= self.xc2 and self.touch2 == True:
            
            if (player2.y1_pos <= self.yc1 and player2.cz_y1 >= self.yc1) or (player2.y1_pos > self.yc1 and player2.y1_pos > self.yc and player2.y1_pos <= self.yc2):
                
                self.contacts += 1
                self.touch1 = True
                self.touch2 = False
                
                if self.contacts > Ball.speed_up:
                    
                    self.move_x = -Ball.max_speedx
                    self.move_y = (-choice(player1.up_or_down1))*2
                
                else:
                    
                    self.move_x = -Ball.normal_speedx
                    self.move_y = -choice(player1.up_or_down1)
        
            elif player2.cz_y1 < self.yc1 and player2.cz_y2 >= self.yc1:
                
                self.contacts += 1
                self.touch1 = True
                self.touch2 = False
                
                if self.contacts > Ball.speed_up:
                    
                    self.move_x = -Ball.max_speedx
                    self.move_y = (-choice(player2.up_or_down2))*2
                
                else:
                    self.move_x = -Ball.normal_speedx
                    self.move_y = -choice(player2.up_or_down2)
                
            elif player2.cz_y2 < self.yc1 and player2.cz_y3 >= self.yc1:
                
                self.contacts += 1
                self.touch1 = True
                self.touch2 = False
                
                if self.contacts > Ball.speed_up:
                    
                    self.move_x = -Ball.max_speedx
                    self.move_y = (choice(player2.up_or_down3))*2
                    
                else:
                    self.move_x = -Ball.normal_speedx
                    self.move_y = choice(player2.up_or_down3)
            
            elif player2.cz_y3 < self.yc1 and player2.cz_y4 >= self.yc1:
                
                self.contacts += 1
                self.touch1 = True
                self.touch2 = False
                
                if self.contacts > Ball.speed_up:
                    
                    self.move_x = -Ball.max_speedx
                    self.move_y = (choice(player2.up_or_down2))*2
                    
                else:
                    
                    self.move_x = -Ball.normal_speedx
                    self.move_y = choice(player2.up_or_down2)
            
            elif (player2.cz_y4 < self.yc1 and player2.y2_pos >= self.yc1) or (player2.y2_pos < self.yc1 and player2.y2_pos < self.yc2 and player2.y2_pos >= self.yc):
            
                self.contacts += 1
                self.touch1 = True
                self.touch2 = False
                
                if self.contacts > Ball.speed_up:
                    self.move_x = -Ball.max_speedx
                    self.move_y = (choice(player2.up_or_down1))*2
                    
                else:
                    self.move_x = -Ball.normal_speedx
                    self.move_y = choice(player2.up_or_down1) 
        
        self.xc += self.move_x
        self.yc += self.move_y
        
        self.yc1 = self.yc + (self.dim/2)
        self.xc1 = self.xc + (self.dim/2)
        self.xc2 = self.xc + self.dim
        self.yc2 = self.yc + self.dim