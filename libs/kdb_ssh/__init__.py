"""
SSH library for connecting to remote servers.
"""

from .client import SSHClient
from .models.command_result import SSHCommandResult
__all__ = ["SSHClient", "SSHCommandResult"]