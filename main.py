import math
import sys

import consts

import numpy as np
import pygame as pg
from pygame.locals import *

from phong import PhongShading
from utils import compute_normal, parse_materials


class App:
    def __init__(self):
        colors, parameters, descriptions = parse_materials()
        self.colors = colors
        self.parameters = parameters
        self.descriptions = descriptions
        self.material = 0

        self.phong = PhongShading(
            self.parameters[0][0],
            self.parameters[0][1],
            self.parameters[0][2],
            self.parameters[0][3],
        )

        pg.init()
        pg.display.set_caption("Phong Reflection Model: " + self.descriptions[0])
        self.screen = pg.display.set_mode((consts.WIDTH, consts.HEIGHT))
        self.clock = pg.time.Clock()
        self.fps = 30

        self.main_loop()

    def render_sphere(self):
        self.phong.update_params(
            self.parameters[self.material][0],
            self.parameters[self.material][1],
            self.parameters[self.material][2],
            self.parameters[self.material][3],
        )

        self.screen.fill(consts.BACKGROUND_COLOR)

        for x in range(2 * consts.SPHERE_RADIUS):
            for y in range(2 * consts.SPHERE_RADIUS):
                x_coord = x - consts.SPHERE_RADIUS
                y_coord = y - consts.SPHERE_RADIUS
                z_squared = consts.SPHERE_RADIUS**2 - x_coord**2 - y_coord**2

                if z_squared >= 0:
                    z_coord = math.sqrt(z_squared)
                    normal = compute_normal(x_coord, y_coord, z_coord)
                    view_direction = np.array((0, 0, 1))
                    point = np.array((x_coord, y_coord, z_coord))

                    shading = self.phong.phong_shading(normal, view_direction, point)

                    sphere_color = self.colors[self.material]
                    color = (
                        min(255, int(sphere_color[0] * shading)),
                        min(255, int(sphere_color[1] * shading)),
                        min(255, int(sphere_color[2] * shading)),
                    )

                    self.screen.set_at(
                        (
                            x + consts.SCREEN_CENTER[0] - consts.SPHERE_RADIUS,
                            y + consts.SCREEN_CENTER[1] - consts.SPHERE_RADIUS,
                        ),
                        color,
                    )

        pg.display.flip()
        pg.display.set_caption(
            "Phong Reflection Model: " + self.descriptions[self.material]
        )

    def main_loop(self):
        self.render_sphere()

        running = True
        while running:
            for event in pg.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        if self.material != 0:
                            self.material = 0
                            self.render_sphere()
                    if event.key == K_2:
                        if self.material != 1:
                            self.material = 1
                            self.render_sphere()
                    if event.key == K_3:
                        if self.material != 2:
                            self.material = 2
                            self.render_sphere()
                    if event.key == K_4:
                        if self.material != 3:
                            self.material = 3
                            self.render_sphere()
                    if event.key == K_5:
                        if self.material != 4:
                            self.material = 4
                            self.render_sphere()
                    if event.key == K_LEFT:
                        self.phong.change_light_position([-consts.LIGHT_POSITION_SPEED, 0, 0])
                        self.render_sphere()
                    if event.key == K_RIGHT:
                        self.phong.change_light_position([consts.LIGHT_POSITION_SPEED, 0, 0])
                        self.render_sphere()
                    if event.key == K_UP:
                        self.phong.change_light_position([0, -consts.LIGHT_POSITION_SPEED, 0])
                        self.render_sphere()
                    if event.key == K_DOWN:
                        self.phong.change_light_position([0, consts.LIGHT_POSITION_SPEED, 0])
                        self.render_sphere()
                    if event.key == K_w:
                        self.phong.change_light_position([0, 0, -consts.LIGHT_POSITION_SPEED])
                        self.render_sphere()
                    if event.key == K_s:
                        self.phong.change_light_position([0, 0, consts.LIGHT_POSITION_SPEED])
                        self.render_sphere()

            self.clock.tick(self.fps)

        self.quit()

    @staticmethod
    def quit() -> None:
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    app = App()
