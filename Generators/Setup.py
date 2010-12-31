# -*- coding: utf-8 -*- 

import os
import subprocess

class Setup(object):

    def __init__(self, data):
            
        template = open(os.path.join(os.getcwd(), "templates\\setup.py")).read()
        
        data.logo_tuple = ''
        if data.logo != '':
            data.logo_tuple = '(1, "' + data.logo + '")'
        
        template %= {"main_script" : data.main_script, "version" : data.version, "company_name" : data.company_name,
                    "copyright" : data.copyright, "name" : data.name, "data_files" : data.data_files, "dist" : data.dist,
                    "includes" : data.includes,  "excludes" : data.excludes, "packages" : data.packages,
                    "custom_code" : data.custom_code, 'bundle': data.bundle, 'logo_tuple': data.logo_tuple}

        setup = data.root + "\\setup.py"
        f = open(setup, "w")
        f.write(template)
        f.close()
        
        #f = open("log", "w")
                        
        cmd = ["python", setup, "py2exe"]
        p = subprocess.Popen(cmd)
        while p.poll() is None:
            pass
