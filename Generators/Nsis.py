# -*- coding: utf-8 -*-

import os
import subprocess

class Nsis(object):
    """ Class that generate the Installer.nsi file based on the 'installer.nsi' template
        and run the Nsis command in order to generate the installer.

        params:
            - data: an AppData object containing the parameters for Nsis
    """

    def __init__(self, data):

        #generate a list of files that contains the dist dir wich
        #must be specified to Nsis for the xcopy install
        files = []
        dir = os.path.join(data.root, data.dist)
        for root, sub_folders, fs in os.walk(dir):
            for file in fs:
                path = os.path.join(root, file)
                files.append(path)

        sorted(files, key=lambda x: (x.count("\\"), x))

        #add the files to delete when uninstall the application
        data_files = []
        delete_dirs = []
        ant_dir = ''
        for file in files:
            file = file.encode('ascii')
            set_dir = file[file.rindex(dir)+len(dir):file.rindex("\\")]
            #change between diferent directories
            if set_dir != '' and ant_dir != set_dir:
                #if there is a different dir, SetOutPath to the new dir
                data_files.append('*** SetOutPath "$INSTDIR' + set_dir + '" *** ***')
                data_files.append("File " + file + "***")
                ant_dir = set_dir
                delete_dirs.append(set_dir)
            else:
                # else continue appending files in the dir
                data_files.append("File " + file + "***")

        data.files = str(data_files)[1:-1].replace(",", "").replace("'", "")

        #if there is a logo, add to the installer.nsi
        if data.logo != '':
            data.logo = data.logo[data.logo.rindex(data.root)+len(data.root)+1:]
            data.logo = "!define MUI_ICON " + data.logo

        #add the Del instruction for installer.nsi
        data.delete_dirs = ['Delete "$INSTDIR\\' + dir + '\\*" ***' for dir in delete_dirs]
        data.delete_dirs = str(data.delete_dirs).replace(",", "").replace("'", "").replace("[", "").replace("]", "")

        data.rm_dirs = data.delete_dirs.replace("Delete", "Rmdir").replace("\\*","\\")

        #generate the string based on the template and the AppData object
        template = open(os.path.join(os.getcwd(), "templates\\installer.nsi")).read()
        template %= {"main_script" : data.main_script, "version" : data.version, "company_name" : data.company_name,
                   "copyright" : data.copyright, "name" : data.name, "data_files" : data.data_files, "dist" : data.dist,
                   "includes" : data.includes,  "excludes" : data.excludes, "packages" : data.packages,
                   "files": data.files, "main" : data.main, "logo" : data.logo, "delete_dirs" : data.delete_dirs,
                   "rm_dirs" : data.rm_dirs}

        #replace '***' for '\n' to make a readable file
        template = template.replace("***","\n")

        #write the setup.py file for nsis
        f = open(data.dist + "\\installer.nsi", "w")
        f.write(template)
        f.close()

        #considere log the output of Nsis
        #f = open("log2", "w")

        #run the Nsis command
        #Nsis must be instaled!
        cmd = [data.nsisPath, data.dist + "\\installer.nsi"]
        p = subprocess.Popen(cmd)
        while p.poll() is None:
            pass

        print "\n\nFinished Succefully!"
