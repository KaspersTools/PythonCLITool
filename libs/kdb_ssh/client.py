"""
Author: Kasper de Bruin k.debruin@hellebrekers.nl
Date: 2024-08-01 01:52:27
LastEditors: Kasper de Bruin k.debruin@hellebrekers.nl
LastEditTime: 2024-08-05 16:51:43
FilePath: libs/kdb_ssh/client.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""

from threading import Thread

import paramiko

class SSHClient:
    """
    A class to represent an SSH client.
    """
    def __init__(self, server: str, user: str, passwd: str) -> None:
        self.server = server
        self.user = user
        self.passwd = passwd

        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print(f"Connecting to {server} as {user} with password {passwd}")
        self.ssh.connect(self.server, username=self.user, password=self.passwd)
        self.current_thread: None | Thread = None

    def close(self):
        if self.ssh:
            self.ssh.close()
            self.ssh = None
        if self.current_thread:
            self.current_thread.join()

    # def run_tail_threaded(self, file: str, should_print: bool = True) -> Thread:
    #     """
    #     Run a command on the remote server in a separate thread.
    #     
    #     Args:
    #         :param file: The file to tail
    #         :param should_print: Whether to print the output to the console
    #         :return: The thread object that is running the command
    #     """
    #     self.current_thread = Thread(
    #         target=tail_and_print,args=(self.ssh,file,should_print))
    #     
    #     self.current_thread.start()
    #     return self.current_thread
