# -*- encoding: utf-8 -*-
#appModules/dvbviewer.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2012 NVDA Contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
############################
# wird für die Zwangspause beim Start von dvbviewer gebraucht
import time
# apmodulehandler wird von jedem NVDA-Anwendungsmodul gebraucht
import appModuleHandler
import comtypes.client
import os
import sys
# ui gehört zu nvda und gibt eine Meldung per Sprache und (sofern eine Braillezeile angeschlossen ist) in Braille aus.
import ui
impPath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(impPath)
# dvbviewerhelper wurde von comtypes.client.getactiveobject automatisch erzeugt. Das Modul enthielt allerdings einen Fehler, der die in meiner Ausgangsnachricht gezeigte Meldung cannot assign to None erzeugt hat. Im Modul gab es auch tatsächlich eine Zeile none = 0, die ich auskommentiert habe und danach ließ sich das Modul auch problemlos importieren.
import dvbviewerhelper
from logHandler import log
# hier sollen meine Ereignisbehandlungsroutinen rein
class dvbv_eventsink(object):
	# die als Kommentar hinterlegten Anweisungen kann ich leider nicht testen, weil keine Ereignisse durchkommen.
	def __init__(self, server):
		self.server = server
		super(dvbv_eventsink, self).__init__()
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
	def __init__(self, *flags, **kwflags):
		super(AppModule, self).__init__(*flags, **kwflags)
		# der NVDA braucht eine kleine Denkpause, weil er sonst zu früh versuchen würde, das com-Objekt anzuzapfen. und dann schreibt er entweder "Vorgang nicht verfügbar" oder "der Aufruf wurde durch messagefilter abgebrochen" ins Protokoll.
		time.sleep(10)
		self.dvbviewer = comtypes.client.GetActiveObject(dvbviewerhelper.DVBViewer, interface=dvbviewerhelper.IDVBViewer)
		# Und hier vermute ich das Problem. Aus irgendeinem Grund kommen die Ereignisse nicht zu meiner Ereignissenke durch.
		self.connection = comtypes.client.GetEvents(self.dvbviewer.Events,dvbv_eventsink(self.dvbviewer),dvbviewerhelper.IDVBViewerEvents)



