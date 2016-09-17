#Arvutimängud lõputöö
#Kivi-paber-käärid
#Tarvo Mäaesepp 2016

import pygame, random, time, sys

#Ekraan
pygame.init()
ekraan = pygame.display.set_mode((640, 480))
ekraan.fill((246, 231, 195))


#Funktsiooni esileht elemendid
header = pygame.image.load("header.png") #493x71 px
alusta = pygame.image.load("alusta.png") #287x60 px
alusta2 = pygame.image.load("alusta2.png") #287x60 px

võite = pygame.image.load("voite.png") #104x49px
viike = pygame.image.load("viike.png") #94x46px
kaotusi = pygame.image.load("kaotusi.png") #150x46px

#Funktsioon tekst elemendid
font = pygame.font.Font("Kelson Sans Bold.otf", 60)

#Funktsioondide valik ja arvuti elemendid
kivi = pygame.image.load("kivi.png") #128x128px
paber = pygame.image.load("paber.png") #128x128px
käärid = pygame.image.load("k22rid.png") #128x128px

kivi2 = pygame.image.load("kivi2.png") #128x128px
paber2 = pygame.image.load("paber2.png") #128x128px
käärid2 = pygame.image.load("k22rid2.png") #128x128px

teevalik = pygame.image.load("teevalik.png") #290x83px
arvutivalik = pygame.image.load("arvutivalik.png") #384x83px

#Helid
heli_valik = pygame.mixer.Sound("vajutus.wav")
heli_võit = pygame.mixer.Sound("voit.ogg")
heli_viik = pygame.mixer.Sound("viik.wav")
heli_kaotus = pygame.mixer.Sound("kaotus.wav")

#Muutujuad
inimese_valik = "tühi hetkel"
arvuti_valik = "tühi hetkel"

võite1 = 0
viike1 = 0
kaotusi1 = 0

#Funktsiooni lõpp elemendid
võit = pygame.image.load("voit.png") #167x57px
viik = pygame.image.load("viik.png") #99X61px
kaotus = pygame.image.load("kaotus.png") #200x57px
    
def esileht():
    ekraan.fill((246, 231, 195))
    ekraan.blit(header, (73.5, 40))
    mx, my = pygame.mouse.get_pos()
    a = (640-287)/2
    b = 150
    if a < mx < a+287 and b < my <b+60:
        ekraan.blit(alusta2, (a, b))
    else:
        ekraan.blit(alusta, (a, b))
    ekraan.blit(võite, (160-(104/2), 275))
    tekst(str(võite1), 140)
    ekraan.blit(viike, (320-(94/2), 275))
    tekst(str(viike1), 305)
    ekraan.blit(kaotusi, (480-(150/2), 275))
    tekst(str(kaotusi1), 465)
    pygame.display.flip()

def tekst(tekst, xkoordinaat):
    ekraani_tekst = font.render(tekst, True, (51, 51, 51))
    ekraan.blit(ekraani_tekst, [xkoordinaat ,325])

def valik():
    ekraan.fill((246, 231, 195))
    mx, my = pygame.mouse.get_pos()
    a=(640-3*128)/4
    b=30+83+(480-83-30-128)/2
    ekraan.blit(teevalik, ((640-290)/2, 30))
    if i.type == pygame.MOUSEBUTTONDOWN and a < mx < a + 128 and b < my < b+128:
        heli_valik.play()
        global inimese_valik
        inimese_valik = "kivi"
    if a < mx < a + 128 and b < my < b+128:
        ekraan.blit(kivi2, (a, b))
    else:
        ekraan.blit(kivi, (a, b))
    if i.type == pygame.MOUSEBUTTONDOWN and a*2+128 < mx < a*2+128*2 and b < my < b + 128:
        heli_valik.play()
        global inimese_valik
        inimese_valik = "paber"
    if a*2+128 < mx < a*2+128*2 and b < my < b + 128:
        ekraan.blit(paber2, (a*2+128, b))
    else:
        ekraan.blit(paber, (a*2+128, b))
    if i.type == pygame.MOUSEBUTTONDOWN and a*3+128*2 < mx < a*3+128*4 and b < my < b+128:
        heli_valik.play()
        global inimese_valik
        inimese_valik = "käärid"
    if a*3+128*2 < mx < a*3+128*4 and b < my < b+128:
        ekraan.blit(käärid2, (a*3+128*2, b))
    else:
        ekraan.blit(käärid, (a*3+128*2, b))
    pygame.display.flip()
    
