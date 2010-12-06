# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class FrmBar
###########################################################################

class FrmBar ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generating...", pos = wx.DefaultPosition, size = wx.Size( 500,100 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.lbGenerate = wx.StaticText( self.m_panel2, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbGenerate.Wrap( -1 )
		bSizer11.Add( self.lbGenerate, 0, wx.ALL, 5 )
		
		self.pgGenerate = wx.Gauge( self.m_panel2, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		bSizer11.Add( self.pgGenerate, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel2.SetSizer( bSizer11 )
		self.m_panel2.Layout()
		bSizer11.Fit( self.m_panel2 )
		bSizer10.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer10 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

