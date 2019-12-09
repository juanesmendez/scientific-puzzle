##
import pygame
import numpy as np
import random
import time
import datetime

# Colores usando rgb
Cafesito = (204, 102, 0)
Naranja = (247, 160, 27)
CafeOscuro = (56, 27, 0)
Negro = (0, 0, 0)
Blanco = (255, 252, 238)


pygame.init()
# Tamaño de la pantalla
alto = 600
ancho = 1000
# Se inicializa la pantalla
DISP = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Scientific Puzzle')
DISP.fill(Cafesito)
clock = pygame.time.Clock()


BOARDX = ancho/2
BOARDY = alto/2
TILESIZE = 80
BASICFONTSIZE = 20
BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

slide_to = None

def create_board_surface(tam):
    surface = pygame.Surface((tam*TILESIZE, tam*TILESIZE))
    return surface


def drawBoardSurface(screen, board_surface, boardx, boardy):
    screen.blit(board_surface, (boardx, boardy))


def create_tiles(boardsurface, board, tilesize, boardrows, boardcols):
    global BASICFONT
    colcount = 0
    # Ver como traer la matriz con los numeros y mapearlos al dibujo

    for i in range(0, len(board[0])):
        rowcount = 0
        for j in range(0, len(board)):
            if board[i][j] == None:
                pygame.draw.rect(boardsurface, Negro,
                                 (rowcount, colcount, tilesize - 1, tilesize - 1))  # Ver como meter esto en un arreglo
            else:
                pygame.draw.rect(boardsurface, Naranja , (rowcount, colcount, tilesize-1, tilesize-1)) #Ver como meter esto en un arreglo

                textsurf = BASICFONT.render(str(board[i][j]), True, CafeOscuro)
                textrect = textsurf.get_rect()
                textrect.center = rowcount + (tilesize/2), colcount + (tilesize/2)

                boardsurface. blit(textsurf, textrect)

            rowcount = rowcount + tilesize
        colcount = colcount + tilesize


def Fibonacci(boardrows, boardcols):
    print("Inside FIBONACCI")
    size = boardrows * boardcols

    numbers = []
    #inicializamos la secuencia de fibonnaci
    primerNumero = 0
    segundoNumero = 1
    numeroFibonacci = 0

    numbers.append(primerNumero)
    numbers.append(segundoNumero)
    print("Numbers array length:", len(numbers))
    print("SIZE IT SHOULD HAVE:", size)
    #Se sale del ciclo cuando el i-esimo elemento de la secuencia Fib sea mayor que el numero que entra por parametro
    while len(numbers) < size:
        print("Numbers array length:", len(numbers))
        # Se utiliza la formula de Fibonacci
        numeroFibonacci = primerNumero + segundoNumero
        primerNumero = segundoNumero
        segundoNumero = numeroFibonacci
        numbers.append(numeroFibonacci)

    return numbers

def Primos(boardrows, boardcols):
    print("Inside PRIMOS")
    size = boardrows * boardcols

    if size == 9:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23]
    elif size == 16:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
    elif size == 25:
        return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def Pares(boardrows, boardcols):
    numbers = []
    size = boardrows*boardcols
    num = 2
    while len(numbers) < size:
        numbers.append(num)
        num += 2

    return numbers


def Impares(boardrows, boardcols):
    numbers = []
    size = boardrows * boardcols
    num = 1
    while len(numbers) < size:
        numbers.append(num)
        num += 2

    return numbers

def Potencias(boardrows, boardcols):
    numbers = []
    size = boardrows * boardcols
    counter = 1
    while len(numbers) < size:
        num = 2 ** counter
        numbers.append(num)
        counter += 1

    return numbers


def Cuadrada(boardrows, boardcols):
    numbers = []
    size = boardrows * boardcols
    counter = 1
    while len(numbers) < size:
        num = 2 ** counter
        numbers.append(num)
        counter += 1

    return numbers


