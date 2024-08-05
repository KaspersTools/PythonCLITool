"""
Author: Kasper de Bruin k.debruin@hellebrekers.nl
Date: 2024-08-01 01:53:24
LastEditors: Kasper de Bruin k.debruin@hellebrekers.nl
LastEditTime: 2024-08-04 12:26:12
FilePath: libs/kdb_ssh/models/command_result.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""

from typing import Any

from paramiko.channel import ChannelFile, ChannelStdinFile, ChannelStderrFile


class SSHCommandResult:
    def __init__(self,
                 std_in: ChannelStdinFile,
                 std_out: ChannelFile,
                 std_err: ChannelStderrFile,
                 error_message: Any = ""
                 ):
        self.std_in = std_in
        self.std_out = std_out
        self.std_err = std_err
        self.error_message = error_message
