import numpy as np

import consts


class PhongShading:
    def __init__(
        self,
        ambient_reflection,
        diffuse_reflection,
        specular_reflection,
        specular_exponent,
    ):
        self.ambient_reflection = ambient_reflection
        self.diffuse_reflection = diffuse_reflection
        self.specular_reflection = specular_reflection
        self.specular_exponent = specular_exponent

        self.light_position = consts.INITIAL_LIGHT_POSITION

    def change_light_position(self, light_position):
        self.light_position[0] += light_position[0]
        self.light_position[1] += light_position[1]
        self.light_position[2] += light_position[2]

    def update_params(
        self,
        ambient_reflection,
        diffuse_reflection,
        specular_reflection,
        specular_exponent,
    ):
        self.ambient_reflection = ambient_reflection
        self.diffuse_reflection = diffuse_reflection
        self.specular_reflection = specular_reflection
        self.specular_exponent = specular_exponent

    def phong_shading(self, normal, view_direction, point):
        light_direction = np.array(self.light_position) - point
        light_direction = light_direction / np.linalg.norm(light_direction)

        ambient = self.ambient_reflection * consts.AMBIENT_INTENSITY

        diffuse = (
            self.diffuse_reflection
            * max(np.dot(normal, light_direction), 0)
            * consts.DIFFUSE_INTENSITY
        )

        reflection = 2 * np.dot(normal, light_direction) * np.array(normal) - np.array(
            light_direction
        )
        specular = (
            self.specular_reflection
            * max(np.dot(reflection, view_direction), 0) ** self.specular_exponent
            * consts.SPECULAR_INTENSITY
        )

        return ambient + diffuse + specular
