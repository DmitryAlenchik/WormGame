#ЧервьЯрикV1

import pygame
import random
pygame.init()
 
width = 1280
height = 720
display = pygame.display.set_mode((width, height))
 
pygame.display.update()
pygame.display.set_caption("Игра про червя Ярика")

colors = {
    "worm_head": (210, 105, 30),
    "worm_tail": (139, 69, 19),
    "apple": (0, 255, 0)
}
 
#Позиция червя Ярика
worm_pos = {
    "x": width/2-10,
    "y": height/2-10,
    "x_change": 0,
    "y_change": 0
}
 
#Размер червя Ярика
worm_size = (10, 10)

worm_speed = 5
 
worm_tails = []
 
worm_pos["x_change"] = -worm_speed
for i in range(75):
    worm_tails.append([worm_pos["x"] + 10*i, worm_pos["y"]])
 
# Едааа
food_pos = {
    "x": round(random.randrange(0, width - worm_size[0]) / 10) * 10,
    "y": round(random.randrange(0, height - worm_size[1]) / 10) * 10,
}

food_size = (10, 10)
food_eaten = 0
 
game_end = False
clock = pygame.time.Clock()
 
while not game_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and worm_pos["x_change"] == 0:
                worm_pos["x_change"] = -worm_speed
                worm_pos["y_change"] = 0
 
            elif event.key == pygame.K_RIGHT and worm_pos["x_change"] == 0:
                worm_pos["x_change"] = worm_speed
                worm_pos["y_change"] = 0
 
            elif event.key == pygame.K_UP and worm_pos["y_change"] == 0:
                worm_pos["x_change"] = 0
                worm_pos["y_change"] = -worm_speed
 
            elif event.key == pygame.K_DOWN and worm_pos["y_change"] == 0:
                worm_pos["x_change"] = 0
                worm_pos["y_change"] = worm_speed
 
    display.fill((0,0,0))
 
    ltx = worm_pos["x"]
    lty = worm_pos["y"]
 
    for i,v in enumerate(worm_tails):
        _ltx = worm_tails[i][0]
        _lty = worm_tails[i][1]
 
        worm_tails[i][0] = ltx
        worm_tails[i][1] = lty
 
        ltx = _ltx
        lty = _lty
 
    for t in worm_tails:
        pygame.draw.rect(display, colors["worm_tail"], [
            t[0],
            t[1],
            worm_size[0],
            worm_size[1]])

    worm_pos["x"] += worm_pos["x_change"]
    worm_pos["y"] += worm_pos["y_change"]
 
    if(worm_pos["x"] < -worm_size[0]):
        worm_pos["x"] = width
 
    elif(worm_pos["x"] > width):
        worm_pos["x"] = 0
 
    elif(worm_pos["y"] < -worm_size[1]):
        worm_pos["y"] = height
 
    elif(worm_pos["y"] > height):
        worm_pos["y"] = 0
 
    pygame.draw.rect(display, colors["worm_head"], [
        worm_pos["x"],
        worm_pos["y"],
        worm_size[0],
        worm_size[1]])
 
    pygame.draw.rect(display, colors["apple"], [
        food_pos["x"],
        food_pos["y"],
        food_size[0],
        food_size[1]])
 
    if(worm_pos["x"] == food_pos["x"]
        and worm_pos["y"] == food_pos["y"]):
        food_eaten += 1
        worm_tails.append([food_pos["x"], food_pos["y"]])
 
        food_pos = {
            "x": round(random.randrange(5, width - worm_size[0]) / 10) * 10,
            "y": round(random.randrange(5, height - worm_size[1]) / 10) * 10,
        }
 
    for i,v in enumerate(worm_tails):
        if(worm_pos["x"]+worm_pos["x_change"] == worm_tails[i][0]
            and worm_pos["y"]+worm_pos["y_change"] == worm_tails[i][1]):
            worm_tails = worm_tails[:i]
            break
 
    pygame.display.update()
    
#FPS60
    clock.tick(60)
    
pygame.quit()
quit()