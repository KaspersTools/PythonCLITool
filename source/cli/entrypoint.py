"""
Author: Kasper de Bruin k.debruin@hellebrekers.nl
Date: 2024-08-05 15:55:36
LastEditors: Kasper de Bruin k.debruin@hellebrekers.nl
LastEditTime: 2024-08-05 18:12:18
FilePath: source/cli/entrypoint.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""

import sys
import os

# Add the project root directory to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import app

def main():
    app.cli()

if __name__ == "__main__":
    main()