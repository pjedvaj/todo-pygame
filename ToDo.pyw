import pygame
import sys
import json
pygame.init()
clock = pygame.time.Clock()

# window
pygame.display.set_caption("ToDo")
icon = pygame.image.load('./icon.ico')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((360, 480))
background_color = pygame.Color('#242424')
base_font = pygame.font.Font(None, 24)
text_color = pygame.Color('#FFFFFF')
alt_color = pygame.Color('#000000')

# load data
with open('list.json') as read_file:
    todo_text = json.load(read_file)

# rectangles
col0 = '#D33930'
col1 = '#D53F31'
col2 = '#D74C32'
col3 = '#D95B34'
col4 = '#DB6C37'
col5 = '#DD7C3A'
col6 = '#DF8D3D'
col7 = '#E29D41'
col8 = '#E5AC44'
col9 = '#E8BC48'

rect0 = pygame.Rect(0,0,360,48)
rect1 = pygame.Rect(0,48,360,48)
rect2 = pygame.Rect(0,96,360,48)
rect3 = pygame.Rect(0,144,360,48)
rect4 = pygame.Rect(0,192,360,48)
rect5 = pygame.Rect(0,240,360,48)
rect6 = pygame.Rect(0,288,360,48)
rect7 = pygame.Rect(0,336,360,48)
rect8 = pygame.Rect(0,384,360,48)
rect9 = pygame.Rect(0,432,360,48)

act0 = False
act1 = False
act2 = False
act3 = False
act4 = False
act5 = False
act6 = False
act7 = False
act8 = False
act9 = False

