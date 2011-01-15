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
        DIST = data.dist

        #configure pyinstaller
        cmd = ["python", os.path.join(self.PYINSTALLER_DIR, "Configure.py")]
        self.execute(cmd)

        if os.path.exists(DIST):
            shutil.rmtree(DIST)
        #Run the makespec.py
        cmd = ["python", os.path.join(self.PYINSTALLER_DIR, "Makespec.py"), "--noconsole", "-w",
               "--out=" + DIST,
               data.main_script]
        self.execute(cmd)

        #generate a string with a tuple (TOC) of data files
        #to add to the run.spec file
        datas = "import os \r\n"
        for d in data.datas:
            datas += "a.datas += [" + str(d) + "] \r\n"

        f = open(os.path.join(DIST, "run.spec"), 'r')
        string = f.read()
        f.close()

        separator = string.index("coll")
        s1 = string[:separator]
        s2 = string[separator:]

        string = s1 + datas + s2

        f = open(os.path.join(DIST, "run.spec"), 'w')
        f.write(string)
        f.close()

        #Run the Build.py
        cmd = ["python", os.path.join(self.PYINSTALLER_DIR, "Build.py") ,
                os.path.join(DIST, "run.spec")]
        self.execute(cmd)


if __name__ == '__main__':
    PyInstaller()