def getSeriesNumbers(serie, boardrows, boardcols):
    if serie == 1:
        # Caso Fibonacci
        print("Inside fibonacci case")
        numbers = Fibonacci(boardrows, boardcols)
        print(numbers)
    elif serie == 2:
        # Caso cuadrada
        print("Inside cuadrada case")
        numbers = Cuadrada(boardrows, boardcols)

    elif serie == 3:
        # Caso primos
        print("Inside primos case")
        numbers = Primos(boardrows, boardcols)
    elif serie == 4:
        # Caso potencias
        print("Inside potencias case")
        numbers = Potencias(boardrows, boardcols)

    elif serie == 5:
        # Caso par
        print("Inside pares case")
        numbers = Pares(boardrows, boardcols)

    elif serie == 6:
        # Caso impar
        print("Inside impares case")
        numbers = Impares(boardrows, boardcols)

    return numbers


def checkSolved(board):
    aux = -1
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            #print(board[i][j])
            if board[i][j] == None:
                continue
            if board[i][j] < aux:
                return False
            aux = board[i][j]

    return True


def getSolution(serie, boardrows, boardcols):
    numbers = getSeriesNumbers(serie, boardrows, boardcols)
    counter = 0
    board = []
    max = -1
    maxpos = (-1, -1)
    for x in range(boardrows):
        column = []
        for y in range(boardcols):
            if numbers[counter] >= max:
                max = numbers[counter]
                maxpos = (x, y)
            column.append(numbers[counter])
            counter += 1
        board.append(column)

    board[maxpos[0]][maxpos[1]] = None
    return board

def createBoard(serie, boardrows, boardcols):

    numbers = getSeriesNumbers(serie, boardrows, boardcols)
    # Se mezclan los numeros para que queden en desorden
    numbers = random.sample(numbers, len(numbers))
    #print("numbers shuffled:", numbers)

    counter = 0
    board = []
    max = -1
    maxpos = (-1, -1)
    for x in range(boardrows):
        column = []
        for y in range(boardcols):
            if numbers[counter] >= max:
                max = numbers[counter]
                maxpos = (x, y)
            column.append(numbers[counter])
            counter += 1
        board.append(column)

    board[maxpos[0]][maxpos[1]] = None
    return board


def get_blank_position(board):
    # Return the x and y of board coordinates of the blank space.
    for x in range(len(board[0])):
        for y in range(len(board)):
            if board[x][y] == None:
                return (x, y)


def is_valid_move(board, move):
    blankx, blanky = get_blank_position(board)
    if move == UP:
        if blankx == (len(board) - 1):
            return False
    elif move == DOWN:
        if blankx == 0:
            return False
    elif move == LEFT:
        if blanky == (len(board[0]) - 1):
            return False
    elif move == RIGHT:
        #print(len(board[0]))
        if blanky == 0:
            return False

    return True
    '''
    return (move == UP and blanky != len(board[0]) - 1) or \
           (move == DOWN and blanky != 0) or \
           (move == LEFT and blankx != len(board) - 1) or \
           (move == RIGHT and blankx != 0)
    '''


def make_move(board, move):
    # This function does not check if the move is valid.
    blankx, blanky = get_blank_position(board)
    if move == UP:
        aux = board[blankx+1][blanky]
        board[blankx + 1][blanky] = board[blankx][blanky]
        board[blankx][blanky] = aux
    elif move == DOWN:
        aux = board[blankx-1][blanky]
        board[blankx - 1][blanky] = board[blankx][blanky]
        board[blankx][blanky] = aux
    elif move == LEFT:
        aux = board[blankx][blanky + 1]
        board[blankx][blanky + 1] = board[blankx][blanky]
        board[blankx][blanky] = aux
    elif move == RIGHT:
        aux = board[blankx][blanky - 1]
        board[blankx][blanky - 1] = board[blankx][blanky]
        board[blankx][blanky] = aux

    '''
    if move == UP:
        board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
    elif move == DOWN:
        board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
    elif move == LEFT:
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
    elif move == RIGHT:
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]
    '''


