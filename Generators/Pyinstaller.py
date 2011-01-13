import os
import shutil
from BaseGenerator import BaseGenerator

class PyInstaller(BaseGenerator):
    """
        Class to generate the executable using pyInstaller
    """
    def __init__(self):
        commands = []
        DIST = os.getcwd() + "/installer"

        #configure pyinstaller
        #cmd = ["python", "Libs/pyinstaller-1.5-rc/Configure.py"]
        #commands.append(cmd)
        if os.path.exists(DIST):
            shutil.rmtree(DIST)
        #Run the makespec.yp
        cmd = ["python", "Libs/pyinstaller-1.5-rc/Makespec.py", "--noconsole", "-w",
               "--out=" + DIST,
               "/home/jm/DESARROLLO/py2nsis/run.py"]
        commands.append(cmd)
        #Run the Build.py
        cmd = ["python", "Libs/pyinstaller-1.5-rc/Build.py",
                DIST + "/run.spec"]
        commands.append(cmd)
        #call the execute in the superclass
        for cmd in commands:
            self.execute(cmd)


if __name__ == '__main__':
    PyInstaller()
