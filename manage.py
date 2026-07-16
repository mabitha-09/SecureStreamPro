"""Django-style development command for this Flask project."""

from pathlib import Path
import runpy
import sys


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] != "runserver":
        print("Usage: python manage.py runserver")
        raise SystemExit(1)

    runpy.run_path(str(Path(__file__).parent / "run.py"), run_name="__main__")


if __name__ == "__main__":
    main()
