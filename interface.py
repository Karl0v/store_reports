import argparse


cli_arguments_parser = argparse.ArgumentParser(
    prog="our_program.exe",
    description="Our description",
)

cli_arguments_parser.add_argument(
    "--logging-directory",
    action="store",
    nargs="?",
    const=None,
    default="logs",
    type=str,
    choices=None,
    required=False,
    help="If specified, application logs will be saved to this directory. Default value is logs",
    dest="log_dir",
)

cli_arguments_parser.add_argument(
    "---many_parameters",
    action="store",
    nargs="+", # параметр будет указывать сколько будет записано параметров: * - от 0 до n, + от 1 до n, ? - 0 или 1, 1
    default=[3, 4, 5],# когда required=False и пользователь не передал это значение, устанавливается значение default
    type=str,
    choices=['a', 'b', 'c'],#можно передать список допустимых значений
    required=False,
    help="We can",

)
args = cli_arguments_parser.parse_args()
print(args.many_parameters)