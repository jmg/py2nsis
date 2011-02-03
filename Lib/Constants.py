import os

DEFAULT_DIST = "dist"
ICON_FILE = os.path.join("Images", "py2nsis.ico")

class MODES:
    """
        Enum of modes
    """

    PYINSTALLER = 1
    PY2EXE = 2