def text_objects(text, font):
    textSurface = font.render(text, True, CafeOscuro)
    return textSurface, textSurface.get_rect()


# Función para que funcionen los botones
def oprimido(x, y, w, h, ic, tam, serie, modo, action=None): # De parametros se tiene las cordenadas, el color y la palabra clave que indica la acción
    # print("ADENTRO DE FUNCION OPRIMIDO")
    # print("Action:", action)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y: # Revisa si el mouse está sobre el botón
        if click[0] == 1 and action != None: # Revisa si se hizo click
            # Funcion de juego
            if action == "jugar":
                print("Tablero con tamaño: ", tam)
                print("Serie escogida: ", serie)
                print("Modo de juego: ", modo)
                juego(tam, serie, modo)

            if action == "nuevojuego":
                return True

            if action == "sol":
                return True

            if action == "solu":
                print("ADENTRO DE ACTION SOLU IF")
                return True
            # Si se seleccionan los tamaños
            if action == "cinco":
                return True
            if action == "tres":
                return True
            if action == "cuatro":
                return True

            # Modo de juego
            if action == "ave":
                return True
            if action == "desa":
                return True

            # Series
            if action == "prim":
                return True
            if action == "pot":
                return True
            if action == "cuad":
                return True
            if action == "fibo":
                return True
            if action == "par":
                return True
            if action == "impar":
                return True


def oprimidotam(x, y, w, h, ic, tam, action=None): # De parametros se tiene las cordenadas, el color y la palabra clave que indica la acción
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y: # Revisa si el mouse está sobre el botón
        if click[0] == 1 and action != None: # Revisa si se hizo click
            if action == "tres":
                pygame.draw.rect(DISP, ic, (x, y, w, h))
                nuevo = pygame.font.Font('freesansbold.ttf', 17)
                TextSurf, TextRect = text_objects("Se selccionó tamaño = 3", nuevo)
                TextRect.center = (850 + (50 / 2), 10 + (50 / 2))
                DISP.blit(TextSurf, TextRect)
                print("El tamaño ahora es:", tam)
            if action == "cuatro":
                pygame.draw.rect(DISP, ic, (x, y, w, h))
                nuevo = pygame.font.Font('freesansbold.ttf', 17)
                TextSurf, TextRect = text_objects("Se selccionó tamaño = 4", nuevo)
                TextRect.center = (850 + (50 / 2), 10 + (50 / 2))
                DISP.blit(TextSurf, TextRect)
                print("El tamaño ahora es:", tam)
            if action == "cinco":
                pygame.draw.rect(DISP, ic, (x, y, w, h))
                nuevo = pygame.font.Font('freesansbold.ttf', 17)
                TextSurf, TextRect = text_objects("Se selccionó tamaño = 5", nuevo)
                TextRect.center = (850 + (50 / 2), 10 + (50 / 2))
                DISP.blit(TextSurf, TextRect)
                print("El tamaño ahora es:", tam)
    return tam


