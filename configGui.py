# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class FrmConfig
###########################################################################

class FrmConfig ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 434,152 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText11 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Path to Nsis Exe", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		
		bSizer10.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"In order to configurate py2Nsis you have to select the path to your makensis.exe file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer10.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.dpNsisPath = wx.FilePickerCtrl( self.m_panel3, wx.ID_ANY, u"C:\\Archivos de programa\\NSIS\\makensisw.exe", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer10.Add( self.dpNsisPath, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btOk = wx.Button( self.m_panel3, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.btOk, 0, wx.ALL, 5 )
		
		self.btCancel = wx.Button( self.m_panel3, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.btCancel, 0, wx.ALL, 5 )
		
		bSizer10.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		self.m_panel3.SetSizer( bSizer10 )
		self.m_panel3.Layout()
		bSizer10.Fit( self.m_panel3 )
		bSizer9.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( bSizer9 )
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
	

