#!/usr/bin/env python3

import subprocess
import typer

app = typer.Typer()

@app.command(help="Searches for a package in the system's package manager using the provided name.")
def search_package(name: str = typer.Option(..., help="The name of the package to search for.")):
    """
    Searches for a package in the system's package manager using the provided name.

    Args:
        name (str): The name of the package to search for.
    """
    try:
        subprocess.run(f"sudo apt list | grep {name}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Task Cannot Be Completed: {e}")

@app.command(help="Fixes broken dependencies in the system's package manager.")
def fix_broken_dependencies():
    """
    Fixes broken dependencies in the system's package manager.
    """
    try:
        subprocess.run("sudo apt --fix-broken install && sudo dpkg --configure -a", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Task Cannot Be Completed: {e}")

@app.command(help="Cleans up packages and removes unnecessary files from the system.")
def clean(package: str = typer.Option(None, help="The name of the package to purge.")):
    """
    Cleans up packages and removes unnecessary files from the system.
    :param package: The name of the package to purge.
    """
    if package is not None:
        try:
            subprocess.run(f"sudo apt purge {package} && sudo apt autoremove --purge", shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Task Cannot Be Completed: {e}")
    try:
        subprocess.run("sudo apt autoremove --purge && sudo apt autoclean && sudo apt clean", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Task Cannot Be Completed: {e}")

@app.command(help="Finds dependencies for a given package.")
def find_package_dependencies(package: str = typer.Option(..., help="The name of the package to check dependencies for.")):
    """
    Finds dependencies for a given package.

    Args:
        package (str): The name of the package to check dependencies for.
    """
    try:
        subprocess.run(f"apt depends {package} && apt rdepends {package}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Task Cannot Be Completed: {e}")

if __name__ == "__main__":
    app()
