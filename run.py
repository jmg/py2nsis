#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#       py2Nsis v0.0.0.1
#
#       Copyright 2010 Juan Manual García <jmg.utn@gmail.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.


from wx import App
from main import FrmApplication

class Application(App):
    """
        The Main Class of the application that implents the Entry Point
    """

    def OnInit(self):
        frmApplication = FrmApplication(None)
        frmApplication.Show()
        return True


if __name__ == '__main__':

    app = Application(0)
    app.MainLoop()
