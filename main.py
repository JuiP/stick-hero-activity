#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Stick Hero
# Copyright (C) 2015  Utkarsh Tiwari
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Utkarsh Tiwari    iamutkarshtiwari@gmail.com

import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pickle
import pygame
import sys
from gettext import gettext as _

from sugar3.activity.activity import get_activity_root

from math import *
from random import *

from scorescreen import *
from welcomescreen import *

from rules import *


class game:

    def make(self):

        pygame.init()
        sound = True

        try:
            pygame.mixer.init()
        except Exception as err:
            sound = False
            print('error with sound', err)

        black = (0, 0, 0)
        white = (255, 255, 255)
        clock = pygame.time.Clock()
        timer = pygame.time.Clock()

        crashed = False
        disp_width = 600
        disp_height = 600

        press = 0

        info = pygame.display.Info()
        gameDisplay = pygame.display.get_surface()
        w, h = gameDisplay.get_width() , gameDisplay.get_height()
        scale_x = w / 1280.0
        scale_y = h / 720.0


        if not(gameDisplay):

            gameDisplay = pygame.display.set_mode(
                (info.current_w, info.current_h))

            pygame.display.set_caption(_("Stick Hero"))
            gameicon = pygame.image.load('images/icon.png')
            pygame.display.set_icon(gameicon)

        hero = pygame.image.load("images/hero.png")
        hero = pygame.transform.scale(hero, (int(27 * scale_x), int(28 * scale_y)))
        herotr = hero

        hero1 = pygame.image.load("images/hero1.png")
        hero1 = pygame.transform.scale(hero1, (int(27 * scale_x), int(28 * scale_y)))
        hero2 = pygame.image.load("images/hero2.png")
        hero2 = pygame.transform.scale(hero2, (int(27 * scale_x), int(28 * scale_y)))
        hero3 = pygame.image.load("images/hero3.png")
        hero3 = pygame.transform.scale(hero3, (int(27 * scale_x), int(28 * scale_y)))

        herodown = pygame.transform.flip(hero, False, True)
        hero1down = pygame.transform.flip(hero1, False, True)
        hero2down = pygame.transform.flip(hero2, False, True)
        hero3down = pygame.transform.flip(hero3, False, True)

        scoreplate = pygame.image.load("images/scoreplate.png").convert()
        scoreplate = pygame.transform.scale(scoreplate, (int(108 * scale_x), int(61 * scale_y)))
        scoreplate.set_alpha(50)

        stick = pygame.image.load("images/stick.png").convert()
        stick = pygame.transform.scale(stick, (int(4 * scale_x), int(601 * scale_y)))
        # background=pygame.image.load("images/background.png").convert()
        alpha = pygame.image.load("images/alpha.png").convert()
        alpha = pygame.transform.scale(alpha, (int(105 * scale_x), int(248 * scale_y)))
        beta = pygame.image.load("images/beta.png").convert()
        beta = pygame.transform.scale(beta, (int(67 * scale_x), int(248 * scale_y)))
        gamma = pygame.image.load("images/gamma.png").convert()
        gamma = pygame.transform.scale(gamma, (int(37 * scale_x), int(248 * scale_y)))
        delta = pygame.image.load("images/delta.png").convert()
        delta = pygame.transform.scale(delta, (int(19 * scale_x), int(248 * scale_y)))

        back1 = pygame.image.load("background/back1.png").convert()
        back1 = pygame.transform.scale(back1, (int(1280 * scale_x), int(720 * scale_y)))

        back2 = pygame.image.load("background/back2.png").convert()
        back2 = pygame.transform.scale(back2, (int(1280 * scale_x), int(720 * scale_y)))

        back3 = pygame.image.load("background/back3.jpg").convert()
        back3 = pygame.transform.scale(back3, (int(1280 * scale_x), int(720 * scale_x)))

        back4 = pygame.image.load("background/back4.png").convert()
        back4 = pygame.transform.scale(back4, (int(1280 * scale_x), int(720 * scale_y)))

        back5 = pygame.image.load("background/back5.jpg").convert()
        back5 = pygame.transform.scale(back5, (int(1280 * scale_x), int(720 * scale_y)))

        back6 = pygame.image.load("background/back6.jpg").convert()
        back6 = pygame.transform.scale(back6, (int(1280 * scale_x), int(720 * scale_y)))

        back7 = pygame.image.load("background/back7.png").convert()
        back7 = pygame.transform.scale(back7, (int(1280 * scale_x), int(720 * scale_y)))

        fruit = pygame.image.load("images/fruit.png").convert()
        fruit = pygame.transform.scale(fruit, (int(30 * scale_x), int(19 * scale_y)))

        # BIRD FRAMES

        frame1 = pygame.image.load("birds/1.png")
        # frame1=pygame.transform.flip(frame1,True,False)

        frame2 = pygame.image.load("birds/2.png")
        # frame2=pygame.transform.flip(frame2,True,False)

        frame3 = pygame.image.load("birds/3.png")
        # frame3=pygame.transform.flip(frame3,True,False)

        frame4 = pygame.image.load("birds/4.png")
        # frame4=pygame.transform.flip(frame4,True,False)

        frame5 = pygame.image.load("birds/5.png")
        # frame5=pygame.transform.flip(frame5,True,False)

        frame6 = pygame.image.load("birds/6.png")
        # frame6=pygame.transform.flip(frame6,True,False)

        frame7 = pygame.image.load("birds/7.png")
        # frame7=pygame.transform.flip(frame7,True,False)

        frame8 = pygame.image.load("birds/8.png")
        # frame8=pygame.transform.flip(frame8,True,False)

        birds = [frame1, frame2, frame3, frame4,
                 frame5, frame6, frame7, frame8]

        backgroundlist = [back1, back2, back3, back4, back5, back6, back7]

        back = backgroundlist[randint(0, 6)]
        # back=back5

        # stickx1=455
        # sticky1=50

        herokicklist = [hero, herotr]

        herolist = [hero, hero1, hero2, hero3]

        herodownlist = [herodown, hero1down, hero2down, hero3down]

        pillarlist = [alpha, beta, gamma, delta]

        # Sound loads

        pop1 = pygame.mixer.Sound("sound/pop_1.ogg")
        pop2 = pygame.mixer.Sound("sound/pop_2.ogg")

        stickgrow = pygame.mixer.Sound("sound/stick_grow_loop.ogg")

        kick = pygame.mixer.Sound("sound/kick.ogg")

        landing = pygame.mixer.Sound("sound/fall.ogg")

        scoresound = pygame.mixer.Sound("sound/score.ogg")

        dead = pygame.mixer.Sound("sound/dead.ogg")
        kick = pygame.mixer.Sound("sound/kick.ogg")
        rollupdown = pygame.mixer.Sound("sound/roll_up_down.ogg")
        eating_fruit = pygame.mixer.Sound("sound/eating_fruit.ogg")
        perfectsound = pygame.mixer.Sound("sound/perfect.ogg")

        flappy = pygame.mixer.Sound("sound/bird/bonus_loop_bird.ogg")
        chichi = pygame.mixer.Sound("sound/bird/bonus_trigger_bird.ogg")

        font_path = "fonts/Arimo.ttf"
        font_size = int(40 * scale_x)
        font1 = pygame.font.Font(font_path, font_size)
        font2 = pygame.font.Font("fonts/Arimo.ttf", int(25 * scale_x))
        font3 = pygame.font.Font("fonts/Arimo.ttf", int(40 * scale_x))
        font4 = pygame.font.Font("fonts/Arimo.ttf", int(20 * scale_x))

        # VARIABLE INITIALIZATION

        stickx1 = stickx = (455 + 45) * scale_x
        sticky1 = sticky = 472 * scale_y

        anglenum = 90
        angle = (pi / 180) * anglenum

        sticklength = 0

        time = 0
        flag = 0  # stick fall flag
        keypressflag = 0

        moveit = 0  # hero move flag

        herox = (429 + 45) * scale_x
        heroy = 442 * scale_y

        heropointer = 0

        i = 0
        j = 0
        k = 0

        pillar1x = (355 + 45) * scale_x
        msgx = pillar2x = (650 + 45) * scale_x

        pillar3x = randint(int((845 + 45) * scale_x), int((900 + 45) * scale_x))

        pillar1 = alpha
        pillar2 = beta
        pillar3 = pillarlist[randint(0, 2)]

        herofall = 0
        herofallflag = 0

        pillarmoveflag = 0

        stickmove = 0

        backx = 0

        pillarfound = 0

        score = 0

        keyinit = 0

        speed = (8 + 45) * scale_x

        acc1 = acc2 = acc3 = 0

        pillarfast = 0

        pillardist = randint(int((60 + 45) * scale_x), int((260 + 45) * scale_x))
        lastpillardist = pillardist

        stickgrowsound = 0

        ext = 0

        backx1 = (350 + 45) * scale_x
        backx2 = (1630 + 45) * scale_x

        upsidedown = False

        keypress = 0

        if(pillar1x > ((429 + 45) * scale_x) and pillar1x < ((840 + 45) * scale_x)):
            # acc1=2
            pillar2nd = pillar1x

        if(pillar2x > ((429 + 45) * scale_x) and pillar2x < ((840 + 45) * scale_x)):
            # acc2=2
            pillar2nd = pillar2x

        if(pillar3x > ((429 + 45) * scale_x) and pillar3x < ((840 + 45) * scale_x)):
            # acc3=2
            pillar2nd = pillar3x

        bouncedown = True
        bounce = 0

        fruitx = 0

        fruitgot = False
        fruitflag = 0

        herod = 33 * scale_y

        fruitscore = 0
        score = 0
        
        score_path = os.path.join(get_activity_root(), 'data', 'score.pkl')
        if not os.path.exists(score_path):
            open(score_path,'w+')

        if os.path.getsize(score_path) == 0:

            with open(score_path, 'wb') as output:
                pickle.dump(0, output, pickle.HIGHEST_PROTOCOL)
                pickle.dump(0, output, pickle.HIGHEST_PROTOCOL)

        with open(score_path, 'rb') as input:  # REading
            fruitscore = pickle.load(input)
            fruitscore = pickle.load(input)

        scoreshift = 0
        fruitscoreshift = 0
        shift1 = 1
        shift2 = 1

        perfectflag = 0
        vanish = 0
        perfect = 0
        b1 = 0
        b2 = 2
        b3 = 4
        b4 = 6

        birdx = (900 + 45) * scale_x
        birdxslow = (950 + 45) * scale_x
        birdxfast = (860 + 45) * scale_x

        birdgroupshow = 0
        birdsingleshow = 0
        birdmainshow = 0
        birdpickup = 0
        birdsound = 0

        flagchk1 = flagchk2 = flagchk3 = 0

        flagchk = 0

        catch = 0

        # lastpillardist=pillar2x-457

        # GAME LOOP BEGINS !!!

        while not crashed:
            # Gtk events

            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                # totaltime+=timer.tick()
                if event.type == pygame.QUIT:
                    crashed = True

            mos_x, mos_y = pygame.mouse.get_pos()

            # print "hello"

            if(catch == 0):
                b = welcomescreen()
                catch = b.make(gameDisplay, back)

            gameDisplay.fill(white)
            gameDisplay.blit(back, (backx1, 0))
            gameDisplay.blit(back, (backx2, 0))
            gameDisplay.blit(fruit, ((800 + 45) * scale_x, 20 * scale_y))

            # scoreplate.set_alpha(20)
            gameDisplay.blit(scoreplate, ((540 + 45) * scale_x, 40 * scale_y))

            # score blitting

            # Bird frames processing

            if(i % 7 == 0):
                b1 += 1
                if(b1 == 8):
                    b1 = 0

                b2 += 1
                if(b2 == 8):
                    b2 = 0

                b3 += 1
                if(b3 == 8):
                    b3 = 0

                b4 += 1
                if(b4 == 8):
                    b4 = 0

            if(birdgroupshow == 1):

                gameDisplay.blit(pygame.transform.scale(
                    birds[b1], (int(57 * scale_x), int(39 * scale_y))), (birdx + 10 * scale_x, 100 * scale_y))
                gameDisplay.blit(pygame.transform.scale(
                    birds[b2], (int((57 - 10) * scale_x), int((39 - 10) * scale_y))), (birdx - 50 * scale_x, 115 * scale_y))

                gameDisplay.blit(pygame.transform.scale(
                    birds[b3], (int((57 - 20) * scale_x), int((39 - 20) * scale_y))), (birdx, (110 + 30) * scale_y))

            if(birdsingleshow == 1):

                gameDisplay.blit(pygame.transform.scale(
                    birds[b3], (int((57 + 10) * scale_x), int((39 + 10) * scale_y))), (birdxslow, 110 * scale_y))

            # Birds movement

            if(birdx >= ((300 + 45) * scale_x) and birdgroupshow == 1):
                birdx -= 3 * scale_x

            if(birdxslow >= ((300 + 45) * scale_x) and birdsingleshow == 1):
                birdxslow -= 2 * scale_x

            if(birdmainshow == 1):

                birdxfast -= birdspeed

            # Birds coordinates updates

            if(birdx < ((300 + 45) * scale_x)):
                birdx = (900 + 45) * scale_x
                birdgroupshow = 0

            if(birdxslow < ((300 + 45) * scale_x)):
                birdxslow = (950 + 45) * scale_x
                birdsingleshow = 0

            if((birdxfast + 30 * scale_x) <= ((300 + 45) * scale_x)):
                birdxfast = (860 + 45) * scale_x
                birdmainshow = 0

            if(birdsingleshow == 0 and i % 18 == 0):
                r = randint(0, 99)
                if(r % 18 == 0):
                    birdgroupshow = 1
                    birdsingleshow = 1

            # BIRD PICK'S YOU UP

            if(pygame.transform.scale(birds[b4], (int((57 + 30) * scale_x), int((39 + 20) * scale_y))).get_rect(center=(birdxfast + 40 * scale_x, (400 + 20) * scale_y)).colliderect(herolist[j].get_rect(center=(herox + 18 * scale_x, heroy + herod + 15 * scale_y)))):

                herox = birdxfast + 30 * scale_x
                birdpickup = 1

                if(birdsound == 0):
                    birdsound = 1

                moveit = 0

                if(herox < ((320 + 45) * scale_x)):

                    ext = 1

            #pygame.draw.circle(gameDisplay,white, (birdxfast,400) ,3, 2)

            #pygame.draw.circle(gameDisplay,white, (herox+18,heroy+herod) ,3, 2)

            if(birdsound == 1):
                birdsound = 2
                flappy.play(0)

            scores = font1.render(str(score), 1, (255, 255, 255))
            gameDisplay.blit(scores, ((580 + scoreshift + 45) * scale_x, 40 * scale_y))
            fruitscores = font2.render(str(fruitscore), 1, (0, 0, 0))
            gameDisplay.blit(fruitscores, ((770 + fruitscoreshift + 45) * scale_x, 13 * scale_y))

            if(perfect == 1):

                vanish -= 1

                msg1 = font3.render(_("Perfect!!!"), 1, (0, 0, 0))
                gameDisplay.blit(msg1, ((510 + 45) * scale_x, 120 * scale_y))

                msg2 = font4.render(_("+1"), 1, (0, 0, 0))
                gameDisplay.blit(msg2, (msgx, (460 + vanish) * scale_y))

                if(vanish < -50):
                    perfect = 0
                    vanish = 0

            # fruits bounce up-down

            if((pillar2nd - 429 * scale_x) > ((80 + 45) * scale_x) and fruitx >= ((429 + 45) * scale_x) and fruitx != 0 and not(fruitgot)):
                gameDisplay.blit(fruit, (fruitx, (480 + bounce) * scale_y))

            if(bouncedown == True):
                if(i % 6 == 0):
                    bounce += 1
                    if(bounce > 5):
                        bouncedown = not(bouncedown)
            else:
                if(i % 6 == 0):
                    bounce -= 1
                    if(bounce < 0):
                        bouncedown = not(bouncedown)

            # Fruit vanish condition

            if(fruitflag == 0 and herodownlist[j].get_rect(center=(herox + 18 * scale_x, heroy + herod + 10 * scale_y)).colliderect(fruit.get_rect(center=(fruitx + 14 * scale_x, (480 + bounce + 10) * scale_y)))):
                fruitgot = not fruitgot
                fruitflag = 1
                if(herofallflag != 1):
                    fruitscore += 1
                    # rollupdown.stop()
                    # eating_fruit.stop()
                    eating_fruit.play()

            # if(upsidedown==1 and herox+15>=fruitx):
            #    fruitgot=not fruitgot

            #pygame.draw.circle(gameDisplay,black, (herox+15,heroy+60) ,3, 2)

            #pygame.draw.circle(gameDisplay,black, (herox+18,heroy+10+33) ,3, 2)

            #pygame.draw.circle(gameDisplay,black, (fruitx+13,480+bounce+10) ,3, 2)

            # backgound frames roll-over

            if(backx1 < -(1280 * scale_x)):
                # if not(back==back2):
                backx1 = 1270 * scale_x
                # else:
                #    backx1=1260
            if(backx2 < -(1280 * scale_x)):
                # if not(back==back2):
                backx2 = 1270 * scale_x
                # else:
                #    backx2=1260

            if(i > 20):
                i = 0

            i += 1
            if(i % 4 == 0):
                j += 1

            if(j == 4):
                j = 0

            if(moveit == 1):

                if(upsidedown == False):
                    herod = 0
                    gameDisplay.blit(
                        herolist[j], (herox, heroy + (herod - (birdpickup * 5)) * scale_y))
                else:
                    herod = 33
                    gameDisplay.blit(herodownlist[j], (herox, heroy + herod * scale_y))

            # Main bird display

            if(birdmainshow == 1):

                gameDisplay.blit(pygame.transform.scale(
                    birds[b4], (int((57 + 30) * scale_x), int((39 + 20) * scale_y))), (birdxfast, 400 * scale_y))

            # Inverted hero collsion with pillar test

            if(upsidedown == True and (herox + 30 * scale_x) >= pillar2nd):

                herofall = 1
                moveit = 0
                flag = 1

            # print upsidedown

            if(moveit == 0):

                if(k <= 6):
                    gameDisplay.blit(herokicklist[0], (herox, heroy))
                if(k <= 12):
                    gameDisplay.blit(herokicklist[1], (herox - 1 * scale_x, heroy + 2 * scale_y))

                if(keypressflag == 1):
                    k += 1
                if(k == 12):
                    k = 0

            if(moveit == 1):  # hero moving right
                herox += 4 * scale_x
                heropointer += 4 * scale_x
                backx1 -= 1 * scale_x
                backx2 -= 1 * scale_x

            if(herox >= ((845 + 45) * scale_x)):
                herofallflag = 1
                herofall = 1
                moveit = 0
                flag = 1

            gameDisplay.blit(pillar1, (pillar1x, 470 * scale_y))

            gameDisplay.blit(pillar2, (pillar2x, 470 * scale_y))

            gameDisplay.blit(pillar3, (pillar3x, 470 * scale_y))

            #pygame.draw.circle(gameDisplay,white, (birdxfast+40,400+40) ,3, 2)

            #pygame.draw.circle(gameDisplay,white, (herox+18,heroy+herod+15) ,3, 2)

            # sticklength calculation

            if(flag == 0):

                if(stickx == stickx1):
                    sticklength = abs(sticky - sticky1)
                if(sticky == sticky1):
                    sticklength = abs(stickx1 - stickx)

            # stick fall from Vertical to Horizontal

            if(anglenum > 0 and flag == 1):

                anglenum -= 0.03 * (time) * (time)
                if(anglenum <= 0):
                    kick.stop()
                    landing.play(0)
                    anglenum = 0
                    sticky1 = 472 * scale_y
                    stickx1 = stickx + sticklength
                    # sticklength=stickx1-stickx
                    flag = 0
                    moveit = 1
                    time = 0

                    # 2nd PILLAR DETECTION

                    '''
                    
                    if(pillar1x>429 and pillar1x<840):
                        #acc1=2
                        pillar2nd=pillar1x
                 
                    if(pillar2x>429 and pillar2x<840):
                        #acc2=2
                        pillar2nd=pillar2x
                       
                    if(pillar3x>429 and pillar3x<840):
                        #acc3=2
                        pillar2nd=pillar3x
                    
                    '''

                    # Birds Speed calculation

                    if(sticklength > (190 + 45) * scale_x and randint(0, 2) == 0):
                        birdspeed = int((1680 * scale_x) / sticklength)
                        birdspeed += 3 * scale_x
                        birdmainshow = 1
                        chichi.play(0)

                    colortest = gameDisplay.get_at(
                        (int((457 + 45) * scale_x + sticklength + 2 * scale_x), int(heroy + 40 * scale_y)))

                    if not((colortest[0] == 0 and colortest[1] == 0 and colortest[2] == 0) or (colortest[0] == 1 and colortest[1] == 1 and colortest[2] == 1)):
                        herofallflag = 1
                    colortest = gameDisplay.get_at(
                        (int((457 + 45) * scale_x + sticklength), int(heroy + 30 * scale_y)))

                    if(colortest[0] == 255):
                        perfectflag = 1
                        perfectsound.play()
                        perfect = 1
                        msgx = pillar2nd

                time += 1

            # stick fall from horizontal to bottom

            if(herofall == 1):

                if(anglenum > -90):
                    anglenum -= 0.03 * (time) * (time)

                    # print "hey"

                    if(anglenum <= -90):

                        # print "hey"
                        anglenum = -90
                        sticky1 = sticky + sticklength
                        stickx1 = (455 + 45) * scale_x
                        # sticklength=stickx1-stickx
                        # flag=0
                        moveit = 1
                        time = 0

                    time += 1

            # angle calculation

            angle = (pi / 180) * anglenum

            # keypress check

            if(keyinit == 0):

                if event.type == pygame.KEYDOWN and event.key == 273:
                    # jump.play(0)

                    keypressflag = 1
                    keyinit = 1
                    stickgrowsound = 1

            if(keypressflag == 1):

                if event.type == pygame.KEYUP and event.key == 273:
                    flag = 1

                    stickgrow.stop()
                    kick.stop()
                    kick.play()

                    kick.play(0)
                    keypressflag = 0

            if(stickgrowsound == 1):

                stickgrow.play(-1)

            '''            
            if(pillar1x>429 and pillar1x<840):
                #acc1=2
                pillar2nd=pillar1x
                    
            if(pillar2x>429 and pillar2x<840):
                #acc2=2
                pillar2nd=pillar2x
                        
            if(pillar3x>429 and pillar3x<840):
                #acc3=2
                pillar2nd=pillar3x
            
            '''

            if(moveit == 1 and heropointer <= (pillar2nd - (457 + 45) * scale_x)):

                if event.type == pygame.KEYDOWN and event.key == 273 and keypress == 0:
                    # jump.play(0)

                    rollupdown.play()
                    upsidedown = not upsidedown

                    keypress = 1

            if event.type == pygame.KEYUP and event.key == 273 and keypress == 1:

                keypress = 0

            if keypressflag == 1:

                stickgrowsound = 0
                if(sticky1 >= 0):
                    sticky1 -= 5 * scale_y

            # print pillar2nd

            # coordinates calculation while stick free fall

            if(flag == 1):
                sticky1 = 472 * scale_y - sticklength * sin(angle)
                stickx1 = (455 + 45) * scale_x + sticklength * cos(angle)

            # zeroing the length of the stick as it surpassed left boundary

            if(stickx <= ((349 + 45) * scale_x)):

                stickmove = 0
                stickx1 = stickx = (455 + 45) * scale_x
                sticky1 = sticky = 472 * scale_y

            if((stickx1 - stickx) != 0 or sticky1 - sticky != 0):
                pygame.draw.line(gameDisplay, black,
                                 (stickx1, sticky1), (stickx, sticky), int(6 * scale_x))

            # test circles

            #pygame.draw.circle(gameDisplay,white, (herox+30,heroy+30) ,2, 2)
            #pygame.draw.circle(gameDisplay,white, (457+sticklength+2,heroy+30) ,2, 2)

            # if hero has to fall

            if((herox + 30 * scale_x) >= (457 + 45) * scale_x + sticklength and herofallflag == 1):
                herofall = 1
                moveit = 0
                flag = 1

            # if hero has to stop
            if((herox + 30 * scale_x) >= (457 + 45) * scale_x + sticklength and herofallflag == 0 and moveit == 1 and heroy < 768 * scale_y):

                color = gameDisplay.get_at((int(herox + (30 + 4) * scale_x), int(heroy + 40 * scale_y)))

                if not((color[0] == 0 and color[1] == 0 and color[2] == 0) or (color[0] == 1 and color[1] == 1 and color[2] == 1)):
                    moveit = 0
                    pillarmoveflag = 1
                    stickmove = 1

                    if(pillar1x > (840 + 45) * scale_x):
                        acc1 = 1
                        acc2 = 0
                        acc3 = 0
                        pillarfast = pillar1x

                    if(pillar2x > (840 + 45) * scale_x):
                        acc1 = 0
                        acc2 = 1
                        acc3 = 0
                        pillarfast = pillar2x

                    if(pillar3x > (840 + 45) * scale_x):
                        acc1 = 0
                        acc2 = 0
                        acc3 = 1
                        pillarfast = pillar3x

                    '''
                    
                        
                    if(pillar1x>429 and pillar1x<840):
                        #acc1=2
                        pillar2nd=pillar1x
                    
                    if(pillar2x>429 and pillar2x<840):
                        #acc2=2
                        pillar2nd=pillar2x
                        
                    if(pillar3x>429 and pillar3x<840):
                        #acc3=2
                        pillar2nd=pillar3x 
                        
                    
                    '''

                    time = abs((heropointer) / speed)
                    # print heropointer

                    acc = abs(((pillarfast) - ((429 + 45) * scale_x + pillardist)) / time)

                    # print
                    # str(((pillarfast)-(429+pillardist)))+str(heropointer)

                    # print pillardist
                    # print heropointer

            if(moveit == 0 and pillarmoveflag == 1):

                if(stickmove == 1):
                    stickx1 -= speed
                    stickx -= speed

                if(heropointer > 0):

                    if(acc1 == 0):
                        pillar1x -= (speed)
                    if(acc2 == 0):
                        pillar2x -= (speed)
                    if(acc3 == 0):
                        pillar3x -= (speed)

                    herox -= speed
                    heropointer -= speed
                    fruitx -= speed
                    # print "help"

                # if(abs(pillarfast-450)>=pillardist):
                    if(acc1 == 1):
                        pillar1x -= (acc)
                        pillarfast = pillar1x

                    if(acc2 == 1):
                        pillar2x -= (acc)
                        pillarfast = pillar2x

                    if(acc3 == 1):
                        pillar3x -= (acc)
                        pillarfast = pillar3x

                else:
                    # if ((heropointer<=0) and
                    # (abs(pillarfast-450)<=pillardist)):

                    landing.stop()
                    scoresound.stop()
                    scoresound.play(0)

                    # print "hello"

                    vanish = 0

                    pillarmoveflag = 0

                    if(lastpillardist < (160 + 45) * scale_x):
                        pillardist = randint(int((160 + 45) * scale_x), int((260 + 45) * scale_x))
                        lastpillardist = pillardist
                    else:
                        pillardist = randint(int((100 + 45) * scale_x), int((160 + 45) * scale_x))
                        lastpillardist = pillardist

                    if(score < (10**shift1) - 1):
                        if not(perfectflag == 1):
                            score += 1
                        else:
                            score += 2
                    else:
                        if not(perfectflag == 1):
                            score += 1
                        else:
                            score += 2
                        shift1 += 1
                        scoreshift -= 10

                    if not(fruitscore < (10**shift2) - 1):

                        # fruitscore+=1
                        shift2 += 1
                        fruitscoreshift -= 4

                    perfectflag = 0

                    pillar1x += speed
                    pillar2x += speed
                    pillar3x += (speed)

                    # re-initialization of the variables

                    stickx1 = stickx = (455 + 45) * scale_x
                    sticky1 = sticky = 472 * scale_y

                    anglenum = 90
                    angle = (pi / 180) * anglenum

                    sticklength = 0

                    time = 0
                    flag = 0  # stick fall flag
                    keypressflag = 0

                    moveit = 0  # hero move flag

                    herox = (429 + 45) * scale_x
                    heroy = 442 * scale_y
                    heropointer = 0

                    i = 0
                    j = 0
                    k = 0

                    fruitgot = False
                    fruitflag = 0

                    herofall = 0
                    herofallflag = 0

                    pillarmoveflag = 0

                    stickmove = 0

                    keyinit = 0
                    flagchk = 0

                    # print fruitx

            if(pillarmoveflag == 0):
                pillarmoveflag = 2

                # print "help"

                if(pillar1 == delta and pillar1x < ((415 + 45) * scale_x)):
                    pillarfast = pillar1x = randint(int((845 + 45) * scale_x), int((900 + 45) * scale_x))
                    pillar1 = pillarlist[randint(0, 2)]
                    flagchk1 = 1

                if(pillar2 == delta and pillar2x < ((415 + 45) * scale_x)):
                    pillarfast = pillar2x = randint(int((845 + 45) * scale_x), int((900 + 45) * scale_x))
                    pillar2 = pillarlist[randint(0, 2)]
                    flagchk2 = 1

                if(pillar3 == delta and pillar3x < ((415 + 45) * scale_x)):
                    pillarfast = pillar3x = randint(int((845 + 45) * scale_x), int((900 + 45) * scale_x))
                    pillar3 = pillarlist[randint(0, 2)]
                    flagchk3 = 1

                if(pillar1x <= ((348 + 45) * scale_x) and flagchk1 != 1):
                    pillarfast = pillar1x = randint(int((845 + 45) * scale_x), int((900 + 45) * scale_x))
                    pillar1 = pillarlist[randint(0, 2)]

                if(pillar2x <= ((348 + 45) * scale_x) and flagchk2 != 1):
                    pillarfast = pillar2x = randint(int((845 + 45) * scale_x), int((900 + 45) * scale_x))
                    pillar2 = pillarlist[randint(0, 2)]

                if(pillar3x <= ((348 + 45) * scale_x) and flagchk3 != 1):
                    pillarfast = pillar3x = randint(int((845 + 45) * scale_x), int((900 + 45) * scale_x))
                    pillar3 = pillarlist[randint(0, 2)]

                # 2nd PILLAR DETECTION

                if(pillar1x > ((457 + 45) * scale_x) and pillar1x < ((840 + 45) * scale_x)):
                    # acc1=2
                    pillar2nd = pillar1x

                if(pillar2x > ((457 + 45) * scale_x) and pillar2x < ((840 + 45) * scale_x)):
                    # acc2=2
                    pillar2nd = pillar2x

                if(pillar3x > ((457 + 45) * scale_x) and pillar3x < ((840 + 45) * scale_x)):
                    # acc3=2
                    pillar2nd = pillar3x

                flagchk1 = flagchk2 = flagchk3 = 0

                # fruit placement

                if((pillar2nd - (459 + 45) * scale_x) > ((80 + 45) * scale_x)):
                    fruitx = randint(int((470 + 45) * scale_x), int(pillar2nd - (20 - 8) * scale_x))

            # print pillar1.rect.topleft

            # left and right black background patches

            pygame.draw.rect(gameDisplay, black, (0, 0, (350 + 45) * scale_x, 768 * scale_y))

            pygame.draw.rect(gameDisplay, black, ((840 + 45) * scale_x, 0, (693 + 45) * scale_x, 768 * scale_y))

            if(herofall == 1 or ext == 1):

                if(ext != 1):
                    heroy += 15 * scale_y

                if(heroy > (770 * scale_y) or ext == 1):

                    landing.stop()
                    dead.stop()
                    dead.play()
                    #rect = pygame.Rect(350, 0, 490, 768)
                    #sub = gameDisplay.subsurface(rect)
                    #pygame.image.save(sub, "screenshot/screenshot.png")

                    a = scorescreen()
                    catch = a.make(gameDisplay, back, score, fruitscore)

                    if(catch == 1):

                        # VARIABLE INITIALIZATION

                        stickx1 = stickx = (455 + 45) * scale_x
                        sticky1 = sticky = 472 * scale_y

                        anglenum = 90
                        angle = (pi / 180) * anglenum

                        sticklength = 0

                        time = 0
                        flag = 0  # stick fall flag
                        keypressflag = 0

                        moveit = 0  # hero move flag

                        herox = (429 + 45) * scale_x
                        heroy = 442 * scale_y

                        heropointer = 0

                        i = 0
                        j = 0
                        k = 0

                        pillar1x = (355 + 45) * scale_x
                        msgx = pillar2x = (650 + 45) * scale_x
                        pillar3x = randint(int((845 + 45) * scale_x), int((900 + 45) * scale_x))

                        pillar1 = alpha
                        pillar2 = beta
                        pillar3 = pillarlist[randint(0, 2)]

                        herofall = 0
                        herofallflag = 0

                        pillarmoveflag = 0

                        stickmove = 0

                        ackx = 0

                        pillarfound = 0

                        score = 0

                        keyinit = 0

                        ext = 0

                        speed = (8 + 45) * scale_x

                        acc1 = acc2 = acc3 = 0

                        pillarfast = 0

                        pillardist = randint(int((60 + 45) * scale_x), int((260 + 45) * scale_x))
                        lastpillardist = pillardist

                        stickgrowsound = 0

                        back = backgroundlist[randint(0, 6)]

                        keypress = 0

                        backx1 = (350 + 45) * scale_x
                        backx2 = (1630 + 45) * scale_x

                        upsidedown = False

                        '''
        
                        if(pillar1x>429 and pillar1x<840):
                            #acc1=2
                            pillar2nd=pillar1x
                    
                        if(pillar2x>429 and pillar2x<840):
                            #acc2=2
                            pillar2nd=pillar2x
                        
                        if(pillar3x>429 and pillar3x<840):
                            #acc3=2
                            pillar2nd=pillar3x 
                            
                        '''

                        bouncedown = True
                        bounce = 0

                        fruitx = 0

                        fruitgot = False
                        fruitflag = 0

                        herod = 33 * scale_y

                        fruitscore = 0
                        score = 0

                        scoreshift = 0
                        fruitscoreshift = 0
                        shift1 = 1
                        shift2 = 1

                        perfectflag = 0
                        vanish = 0
                        perfect = 0
                        b1 = 0
                        b2 = 2
                        b3 = 4
                        b4 = 6

                        birdx = (900 + 45) * scale_x
                        birdxslow = (950 + 45) * scale_x
                        birdxfast = (860 + 45) * scale_x

                        birdgroupshow = 0
                        birdsingleshow = 0
                        birdmainshow = 0
                        birdpickup = 0
                        birdsound = 0

                        flagchk1 = flagchk2 = flagchk3 = 0

                        flagchk = 0

            #pygame.draw.circle(gameDisplay,white,(pillar2nd,700) ,3, 2)

            pygame.display.update()
            clock.tick(60)

            if crashed == True:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()

        # Just a window exception check condition

        event1 = pygame.event.get()
        if event1.type == pygame.QUIT:
            crashed = True

        if crashed == True:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    g = game()
    g.make()
