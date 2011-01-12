# -*- coding: utf-8 -*-

import os
import subprocess

class Setup(object):
    """ Class that generate the Setup.py file based on the 'setup.py' template
        and run py2exe in order to generate the executable.

        params:
            - data: an AppData object containing the parameters for py2exe
    """

    def __init__(self, data):

        #generate the string based on the template and the AppData object
        template = open(os.path.join(os.getcwd(), "templates\\setup.py")).read()
        
        data.logo_tuple = ''
        if data.logo != '':
            data.logo_tuple = '(1, "' + data.logo + '")'
        
        template %= {"main_script" : data.main_script, "version" : data.version, "company_name" : data.company_name,
                    "copyright" : data.copyright, "name" : data.name, "data_files" : data.data_files, "dist" : data.dist,
                    "includes" : data.includes,  "excludes" : data.excludes, "packages" : data.packages,
                    "custom_code" : data.custom_code, 'bundle': data.bundle, 'logo_tuple': data.logo_tuple}

        #write the setup.py file for py2exe
        setup = data.root + "\\setup.py"
        f = open(setup, "w")
        f.write(template)
        f.close()

        #considere log the output of py2exe
        #f = open("log", "w")

        #run the py2exe command
        #python must be in the environment variables!
        cmd = ["python", setup, "py2exe"]
        p = subprocess.Popen(cmd)
        while p.poll() is None:
            pass
