import sys
import os

# Add the 'libs' directory to the Python path
#
from kdb_logging import info
import rich.console

info("Imported source.cli", console=rich.console.Console())


# os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))

# cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))
# pass_environment = click.make_pass_decorator(enviroment.Environment, ensure=True)

# __all__ = ["app"]
