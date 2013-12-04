# -*- encoding: utf-8 -*-
#appModules/dvbviewer.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2012 NVDA Contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
import time
import appModuleHandler
import comtypes.client
import os
import sys
import ui
impPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(impPath)
import dvbviewerhelper
from logHandler import log
import api
import comHelper
class dvbv_eventsink(object):
	def __init__(self, server):
		super(dvbv_eventsink, self).__init__()
		self.dvbviewer = server
		self.current = dict()
	def IDVBViewerEvents_onAction(self,ActionID):
		log.debugWarning("IDVBViewerEvents_onAction("+str(ActionID)+")")
	def IDVBViewerEvents_onControlChange(self,WindowID, ControlID):
		self.current['control'] = self.dvbviewer.datamanager.Value('#currentcontrol')
		log.debugWarning("IDVBViewerEvents_onControlChange("+str(WindowID)+", "+str(ControlID))
	def IDVBViewerEvents_OnPlaystatechange(self,RendererType, State):
		log.debugWarning("IDVBViewerEvents_OnPlaystatechange("+str(RendererType)+', '+str(State))

	def IDVBViewerEvents_onSelectedItemChange(self):
		self.current['item'] = self.dvbviewer.datamanager.Value('#selecteditem')
		msg = ''
		if self.current.has_key('window') and self.current['window']: msg = self.current['window']
		if self.current.has_key('control') and self.current['control']: msg += ' '+self.current['control']
		if self.current.has_key('item') and self.current['item']: msg += ' '+self.current['item']
		ui.message(msg)
		log.debugWarning("IDVBViewerEvents_onSelectedItemChange()")
	def IDVBViewerEvents_onOSDWindow(self,WindowID):
		self.current['window'] = self.dvbviewer.datamanager.Value('#currentwindow')
		log.debugWarning("IDVBViewerEvents_onOSDWindow("+str(WindowID)+")")

class AppModule(appModuleHandler.AppModule):
	def terminate(self):
		del self.connection
		del self.dvbviewer
		super(AppModule, self).terminate()
	def __init__(self, *flags, **kwflags):
		super(AppModule, self).__init__(*flags, **kwflags)
		time.sleep(10)
		self.dvbviewer = comHelper.getActiveObject("DVBViewerServer.DVBViewer", dynamic=True)
		self.connection = comtypes.client.GetEvents(self.dvbviewer.Events,dvbv_eventsink(self.dvbviewer),dvbviewerhelper.IDVBViewerEvents)



