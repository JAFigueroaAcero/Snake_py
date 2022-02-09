import pygame,sys
import random as r
def main():
    global grid
    global gridnum
    global gridgen
    global screen
    global W
    X = 475
    Y = 475
    size = (X,Y)
    fpsClock = pygame.time.Clock()
    fps = 10
    grid = [0 for n in range(361)]
    gridnum = []
    gridgen = [[0 for n in range(19)] for m in range(19)]
    border_list = []
    screen = pygame.display.set_mode(size)
    i = 0
    for n in range(19):
        loc = []
        for m in range(19):
            loc.append(i)
            i += 1
        gridnum.append(loc)


    #Colores

    B = (0,0,0)
    W = (255,255,255)
    R = (255,0,0)
    B2 = (125,125,125)

    tail_list = []
    seed = r.seed()
    xvel = 1
    yvel = 0
    f1 = pygame.font.Font('freesansbold.ttf', 32)
    t1 = f1.render('GAME OVER', True, R)

    tr1 = t1.get_rect()
    tr1.center = (X // 2, Y // 2 - 25)

    f2 = pygame.font.Font('freesansbold.ttf', 16)
    t2 = f2.render('Press \'space\' to continue', True, R)

    tr2 = t2.get_rect()
    tr2.center = (X // 2, Y // 2)
    def sum(x,y,n):
            global grid
            global gridnum
            global gridgen
            pos = gridnum[y][x]
            gridgen[y][x] += n
            grid[pos] += n

    class borders():
        def __init__(self,x,y):
            self.x = x
            self.y = y
            sum(self.x,self.y,1)

        def update(self):
            pygame.draw.rect(screen, B2, (self.x*25,self.y*25,25,25))
    class head():
        def __init__(self,x,y):
            self.x = x
            self.y = y
            sum(self.x,self.y,1)

        def show(self,x,y):
            global screen
            global W
            sum(self.x,self.y,-1)
            self.x += x
            self.y += y
            pygame.draw.rect(screen, W, (self.x*25,self.y*25,25,25))
            sum(self.x,self.y,1)
        

    class tail():
        def __init__(self,x,y,front):
            self.x = x
            self.y = y
            self.front = front
            sum(self.x,self.y,1)
            
        def show(self,x,y):
            global screen
            global W
            sum(self.x,self.y,-1)
            self.x += x
            self.y += y
            pygame.draw.rect(screen, W, (self.x*25,self.y*25,25,25))
            sum(self.x,self.y,1)
        def update(self):
            global screen
            global W
            sum(self.x,self.y,-1)
            self.x = self.front.x
            self.y = self.front.y
            pygame.draw.rect(screen, W, (self.x*25,self.y*25,25,25))
            sum(self.x,self.y,1)
    class dot():
        def __init__(self,pos):
            self.pos = pos
            self.exists = False
            self.x = None
            self.y = None
        def rand(self):
            global gridnum
            posible = []
            for n,e in enumerate(self.pos):
                if e == 0:
                    posible.append(n)
            p = posible[r.randint(0, len(posible))]
            for n, el in enumerate(gridnum):
                if p in el:
                    self.x = el.index(p)
                    self.y = n
                    break
            self.exists = True
            pygame.draw.rect(screen, R, (self.x*25,self.y*25,25,25))
            sum(self.x,self.y,5)
        def update(self):
            pygame.draw.rect(screen, R, (self.x*25,self.y*25,25,25))
    d = dot(grid)
    h = head(0,0)
    tail_list.append(tail(4,8,h))
    tail_list.append(tail(3,8,tail_list[-1]))
    tail_list.append(tail(2,8,tail_list[-1]))
    tail_list.append(tail(1,8,tail_list[-1]))
    for n, e in enumerate(gridgen):
        if n == 0 or n == 18:
            for m, p in enumerate(e):
                border_list.append(borders(m,n))
        else:
            border_list.append(borders(0,n))
            border_list.append(borders(18,n))


    screen.fill(B)
    h.show(4,8)
    for e in tail_list:
        e.show(0,0)
    for e in border_list:
        e.update()
    pygame.display.flip()
    fpsClock.tick(fps)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if xvel == 0:
                    if event.key == 97:
                        xvel = -1
                        yvel = 0
                        break
                    elif event.key == 100:
                        xvel = 1
                        yvel = 0
                        break
                elif yvel == 0:
                    if event.key == 119:
                        yvel = -1
                        xvel = 0
                        break
                    elif event.key == 115:
                        yvel = 1
                        xvel = 0
                        break
            elif event.type == pygame.QUIT:
                sys.exit()
        screen.fill(B)
        if not d.exists:
            d.pos = grid
            d.rand()
        else:
            d.update()
        h.show(xvel,yvel)
        for e in tail_list[::-1]:
            e.update()
        for e in border_list:
            e.update()
        if 3 in grid:
            screen.blit(t1, tr1)
            screen.blit(t2, tr2)
            pygame.display.flip()
            break
        elif 7 in grid:
            tail_list.append(tail(tail_list[-1].x,tail_list[-1].x,tail_list[-1]))
            d.exists = False
            sum(d.x,d.y,-5)
        pygame.display.flip()
        fpsClock.tick(fps)


if __name__ == '__main__':
    pygame.init()
    f = True
    main()
    while f:
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        f = False
                    elif event.key == pygame.K_SPACE:
                        main()
                elif event.type == pygame.QUIT:
                    sys.exit()