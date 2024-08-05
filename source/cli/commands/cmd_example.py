import rich_click as click

from cli.app import (pass_environment)
from cli.enviroment import Environment


@click.command("status", short_help="Shows file changes.")
@click.option("--user", "-u", type=str, help="The username to use.")
@click.option("--passwd", "-p", type=str, help="The password to use.")
@click.option('--n', required=True, type=int, help='Number of lines to show.')
@pass_environment
def cli(ctx: Environment, user: str, passwd: str)\
        -> None:
    """Shows file changes in the current working directory."""
    ctx.info("bla bla bla, info")
    ctx.warning("bla bla bla, warning")
    ctx.debug("bla bla bla, debug")
    ctx.trace("bla bla bla, trace")

