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

SHIFT_CORRECTOR = 45


class scorescreen:

    def make(self, gameDisplay, back, score, fruitscore):

        pygame.init()
        sound = True

        try:
            pygame.mixer.init()
        except Exception, err:
            sound = False
            print 'error with sound', err

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
        w, h = gameDisplay.get_width(), gameDisplay.get_height()
        scale_x = w / 1280.0
        scale_y = h / 720.0

        if not(gameDisplay):

            gameDisplay = pygame.display.set_mode(
                (info.current_w, info.current_h))

        replay = pygame.image.load("images/scorescreen/replay.png")
        replay = pygame.transform.scale(replay, (int(104 * scale_x),
                                                 int(102 * scale_y)))
        scoreplate = pygame.image.load("images/scorescreen/scoreplate.png")
        scoreplate = pygame.transform.scale(scoreplate,
                                            (int((230 + 130) * scale_x),
                                             int((140 + 80) * scale_y)))

        plate = pygame.image.load("images/scoreplate.png").convert()
        plate = pygame.transform.scale(plate, (int(340 * scale_x),
                                               int(90 * scale_y)))
        plate.set_alpha(220)

        home = pygame.image.load("images/scorescreen/home.png")
        home = pygame.transform.scale(
                   home, (int(108 * scale_x), int(106 * scale_y)))

        back.convert()
        back.set_alpha(225)

        font_path = "fonts/Arimo.ttf"
        font_size = int(50 * scale_x)
        font1 = pygame.font.Font(font_path, font_size)
        font2 = pygame.font.Font("fonts/Arimo.ttf", int(30 * scale_x))
        font3 = pygame.font.Font("fonts/Arimo.ttf", int(40 * scale_x))
        font4 = pygame.font.Font("fonts/Arimo.ttf", int(20 * scale_x))

        down = 1
        bounce = 0
        i = 0

        keypressflag = 0

        maxscore = 0
        fruitmaxscore = 0
        score_path = os.path.join(get_activity_root(), 'data', 'score.pkl')

        with open(score_path, 'rb') as input:  # REading
            maxscore = pickle.load(input)
            fruitmaxscore = pickle.load(input)

        if(fruitscore > fruitmaxscore):
            fruitmaxscore = fruitscore
            with open(score_path, 'wb') as output:
                pickle.dump(maxscore, output, pickle.HIGHEST_PROTOCOL)
                pickle.dump(fruitmaxscore, output, pickle.HIGHEST_PROTOCOL)

        if(score > maxscore):
            maxscore = score
            with open(score_path, 'wb') as output:
                pickle.dump(maxscore, output, pickle.HIGHEST_PROTOCOL)
                pickle.dump(fruitmaxscore, output, pickle.HIGHEST_PROTOCOL)

        # GAME LOOP BEGINS !!!

        while not crashed:
            # Gtk events

            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

            mos_x, mos_y = pygame.mouse.get_pos()

            # print event

            i += 1

            if(i > 20):
                i = 0

            if(i % 3 == 0):
                if(down == 1):
                    bounce += 1
                    if(bounce > 8):
                        down = 0
                if(down == 0):
                    bounce -= 1
                    if(bounce < 0):
                        down = 1

            gameDisplay.fill(white)
            gameDisplay.blit(back, ((350 + SHIFT_CORRECTOR) * scale_x, 0))

            gameDisplay.blit(plate, ((430 + SHIFT_CORRECTOR) * scale_x,
                                     40 * scale_y))

            head1 = font1.render(_("GAME OVER!"), 1, (white))
            gameDisplay.blit(head1, ((440 + SHIFT_CORRECTOR)* scale_x,
                                     50 * scale_y))

            gameDisplay.blit(scoreplate, ((420 + SHIFT_CORRECTOR)* scale_x,
                                          200 * scale_y))

            gameDisplay.blit(home,
                             ((380 + 60 + 25 + SHIFT_CORRECTOR) * scale_x,
                              (400 + 50) * scale_y))

            gameDisplay.blit(replay,
                             ((600 + 60 - 25 + SHIFT_CORRECTOR) * scale_x,
                              (400 + 50) * scale_y))

            # score check

            scores = font2.render(str(score), 1, black)
            gameDisplay.blit(scores, ((575 + SHIFT_CORRECTOR) * scale_x,
                                      250 * scale_y))

            maxscores = font2.render(str(maxscore), 1, black)
            gameDisplay.blit(maxscores, ((575 + SHIFT_CORRECTOR) * scale_x,
                                         350 * scale_y))

            # GAME START

            if(home.get_rect(
               center=((380 + 60 + 52 + 25 + SHIFT_CORRECTOR) * scale_x,
                       (400 + 50 + 51) * scale_y)).collidepoint(mos_x, mos_y)):
                gameDisplay.blit(home, ((
                    380 + 60 + 25 - 2 + SHIFT_CORRECTOR) * scale_x,
                    (400 + 50 - 2) * scale_y))

                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:

                    return 0

                if event.type == pygame.MOUSEBUTTONUP:
                    press = 0

            # Help menu

            if(replay.get_rect(
               center=((600 + 60 + 52 - 25 + SHIFT_CORRECTOR) * scale_x,
                       (400 + 50 + 51) * scale_y)).collidepoint(mos_x, mos_y)):
                gameDisplay.blit(replay, ((
                    600 + 60 - 25 - 2 + SHIFT_CORRECTOR) * scale_x,
                    (400 + 50 - 2) * scale_y))

                if(pygame.mouse.get_pressed())[0] == 1 and press == 0:

                    return 1

            pygame.draw.rect(gameDisplay, black,
                             (0, 0, (350 + SHIFT_CORRECTOR) * scale_x,
                              768 * scale_y))

            pygame.draw.rect(gameDisplay, black,
                             ((840 + SHIFT_CORRECTOR) * scale_x, 0,
                              (693 + SHIFT_CORRECTOR) * scale_x,
                              768 * scale_y))

            pygame.display.update()
            clock.tick(60)

            if crashed == True:
                # Game crash or Close check
                pygame.quit()
                sys.exit()

        # Just a window exception check condition

        event1 = pygame.event.get()
        if event1.type == pygame.QUIT:
            crashed = True

        if crashed == True:
            pygame.quit()
            sys.exit()
