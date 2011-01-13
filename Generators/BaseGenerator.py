# -*- coding: utf-8 -*-
import abc
import subprocess

class BaseGenerator(object):
    """
        An abstract class that defines the base for the installer/executable
        generators objects
    """
    def __init__(self):
        pass

    def log(self):
        #Todo: implement a logging system for the outputs of the generators
        pass

    def execute(self, cmd):
        """
            Execute the command to generate the executable/intaller

            params:
                cmd: A list of string starting from the command
                     followed for the parameters
        """
        p = subprocess.Popen(cmd)
        while p.poll() is None:
            pass

