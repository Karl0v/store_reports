from math import sqrt
import argparse


def solution(area: int):
    """
    Uses MegaCorp Solar Tape(TM) to produce square solar panels for LAMBCHOP's
     quantom antimatter reactor core with MAXIMUM efficiency!!!
    :param area: square yars of solar material provided
    :return: array of solar panels, from largest to smallest
    """
    # warehouse of ready to use maximum efficiency MegaCorp Solar Tape(TM) fixated square solar panels
    solar_array = list()
    # currently worked area of solar material
    if area < 0:
        raise ValueError(f'Area should be a positive integer, received {area}')
    worked_area = area
    while worked_area > 0:
        to_tape = sqrt(worked_area)
        taped = int(to_tape)
        # found solar panel
        square_found = taped * taped
        # register incoming solar panel
        solar_array.append(square_found)
        # define new area
        worked_area -= square_found
    return solar_array


if __name__ == '__main__':

    cli_arguments_parser = argparse.ArgumentParser(
    prog="our_program.exe",
    description="Our description",
)

    cli_arguments_parser.add_argument(
        "--solar-area",
        action="store",
        nargs="?",
        const=None,
        type=int,
        choices=None,
        required=False,
        default=0,
        help="Provide square yards of solar material",

    )

    cli_args = cli_arguments_parser.parse_args()
    print(solution(cli_args.solar_area))