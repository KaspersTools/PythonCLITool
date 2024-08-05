import rich_click as click
import paramiko
import rich
from paramiko.client import SSHClient

from app import pass_environment
from enviroment import Environment
from kdb_ssh.models.command_result import SSHCommandResult
import kdb_logging


@click.command("tail", short_help="Tail a log file.",
               context_settings=dict(
                    auto_envvar_prefix="RTAIL"
                   )
               )
@click.option(
    "--path", "-p", type=str, help="The path to the file to tail.",
    required=False, show_envvar=True)
@click.option(
    "--server", "-s",
    type=str, help="The server to connect to.", required=False, show_envvar=True)
@click.option("--user", "-u", type=str, help="The username to use.",
              required=False, show_envvar=True)
@click.option("--passwd", "-p", type=str, help="The password to use.",
              required=False, show_envvar=True)
@pass_environment
def cli(ctx: Environment, path: str, server: str, user: str, passwd: str):
    """Shows file changes in the current working directory."""
    ctx.info(f"Connecting to {server} as {user} with password {passwd} to tail {path}")
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ctx.log(f"Connecting to {server} as {user} with password {passwd}")
    ssh_client.connect(server, username=user, password=passwd)

    try:
        tail_and_print(ssh_client, path, True)
    except Exception as e:
        kdb_logging.err(f"An error occurred: {e}", console=rich.console.Console())
    finally:
        ssh_client.close()


def tail(ssh_client: paramiko.client.SSHClient, file: str) \
        -> SSHCommandResult:
    try:
        res = ssh_client.exec_command(f"tail -f {file}")
        return SSHCommandResult(res[0], res[1], res[2], None)
    except Exception as e:
        kdb_logging.err(f"occurred: {e}", console=rich.console.Console())
        raise e


def tail_and_print(
        ssh_client: paramiko.SSHClient,
        file: str,
        should_print: bool) -> None:
    """
    Connect to a remote server and tail a log file, printing the output if specified.

    :param ssh_client: The SSHClient object
    :param file: The file to tail
    :param should_print: Whether to print the output to the console
    """
    console = rich.console.Console()

    result: SSHCommandResult = tail(ssh_client, file)

    if result.error_message:
        kdb_logging.err(f"An error occurred: {result.error_message}", console)
        return

    try:
        if should_print and result.std_out:
            for line in iter(result.std_out.readline, ""):
                kdb_logging.info(line.decode("utf-8"), console)

        # Check for errors in stderr
        if result.std_err:
            err_output = result.std_err.read()
            if err_output:
                kdb_logging.err(
                    f"command execution: {err_output.decode('utf-8')}", console)

    except Exception as e:
        kdb_logging.err(f"An error occurred: {e}", console)
