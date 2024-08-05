from setuptools import setup, find_packages

setup(
    name='cli_tool',
    version='0.1',
    packages=find_packages(
        include=[
            'source',
            'source.*',
            'libs.*'
            ]
        ),
    install_requires=[
        # List your dependencies here
        ],
    entry_points={
        'console_scripts': [
            # Define your CLI entry points here
            'cli-tool=source.cli.entrypoint:main',
            ],
        },
    include_package_data=True,
    package_data={
        # If you have data files in your packages, specify them here
        },
    )