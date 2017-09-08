import readchar

class Sokoban:

    level = 1
    mapa = []
    fil = 1
    col = 1
    n = 1
    jalar = False
    movi = 0
    metas = 0

    def __init__(self):
        print "Sokoban"

    def load_game_map(self):
        file = open(str(self.level) + 'level.skb','r')
        for line in file:
            fila = []
            for c in line[:-1]:
                fila.append(int(c))
            self.mapa.append(fila)

    def prin_map(self):
        for row in range(len(self.mapa)):
            line = ' '
            for col in range(len(self.mapa[row])):
                line += str(self.mapa[row][col]) + ' '
            print line  

    def cont_metas(self):
        for f in range(8):
            for c in range(8):
                if self.mapa[f][c]==4:
                    self.metas+=1
    def enc_mon(self):
        for f in range(8):
            for c in range(8):
                if self.mapa[f][c]==0:
                    self.fil=f
                    self.col=c


    def car_map(sel):
        objeto.load_game_map()
        objeto.enc_mon()
        objeto.cont_metas()
    
    def cam_niv(self):
            print "*** Nivel superado***"
            self.level += 1

    def jal_caj(self):
        self.jalar = True
        print "Modo jalar caja: ACTIVADO"
    def dej_caj(self):
        self.jalar = False
        print "Modo jalar caja: DESACTIVADO"
    def movi_tot(self):
        print "Movimientos:",self.movi

    def mov_der(self):
        if self.mapa[self.fil][self.col-1] == 3 and self.mapa[self.fil][self.col+1] == 1 and self.jalar == True:
            self.mapa[self.fil][self.col-1] = self.n
            self.mapa[self.fil][self.col] = 3
            self.mapa[self.fil][self.col+1] = 0
            self.col += 1
            self.n = 1
            self.movi += 1
        elif self.mapa[self.fil][self.col-1] == 3 and self.mapa[self.fil][self.col+1] == 4 and self.jalar == True:
            self.mapa[self.fil][self.col-1] = self.n
            self.mapa[self.fil][self.col] = 3
            self.mapa[self.fil][self.col+1] = 0
            self.col += 1
            self.n = 4
            self.movi += 1
        elif self.mapa[self.fil][self.col+1] == 1:
            self.mapa[self.fil][self.col+1] = 0
            self.mapa[self.fil][self.col] = self.n
            self.col += 1
            self.n = 1
            self.movi += 1
        elif self.mapa[self.fil][self.col+1] == 3:
            if self.mapa[self.fil][self.col+2] == 1:
                self.mapa[self.fil][self.col+2] = 3
                self.mapa[self.fil][self.col+1] = 0
                self.mapa[self.fil][self.col] = self.n
                self.col += 1
                self.n = 1
                self.movi += 1
            elif self.mapa[self.fil][self.col+2] == 4:
                self.mapa[self.fil][self.col+2] = 5
                self.mapa[self.fil][self.col+1] = 0
                self.mapa[self.fil][self.col] = self.n
                self.col += 1
                self.n = 1
                self.movi += 1
                self.metas -= 1
        elif self.mapa[self.fil][self.col+1] == 4:
            self.mapa[self.fil][self.col+1] = 0
            self.mapa[self.fil][self.col] = self.n
            self.col += 1
            self.n = 4
            self.movi += 1          
        elif self.mapa[self.fil][self.col+1] == 5:
            if self.mapa[self.fil][self.col+2] == 1:
                self.mapa[self.fil][self.col+1] = 3
                self.mapa[self.fil][self.col+2] = 0
                self.mapa[self.fil][self.col] = self.n
                self.col +=1
                self.n = 4
                self.movi += 1
                self.metas += 1
    def mov_izq(self):
        if self.mapa[self.fil][self.col+1] == 3 and self.mapa[self.fil][self.col-1] == 1 and self.jalar == True:
            self.mapa[self.fil][self.col+1] = self.n
            self.mapa[self.fil][self.col] = 3
            self.mapa[self.fil][self.col-1] = 0
            self.col -= 1
            self.n = 1
            self.movi += 1
        elif self.mapa[self.fil][self.col+1] == 3 and self.mapa[self.fil][self.col-1] == 4 and self.jalar == True:
            self.mapa[self.fil][self.col+1] = self.n
            self.mapa[self.fil][self.col] = 3
            self.mapa[self.fil][self.col-1] = 0
            self.col -= 1
            self.n = 4
            self.movi += 1
        elif self.mapa[self.fil][self.col-1] == 1:
            self.mapa[self.fil][self.col-1] = 0
            self.mapa[self.fil][self.col] = self.n
            self.col -= 1
            self.n = 1
            self.movi += 1
        elif self.mapa[self.fil][self.col-1] == 3:
            if self.mapa[self.fil][self.col-2] == 1:
                self.mapa[self.fil][self.col-2] = 3
                self.mapa[self.fil][self.col-1] = 0
                self.mapa[self.fil][self.col] = self.n
                self.col -= 1
                self.n = 1
                self.movi += 1
            elif self.mapa[self.fil][self.col-2] == 4:
                self.mapa[self.fil][self.col-2] = 5
                self.mapa[self.fil][self.col-1] = 0
                self.mapa[self.fil][self.col] = self.n
                self.col -= 1
                self.n = 1
                self.movi += 1
                self.metas -= 1 
        elif self.mapa[self.fil][self.col-1] == 4:
            self.mapa[self.fil][self.col-1] = 0
            self.mapa[self.fil][self.col] = self.n
            self.col -= 1
            self.n = 4
            self.movi += 1
        elif self.mapa[self.fil][self.col-1] == 5:
            if self.mapa[self.fil][self.col-2] == 1:
                self.mapa[self.fil][self.col-1] = 0
                self.mapa[self.fil][self.col-2] = 3
                self.mapa[self.fil][self.col] = self.n
                self.col -=1
                self.n = 4
                self.movi += 1
                self.metas += 1
    def mov_arr(self):
        if self.mapa[self.fil+1][self.col] == 3 and self.mapa[self.fil-1][self.col] == 1 and self.jalar == True:
            self.mapa[self.fil+1][self.col] = self.n
            self.mapa[self.fil][self.col] = 3
            self.mapa[self.fil-1][self.col] = 0
            self.fil -= 1
            self.n = 1
            self.movi += 1
        elif self.mapa[self.fil+1][self.col] == 3 and self.mapa[self.fil-1][self.col] == 4 and self.jalar == True:
            self.mapa[self.fil+1][self.col] = self.n
            self.mapa[self.fil][self.col] = 3
            self.mapa[self.fil-1][self.col] = 0
            self.fil -= 1
            self.n = 4
            self.movi += 1
        elif self.mapa[self.fil-1][self.col] == 1:
            self.mapa[self.fil-1][self.col] = 0
            self.mapa[self.fil][self.col] = self.n
            self.fil -= 1
            self.n = 1
            self.movi += 1
        elif self.mapa[self.fil-1][self.col] == 3:
            if self.mapa[self.fil-2][self.col] == 1:
                self.mapa[self.fil-2][self.col] = 3
                self.mapa[self.fil-1][self.col] = 0
                self.mapa[self.fil][self.col] = self.n
                self.fil -= 1
                self.n = 1
                self.movi += 1
            elif self.mapa[self.fil-2][self.col] == 4:
                self.mapa[self.fil-2][self.col] = 5
                self.mapa[self.fil-1][self.col] = 0
                self.mapa[self.fil][self.col] = self.n
                self.fil -= 1
                self.n = 1
                self.movi += 1
                self.metas -= 1
        elif self.mapa[self.fil-1][self.col] == 4:
            self.mapa[self.fil-1][self.col] = 0
            self.mapa[self.fil][self.col] = self.n
            self.fil -= 1
            self.n = 4
            self.movi += 1
        elif self.mapa[self.fil-1][self.col] == 5:
            if self.mapa[self.fil-2][self.col] == 1:
                self.mapa[self.fil-1][self.col] = 0
                self.mapa[self.fil-2][self.col] = 3
                self.mapa[self.fil][self.col] = self.n
                self.fil -=1
                self.n = 4
                self.movi += 1
                self.metas += 1
    def mov_aba(self):
        if self.mapa[self.fil-1][self.col] == 3 and self.mapa[self.fil+1][self.col] == 1 and self.jalar == True:
            self.mapa[self.fil-1][self.col] = self.n
            self.mapa[self.fil][self.col] = 3
            self.mapa[self.fil+1][self.col] = 0
            self.fil += 1
            self.n = 1
            self.movi += 1
        elif self.mapa[self.fil-1][self.col] == 3 and self.mapa[self.fil+1][self.col] == 4 and self.jalar == True:
            self.mapa[self.fil-1][self.col] = self.n
            self.mapa[self.fil][self.col] = 3
            self.mapa[self.fil+1][self.col] = 0
            self.fil += 1
            self.n = 4
            self.movi += 1
        elif self.mapa[self.fil+1][self.col] == 1:
            self.mapa[self.fil+1][self.col] = 0
            self.mapa[self.fil][self.col] = self.n
            self.fil += 1
            self.n = 1
            self.movi += 1
        elif self.mapa[self.fil+1][self.col] == 3:
            if self.mapa[self.fil+2][self.col] == 1:
                self.mapa[self.fil+2][self.col] = 3
                self.mapa[self.fil+1][self.col] = 0
                self.mapa[self.fil][self.col] = self.n
                self.fil += 1
                self.n = 1
                self.movi += 1
            elif self.mapa[self.fil+2][self.col] == 4:
                self.mapa[self.fil+2][self.col] = 5
                self.mapa[self.fil+1][self.col] = 0
                self.mapa[self.fil][self.col] = self.n
                self.fil += 1
                self.n = 1
                self.movi += 1
                self.metas -= 1
        elif self.mapa[self.fil+1][self.col] == 4:
            self.mapa[self.fil+1][self.col] = 0
            self.mapa[self.fil][self.col] = self.n
            self.fil += 1
            self.n = 4
            self.movi += 1
        elif self.mapa[self.fil+1][self.col] == 5:
            if self.mapa[self.fil+2][self.col] == 1:
                self.mapa[self.fil+2][self.col] = 3
                self.mapa[self.fil+1][self.col] = 0
                self.mapa[self.fil][self.col] = self.n
                self.fil +=1
                self.n = 4
                self.movi += 1
                self.metas += 1
objeto = Sokoban()
objeto.car_map()

while True:
    if objeto.metas == 0:
        objeto.cam_niv()
        objeto.movi = 0
    objeto.prin_map()
    objeto.movi_tot()
    print 'Metas: '+str(objeto.metas)
    print 'Nivel: '+str(objeto.level)
    print '        W\n    [A     D]\n        S       J - L'
    mov = readchar.readchar()
    if mov == "D" or mov == "d":
        objeto.mov_der()
    elif mov == "A" or mov == "a":
        objeto.mov_izq()
    elif mov == "W" or mov == "w":
        objeto.mov_arr()
    elif mov == "S" or mov == "s":
        objeto.mov_aba()
    elif mov == "J" or mov == "j":
        objeto.jal_caj()
    elif mov == "L" or mov == "l":
        objeto.dej_caj()
    
    
    
