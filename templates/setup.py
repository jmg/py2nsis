#*********************************************
#        Auto-Generated With py2Nsis
#*********************************************

import warnings 
#ignore the sets DeprecationWarning
warnings.simplefilter('ignore', DeprecationWarning) 
import py2exe
warnings.resetwarnings() 
from distutils.core import setup
		
target = {
'script' : "%(main_script)s",
'version' : "%(version)s",
'company_name' : "%(company_name)s",
'copyright' : "%(copyright)s",
'name' : "%(name)s", 
'dest_base' : "%(name)s", 
'icon_resources': [%(logo_tuple)s]
}		

%(custom_code)s

setup(

	data_files = %(data_files)s,
    
    zipfile = None,

	options = {"py2exe": {"compressed": 0, 
						  "optimize": 0,
						  "includes": %(includes)s,
						  "excludes": %(excludes)s,
						  "packages": %(packages)s,
						  "bundle_files": %(bundle)s,
						  "dist_dir": "%(dist)s",
						  "xref": False,
						  "skip_archive": False,
						  "ascii": False,
						  "custom_boot_script": '',                          
						 }
			  },
	console = [],
	windows = [target],
	service = [],
	com_server = [],
	ctypes_com_server = []
)
		
