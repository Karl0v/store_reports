import argparse


cli_arguments_parser = argparse.ArgumentParser(
    prog="our_program.exe",
    description="Our description",
)

cli_arguments_parser.add_argument(
    "--crg-input-file",
    action="store",
    nargs="?",
    const=None,
    type=str,
    choices=None,
    required=True,
    help="Open CRG-file",
)

cli_arguments_parser.add_argument(
    "--crg-output-file",
    action="store",
    nargs="?",
    const=None,
    type=str,
    choices=None,
    required=True,
    help="Write crg.txt file",

)

cli_arguments_parser.add_argument(
    "--exp-warning-days",
    action="store",
    nargs="?",
    const=None,
    type=int,
    choices=None,
    required=False,
    default=14,
    help="Provides number of warning days period for expiration report",

)

cli_arguments_parser.add_argument(
    "--exp-start-date",
    action="store",
    nargs="?",
    const=None,
    type=str,
    choices=None,
    required=False,
    default=None,
    help="Starting date for expiration report in this format YYYY-MM-DD",

)

cli_arguments_parser.add_argument(
    "--sku-input-file",
    action="store",
    nargs="?",
    const=None,
    type=str,
    choices=None,
    required=True,
    help="Open SKU-file",
)

cli_arguments_parser.add_argument(
    "--sku-output-file",
    action="store",
    nargs="?",
    const=None,
    type=str,
    choices=None,
    required=True,
    help="Write sku.txt file",

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
