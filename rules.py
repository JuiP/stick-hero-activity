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

from math import *
from random import *

class rulescreen:

    def make(self, gameDisplay):

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

        frame1 = pygame.image.load("images/rulescreen/ruleframes/frame1.png")
        frame2 = pygame.image.load("images/rulescreen/ruleframes/frame2.png")
        frame3 = pygame.image.load("images/rulescreen/ruleframes/frame3.png")
        frame4 = pygame.image.load("images/rulescreen/ruleframes/frame4.png")
        frame5 = pygame.image.load("images/rulescreen/ruleframes/frame5.png")
        frame6 = pygame.image.load("images/rulescreen/ruleframes/frame6.png")
        frame7 = pygame.image.load("images/rulescreen/ruleframes/frame7.png")
        frame8 = pygame.image.load("images/rulescreen/ruleframes/frame8.png")
        frame9 = pygame.image.load("images/rulescreen/ruleframes/frame9.png")
        frame10 = pygame.image.load("images/rulescreen/ruleframes/frame10.png")
        frame11 = pygame.image.load("images/rulescreen/ruleframes/frame11.png")
        frame12 = pygame.image.load("images/rulescreen/ruleframes/frame12.png")
        frame13 = pygame.image.load("images/rulescreen/ruleframes/frame13.png")
        frame14 = pygame.image.load("images/rulescreen/ruleframes/frame14.png")
        frame15 = pygame.image.load("images/rulescreen/ruleframes/frame15.png")
        frame16 = pygame.image.load("images/rulescreen/ruleframes/frame16.png")
        frame17 = pygame.image.load("images/rulescreen/ruleframes/frame17.png")
        frame18 = pygame.image.load("images/rulescreen/ruleframes/frame18.png")
        frame19 = pygame.image.load("images/rulescreen/ruleframes/frame19.png")
        frame20 = pygame.image.load("images/rulescreen/ruleframes/frame20.png")
        frame21 = pygame.image.load("images/rulescreen/ruleframes/frame21.png")
        frame22 = pygame.image.load("images/rulescreen/ruleframes/frame22.png")
        frame23 = pygame.image.load("images/rulescreen/ruleframes/frame23.png")
        frame24 = pygame.image.load("images/rulescreen/ruleframes/frame24.png")
        frame25 = pygame.image.load("images/rulescreen/ruleframes/frame25.png")

        play = pygame.image.load("images/rulescreen/back.png")

        button = pygame.image.load("images/rulescreen/button.png")

        hide = pygame.image.load("images/rulescreen/hideboard.png").convert()

        framelist = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10, frame11, frame12,
                     frame13, frame14, frame15, frame16, frame17, frame18, frame19, frame20, frame21, frame22, frame23, frame24, frame25]

        font_path = "fonts/Arimo.ttf"
        font_size = int(20 * scale_x)
        font1 = pygame.font.Font(font_path, font_size)
        font2 = pygame.font.Font("fonts/Arimo.ttf", int(30 * scale_x))
        font3 = pygame.font.Font("fonts/Arimo.ttf", int(40 * scale_x))
        font4 = pygame.font.Font("fonts/Arimo.ttf", int(20 * scale_x))

        chichi = pygame.mixer.Sound("sound/bird/bonus_trigger_bird.ogg")
        eating_fruit = pygame.mixer.Sound("sound/eating_fruit.ogg")
        perfectsound = pygame.mixer.Sound("sound/perfect.ogg")

        i = k = 0
        press = 0
        flag1 = flag2 = flag3 = 0

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

            # print event

            i += 1

            if(i > 30):
                i = 0

            # gameDisplay.fill(white)

            if(i == 30):
                k += 1
                if(k == 25):
                    k = 0
                    flag1 = flag2 = flag3 = 0

            gameDisplay.blit(pygame.transform.scale(
                framelist[k], (int(491 * scale_x), int(768 * scale_y))), ((350 + 45) * scale_x, 0))

            if(k == 18 and flag1 == 0):
                chichi.play(0)
                flag1 = 1

            if(k == 16 and flag2 == 0):
                perfectsound.play(0)
                flag2 = 1

            if(k == 7 and flag3 == 0):
                eating_fruit.play(0)
                flag3 = 1

            head1 = font1.render(
                "To roll hero upside-down use UP arrow key", 1, (white))
            gameDisplay.blit(head1, ((400 + 45)*scale_x, 100*scale_y))

            gameDisplay.blit(button, ((550)*scale_x, 140*scale_y))

            gameDisplay.blit(hide, ((400 + 45)*scale_x, 600*scale_y))
            gameDisplay.blit(pygame.transform.scale(
                    play, (189, 70)), ((500)*scale_x, 600*scale_y))

            if play.get_rect(center=((500 + 92)*scale_x, (600 + 33)*scale_y)).collidepoint(mos_x, mos_y):
                gameDisplay.blit(pygame.transform.scale(
                    play, (189, 70)), ((500 - 2)*scale_x, (600 - 2)*scale_y))

                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:
                    return 0

                if event.type == pygame.MOUSEBUTTONUP:
                    press = 0

            # left and right black background patches

            pygame.draw.rect(gameDisplay, black, (0, 0, (350 + 45)*scale_x, 768*scale_y))

            pygame.draw.rect(gameDisplay, black, ((839 + 45)*scale_x, 0, 693*scale_x, 768*scale_y))

            pygame.display.update()
            clock.tick(60)

            # Game crash or Close check
            if crashed == True:
                pygame.quit()
                sys.exit()

        # Just a window exception check condition

        event1 = pygame.event.get()
        if event1.type == pygame.QUIT:
            crashed = True

        if crashed == True:
            pygame.quit()
            sys.exit()
