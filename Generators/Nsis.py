# -*- coding: utf-8 -*- 

import os
import subprocess

class Nsis(object):
    	
    def __init__(self, data):
            
        files = []
        dir = os.path.join(data.root, data.dist)
        for root, sub_folders, fs in os.walk(dir):
            for file in fs:
                path = os.path.join(root, file)
                files.append(path)
                        
        sorted(files, key=lambda x: (x.count("\\"), x))
        
        data_files = []
        delete_dirs = []
        ant_dir = ''
        for file in files:
            file = file.encode('ascii')
            set_dir = file[file.rindex(dir)+len(dir):file.rindex("\\")]            
            if set_dir != '' and ant_dir != set_dir:
                data_files.append('*** SetOutPath "$INSTDIR' + set_dir + '" *** ***')
                data_files.append("File " + file + "***")
                ant_dir = set_dir
                delete_dirs.append(set_dir)
            else:
                data_files.append("File " + file + "***")							
        
        data.files = str(data_files)[1:-1].replace(",", "").replace("'", "")
        
        if data.logo != ''
            data.logo = data.logo[data.logo.rindex(data.root)+len(data.root)+1:]
        
        data.delete_dirs = ['Delete "$INSTDIR\\' + dir + '\\*" ***' for dir in delete_dirs]
        data.delete_dirs = str(data.delete_dirs).replace(",", "").replace("'", "").replace("[", "").replace("]", "")
        
        data.rm_dirs = data.delete_dirs.replace("Delete", "Rmdir").replace("\\*","\\")
        
        template = open(os.path.join(os.getcwd(), "templates\\installer.nsi")).read()
        template %= {"main_script" : data.main_script, "version" : data.version, "company_name" : data.company_name,
                   "copyright" : data.copyright, "name" : data.name, "data_files" : data.data_files, "dist" : data.dist,
                   "includes" : data.includes,  "excludes" : data.excludes, "packages" : data.packages,
                   "files": data.files, "main" : data.main, "logo" : data.logo, "delete_dirs" : data.delete_dirs,
                   "rm_dirs" : data.rm_dirs}
        
        template = template.replace("***","\n")
        f = open(data.dist + "\\installer.nsi", "w")
        f.write(template)
        f.close()
                        
        #f = open("log2", "w") 
        
        cmd = [data.nsisPath, data.dist + "\\installer.nsi"]
        p = subprocess.Popen(cmd)
        while p.poll() is None:
            pass
            
        print "\n\nFinished Succefully!"
