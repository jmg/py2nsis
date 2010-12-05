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
}		

setup(

	data_files = %(data_files)s,

	options = {"py2exe": {"compressed": 0, 
						  "optimize": 0,
						  "includes": %(includes)s,
						  "excludes": %(excludes)s,
						  "packages": %(packages)s,
						  #"dll_excludes": dll_excludes,
						  "bundle_files": 3,
						  "dist_dir": "dist",
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
		
