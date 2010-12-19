# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class FrmAbout
###########################################################################

class FrmAbout ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About py2Nsis", pos = wx.DefaultPosition, size = wx.Size( 200,270 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self.m_panel4, wx.ID_ANY, wx.Bitmap( u"Images/py2nsis_big.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_bitmap2, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.lbVersion = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Version: 0.0.0.1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbVersion.Wrap( -1 )
		bSizer13.Add( self.lbVersion, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lbLicense = wx.StaticText( self.m_panel4, wx.ID_ANY, u"License: GPL v3.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbLicense.Wrap( -1 )
		bSizer13.Add( self.lbLicense, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText18 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Author: Juan Manuel García", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		bSizer13.Add( self.m_staticText18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText19 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Contact: jmg.utn@gmail.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		bSizer13.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_panel4.SetSizer( bSizer13 )
		self.m_panel4.Layout()
		bSizer13.Fit( self.m_panel4 )
		bSizer12.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer12 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