def oprimidoserie(x, y, w, h, ic, serie, action=None): # De parametros se tiene las cordenadas, el color y la palabra clave que indica la acción
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y: # Revisa si el mouse está sobre el botón
        if click[0] == 1 and action != None: # Revisa si se hizo click
            if action == "fibo":
                pygame.draw.rect(DISP, ic, (x, y, w, h))
                nuevo = pygame.font.Font('freesansbold.ttf', 17)
                TextSurf, TextRect = text_objects("Se seleccionó la serie Fibonacci", nuevo)
                TextRect.center = (500 + (50 / 2), 10 + (50 / 2))
                DISP.blit(TextSurf, TextRect)
                print("La serie ahora es:", serie)
            if action == "cuad":
                pygame.draw.rect(DISP, ic, (x, y, w, h))
                nuevo = pygame.font.Font('freesansbold.ttf', 17)
                TextSurf, TextRect = text_objects("Se seleccionó la serie Cuadrada", nuevo)
                TextRect.center = (500 + (50 / 2), 10 + (50 / 2))
                DISP.blit(TextSurf, TextRect)
                print("La serie ahora es:", serie)
            if action == "prim":
                pygame.draw.rect(DISP, ic, (x, y, w, h))
                nuevo = pygame.font.Font('freesansbold.ttf', 17)
                TextSurf, TextRect = text_objects("Se seleccionó la serie Pirmos", nuevo)
                TextRect.center = (500 + (50 / 2), 10 + (50 / 2))
                DISP.blit(TextSurf, TextRect)
                print("La serie ahora es:", serie)
            if action == "pot":
                pygame.draw.rect(DISP, ic, (x, y, w, h))
                nuevo = pygame.font.Font('freesansbold.ttf', 17)
                TextSurf, TextRect = text_objects("Se seleccionó la serie Potencias", nuevo)
                TextRect.center = (500 + (50 / 2), 10 + (50 / 2))
                DISP.blit(TextSurf, TextRect)
                print("La serie ahora es:", serie)
            if action == "par":
                pygame.draw.rect(DISP, ic, (x, y, w, h))
                nuevo = pygame.font.Font('freesansbold.ttf', 17)
                TextSurf, TextRect = text_objects("Se seleccionó la serie Par", nuevo)
                TextRect.center = (500 + (50 / 2), 10 + (50 / 2))
                DISP.blit(TextSurf, TextRect)
                print("La serie ahora es:", serie)
            if action == "impar":
                pygame.draw.rect(DISP, ic, (x, y, w, h))
                nuevo = pygame.font.Font('freesansbold.ttf', 17)
                TextSurf, TextRect = text_objects("Se seleccionó la serie Impar", nuevo)
                TextRect.center = (500 + (50 / 2), 10 + (50 / 2))
                DISP.blit(TextSurf, TextRect)
                print("La serie ahora es:", serie)
    return serie


def oprimidomodo(x, y, w, h, ic, modo, action=None): # De parametros se tiene las cordenadas, el color y la palabra clave que indica la acción
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y: # Revisa si el mouse está sobre el botón
        if click[0] == 1 and action != None: # Revisa si se hizo click
            if action == "ave":
                pygame.draw.rect(DISP, ic, (x, y, w, h))
                nuevo = pygame.font.Font('freesansbold.ttf', 17)
                TextSurf, TextRect = text_objects("Se seleccionó el modo Aventura", nuevo)
                TextRect.center = (170 + (50 / 2), 10 + (50 / 2))
                DISP.blit(TextSurf, TextRect)
                print("El modo ahora es:", modo)
            if action == "desa":
                pygame.draw.rect(DISP, ic, (x, y, w, h))
                nuevo = pygame.font.Font('freesansbold.ttf', 17)
                TextSurf, TextRect = text_objects("Se seleccionó el modo Desafio", nuevo)
                TextRect.center = (170 + (50 / 2), 10 + (50 / 2))
                DISP.blit(TextSurf, TextRect)
                print("El modo ahora es:", modo)
    return modo


def getBlankPosition(board):
    # Return the x and y of board coordinates of the blank space.
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == None:
                return (x, y)


def getLeftTopOfTile(tileX, tileY):
    left = BOARDX + (tileX * TILESIZE) + (tileX - 1)
    top = BOARDY + (tileY * TILESIZE) + (tileY - 1)

    return (left, top)


def getSpotClicked(board, x, y):
    # from the x & y pixel coordinates, get the x & y board coordinates
    for tileX in range(len(board)):
        for tileY in range(len(board[0])):
            left, top = getLeftTopOfTile(tileX, tileY)
            print(left, top)
            tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
            if tileRect.collidepoint(x, y):
                return (tileX, tileY)

    return (None, None)


