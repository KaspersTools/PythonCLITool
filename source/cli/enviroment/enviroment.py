"""
Author: Kasper de Brsuin k.debruin@hellebrekers.nl
Date: 2024-08-05 15:53:33
LastEditors: Kasper de Bruin k.debruin@hellebrekers.nl
LastEditTime: 2024-08-05 18:04:26
FilePath: source/cli/enviroment/enviroment.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""

import os
from sys import stdout, stderr
import typing as t

import click


class Environment:
    def __init__(self):
        # self.console = console.Console()
        self.verbose = False
        self.home = os.getcwd()

    def log(self, msg: str, *args,
            file: t.Optional[t.IO[t.Any]] = stdout,
            is_error: bool = False
            ):
        """Logs a message to {file}."""
        """Logs a message to {file}."""
        if args:
            msg %= args

        # self.console.print(msg)
        click.echo(msg, file=stdout, err=is_error)

    def info(self, msg:str, *args):
        self.log(msg, *args)
        # click.echo(msg, file=sys.stderr)

    def warning(self, msg:str, *args):
        """Logs a message to stderr."""
        self.log(msg, *args)
        # click.echo(msg, file=sys.stderr)

    def debug(self, msg:str, *args):
        """Logs a message to stderr."""
        self.log(msg, *args)
        # click.echo(msg, file=sys.stderr)

    def trace(self, msg:str, *args):
        """Logs a message to stderr."""
        self.log(msg, *args)
        # click.echo(msg, file=sys.stderr)

    # def error(self, msg:str, *args):
    #     """Logs a message to stderr."""
    #     self.log(msg=msg, is_error=True, *args) 
    #     # click.echo(msg, file=sys.stderr)
