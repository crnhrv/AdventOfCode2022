from dataclasses import dataclass
import math


@dataclass
class Robot:
    def __init__(self, ore_cost, type, clay_cost=0, obsidian_cost=0) -> None:
        self.ore_cost = ore_cost
        self.clay_cost = clay_cost
        self.obsidian_cost = obsidian_cost
        self.type = type

    def __repr__(self) -> str:
        return f"({self.ore_cost}o, {self.clay_cost}c, {self.obsidian_cost}o)"


@dataclass
class Blueprint:
    def __init__(self, ore: Robot, clay: Robot, obs: Robot, geo: Robot) -> None:
        self.ore_robot = ore
        self.clay_robot = clay
        self.obs_robot = obs
        self.geo_robot = geo

    def robots(self) -> list[Robot]:
        return [self.geo_robot, self.obs_robot, self.clay_robot, self.ore_robot]

    def __repr__(self) -> str:
        return f"robots: [ore: {self.ore_robot}, clay: {self.clay_robot}, obs: {self.obs_robot}, geo: {self.geo_robot}]"


def p1(blueprints):
    id = 1
    ans1 = 0
    for blueprint in blueprints:
        ans1 += id * get_max_blueprint_score(blueprint, 24)
        id += 1
    print(ans1)


def p2(blueprints):
    ans2 = 1
    for blueprint in blueprints:
        ans2 *= get_max_blueprint_score(blueprint, 32)
        print(ans2)
    print(ans2)


def get_max_blueprint_score(blueprint: Blueprint, mins):
    collected = [0, 0, 0, 0]
    collection_rate = [1, 0, 0, 0]
    state = {}
    max_ore = max(blueprint.robots(), key=lambda x: x.ore_cost).ore_cost
    max_clay = max(blueprint.robots(), key=lambda x: x.clay_cost).clay_cost
    max_obs = max(blueprint.robots(), key=lambda x: x.obsidian_cost).obsidian_cost
    find_best_option(
        blueprint,
        collected,
        collection_rate,
        0,
        state,
        set(),
        max_ore,
        max_clay,
        max_obs,
        mins,
        False,
    )
    return state[mins]


def find_best_option(
    blueprint: Blueprint,
    collected,
    collection_rate,
    minute,
    state: dict[int, tuple[int, int, int, int]],
    seen,
    max_ore,
    max_clay,
    max_obs,
    max_mins,
    built_something_previously,
):
    if minute > max_mins:
        return
    key = (
        minute,
        collected[0],
        collected[1],
        collected[2],
        collected[3],
        collection_rate[0],
        collection_rate[1],
        collection_rate[2],
        collection_rate[3],
    )
    if key in seen:
        return
    seen.add(key)

    if minute in state:
        state[minute] = max(state[minute], collected[3])
    else:
        state[minute] = collected[3]

    built_geo = False
    built_anything = False
    for (i, robot) in enumerate(blueprint.robots()):
        if built_geo:
            return
        if robot.type == "ore" and collection_rate[0] >= max_ore:
            continue
        if robot.type == "clay" and collection_rate[1] >= max_clay:
            continue
        if robot.type == "obs" and collection_rate[2] >= max_obs:
            continue
        if can_afford(collected, robot):
            if not built_something_previously:
                old_collected = [
                    collected[0] - collection_rate[0],
                    collected[1] - collection_rate[1],
                    collected[2] - collection_rate[2],
                    collected[3] - collection_rate[3],
                ]
                if can_afford(old_collected, robot):
                    return

            new_collected = make_robot(collected[:], robot)
            new_collection_rate = collection_rate[:]
            new_collection_rate[3 - i] += 1
            new_collected = collect_ore(new_collected, collection_rate)
            if robot.type == "geo":
                built_geo = True
            else:
                built_anything = True
            find_best_option(
                blueprint,
                new_collected,
                new_collection_rate,
                minute + 1,
                state,
                seen,
                max_ore,
                max_clay,
                max_obs,
                max_mins,
                True,
            )
        elif not built_anything:
            new_collected = collect_ore(collected[:], collection_rate)
            find_best_option(
                blueprint,
                new_collected,
                collection_rate,
                minute + 1,
                state,
                seen,
                max_ore,
                max_clay,
                max_obs,
                max_mins,
                False,
            )

    return


def make_robot(collected, robot: Robot):
    collected[0] -= robot.ore_cost
    collected[1] -= robot.clay_cost
    collected[2] -= robot.obsidian_cost
    return collected


def can_afford(collected, robot: Robot):
    return (
        collected[0] >= robot.ore_cost
        and collected[1] >= robot.clay_cost
        and collected[2] >= robot.obsidian_cost
    )


def collect_ore(collected, collection_rate):
    return [
        collected[0] + collection_rate[0],
        collected[1] + collection_rate[1],
        collected[2] + collection_rate[2],
        collected[3] + collection_rate[3],
    ]


def read_input(filename):
    blueprints = []
    with open(filename, encoding="utf8") as f:
        lines = f.read().splitlines()

        for line in lines:
            robots = line.split(".")
            ore_robot_sections = robots[0].split(" ")
            ore_robot = Robot(int(ore_robot_sections[-2]), type="ore")
            clay_robot_sections = robots[1].split(" ")
            clay_robot = Robot(int(clay_robot_sections[-2]), type="clay")
            obsidian_robot_sections = robots[2].split(" ")
            obsidian_robot = Robot(
                int(obsidian_robot_sections[-5]),
                "obs",
                int(obsidian_robot_sections[-2]),
            )
            geode_robot_sections = robots[3].split(" ")
            geode_robot = Robot(
                int(geode_robot_sections[-5]),
                "geo",
                0,
                int(geode_robot_sections[-2]),
            )

            blueprint = Blueprint(ore_robot, clay_robot, obsidian_robot, geode_robot)
            blueprints.append(blueprint)

    return blueprints


if __name__ == "__main__":
    dt = read_input("input.txt")
    p1(dt[:])
    p2(dt[:3])
