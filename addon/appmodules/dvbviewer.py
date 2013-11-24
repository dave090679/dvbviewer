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
class dvbv_eventsink(object):
	def IDVBViewerEvents_onAction(self,ActionID):
		log.debugWarning("IDVBViewerEvents_onAction("+str(ActionID)+")")
	def IDVBViewerEvents_onControlChange(self,WindowID, ControlID):
		# ui.message(self.server.datamanager.value('#currentcontrol'))
		log.debugWarning("IDVBViewerEvents_onControlChange("+str(WindowID)+", "+str(ControlID))
	def IDVBViewerEvents_OnPlaystatechange(self,RendererType, State):
		log.debugWarning("IDVBViewerEvents_OnPlaystatechange("+str(RendererType)+', '+str(State))

	def IDVBViewerEvents_onSelectedItemChange(self):
		# ui.message(self.server.datamanager.value('#selecteditem'))
		log.debugWarning("IDVBViewerEvents_onSelectedItemChange()")
	def IDVBViewerEvents_onOSDWindow(self,WindowID):
		log.debugWarning("IDVBViewerEvents_onOSDWindow("+str(ID)+")")
		# ui.message(self.server.datamanager.value('#currentwindow'))

class AppModule(appModuleHandler.AppModule):
	def terminate(self):
		del self.connection
		del self.dvbviewer
		super(AppModule, self).terminate()
	def __init__(self, *flags, **kwflags):
		super(AppModule, self).__init__(*flags, **kwflags)
		time.sleep(10)
		self.dvbviewer = comtypes.client.GetActiveObject(dvbviewerhelper.DVBViewer, interface=dvbviewerhelper.IDVBViewer)
		self.connection = comtypes.client.GetEvents(self.dvbviewer.Events,dvbv_eventsink(),dvbviewerhelper.IDVBViewerEvents)