def arvuti():
    ekraan.fill((246, 231, 195))
    ekraan.blit(arvutivalik, ((640-384)/2, 30))
    pygame.display.flip()
    x = random.randint(0, 2)
    a=(640-128)/2
    b=30+83+(480-83-30-128)/2
    time.sleep(1.5)
    global arvuti_valik
    if x == 0:
        ekraan.blit(kivi, (a, b))
        pygame.display.flip()
        arvuti_valik = "kivi"
    elif x == 1:
        ekraan.blit(paber, (a, b))
        pygame.display.flip()
        arvuti_valik = "paber"
    elif x == 2:
        ekraan.blit(käärid, (a, b))
        pygame.display.flip()
        arvuti_valik = "käärid"
    time.sleep(1.5)

def lõpp():
    ekraan.fill((246, 231, 195))
    global võite1
    global viike1
    global kaotusi1
    if inimese_valik == arvuti_valik:
        ekraan.blit(viik, ((640-99)/2, 180))
        pygame.display.flip()
        heli_viik.play()
        viike1 += 1
    elif inimese_valik == "kivi" and arvuti_valik == "paber":
        ekraan.blit(kaotus, ((640-200)/2, 180))
        pygame.display.flip()
        heli_kaotus.play()
        kaotusi1 += 1
    elif inimese_valik == "kivi" and arvuti_valik == "käärid":
        ekraan.blit(võit, ((640-167)/2, 180))
        pygame.display.flip()
        heli_võit.play()
        võite1 += 1
    elif inimese_valik == "paber" and arvuti_valik == "kivi":
        ekraan.blit(võit, ((640-167)/2, 180))
        pygame.display.flip()
        heli_võit.play()
        võite1 += 1
    elif inimese_valik == "paber" and arvuti_valik == "käärid":
        ekraan.blit(kaotus, ((640-200)/2, 180))
        pygame.display.flip()
        heli_kaotus.play()
        kaotusi1 += 1
    elif inimese_valik == "käärid" and arvuti_valik == "kivi":
        ekraan.blit(kaotus, ((640-200)/2, 180))
        pygame.display.flip()
        heli_kaotus.play()
        kaotusi1 += 1
    elif inimese_valik == "käärid" and arvuti_valik == "paber":
        ekraan.blit(võit, ((640-167)/2, 180))
        pygame.display.flip()
        heli_võit.play()
        võite1 += 1
    time.sleep(2)           
     
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        mx, my = pygame.mouse.get_pos()
        esileht()
        x = (640-287)/2
        y = 150
        if i.type == pygame.MOUSEBUTTONDOWN and x < mx < x+287 and y < my <y+60:
            heli_valik.play()
            k = True
            while  k == True:
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                       pygame.quit()
                mx, my = pygame.mouse.get_pos()
                valik()
                x=(640-3*128)/4
                y=30+83+(480-83-30-128)/2
                if i.type == pygame.MOUSEBUTTONDOWN and x < mx < x + 128 and y < my < y+128:
                    e = True
                    while e == True:
                        for i in pygame.event.get():
                            if i.type == pygame.QUIT:
                                pygame.quit()
                            valik1 = "kivi"
                            arvuti()
                            lõpp()
                            e = False
                            k = False
                    
                if i.type == pygame.MOUSEBUTTONDOWN and x*2+128 < mx < x*2+128 + 128 and y < my < y+128:
                    e = True
                    while e == True:
                        for i in pygame.event.get():
                            if i.type == pygame.QUIT:
                                pygame.quit()
                            valik1 = "paber"
                            arvuti()
                            lõpp()
                            e = False
                            k = False
                    
                if i.type == pygame.MOUSEBUTTONDOWN and x*3+128*2 < mx < x*3+128*2 + 128 + 128 and y < my < y+128:
                    e = True
                    while e == True:
                        for i in pygame.event.get():
                            if i.type == pygame.QUIT:
                                pygame.quit()
                            valik1 = "käärid"
                            arvuti()

                            lõpp()
                            e = False
                            k = False
                    
               
