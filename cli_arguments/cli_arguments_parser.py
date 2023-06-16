import argparse


cli_arguments_parser = argparse.ArgumentParser(
    prog="our_program.exe",
    description="Our description",
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
    "--output-folder",
    action="store",
    nargs="?",
    const=None,
    type=str,
    choices=None,
    required=True,
    help="Where all reports will be saved",

)

cli_arguments_parser.add_argument(
    "--source-folder",
    action="store",
    nargs="?",
    const=None,
    type=str,
    choices=None,
    required=True,
    help="From what folder will be read",

)