# Función de la pantalla de inicio. Contiene todas las instrucciones para dibujar la pantalla de inicio
def game_intro():
    intro = True
    tam = 3
    serie = 1
    modo = 1

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



        # Texto inicio
        titulo = pygame.font.Font('freesansbold.ttf', 70)
        TextSurf, TextRect = text_objects("Scientific Puzzle", titulo)
        TextRect.center = ((ancho / 2), (alto / 6))
        DISP.blit(TextSurf, TextRect)

        mod = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("Modo de juego", mod)
        TextRect.center = ((ancho / 2), 250)
        DISP.blit(TextSurf, TextRect)

        tamano = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("Tamaño del tablero", tamano)
        TextRect.center = ((ancho / 2), 350)
        DISP.blit(TextSurf, TextRect)

        ser = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("Serie numérica", ser)
        TextRect.center = ((ancho / 2), 450)
        DISP.blit(TextSurf, TextRect)

        # Botones de inicio
        pygame.draw.rect(DISP, Naranja, (400, 150, 230, 50))

        # Botones de seleccionar
        # Modo
        pygame.draw.rect(DISP, Naranja, (325, 275, 140, 50))
        pygame.draw.rect(DISP, Naranja, (525, 275, 140, 50))
        # Tamaño
        pygame.draw.rect(DISP, Naranja, (225, 375, 140, 50))
        pygame.draw.rect(DISP, Naranja, (425, 375, 140, 50))
        pygame.draw.rect(DISP, Naranja, (625, 375, 140, 50))
        # Serie
        pygame.draw.rect(DISP, Naranja, (75, 475, 140, 50))
        pygame.draw.rect(DISP, Naranja, (225, 475, 140, 50))
        pygame.draw.rect(DISP, Naranja, (375, 475, 140, 50))
        pygame.draw.rect(DISP, Naranja, (525, 475, 140, 50))
        pygame.draw.rect(DISP, Naranja, (675, 475, 140, 50))
        pygame.draw.rect(DISP, Naranja, (825, 475, 140, 50))

        # Texto botones:
        jueg = pygame.font.Font('freesansbold.ttf', 25)
        TextSurf, TextRect = text_objects("Jugar", jueg)
        TextRect.center = (400 + (230 / 2), 150 + (50 / 2))
        DISP.blit(TextSurf, TextRect)
        oprimido(400, 150, 230, 50, Blanco, tam, serie, modo, "jugar") # Para que el boton funcione al ser oprimido

        # Modo juego
        aventura = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Aventura", aventura)
        TextRect.center = (325 + (140 / 2), 275 + (50 / 2))
        DISP.blit(TextSurf, TextRect)
        if oprimido(325, 275, 140, 50, Blanco, tam, serie, modo, "ave"):
            modo = oprimidomodo(325, 275, 140, 50, Blanco, 1, "ave")

        desafio = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Desafio", desafio)
        TextRect.center = (525 + (140 / 2), 275 + (50 / 2))
        DISP.blit(TextSurf, TextRect)
        if oprimido(525, 275, 140, 50, Blanco, tam, serie, modo, "desa"):
            modo = oprimidomodo(525, 275, 140, 50, Blanco, 2, "desa")

        # Tamaño
        x3 = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("3x3", x3)
        TextRect.center = (225 + (140 / 2), 375 + (50 / 2))
        DISP.blit(TextSurf, TextRect)
        if oprimido(225, 375, 140, 50, Blanco, tam, serie, modo, "tres"):
            tam = oprimidotam(225, 375, 140, 50, Blanco, 3, "tres")

        x4 = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("4x4", x4)
        TextRect.center = (425 + (140 / 2), 375 + (50 / 2))
        DISP.blit(TextSurf, TextRect)
        if oprimido(425, 375, 140, 50, Blanco, tam, serie, modo, "cuatro"):
            tam = oprimidotam(425, 375, 140, 50, Blanco, 4, "cuatro")

        x5 = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("5x5", x5)
        TextRect.center = (625 + (140 / 2), 375 + (50 / 2))
        DISP.blit(TextSurf, TextRect)
        if oprimido(625, 375, 140, 50, Blanco, tam, serie, modo, "cinco"):
            tam = oprimidotam(625, 375, 140, 50, Blanco, 5, "cinco")

        # Series
        fib = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Fibonacci", fib)
        TextRect.center = (75 + (140 / 2), 475 + (50 / 2))
        DISP.blit(TextSurf, TextRect)
        if oprimido(75, 475, 140, 50, Blanco, tam, serie, modo, "fibo"):
            serie = oprimidoserie(75, 475, 140, 50, Blanco, 1, "fibo")

        cuad = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Cuadrada", cuad)
        TextRect.center = (225 + (140 / 2), 475 + (50 / 2))
        DISP.blit(TextSurf, TextRect)
        if oprimido(225, 475, 140, 50, Blanco, tam, serie, modo, "cuad"):
            serie = oprimidoserie(225, 475, 140, 50, Blanco, 2, "cuad")

        prim = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Primos", prim)
        TextRect.center = (375 + (140 / 2), 475 + (50 / 2))
        DISP.blit(TextSurf, TextRect)
        if oprimido(375, 475, 140, 50, Blanco, tam, serie, modo, "prim"):
            serie = oprimidoserie(375, 475, 140, 50, Blanco, 3, "prim")

        pot = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Potencias 2", pot)
        TextRect.center = (525 + (140 / 2), 475 + (50 / 2))
        DISP.blit(TextSurf, TextRect)
        if oprimido(525, 475, 140, 50, Blanco, tam, serie, modo, "pot"):
            serie = oprimidoserie(525, 475, 140, 50, Blanco, 4, "pot")

        par = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Pares", par)
        TextRect.center = (675 + (140 / 2), 475 + (50 / 2))
        DISP.blit(TextSurf, TextRect)
        if oprimido(675, 475, 140, 50, Blanco, tam, serie, modo, "par"):
            serie = oprimidoserie(675, 475, 140, 50, Blanco, 5, "par")

        impar = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Impares", impar)
        TextRect.center = (825 + (140 / 2), 475 + (50 / 2))
        DISP.blit(TextSurf, TextRect)
        if oprimido(825, 475, 140, 50, Blanco, tam, serie, modo, "impar"):
            serie = oprimidoserie(825, 475, 140, 50, Blanco, 6, "impar")

        pygame.display.update()
        clock.tick(15)


