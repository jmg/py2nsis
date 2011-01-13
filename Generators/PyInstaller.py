import os
import shutil
from BaseGenerator import BaseGenerator

class PyInstaller(BaseGenerator):
    """
        Class to generate the executable using pyInstaller

        params:
            - data: an AppData object containing the parameters for Nsis
    """
    PYINSTALLER_DIR = "Generators/Libs/pyinstaller-1.5-rc/"

    def __init__(self, data):
        commands = []
        DIST = data.root + "/installer"

        #configure pyinstaller
        cmd = ["python", self.PYINSTALLER_DIR + "Configure.py"]
        commands.append(cmd)

        if os.path.exists(DIST):
            shutil.rmtree(DIST)
        #Run the makespec.yp
        cmd = ["python", self.PYINSTALLER_DIR + "Makespec.py", "--noconsole", "-w",
               "--out=" + DIST,
               data.main_script]
        commands.append(cmd)

        #Run the Build.py
        cmd = ["python", self.PYINSTALLER_DIR + "Build.py",
                DIST + "/run.spec"]
        commands.append(cmd)

        #call the execute in the superclass
        for cmd in commands:
            self.execute(cmd)


if __name__ == '__main__':
    PyInstaller()
