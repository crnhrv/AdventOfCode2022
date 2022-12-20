from dataclasses import dataclass


def main(blueprints):
    for blueprint in blueprints:
        print(blueprint)


@dataclass
class Blueprint:
    def __init__(self, ore, clay, obs, geo) -> None:
        self.ore_robot = ore
        self.clay_robot = clay
        self.obs_robot = obs
        self.geo_robot = geo

    def __repr__(self) -> str:
        return f"robots: [ore: {self.ore_robot}, clay: {self.clay_robot}, obs: {self.obs_robot}, geo: {self.geo_robot}]"


@dataclass
class Robot:
    def __init__(self, ore_cost, clay_cost=0, obsidian_cost=0) -> None:
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obsidian_cost = obsidian_cost

    def __repr__(self) -> str:
        return f"({self.ore_cost}o, {self.clay_cost}c, {self.obsidian_cost}o)"


def read_input(filename):
    blueprints = []
    with open(filename, encoding="utf8") as f:
        lines = f.read().splitlines()

        for line in lines:
            robots = line.split(".")
            ore_robot_sections = robots[0].split(" ")
            ore_robot = Robot(ore_robot_sections[-2])
            clay_robot_sections = robots[1].split(" ")
            clay_robot = Robot(clay_robot_sections[-2])
            obsidian_robot_sections = robots[2].split(" ")
            obsidian_robot = Robot(
                obsidian_robot_sections[-5], obsidian_robot_sections[-2]
            )
            geode_robot_sections = robots[3].split(" ")
            geode_robot = Robot(geode_robot_sections[-5], 0, geode_robot_sections[-2])

            blueprint = Blueprint(ore_robot, clay_robot, obsidian_robot, geode_robot)
            blueprints.append(blueprint)

    return blueprints


if __name__ == "__main__":
    dt = read_input("test-input.txt")
    main(dt)
