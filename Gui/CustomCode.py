# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class FrmCustomCode
###########################################################################

class FrmCustomCode ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 554,388 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText18 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Add your custom code here", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		bSizer19.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		self.tbCode = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer19.Add( self.tbCode, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer15.Add( bSizer19, 1, wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btOk = wx.Button( self.m_panel5, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.btOk, 0, wx.ALL, 5 )
		
		self.btCancel = wx.Button( self.m_panel5, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.btCancel, 0, wx.ALL, 5 )
		
		bSizer15.Add( bSizer20, 0, wx.EXPAND, 5 )
		
		self.m_panel5.SetSizer( bSizer15 )
		self.m_panel5.Layout()
		bSizer15.Fit( self.m_panel5 )
		bSizer14.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer14 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btOk.Bind( wx.EVT_BUTTON, self.btOk_click )
		self.btCancel.Bind( wx.EVT_BUTTON, self.btCancel_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btOk_click( self, event ):
		event.Skip()
	
	def btCancel_click( self, event ):
		event.Skip()
	