# Función del juego. Contiene todas las instrucciones para que se desarrolle el juego correctamente.
def juego(tam, serie, modo):

    board = createBoard(serie, tam, tam)  # Retorna la matriz de numeros
    # print("Tamaño:", tam)
    # print("Serie:", serie)
    # print("Modo:", modo)
    running = True
    resuelto = False
    timeOver = False
    show_solution = False
    start_time = time.time()

    while running:
        DISP.fill(Cafesito)

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                running = False
                sys: exit()

            if event.type == pygame.MOUSEBUTTONUP:
                print("Mouse event")
                spotx, spoty = getSpotClicked(board, event.pos[0], event.pos[1])
                print(spotx, spoty)
                blankx, blanky = getBlankPosition(board)
                print(blankx, blanky)

                if spotx == blankx + 1 and spoty == blanky:
                    slide_to = LEFT
                    make_move(board, slide_to)
                elif spotx == blankx - 1 and spoty == blanky:
                    slide_to = RIGHT
                    make_move(board, slide_to)
                elif spotx == blankx and spoty == blanky + 1:
                    slide_to = UP
                    make_move(board, slide_to)
                elif spotx == blankx and spoty == blanky - 1:
                    slide_to = DOWN
                    make_move(board, slide_to)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and is_valid_move(board, LEFT):
                    print("Movimiento valido LEFT")
                    slide_to = LEFT
                    make_move(board, slide_to)
                if event.key == pygame.K_RIGHT and is_valid_move(board, RIGHT):
                    print("Movimiento valido RIGHT")
                    slide_to = RIGHT
                    make_move(board, slide_to)
                if event.key == pygame.K_UP and is_valid_move(board, UP):
                    print("Movimiento valido UP")
                    slide_to = UP
                    make_move(board, slide_to)
                if event.key == pygame.K_DOWN and is_valid_move(board, DOWN):
                    print("Movimiento valido DOWN")
                    slide_to = DOWN
                    make_move(board, slide_to)

        '''
        if slide_to:
            make_move()
        '''
        #print(board)
        #print(type(board))

        if resuelto == False:
            if timeOver == False:
                elapsed_time = time.time() - start_time
                #print("TIEMPO:", elapsed_time)

                board_surface = create_board_surface(tam)
                # Dibuja las tiles en el surface del board:
                create_tiles(board_surface, board, TILESIZE, tam, tam)
                # Dibuja el surface del board en la pantalla:
                drawBoardSurface(DISP, board_surface, BOARDX / 2, BOARDY / 2)
                # Chequea si se resolvió el juego:
                if show_solution == False:
                    resuelto = checkSolved(board)
                else:
                    # Dibujar el letrero "SOLUCION:"
                    solution_sign = pygame.font.Font('freesansbold.ttf', 17)
                    solution_text = solution_sign.render("SOLUCION:", True, (0, 255, 0))
                    DISP.blit(solution_text, (130, 130))

                #print("Resuelto?", resuelto)

                pygame.draw.rect(DISP, Naranja, (250, 50, 230, 50))
                pygame.draw.rect(DISP, Naranja, (550, 50, 230, 50))

                nuevo = pygame.font.Font('freesansbold.ttf', 25)
                TextSurf, TextRect = text_objects("Nuevo juego", nuevo)
                TextRect.center = (250 + (230 / 2), 50 + (50 / 2))
                DISP.blit(TextSurf, TextRect)
                oprimido(250, 50, 230, 50, Blanco, tam, serie, modo, "nuevojuego")  # Para que el boton funcione al ser oprimido
                if oprimido(250, 50, 230, 50, Blanco, tam, serie, modo, action="nuevojuego"):
                    print("SE CLIQUEO NUEVO JUEGOOOOO")
                    board = createBoard(serie, tam, tam)  # Retorna la matriz de numeros
                    start_time = time.time()
                    show_solution = False

                solucion = pygame.font.Font('freesansbold.ttf', 25)
                TextSurf, TextRect = text_objects("Mostrar solución", solucion)
                TextRect.center = (550 + (230 / 2), 50 + (50 / 2))
                DISP.blit(TextSurf, TextRect)
                #oprimido(550, 150, 230, 50, Blanco, tam, serie, modo, "solu")
                if oprimido(550, 50, 230, 50, Blanco, tam, serie, modo, action="solu"):
                    print("SE CLIQUEO SOLUCIOOOOOOON")
                    board = getSolution(serie, tam, tam)
                    show_solution = True


                if serie == 1:
                    a = pygame.font.Font('freesansbold.ttf', 17)
                    TextSurf, TextRect = text_objects("Está jugando con la serie: Fibonacci", a)
                    TextRect.center = (125 + (50 / 2), 10 + (50 / 2))
                    DISP.blit(TextSurf, TextRect)
                if serie == 2:
                    b = pygame.font.Font('freesansbold.ttf', 17)
                    TextSurf, TextRect = text_objects("Está jugando con la serie: Cuadrada", b)
                    TextRect.center = (125 + (50 / 2), 10 + (50 / 2))
                    DISP.blit(TextSurf, TextRect)
                if serie == 3:
                    c = pygame.font.Font('freesansbold.ttf', 17)
                    TextSurf, TextRect = text_objects("Está jugando con la serie: Primos", c)
                    TextRect.center = (125 + (50 / 2), 10 + (50 / 2))
                    DISP.blit(TextSurf, TextRect)
                if serie == 4:
                    d = pygame.font.Font('freesansbold.ttf', 17)
                    TextSurf, TextRect = text_objects("Está jugando con la serie: Potencias", d)
                    TextRect.center = (125 + (50 / 2), 10 + (50 / 2))
                    DISP.blit(TextSurf, TextRect)
                if serie == 5:
                    e = pygame.font.Font('freesansbold.ttf', 17)
                    TextSurf, TextRect = text_objects("Está jugando con la serie: Par", e)
                    TextRect.center = (125 + (50 / 2), 10 + (50 / 2))
                    DISP.blit(TextSurf, TextRect)

                if serie == 6:
                    f = pygame.font.Font('freesansbold.ttf', 17)
                    TextSurf, TextRect = text_objects("Está jugando con la serie: Impar", f)
                    TextRect.center = (125 + (50 / 2), 10 + (50 / 2))
                    DISP.blit(TextSurf, TextRect)

                if modo == 1:
                    g = pygame.font.Font('freesansbold.ttf', 17)
                    TextSurf, TextRect = text_objects("Modo Aventura", g)
                    TextRect.center = (75 + (50 / 2), 30 + (50 / 2))
                    DISP.blit(TextSurf, TextRect)

                    #Para mostrar el tiempo progresivo:
                    progressiveTime = pygame.font.Font('freesansbold.ttf', 17)
                    elapsed_time = int(elapsed_time)
                    elapsed_time =  str(datetime.timedelta(seconds=elapsed_time))
                    #elapsed_time = "Tiempo transcurrido: " + str(int(elapsed_time))
                    elapsed_time = "Tiempo transcurrido: " + elapsed_time
                    TextSurf, TextRect = text_objects(elapsed_time, progressiveTime)
                    TextRect.center = (150, alto-40)
                    DISP.blit(TextSurf, TextRect)
                    #print("Buenaa")
                if modo == 2:
                    m = pygame.font.Font('freesansbold.ttf', 17)
                    TextSurf, TextRect = text_objects("Modo Desafio", m)
                    TextRect.center = (75 + (50 / 2), 30 + (50 / 2))
                    DISP.blit(TextSurf, TextRect)

                    # Para mostrar el tiempo progresivo:
                    regressiveTime = pygame.font.Font('freesansbold.ttf', 17)
                    max_time = 60 * 5 # Representa los 5 minutos de tiempo limite
                    elapsed_time = int(elapsed_time)
                    timeCounter = max_time - elapsed_time
                    time_to_show =  max_time - elapsed_time
                    time_to_show= str(datetime.timedelta(seconds=time_to_show))
                    time_to_show = "Tiempo restante: " + time_to_show
                    # elapsed_time = "Tiempo transcurrido: " + str(int(elapsed_time))
                    TextSurf, TextRect = text_objects(time_to_show, regressiveTime)
                    TextRect.center = (150, alto - 40)
                    DISP.blit(TextSurf, TextRect)

                    if timeCounter <= 0:
                        timeOver = True
            else:
                m = pygame.font.Font('freesansbold.ttf', 17)
                TextSurf, TextRect = text_objects("Tu tiempo se ha agotado, perdiste. :(", m)
                TextRect.center = (ancho / 2, alto / 2)
                DISP.blit(TextSurf, TextRect)
        else:
            if show_solution == False:
                congrats_sign = pygame.font.Font('freesansbold.ttf', 50)
                congrats_text = congrats_sign.render("Felicidades! Ganaste el juego!", True, (0, 255, 0))
                DISP.blit(congrats_text, (ancho/2 - 340, alto/2 - 100))


                # m = pygame.font.Font('freesansbold.ttf', 17)
                # TextSurf, TextRect = text_objects("Felicidades! Ganaste el juego!", m)
                # TextRect.center = (ancho/2, alto/2)
                # DISP.blit(TextSurf, TextRect)

        pygame.display.update()




game_intro()
pygame.quit()
quit()
