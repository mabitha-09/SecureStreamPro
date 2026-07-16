"""Launch SecureStreamPro from the repository root."""

from pathlib import Path
import runpy


if __name__ == "__main__":
    app_file = Path(__file__).parent / "CloudAudioPy(ECCAES)" / "App.py"
    runpy.run_path(str(app_file), run_name="__main__")