while True:
    # events
    for event in pygame.event.get():
        # save data on close
        if event.type == pygame.QUIT:
            with open('list.json','w') as write_file:
                json.dump(todo_text,write_file)
            pygame.quit()
            sys.exit()
        # mouse click activation
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect0.collidepoint(event.pos):
                act0 = True
            else:
                act0 = False
            if rect1.collidepoint(event.pos):
                act1 = True
            else:
                act1 = False
            if rect2.collidepoint(event.pos):
                act2 = True
            else:
                act2 = False
            if rect3.collidepoint(event.pos):
                act3 = True
            else:
                act3 = False
            if rect4.collidepoint(event.pos):
                act4 = True
            else:
                act4 = False
            if rect5.collidepoint(event.pos):
                act5 = True
            else:
                act5 = False
            if rect6.collidepoint(event.pos):
                act6 = True
            else:
                act6 = False
            if rect7.collidepoint(event.pos):
                act7 = True
            else:
                act7 = False
            if rect8.collidepoint(event.pos):
                act8 = True
            else:
                act8 = False
            if rect9.collidepoint(event.pos):
                act9 = True
            else:
                act9 = False
        # keyboard editing
        if event.type == pygame.KEYDOWN:
            if act0 == True:
                # delete characters
                if event.key == pygame.K_BACKSPACE:
                    todo_text['0'] = todo_text['0'][0:-1]
                # add characters
                else:
                    todo_text['0'] += event.unicode
                    # limit characters
                    if len(todo_text['0']) > 28:
                        todo_text['0'] = todo_text['0'][0:-1]
            if act1 == True:
                # delete characters
                if event.key == pygame.K_BACKSPACE:
                    todo_text['1'] = todo_text['1'][0:-1]
                # add characters
                else:
                    todo_text['1'] += event.unicode
                    # limit characters
                    if len(todo_text['1']) > 28:
                        todo_text['1'] = todo_text['1'][0:-1]
            if act2 == True:
                # delete characters
                if event.key == pygame.K_BACKSPACE:
                    todo_text['2'] = todo_text['2'][0:-1]
                # add characters
                else:
                    todo_text['2'] += event.unicode
                    # limit characters
                    if len(todo_text['2']) > 28:
                        todo_text['2'] = todo_text['2'][0:-1]
            if act3 == True:
                # delete characters
                if event.key == pygame.K_BACKSPACE:
                    todo_text['3'] = todo_text['3'][0:-1]
                # add characters
                else:
                    todo_text['3'] += event.unicode
                    # limit characters
                    if len(todo_text['3']) > 28:
                        todo_text['3'] = todo_text['3'][0:-1]
            if act4 == True:
                # delete characters
                if event.key == pygame.K_BACKSPACE:
                    todo_text['4'] = todo_text['4'][0:-1]
                # add characters
                else:
                    todo_text['4'] += event.unicode
                    # limit characters
                    if len(todo_text['4']) > 28:
                        todo_text['4'] = todo_text['4'][0:-1]
            if act5 == True:
                # delete characters
                if event.key == pygame.K_BACKSPACE:
                    todo_text['5'] = todo_text['5'][0:-1]
                # add characters
                else:
                    todo_text['5'] += event.unicode
                    # limit characters
                    if len(todo_text['0']) > 28:
                        todo_text['5'] = todo_text['5'][0:-1]
            if act6 == True:
                # delete characters
                if event.key == pygame.K_BACKSPACE:
                    todo_text['6'] = todo_text['6'][0:-1]
                # add characters
                else:
                    todo_text['6'] += event.unicode
                    # limit characters
                    if len(todo_text['6']) > 28:
                        todo_text['6'] = todo_text['6'][0:-1]
            if act7 == True:
                # delete characters
                if event.key == pygame.K_BACKSPACE:
                    todo_text['7'] = todo_text['7'][0:-1]
                # add characters
                else:
                    todo_text['7'] += event.unicode
                    # limit characters
                    if len(todo_text['7']) > 28:
                        todo_text['7'] = todo_text['7'][0:-1]
            if act8 == True:
                # delete characters
                if event.key == pygame.K_BACKSPACE:
                    todo_text['8'] = todo_text['8'][0:-1]
                # add characters
                else:
                    todo_text['8'] += event.unicode
                    # limit characters
                    if len(todo_text['8']) > 28:
                        todo_text['8'] = todo_text['8'][0:-1]
            if act9 == True:
                # delete characters
                if event.key == pygame.K_BACKSPACE:
                    todo_text['9'] = todo_text['9'][0:-1]
                # add characters
                else:
                    todo_text['9'] += event.unicode
                    # limit characters
                    if len(todo_text['9']) > 28:
                        todo_text['9'] = todo_text['9'][0:-1]

    # render background
    screen.fill(background_color)

    # render rectangles
    pygame.draw.rect(screen,col0,rect0)
    pygame.draw.rect(screen,col1,rect1)
    pygame.draw.rect(screen,col2,rect2)
    pygame.draw.rect(screen,col3,rect3)
    pygame.draw.rect(screen,col4,rect4)
    pygame.draw.rect(screen,col5,rect5)
    pygame.draw.rect(screen,col6,rect6)
    pygame.draw.rect(screen,col7,rect7)
    pygame.draw.rect(screen,col8,rect8)
    pygame.draw.rect(screen,col9,rect9)

    # render text

    if act0 == True:
        text_surface0 = base_font.render(todo_text['0'],True,(alt_color))
    else:
        text_surface0 = base_font.render(todo_text['0'],True,(text_color))
    screen.blit(text_surface0,(rect0.x + 16,rect0.y + 16))
    
    if act1 == True:
        text_surface1 = base_font.render(todo_text['1'],True,(alt_color))
    else:
        text_surface1 = base_font.render(todo_text['1'],True,(text_color))
    screen.blit(text_surface1,(rect1.x + 16,rect1.y + 16))
    
    if act2 == True:
        text_surface2 = base_font.render(todo_text['2'],True,(alt_color))
    else:
        text_surface2 = base_font.render(todo_text['2'],True,(text_color))
    screen.blit(text_surface2,(rect2.x + 16,rect2.y + 16))
    
    if act3 == True:
        text_surface3 = base_font.render(todo_text['3'],True,(alt_color))
    else:
        text_surface3 = base_font.render(todo_text['3'],True,(text_color))
    screen.blit(text_surface3,(rect3.x + 16,rect3.y + 16))
    
    if act4 == True:
        text_surface4 = base_font.render(todo_text['4'],True,(alt_color))
    else:
        text_surface4 = base_font.render(todo_text['4'],True,(text_color))
    screen.blit(text_surface4,(rect4.x + 16,rect4.y + 16))
    
    if act5 == True:
        text_surface5 = base_font.render(todo_text['5'],True,(alt_color))
    else:
        text_surface5 = base_font.render(todo_text['5'],True,(text_color))
    screen.blit(text_surface5,(rect5.x + 16,rect5.y + 16))
    
    if act6 == True:
        text_surface6 = base_font.render(todo_text['6'],True,(alt_color))
    else:
        text_surface6 = base_font.render(todo_text['6'],True,(text_color))
    screen.blit(text_surface6,(rect6.x + 16,rect6.y + 16))
    
    if act7 == True:
        text_surface7 = base_font.render(todo_text['7'],True,(alt_color))
    else:
        text_surface7 = base_font.render(todo_text['7'],True,(text_color))
    screen.blit(text_surface7,(rect7.x + 16,rect7.y + 16))
    
    if act8 == True:
        text_surface8 = base_font.render(todo_text['8'],True,(alt_color))
    else:
        text_surface8 = base_font.render(todo_text['8'],True,(text_color))
    screen.blit(text_surface8,(rect8.x + 16,rect8.y + 16))
    
    if act9 == True:
        text_surface9 = base_font.render(todo_text['9'],True,(alt_color))
    else:
        text_surface9 = base_font.render(todo_text['9'],True,(text_color))
    screen.blit(text_surface9,(rect9.x + 16,rect9.y + 16))

    pygame.display.flip()
    clock.tick(6)