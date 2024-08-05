import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             '../../libs')))

import kdb_logging

import rich_click as click
from enviroment import Environment

CONTEXT_SETTINGS = dict(auto_envvar_prefix="COMPLEX")

cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "commands"))
pass_environment = click.make_pass_decorator(Environment, ensure=True)


class ComplexCLI(click.RichGroup):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def list_commands(self, ctx) -> list[str]:
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith(".py") and filename.startswith("cmd_"):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name) -> click.Command:
        try:
            mod = __import__(f"commands.cmd_{name}", None, None, ["cli"])
        except ImportError as e:
            import rich
            kdb_logging.err(f"An error occurred: {e} for {name}", console=rich.console.Console())
            raise ImportError()

        return mod.cli


@click.command(cls=ComplexCLI, context_settings=CONTEXT_SETTINGS)
@pass_environment
def cli(ctx: Environment):
    # info("test", rich.Console())
    """A complex command line interface."""
    # ctx.info("test")
    pass
