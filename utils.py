import math
import yaml


def compute_normal(x, y, z):
    length = math.sqrt(x**2 + y**2 + z**2)
    return x / length, y / length, z / length


def parse_materials():
    with open("materials.yml") as stream:
        try:
            materials = yaml.safe_load(stream)["materials"]
            colors = []
            parameters = []
            descriptions = []

            for material in materials:
                colors.append(material["color"])
                parameters.append(material["parameters"])
                descriptions.append(material["description"])

            return colors, parameters, descriptions
        except yaml.YAMLError as exc:
            print(exc)
