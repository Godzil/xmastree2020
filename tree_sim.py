import re
import pygame
import sys

pygame.init()
window = pygame.display.set_mode((512, 907))

class location():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class led():
    def __init__(self):
        self.colour = [0, 0, 0]
        self.loc = location(0, 0, 0)

    def setLocation(self, loc):
        self.loc = loc

    def setColour(self, colour):
        self.colour = colour


def ThreeD2TwoD(x, y, z):
    return (250+x, 950 - (454+z))


def drawLight(l):
    pt = ThreeD2TwoD(l.loc.x, l.loc.y, l.loc.z)
    c = (l.colour[1], l.colour[0], l.colour[2])
    pygame.draw.rect(window, c, (pt[0]-1, pt[1]-1, 3, 3))


# All the magic happen here.
class neopixel():
    class NeoPixel():
        def __init__(self, board, ledCount, auto_write=False):
            # We need to do the same as the main file, import the tree configuration:
            coordfilename = "coords.txt"

            fin = open(coordfilename, 'r')
            coords_raw = fin.readlines()

            coords_bits = [i.split(",") for i in coords_raw]

            coords = []

            for slab in coords_bits:
                new_coord = []
                for i in slab:
                    new_coord.append(int(re.sub(r'[^-\d]', '', i)))
                coords.append(location(new_coord[0], new_coord[1], new_coord[2]))

            self._count = ledCount
            self._leds = []
            for i in range(0, ledCount):
                l = led()
                l.setLocation(coords[i])
                self._leds.append(l)

        def __setitem__(self, key, value):
            self._leds[key].colour = value

        def __getitem__(self, item):
            return self._leds[item].colour

        def show(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(-1)

            window.fill(0)


            for l in self._leds:
                drawLight(l)

            pygame.display.flip()


# Nothing to be done here, just define some value to pretend.
class board():
    D18 = 0
