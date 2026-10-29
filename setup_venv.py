"""Run with `python setup_venv.py` to prepare the project environment."""

from pathlib import Path
import os
import subprocess
import venv


def main():
    root = Path(__file__).resolve().parent
    environment = root / ".venv"
    scripts = environment / ("Scripts" if os.name == "nt" else "bin")
    python = scripts / ("python.exe" if os.name == "nt" else "python")

    if not python.is_file():
        print(f"Creating virtual environment at {environment}", flush=True)
        venv.EnvBuilder(with_pip=True).create(environment)

    subprocess.run(
        [str(python), "-m", "pip", "install", "-r", str(root / "requirements.txt")],
        check=True,
    )
    print("\nSetup complete. Activate the environment:")
    if os.name == "nt":
        print(f'  PowerShell: & "{scripts / "Activate.ps1"}"')
        print(f'  Command Prompt: "{scripts / "activate.bat"}"')
    else:
        print(f'  source "{scripts / "activate"}"')


if __name__ == "__main__":
    main()
