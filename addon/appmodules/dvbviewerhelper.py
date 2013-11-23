# -*- coding: mbcs -*-
typelib_path = u'C:\\Programme\\DVBViewer\\dvbviewer.exe'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from ctypes.wintypes import VARIANT_BOOL
from ctypes import HRESULT
from comtypes import BSTR
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import CoClass
from comtypes import IUnknown
from comtypes.automation import VARIANT
from comtypes.automation import VARIANT
from comtypes import DISPMETHOD, DISPPROPERTY, helpstring


class ITimerItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A Timer object, it describes a recording timer'
    _iid_ = GUID('{C243EAA6-9638-4EF1-9934-92F31990C0FC}')
    _idlflags_ = ['dual', 'oleautomation']
class ITuner(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A single tunerstructure used by the dvbviewer'
    _iid_ = GUID('{17D7A163-BCAE-4F69-8014-316503CC03F8}')
    _idlflags_ = ['dual', 'oleautomation']

# values for enumeration 'TDVBVShutdown'
# None = 0
PowerOff = 1
Standby = 2
Hibernate = 3
Close = 4
Playlist = 5
Slumbermode = 6
TDVBVShutdown = c_int # enum

# values for enumeration 'TDVBVTimerAction'
Record_ = 0
Tune = 1
AudioPlugin = 2
Videoplugin = 3
TDVBVTimerAction = c_int # enum
ITimerItem._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Cancelled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(202), 'propget'], HRESULT, 'ChannelName',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(203), 'propget'], HRESULT, 'ChannelNr',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(205), 'propget'], HRESULT, 'Done',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(206), 'propget'], HRESULT, 'Filename',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(206), 'propput'], HRESULT, 'Filename',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(207), 'propget'], HRESULT, 'ID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(208), 'propget'], HRESULT, 'Instant',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(209), 'propget'], HRESULT, 'isPlugin',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(210), 'propget'], HRESULT, 'Recording',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(211), 'propget'], HRESULT, 'Tuner',
              ( ['retval', 'out'], POINTER(POINTER(ITuner)), 'Value' )),
    COMMETHOD([dispid(212), 'propget'], HRESULT, 'ChannelID',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(212), 'propput'], HRESULT, 'ChannelID',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(213), 'propget'], HRESULT, 'Date',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([dispid(213), 'propput'], HRESULT, 'Date',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([dispid(214), 'propget'], HRESULT, 'Days',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(214), 'propput'], HRESULT, 'Days',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(215), 'propget'], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(215), 'propput'], HRESULT, 'Description',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(216), 'propget'], HRESULT, 'DisableAV',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(216), 'propput'], HRESULT, 'DisableAV',
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD([dispid(217), 'propget'], HRESULT, 'Enabled',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(217), 'propput'], HRESULT, 'Enabled',
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD([dispid(218), 'propget'], HRESULT, 'EndTime',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([dispid(218), 'propput'], HRESULT, 'EndTime',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([dispid(219), 'propget'], HRESULT, 'Shutdown',
              ( ['retval', 'out'], POINTER(TDVBVShutdown), 'Value' )),
    COMMETHOD([dispid(219), 'propput'], HRESULT, 'Shutdown',
              ( ['in'], TDVBVShutdown, 'Value' )),
    COMMETHOD([dispid(220), 'propget'], HRESULT, 'StartTime',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([dispid(220), 'propput'], HRESULT, 'StartTime',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([dispid(221), 'propget'], HRESULT, 'TimerAction',
              ( ['retval', 'out'], POINTER(TDVBVTimerAction), 'Value' )),
    COMMETHOD([dispid(221), 'propput'], HRESULT, 'TimerAction',
              ( ['in'], TDVBVTimerAction, 'Value' )),
    COMMETHOD([dispid(204), 'propget'], HRESULT, 'Executeable',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
]
################################################################
## code template for ITimerItem implementation
##class ITimerItem_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    EndTime = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Instant(self):
##        '-no docstring-'
##        #return Value
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Description = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Date = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    DisableAV = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    StartTime = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    ChannelID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Enabled = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Days = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Filename = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Recording(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def isPlugin(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Executeable(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Done(self):
##        '-no docstring-'
##        #return Value
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Shutdown = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Tuner(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Cancelled(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def ChannelNr(self):
##        '-no docstring-'
##        #return Value
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    TimerAction = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ChannelName(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def ID(self):
##        '-no docstring-'
##        #return Value
##

class Teletextmanager(CoClass):
    _reg_clsid_ = GUID('{DF1A75B3-A9BB-4625-8893-57EB577F808C}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{017FD4A8-5E00-4DF8-A388-434B8E592CC4}', 1, 1)
class ITeletextEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{CB23390F-A678-4E20-9FFB-9A1C6F741601}')
    _idlflags_ = []
    _methods_ = []
class IVideotext(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The Videotext-Objekt enables you to get videotext from the DVBViewer'
    _iid_ = GUID('{3696EC85-4824-4265-8882-E35290113C1C}')
    _idlflags_ = ['dual', 'oleautomation']
Teletextmanager._com_interfaces_ = [IVideotext]
Teletextmanager._outgoing_interfaces_ = [ITeletextEvents]

class DVBViewerEvents(CoClass):
    _reg_clsid_ = GUID('{1937F78D-255B-4D76-9592-EA190EF2C616}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{017FD4A8-5E00-4DF8-A388-434B8E592CC4}', 1, 1)
class IDVBViewerEventhelper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{C13EC070-D789-4AD2-B1E0-9B53C7F31A11}')
    _idlflags_ = ['dual', 'oleautomation']
class IDVBViewerEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    'Eventhelper'
    _iid_ = GUID('{B397FB16-A027-4D5B-88EB-FD9A2AA28D92}')
    _idlflags_ = []
    _methods_ = []
DVBViewerEvents._com_interfaces_ = [IDVBViewerEventhelper]
DVBViewerEvents._outgoing_interfaces_ = [IDVBViewerEvents]


# values for enumeration 'TDVBVTunerType'
ttCable = 0
ttSatellite = 1
ttTerrestrial = 2
ttATSC = 3
TDVBVTunerType = c_int # enum
ITuner._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'TunerType',
              ( ['retval', 'out'], POINTER(TDVBVTunerType), 'Value' )),
    COMMETHOD([dispid(202), 'propget'], HRESULT, 'Frequency',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(203), 'propget'], HRESULT, 'SymbolRate',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(204), 'propget'], HRESULT, 'LNB',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(205), 'propget'], HRESULT, 'PMT',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(206), 'propget'], HRESULT, 'ECM_0',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(207), 'propget'], HRESULT, 'Unused2',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(208), 'propget'], HRESULT, 'AVFormat',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(209), 'propget'], HRESULT, 'FEC',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(210), 'propget'], HRESULT, 'CAID_0',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(211), 'propget'], HRESULT, 'Polarity',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(212), 'propget'], HRESULT, 'ECM_1',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(213), 'propget'], HRESULT, 'LNBSelection',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(214), 'propget'], HRESULT, 'CAID_1',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(215), 'propget'], HRESULT, 'Diseqc',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(216), 'propget'], HRESULT, 'ECM_2',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(217), 'propget'], HRESULT, 'AudioPID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(218), 'propget'], HRESULT, 'CAID_2',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(219), 'propget'], HRESULT, 'VideoPID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(220), 'propget'], HRESULT, 'TransportStreamID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(221), 'propget'], HRESULT, 'telePID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(222), 'propget'], HRESULT, 'NetworkID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(223), 'propget'], HRESULT, 'SID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(224), 'propget'], HRESULT, 'PCRPID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(225), 'propget'], HRESULT, 'Group',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
]
################################################################
## code template for ITuner implementation
##class ITuner_Impl(object):
##    @property
##    def Polarity(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def LNBSelection(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Group(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def ECM_0(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def SID(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def VideoPID(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def AVFormat(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def CAID_0(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Unused2(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def ECM_1(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def CAID_1(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def CAID_2(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def ECM_2(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def PMT(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def PCRPID(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def TransportStreamID(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def LNB(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Diseqc(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def FEC(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def AudioPID(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def telePID(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def NetworkID(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Frequency(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def SymbolRate(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def TunerType(self):
##        '-no docstring-'
##        #return Value
##

class IEPGCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The EPGCollection is a list of EPGEntries'
    _iid_ = GUID('{605E3A97-B64F-47DF-8E7A-7DC832694F96}')
    _idlflags_ = ['dual', 'oleautomation']
class IEPGItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Describes a EPGItem delivered by the EPGCollection/manager'
    _iid_ = GUID('{340BE5BA-0B5B-490A-B0C3-FB30B88FCEF5}')
    _idlflags_ = ['dual', 'oleautomation']
IEPGCollection._methods_ = [
    COMMETHOD([dispid(0), 'defaultcollelem', 'propget'], HRESULT, 'Item',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(IEPGItem)), 'Value' )),
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(-4), 'propget'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Value' )),
]
################################################################
## code template for IEPGCollection implementation
##class IEPGCollection_Impl(object):
##    @property
##    def Count(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Item(self, Index):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Value
##

class IFavoritesManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{6AF57FCE-44D9-4DC8-9276-87F8F9CFE818}')
    _idlflags_ = ['dual', 'oleautomation']
class IFavoritesCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{83AEB9FB-6FF3-49D6-A5F7-3CA4F0554743}')
    _idlflags_ = ['dual', 'oleautomation']
IFavoritesManager._methods_ = [
    COMMETHOD([dispid(207)], HRESULT, 'GetFavoritesList',
              ( ['out'], POINTER(VARIANT), 'List' ),
              ( ['retval', 'out'], POINTER(c_int), 'Result' )),
    COMMETHOD([dispid(202)], HRESULT, 'GetFavorites',
              ( ['retval', 'out'], POINTER(POINTER(IFavoritesCollection)), 'Value' )),
    COMMETHOD([dispid(201)], HRESULT, 'Add',
              ( ['in'], c_int, 'ChannelNr' ),
              ( ['in'], BSTR, 'Group' )),
    COMMETHOD([dispid(203)], HRESULT, 'AddbyID',
              ( ['in'], BSTR, 'ChannelID' ),
              ( ['in'], BSTR, 'Group' )),
    COMMETHOD([dispid(204)], HRESULT, 'AddGroup',
              ( ['in'], BSTR, 'Group' )),
    COMMETHOD([dispid(205)], HRESULT, 'IsFavorite',
              ( ['in'], c_int, 'SID' ),
              ( ['in'], c_int, 'APID' ),
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(206)], HRESULT, 'IsFavoritebyEPGChannelID',
              ( ['in'], c_int, 'EPGChannelID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(208)], HRESULT, 'IsFavoritebyChannelID',
              ( ['in'], BSTR, 'ChannelID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(209)], HRESULT, 'GetGroupsList',
              ( ['out'], POINTER(VARIANT), 'List' ),
              ( ['retval', 'out'], POINTER(c_int), 'Result' )),
    COMMETHOD([dispid(210)], HRESULT, 'RemoveGroup',
              ( ['in'], c_int, 'ID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(211)], HRESULT, 'RemoveFavorite',
              ( ['in'], c_int, 'ID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
]
################################################################
## code template for IFavoritesManager implementation
##class IFavoritesManager_Impl(object):
##    def IsFavoritebyChannelID(self, ChannelID):
##        '-no docstring-'
##        #return Value
##
##    def AddbyID(self, ChannelID, Group):
##        '-no docstring-'
##        #return 
##
##    def IsFavorite(self, SID, APID, Name):
##        '-no docstring-'
##        #return Value
##
##    def IsFavoritebyEPGChannelID(self, EPGChannelID):
##        '-no docstring-'
##        #return Value
##
##    def RemoveGroup(self, ID):
##        '-no docstring-'
##        #return Value
##
##    def RemoveFavorite(self, ID):
##        '-no docstring-'
##        #return Value
##
##    def Add(self, ChannelNr, Group):
##        '-no docstring-'
##        #return 
##
##    def AddGroup(self, Group):
##        '-no docstring-'
##        #return 
##
##    def GetFavoritesList(self):
##        '-no docstring-'
##        #return List, Result
##
##    def GetGroupsList(self):
##        '-no docstring-'
##        #return List, Result
##
##    def GetFavorites(self):
##        '-no docstring-'
##        #return Value
##

class IFavoritesItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{AB38A523-A294-4CD1-B72E-75E614096620}')
    _idlflags_ = ['dual', 'oleautomation']
IFavoritesCollection._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(0), 'defaultcollelem', 'propget'], HRESULT, 'Item',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(IFavoritesItem)), 'Value' )),
    COMMETHOD([dispid(-4), 'propget'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Value' )),
]
################################################################
## code template for IFavoritesCollection implementation
##class IFavoritesCollection_Impl(object):
##    @property
##    def Count(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Item(self, Index):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Value
##

class IPlaylist(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{43242D96-8407-4100-918C-D76D41FC1B2A}')
    _idlflags_ = ['dual', 'oleautomation']
class IPlaylistItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{40659892-1CBF-48C1-8B41-1B2BECDFB2BA}')
    _idlflags_ = ['dual', 'oleautomation']
IPlaylist._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(201), 'propput'], HRESULT, 'Name',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(0), 'propget'], HRESULT, 'Item',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(IPlaylistItem)), 'Value' )),
    COMMETHOD([dispid(202), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(203)], HRESULT, 'Shuffle'),
    COMMETHOD([dispid(204)], HRESULT, 'ResetStatus'),
    COMMETHOD([dispid(205)], HRESULT, 'Save',
              ( ['in'], BSTR, 'Filename' )),
    COMMETHOD([dispid(207)], HRESULT, 'Remove',
              ( ['in'], BSTR, 'Filename' ),
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(208)], HRESULT, 'Load',
              ( ['in'], BSTR, 'Filename' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(209)], HRESULT, 'Clear'),
    COMMETHOD([dispid(210)], HRESULT, 'Allplayed',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(211)], HRESULT, 'Add',
              ( ['in'], POINTER(IPlaylistItem), 'Item' )),
]
################################################################
## code template for IPlaylist implementation
##class IPlaylist_Impl(object):
##    @property
##    def Count(self):
##        '-no docstring-'
##        #return Value
##
##    def Load(self, Filename):
##        '-no docstring-'
##        #return Value
##
##    def Shuffle(self):
##        '-no docstring-'
##        #return 
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Name = property(_get, _set, doc = _set.__doc__)
##
##    def ResetStatus(self):
##        '-no docstring-'
##        #return 
##
##    def Allplayed(self):
##        '-no docstring-'
##        #return Value
##
##    def Clear(self):
##        '-no docstring-'
##        #return 
##
##    def Remove(self, Filename):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Item(self, Index):
##        '-no docstring-'
##        #return Value
##
##    def Add(self, Item):
##        '-no docstring-'
##        #return 
##
##    def Save(self, Filename):
##        '-no docstring-'
##        #return 
##

class IOSDItems(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{41E45161-06B8-4DF0-AB5C-3FAC75B51403}')
    _idlflags_ = ['dual', 'oleautomation']
class IOSDItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{1A2F98E3-535D-43BE-AA0F-24AB83EF1C51}')
    _idlflags_ = ['dual', 'oleautomation']
IOSDItems._methods_ = [
    COMMETHOD([dispid(201)], HRESULT, 'Add',
              ( ['in'], POINTER(IOSDItem), 'Item' )),
    COMMETHOD([dispid(202)], HRESULT, 'AddFromList',
              ( ['in'], POINTER(IOSDItems), 'SourceList' )),
    COMMETHOD([dispid(203)], HRESULT, 'AddNew',
              ( ['retval', 'out'], POINTER(POINTER(IOSDItem)), 'Value' )),
    COMMETHOD([dispid(204)], HRESULT, 'Clear'),
    COMMETHOD([dispid(205)], HRESULT, 'Clone',
              ( ['retval', 'out'], POINTER(POINTER(IOSDItems)), 'Value' )),
    COMMETHOD([dispid(206)], HRESULT, 'FindItem',
              ( ['in'], BSTR, 'Key' ),
              ( ['in'], VARIANT, 'Value' ),
              ( ['retval', 'out'], POINTER(POINTER(IOSDItem)), 'Value1' )),
    COMMETHOD([dispid(207)], HRESULT, 'FindItemIndex',
              ( ['in'], BSTR, 'Key' ),
              ( ['in'], VARIANT, 'Value' ),
              ( ['retval', 'out'], POINTER(c_int), 'Value1' )),
    COMMETHOD([dispid(208)], HRESULT, 'Remove',
              ( ['in'], c_int, 'Index' )),
    COMMETHOD([dispid(209)], HRESULT, 'Exchange',
              ( ['in'], c_int, 'OldIndex' ),
              ( ['in'], c_int, 'NewIndex' )),
    COMMETHOD([dispid(210), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(0), 'defaultcollelem', 'propget'], HRESULT, 'Items',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(IOSDItem)), 'Value' )),
]
################################################################
## code template for IOSDItems implementation
##class IOSDItems_Impl(object):
##    @property
##    def Count(self):
##        '-no docstring-'
##        #return Value
##
##    def AddNew(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Items(self, Index):
##        '-no docstring-'
##        #return Value
##
##    def Clone(self):
##        '-no docstring-'
##        #return Value
##
##    def Exchange(self, OldIndex, NewIndex):
##        '-no docstring-'
##        #return 
##
##    def Remove(self, Index):
##        '-no docstring-'
##        #return 
##
##    def Add(self, Item):
##        '-no docstring-'
##        #return 
##
##    def FindItemIndex(self, Key, Value):
##        '-no docstring-'
##        #return Value1
##
##    def AddFromList(self, SourceList):
##        '-no docstring-'
##        #return 
##
##    def FindItem(self, Key, Value):
##        '-no docstring-'
##        #return Value1
##
##    def Clear(self):
##        '-no docstring-'
##        #return 
##

IDVBViewerEventhelper._methods_ = [
]
################################################################
## code template for IDVBViewerEventhelper implementation
##class IDVBViewerEventhelper_Impl(object):

class IFreeDB_HTTP(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The FreeDB object allows you to download informations about a AudioCD from freedb'
    _iid_ = GUID('{9FAB3578-0E3E-4BB5-A2AF-3B9D48794D35}')
    _idlflags_ = ['dual', 'oleautomation']
class IMusicCD(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Used by the freedb reader for returning MusicCDData'
    _iid_ = GUID('{5F2B520D-2CCF-4E55-8138-B231EDD4FF2E}')
    _idlflags_ = ['dual', 'oleautomation']
class IMatch(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{9A669514-2F6C-48F5-8ACE-ECCCFFA46B17}')
    _idlflags_ = ['dual', 'oleautomation']
IFreeDB_HTTP._methods_ = [
    COMMETHOD([dispid(201)], HRESULT, 'ReadCDData',
              ( ['in'], BSTR, 'Drive' )),
    COMMETHOD([dispid(202)], HRESULT, 'VerifyDiscID',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(203)], HRESULT, 'QueryCategories',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(204), 'propget'], HRESULT, 'MatchCount',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(205)], HRESULT, 'DoQuery',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(206)], HRESULT, 'DoRead',
              ( ['in'], c_int, 'MatchIndex' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(207), 'propget'], HRESULT, 'LastError',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(208), 'propget'], HRESULT, 'LastResponseCode',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(209), 'propget'], HRESULT, 'CategoryCount',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(212), 'propget'], HRESULT, 'Category',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(115)], HRESULT, 'SetHostParam',
              ( ['in'], BSTR, 'freedb_host' ),
              ( ['in'], c_int, 'freedb_port' ),
              ( ['in'], BSTR, 'freedb_cgi' )),
    COMMETHOD([dispid(210), 'propget'], HRESULT, 'ReturnDiscInfo',
              ( ['retval', 'out'], POINTER(POINTER(IMusicCD)), 'Value' )),
    COMMETHOD([dispid(211), 'propget'], HRESULT, 'Matchlist',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(IMatch)), 'Value' )),
    COMMETHOD([dispid(213)], HRESULT, 'GetMatchlist',
              ( ['in', 'out'], POINTER(VARIANT), 'Value' ),
              ( ['retval', 'out'], POINTER(c_int), 'Result' )),
]
################################################################
## code template for IFreeDB_HTTP implementation
##class IFreeDB_HTTP_Impl(object):
##    @property
##    def Category(self, Index):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def MatchCount(self):
##        '-no docstring-'
##        #return Value
##
##    def ReadCDData(self, Drive):
##        '-no docstring-'
##        #return 
##
##    @property
##    def Matchlist(self, Index):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def LastResponseCode(self):
##        '-no docstring-'
##        #return Value
##
##    def GetMatchlist(self):
##        '-no docstring-'
##        #return Value, Result
##
##    def SetHostParam(self, freedb_host, freedb_port, freedb_cgi):
##        '-no docstring-'
##        #return 
##
##    def VerifyDiscID(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def CategoryCount(self):
##        '-no docstring-'
##        #return Value
##
##    def DoQuery(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def ReturnDiscInfo(self):
##        '-no docstring-'
##        #return Value
##
##    def DoRead(self, MatchIndex):
##        '-no docstring-'
##        #return Value
##
##    def QueryCategories(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def LastError(self):
##        '-no docstring-'
##        #return Value
##

class IEPGItem2(IEPGItem):
    _case_insensitive_ = True
    _iid_ = GUID('{27F04A6A-13B5-40E0-B37A-46B9838F18EC}')
    _idlflags_ = ['dual', 'oleautomation']
IEPGItem._methods_ = [
    COMMETHOD([dispid(208), 'propget'], HRESULT, 'ServiceID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(211), 'propget'], HRESULT, 'TransportID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(207), 'propget'], HRESULT, 'Charset',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(207), 'propput'], HRESULT, 'Charset',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Content',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(201), 'propput'], HRESULT, 'Content',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(202), 'propget'], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(202), 'propput'], HRESULT, 'Description',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(203), 'propget'], HRESULT, 'Duration',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([dispid(203), 'propput'], HRESULT, 'Duration',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([dispid(204), 'propget'], HRESULT, 'Event',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(204), 'propput'], HRESULT, 'Event',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(205), 'propget'], HRESULT, 'EventID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(205), 'propput'], HRESULT, 'EventID',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(206), 'propget'], HRESULT, 'Time',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([dispid(206), 'propput'], HRESULT, 'Time',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([dispid(209), 'propget'], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(209), 'propput'], HRESULT, 'Title',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(210)], HRESULT, 'SetEPGEventID',
              ( ['in'], c_int, 'ServiceID' ),
              ( ['in'], c_int, 'TransportID' )),
    COMMETHOD([dispid(212), 'propget'], HRESULT, 'EndTime',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([dispid(213), 'propget'], HRESULT, 'EPGEventID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(213), 'propput'], HRESULT, 'EPGEventID',
              ( ['in'], c_int, 'Value' )),
]
################################################################
## code template for IEPGItem implementation
##class IEPGItem_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    EventID = property(_get, _set, doc = _set.__doc__)
##
##    def SetEPGEventID(self, ServiceID, TransportID):
##        '-no docstring-'
##        #return 
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Charset = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Description = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Title = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    EPGEventID = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def TransportID(self):
##        '-no docstring-'
##        #return Value
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Content = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def ServiceID(self):
##        '-no docstring-'
##        #return Value
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Time = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Duration = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def EndTime(self):
##        '-no docstring-'
##        #return Value
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Event = property(_get, _set, doc = _set.__doc__)
##

IEPGItem2._methods_ = [
    COMMETHOD([dispid(301), 'propget'], HRESULT, 'EPGChannelID',
              ( ['retval', 'out'], POINTER(c_longlong), 'Value' )),
    COMMETHOD([dispid(301), 'propput'], HRESULT, 'EPGChannelID',
              ( ['in'], c_longlong, 'Value' )),
]
################################################################
## code template for IEPGItem2 implementation
##class IEPGItem2_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    EPGChannelID = property(_get, _set, doc = _set.__doc__)
##


# values for enumeration 'Tagtype'
tpApe = 0
tpFlac = 1
tpID3v2 = 2
tpID3v1 = 3
tpVorbis = 4
Tagtype = c_int # enum
class IMusicTag(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Describes a music tag of the tagreader'
    _iid_ = GUID('{627BFFFA-13DE-48CA-B226-2609B952B7E3}')
    _idlflags_ = ['dual', 'oleautomation']
IMusicTag._methods_ = [
    COMMETHOD([dispid(201)], HRESULT, 'Clear'),
    COMMETHOD([dispid(203), 'propget'], HRESULT, 'Album',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(203), 'propput'], HRESULT, 'Album',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(204), 'propget'], HRESULT, 'Artist',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(204), 'propput'], HRESULT, 'Artist',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(205), 'propget'], HRESULT, 'Comment',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(205), 'propput'], HRESULT, 'Comment',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(206), 'propget'], HRESULT, 'Duration',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(206), 'propput'], HRESULT, 'Duration',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(207), 'propget'], HRESULT, 'Genre',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(207), 'propput'], HRESULT, 'Genre',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(208), 'propget'], HRESULT, 'TimesPlayed',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(208), 'propput'], HRESULT, 'TimesPlayed',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(209), 'propget'], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(209), 'propput'], HRESULT, 'Title',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(210), 'propget'], HRESULT, 'Track',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(210), 'propput'], HRESULT, 'Track',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(211), 'propget'], HRESULT, 'Year',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(211), 'propput'], HRESULT, 'Year',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(202)], HRESULT, 'Clone',
              ( ['retval', 'out'], POINTER(POINTER(IMusicTag)), 'Value' )),
]
################################################################
## code template for IMusicTag implementation
##class IMusicTag_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Album = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Comment = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Artist = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Track = property(_get, _set, doc = _set.__doc__)
##
##    def Clear(self):
##        '-no docstring-'
##        #return 
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Title = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Duration = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Year = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Genre = property(_get, _set, doc = _set.__doc__)
##
##    def Clone(self):
##        '-no docstring-'
##        #return Value
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    TimesPlayed = property(_get, _set, doc = _set.__doc__)
##

class DVBViewer(CoClass):
    u'DVBViewerServer Objekt'
    _reg_clsid_ = GUID('{D0B1ACAD-1190-4E6D-BD60-41DFA6A28E30}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{017FD4A8-5E00-4DF8-A388-434B8E592CC4}', 1, 1)
class IDVBViewer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The Main object of the DVBViewer COM server'
    _iid_ = GUID('{4CD4A1BF-7E90-4AA3-9C44-B36D78020FE8}')
    _idlflags_ = ['dual', 'oleautomation']
DVBViewer._com_interfaces_ = [IDVBViewer]

class IDVBOSD(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The OSD-Object'
    _iid_ = GUID('{CD78F42E-9DBA-459E-B1B9-8747CCE9318D}')
    _idlflags_ = ['dual', 'oleautomation']
class IWindowManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{142150A3-6184-40C9-9E26-BB5F46AD33DE}')
    _idlflags_ = ['dual', 'oleautomation']
class IEPGManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Responsible for EPG'
    _iid_ = GUID('{E06CE24F-EA08-48C5-B661-EC639E3D26B5}')
    _idlflags_ = ['dual', 'oleautomation']
class IChannelCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'A list of Channelitems optained from the Channelmanager.'
    _iid_ = GUID('{4B39BDAF-65A1-4AA7-8C8F-F0753F9454F9}')
    _idlflags_ = ['dual', 'oleautomation']
class IChannelItem(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Describes a  IChannelItem delivered by the ChannelCollection/manager'
    _iid_ = GUID('{76148341-0A9F-436B-BEDE-50FFFED47A31}')
    _idlflags_ = ['dual', 'oleautomation']
class IUtils(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The Utils-Object offers you some helperfunktion'
    _iid_ = GUID('{47C32284-00FF-4367-8A8C-1830E27FF107}')
    _idlflags_ = ['dual', 'oleautomation']
class ITimerCollection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'Listobject for timeritems.'
    _iid_ = GUID('{54E78EB2-B31A-441A-AECE-5EE201E0CEF8}')
    _idlflags_ = ['dual', 'oleautomation']
class IPlayListManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{64EBF69D-6D41-4D3E-A229-4F11640C7D4B}')
    _idlflags_ = ['dual', 'oleautomation']
class IRecordManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{F614DFEE-06E8-4AC8-B78A-0F5FF4EAA3C3}')
    _idlflags_ = ['dual', 'oleautomation']
class IMainMenuConfig(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{E952AED8-6109-4228-BA5F-8ED28F313988}')
    _idlflags_ = ['dual', 'oleautomation']
class IDVBHardware(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{B5E7BC35-DDBD-412C-8B01-0501131897FB}')
    _idlflags_ = ['dual', 'oleautomation']
class IMessageEvents(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{919951CC-7E8A-4872-ABA8-5946B89FCDE1}')
    _idlflags_ = ['dual', 'oleautomation']
class IDataManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{297E2B6F-79B4-4C9F-91D2-7B5AEBA5D151}')
    _idlflags_ = ['dual', 'oleautomation']
IDVBViewer._methods_ = [
    COMMETHOD([dispid(202), helpstring(u'Everything OSD related is found here.'), 'propget'], HRESULT, 'OSD',
              ( ['retval', 'out'], POINTER(POINTER(IDVBOSD)), 'Value' )),
    COMMETHOD([dispid(205), helpstring(u'Sends a Commandvalue, see external List')], HRESULT, 'SendCommand',
              ( ['in'], c_int, 'CMD' )),
    COMMETHOD([dispid(201), helpstring(u'The ManagerObject for the OSDWindows exposes some methods to manipulate the Windows.'), 'propget'], HRESULT, 'WindowManager',
              ( ['retval', 'out'], POINTER(POINTER(IWindowManager)), 'Value' )),
    COMMETHOD([dispid(206), helpstring(u'Responsible for everything related to EPG'), 'propget'], HRESULT, 'EPGManager',
              ( ['retval', 'out'], POINTER(POINTER(IEPGManager)), 'Value' )),
    COMMETHOD([dispid(207), helpstring(u'The Videotext object'), 'propget'], HRESULT, 'Videotext',
              ( ['retval', 'out'], POINTER(POINTER(IVideotext)), 'Value' )),
    COMMETHOD([dispid(208), helpstring(u'Responsible for Channelmanaging'), 'propget'], HRESULT, 'ChannelManager',
              ( ['retval', 'out'], POINTER(POINTER(IChannelCollection)), 'Value' )),
    COMMETHOD([dispid(209), helpstring(u'Exposes the Current Channel object for convinience'), 'propget'], HRESULT, 'CurrentChannel',
              ( ['retval', 'out'], POINTER(POINTER(IChannelItem)), 'Value' )),
    COMMETHOD([dispid(210), helpstring(u'Utility Object with functions like Webaccess, Freedb and Tagreading'), 'propget'], HRESULT, 'Utils',
              ( ['retval', 'out'], POINTER(POINTER(IUtils)), 'Value' )),
    COMMETHOD([dispid(211), helpstring(u'Manages the Recording timer'), 'propget'], HRESULT, 'TimerManager',
              ( ['retval', 'out'], POINTER(POINTER(ITimerCollection)), 'Value' )),
    COMMETHOD([dispid(203), helpstring(u'writes to the OSD log. for level have a look at options -> OSD General. 0= Lowest priority, 99 Critical')], HRESULT, 'Logwrite',
              ( ['in'], c_int, 'Level' ),
              ( ['in'], BSTR, 'Key' ),
              ( ['in'], BSTR, 'Description' )),
    COMMETHOD([dispid(213), helpstring(u'Delivers a value from the internal Datastate manager see external doc')], HRESULT, 'propGetValue',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(214), helpstring(u'Replaces propertytags with a value from the internal Datastate manager see external doc')], HRESULT, 'propParse',
              ( ['in'], BSTR, 'Valu' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(215), helpstring(u'Set/Add a property in the internal Datastate Manager. Can be used to communicate data with other parts')], HRESULT, 'propSetValue',
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(204), helpstring(u'Gets a Value from the setup.xml of the DVBViewer.')], HRESULT, 'GetSetupValue',
              ( ['in'], BSTR, 'Section' ),
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Default' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(212), helpstring(u'Sets a Value in the setup.xml of the DVBViewer, careful, some values are proctected and can not be changed.')], HRESULT, 'SetSetupValue',
              ( ['in'], BSTR, 'Section' ),
              ( ['in'], BSTR, 'Name' ),
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(216), helpstring(u'Everything about playlists here'), 'propget'], HRESULT, 'PlayListManager',
              ( ['retval', 'out'], POINTER(POINTER(IPlayListManager)), 'Value' )),
    COMMETHOD([dispid(217), helpstring(u'The Number of the current shown channel'), 'propget'], HRESULT, 'CurrentChannelNr',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(217), helpstring(u'The Number of the current shown channel'), 'propput'], HRESULT, 'CurrentChannelNr',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(218), helpstring(u'Set the volume (0..1)'), 'propget'], HRESULT, 'Volume',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([dispid(218), helpstring(u'Set the volume (0..1)'), 'propput'], HRESULT, 'Volume',
              ( ['in'], c_double, 'Value' )),
    COMMETHOD([dispid(219), helpstring(u'The channelnumer of the last shown channel, if any otherwise -1'), 'propget'], HRESULT, 'LastChannel',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(220), helpstring(u'Plays a mediafile. Input file with full path')], HRESULT, 'PlayFile',
              ( ['in'], BSTR, 'Filename' )),
    COMMETHOD([dispid(221), helpstring(u'Clears all bookmarks for the file')], HRESULT, 'BookmarksClear',
              ( ['in'], BSTR, 'Filename' )),
    COMMETHOD([dispid(222), helpstring(u'Sets a bookmark for the file. Position is measured in seconds of playtime')], HRESULT, 'BookmarkAdd',
              ( ['in'], BSTR, 'Filename' ),
              ( ['in'], c_double, 'Position' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Result' )),
    COMMETHOD([dispid(227), helpstring(u'Gets a list of bookmarks, see external doc for datadefinition of this list.')], HRESULT, 'BookmarksGet',
              ( ['in'], BSTR, 'Filename' ),
              ( ['retval', 'out'], POINTER(POINTER(IOSDItems)), 'Result' )),
    COMMETHOD([dispid(223), helpstring(u'Manages the recordings from the database.'), 'propget'], HRESULT, 'RecordManager',
              ( ['retval', 'out'], POINTER(POINTER(IRecordManager)), 'Value' )),
    COMMETHOD([dispid(224), 'propget'], HRESULT, 'MainMenuConfig',
              ( ['retval', 'out'], POINTER(POINTER(IMainMenuConfig)), 'Value' )),
    COMMETHOD([dispid(225), 'propget'], HRESULT, 'FavoritesManager',
              ( ['retval', 'out'], POINTER(POINTER(IFavoritesManager)), 'Value' )),
    COMMETHOD([dispid(226)], HRESULT, 'IsTimeshift',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(228)], HRESULT, 'isDVD',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(229)], HRESULT, 'isMediaplayback',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(230)], HRESULT, 'Audiomode',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(231)], HRESULT, 'GetRDS',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(232)], HRESULT, 'ApplyConfig'),
    COMMETHOD([dispid(234), 'propget'], HRESULT, 'PropCount',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(233), 'propget'], HRESULT, 'propName',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(235), 'propget'], HRESULT, 'propValue',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(236)], HRESULT, 'propGetAll',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(237)], HRESULT, 'Stop'),
    COMMETHOD([dispid(238), 'propget'], HRESULT, 'Events',
              ( ['retval', 'out'], POINTER(POINTER(IDVBViewerEventhelper)), 'Value' )),
    COMMETHOD([dispid(239), 'propget'], HRESULT, 'Handle',
              ( ['retval', 'out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([dispid(240)], HRESULT, 'Quit'),
    COMMETHOD([dispid(241)], HRESULT, 'Mute',
              ( ['in'], VARIANT_BOOL, 'Silent' )),
    COMMETHOD([dispid(242), 'propget'], HRESULT, 'DVBHardware',
              ( ['retval', 'out'], POINTER(POINTER(IDVBHardware)), 'Value' )),
    COMMETHOD([dispid(243), 'propget'], HRESULT, 'MsgEvents',
              ( ['retval', 'out'], POINTER(POINTER(IMessageEvents)), 'Value' )),
    COMMETHOD([dispid(244), 'propget'], HRESULT, 'CurrentLanguage',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(245)], HRESULT, 'GetTranslation',
              ( ['in'], BSTR, 'Original' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(246)], HRESULT, 'LoadAddLanguage',
              ( ['in'], BSTR, 'Filename' )),
    COMMETHOD([dispid(247)], HRESULT, 'SendInput',
              ( ['in'], BSTR, 'Source' ),
              ( ['in'], BSTR, 'Event' )),
    COMMETHOD([dispid(248), 'propget'], HRESULT, 'DataManager',
              ( ['retval', 'out'], POINTER(POINTER(IDataManager)), 'Value' )),
    COMMETHOD([dispid(249)], HRESULT, 'Debug',
              ( ['in'], BSTR, 'Param1' )),
]
################################################################
## code template for IDVBViewer implementation
##class IDVBViewer_Impl(object):
##    def Quit(self):
##        '-no docstring-'
##        #return 
##
##    def isDVD(self):
##        '-no docstring-'
##        #return Value
##
##    def isMediaplayback(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def WindowManager(self):
##        u'The ManagerObject for the OSDWindows exposes some methods to manipulate the Windows.'
##        #return Value
##
##    def SendInput(self, Source, Event):
##        '-no docstring-'
##        #return 
##
##    def propParse(self, Valu):
##        u'Replaces propertytags with a value from the internal Datastate manager see external doc'
##        #return Value
##
##    @property
##    def EPGManager(self):
##        u'Responsible for everything related to EPG'
##        #return Value
##
##    @property
##    def RecordManager(self):
##        u'Manages the recordings from the database.'
##        #return Value
##
##    def BookmarkAdd(self, Filename, Position):
##        u'Sets a bookmark for the file. Position is measured in seconds of playtime'
##        #return Result
##
##    @property
##    def Events(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def PlayListManager(self):
##        u'Everything about playlists here'
##        #return Value
##
##    @property
##    def Handle(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Videotext(self):
##        u'The Videotext object'
##        #return Value
##
##    def SetSetupValue(self, Section, Name, Value):
##        u'Sets a Value in the setup.xml of the DVBViewer, careful, some values are proctected and can not be changed.'
##        #return 
##
##    def Stop(self):
##        '-no docstring-'
##        #return 
##
##    def GetRDS(self):
##        '-no docstring-'
##        #return Value
##
##    def _get(self):
##        u'Set the volume (0..1)'
##        #return Value
##    def _set(self, Value):
##        u'Set the volume (0..1)'
##    Volume = property(_get, _set, doc = _set.__doc__)
##
##    def IsTimeshift(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def propValue(self, Index):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def DataManager(self):
##        '-no docstring-'
##        #return Value
##
##    def propSetValue(self, Name, Value):
##        u'Set/Add a property in the internal Datastate Manager. Can be used to communicate data with other parts'
##        #return 
##
##    @property
##    def OSD(self):
##        u'Everything OSD related is found here.'
##        #return Value
##
##    @property
##    def MsgEvents(self):
##        '-no docstring-'
##        #return Value
##
##    def Audiomode(self):
##        '-no docstring-'
##        #return Value
##
##    def BookmarksClear(self, Filename):
##        u'Clears all bookmarks for the file'
##        #return 
##
##    def BookmarksGet(self, Filename):
##        u'Gets a list of bookmarks, see external doc for datadefinition of this list.'
##        #return Result
##
##    def Logwrite(self, Level, Key, Description):
##        u'writes to the OSD log. for level have a look at options -> OSD General. 0= Lowest priority, 99 Critical'
##        #return 
##
##    def propGetAll(self):
##        '-no docstring-'
##        #return Value
##
##    def LoadAddLanguage(self, Filename):
##        '-no docstring-'
##        #return 
##
##    @property
##    def TimerManager(self):
##        u'Manages the Recording timer'
##        #return Value
##
##    def ApplyConfig(self):
##        '-no docstring-'
##        #return 
##
##    @property
##    def ChannelManager(self):
##        u'Responsible for Channelmanaging'
##        #return Value
##
##    @property
##    def PropCount(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def CurrentChannel(self):
##        u'Exposes the Current Channel object for convinience'
##        #return Value
##
##    def Debug(self, Param1):
##        '-no docstring-'
##        #return 
##
##    def propGetValue(self, Name):
##        u'Delivers a value from the internal Datastate manager see external doc'
##        #return Value
##
##    def SendCommand(self, CMD):
##        u'Sends a Commandvalue, see external List'
##        #return 
##
##    def GetTranslation(self, Original):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def CurrentLanguage(self):
##        '-no docstring-'
##        #return Value
##
##    def Mute(self, Silent):
##        '-no docstring-'
##        #return 
##
##    @property
##    def Utils(self):
##        u'Utility Object with functions like Webaccess, Freedb and Tagreading'
##        #return Value
##
##    def _get(self):
##        u'The Number of the current shown channel'
##        #return Value
##    def _set(self, Value):
##        u'The Number of the current shown channel'
##    CurrentChannelNr = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def LastChannel(self):
##        u'The channelnumer of the last shown channel, if any otherwise -1'
##        #return Value
##
##    def GetSetupValue(self, Section, Name, Default):
##        u'Gets a Value from the setup.xml of the DVBViewer.'
##        #return Value
##
##    def PlayFile(self, Filename):
##        u'Plays a mediafile. Input file with full path'
##        #return 
##
##    @property
##    def propName(self, Index):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def DVBHardware(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def MainMenuConfig(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def FavoritesManager(self):
##        '-no docstring-'
##        #return Value
##

ITimerCollection._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(0), 'defaultcollelem', 'propget'], HRESULT, 'Item',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(ITimerItem)), 'Value' )),
    COMMETHOD([dispid(202)], HRESULT, 'Add',
              ( ['in'], POINTER(ITimerItem), 'Value' )),
    COMMETHOD([dispid(203)], HRESULT, 'Remove',
              ( ['in'], c_int, 'Index' )),
    COMMETHOD([dispid(204), 'propget'], HRESULT, 'Recording',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(205)], HRESULT, 'StopRecording',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(206)], HRESULT, 'InstantRecord',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(207), 'propget'], HRESULT, 'NextRecordingTime',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([dispid(208)], HRESULT, 'IsRecording',
              ( ['in'], POINTER(ITuner), 'Value' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Result' )),
    COMMETHOD([dispid(209)], HRESULT, 'isTimerAt',
              ( ['in'], c_double, 'atTime' ),
              ( ['retval', 'out'], POINTER(c_int), 'TimerID' )),
    COMMETHOD([dispid(210)], HRESULT, 'AddItem',
              ( ['in'], BSTR, 'ChannelID' ),
              ( ['in'], c_double, 'Date' ),
              ( ['in'], c_double, 'StartTime' ),
              ( ['in'], c_double, 'EndTime' ),
              ( ['in'], BSTR, 'Description' ),
              ( ['in'], VARIANT_BOOL, 'DisableAV' ),
              ( ['in'], VARIANT_BOOL, 'Enabled' ),
              ( ['in'], c_int, 'RecAction' ),
              ( ['in'], c_int, 'AfterRec' ),
              ( ['in'], BSTR, 'Days' ),
              ( ['retval', 'out'], POINTER(POINTER(ITimerItem)), 'Result' )),
    COMMETHOD([dispid(211)], HRESULT, 'NewItem',
              ( ['retval', 'out'], POINTER(POINTER(ITimerItem)), 'Result' )),
    COMMETHOD([dispid(-4), 'propget'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Value' )),
    COMMETHOD([dispid(212)], HRESULT, 'Overlap',
              ( ['in'], POINTER(ITimerItem), 'Timer' ),
              ( ['retval', 'out'], POINTER(POINTER(ITimerItem)), 'Value' )),
    COMMETHOD([dispid(213)], HRESULT, 'GetTimerList',
              ( ['out'], POINTER(VARIANT), 'List' ),
              ( ['retval', 'out'], POINTER(c_int), 'Result' )),
    COMMETHOD([dispid(214)], HRESULT, 'AddRecordingFolder',
              ( ['in'], BSTR, 'Folder' ),
              ( ['retval', 'out'], POINTER(c_int), 'Result' )),
    COMMETHOD([dispid(215)], HRESULT, 'GetRecordingFolders',
              ( ['out'], POINTER(VARIANT), 'List' ),
              ( ['retval', 'out'], POINTER(c_int), 'Result' )),
]
################################################################
## code template for ITimerCollection implementation
##class ITimerCollection_Impl(object):
##    @property
##    def Count(self):
##        '-no docstring-'
##        #return Value
##
##    def AddRecordingFolder(self, Folder):
##        '-no docstring-'
##        #return Result
##
##    @property
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Value
##
##    def InstantRecord(self):
##        '-no docstring-'
##        #return Value
##
##    def IsRecording(self, Value):
##        '-no docstring-'
##        #return Result
##
##    def AddItem(self, ChannelID, Date, StartTime, EndTime, Description, DisableAV, Enabled, RecAction, AfterRec, Days):
##        '-no docstring-'
##        #return Result
##
##    def StopRecording(self, Value):
##        '-no docstring-'
##        #return 
##
##    def Remove(self, Index):
##        '-no docstring-'
##        #return 
##
##    def GetTimerList(self):
##        '-no docstring-'
##        #return List, Result
##
##    @property
##    def Recording(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Item(self, Index):
##        '-no docstring-'
##        #return Value
##
##    def Add(self, Value):
##        '-no docstring-'
##        #return 
##
##    def GetRecordingFolders(self):
##        '-no docstring-'
##        #return List, Result
##
##    def Overlap(self, Timer):
##        '-no docstring-'
##        #return Value
##
##    def NewItem(self):
##        '-no docstring-'
##        #return Result
##
##    @property
##    def NextRecordingTime(self):
##        '-no docstring-'
##        #return Value
##
##    def isTimerAt(self, atTime):
##        '-no docstring-'
##        #return TimerID
##

IPlaylistItem._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Typ',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(201), 'propput'], HRESULT, 'Typ',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(202), 'propget'], HRESULT, 'Played',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(202), 'propput'], HRESULT, 'Played',
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD([dispid(203), 'propget'], HRESULT, 'Filename',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(203), 'propput'], HRESULT, 'Filename',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(204), 'propget'], HRESULT, 'Duration',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(204), 'propput'], HRESULT, 'Duration',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(205), 'propget'], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(205), 'propput'], HRESULT, 'Description',
              ( ['in'], BSTR, 'Value' )),
]
################################################################
## code template for IPlaylistItem implementation
##class IPlaylistItem_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Duration = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Filename = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Typ = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Description = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Played = property(_get, _set, doc = _set.__doc__)
##

IFavoritesItem._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Group',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(202), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(203), 'propget'], HRESULT, 'ChannelID',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(204), 'propget'], HRESULT, 'Nr',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
]
################################################################
## code template for IFavoritesItem implementation
##class IFavoritesItem_Impl(object):
##    @property
##    def Nr(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def ChannelID(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Group(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Name(self):
##        '-no docstring-'
##        #return Value
##

IDVBHardware._methods_ = [
    COMMETHOD([dispid(201)], HRESULT, 'SignalErrorRate',
              ( ['in'], c_int, 'Card' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([dispid(202)], HRESULT, 'SignalQuality',
              ( ['in'], c_int, 'Card' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([dispid(203)], HRESULT, 'SignalStrength',
              ( ['in'], c_int, 'Card' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([dispid(204)], HRESULT, 'HardwareName',
              ( ['in'], c_int, 'Card' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(205), 'propget'], HRESULT, 'CardCount',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
]
################################################################
## code template for IDVBHardware implementation
##class IDVBHardware_Impl(object):
##    def SignalStrength(self, Card):
##        '-no docstring-'
##        #return Value
##
##    def SignalQuality(self, Card):
##        '-no docstring-'
##        #return Value
##
##    def HardwareName(self, Card):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def CardCount(self):
##        '-no docstring-'
##        #return Value
##
##    def SignalErrorRate(self, Card):
##        '-no docstring-'
##        #return Value
##

class MessageEvents(CoClass):
    _reg_clsid_ = GUID('{447C6500-03DE-42E0-9CF5-6D5B5BEF7324}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{017FD4A8-5E00-4DF8-A388-434B8E592CC4}', 1, 1)
class IMessageEv(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{9891B0B0-086D-4A6D-B1F5-2287BF06C2C4}')
    _idlflags_ = []
    _methods_ = []
MessageEvents._com_interfaces_ = [IMessageEvents]
MessageEvents._outgoing_interfaces_ = [IMessageEv]

class IOSDMessage(IOSDItem):
    _case_insensitive_ = True
    _iid_ = GUID('{D0D14E3A-EE5D-4109-804F-98AF39B2A44A}')
    _idlflags_ = ['dual', 'oleautomation']
IOSDItem._methods_ = [
    COMMETHOD([dispid(0), 'defaultcollelem', 'propget'], HRESULT, 'Values',
              ( ['in'], VARIANT, 'Index' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([dispid(0), 'defaultcollelem', 'propput'], HRESULT, 'Values',
              ( ['in'], VARIANT, 'Index' ),
              ( ['in'], VARIANT, 'Value' )),
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Keys',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(202), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(203)], HRESULT, 'Clear'),
    COMMETHOD([dispid(204)], HRESULT, 'Contains',
              ( ['in'], BSTR, 'Key' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(205)], HRESULT, 'CopyForm',
              ( ['in'], POINTER(IOSDItem), 'SourceItem' )),
    COMMETHOD([dispid(206)], HRESULT, 'Get',
              ( ['in'], BSTR, 'Key' ),
              ( ['in'], VARIANT, 'Default' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'Value' )),
]
################################################################
## code template for IOSDItem implementation
##class IOSDItem_Impl(object):
##    @property
##    def Count(self):
##        '-no docstring-'
##        #return Value
##
##    def Get(self, Key, Default):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Keys(self, Index):
##        '-no docstring-'
##        #return Value
##
##    def Clear(self):
##        '-no docstring-'
##        #return 
##
##    def Contains(self, Key):
##        '-no docstring-'
##        #return Value
##
##    def _get(self, Index):
##        '-no docstring-'
##        #return Value
##    def _set(self, Index, Value):
##        '-no docstring-'
##    Values = property(_get, _set, doc = _set.__doc__)
##
##    def CopyForm(self, SourceItem):
##        '-no docstring-'
##        #return 
##

IOSDMessage._methods_ = [
    COMMETHOD([dispid(215)], HRESULT, 'Send'),
    COMMETHOD([dispid(209), 'propget'], HRESULT, 'TargetWindowId',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(209), 'propput'], HRESULT, 'TargetWindowId',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(210), 'propget'], HRESULT, 'TargetControlId',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(210), 'propput'], HRESULT, 'TargetControlId',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(211), 'propget'], HRESULT, 'Subject',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(211), 'propput'], HRESULT, 'Subject',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(213), 'propget'], HRESULT, 'SenderControlID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(213), 'propput'], HRESULT, 'SenderControlID',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(207), 'propget'], HRESULT, 'Messages',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(207), 'propput'], HRESULT, 'Messages',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(208), 'propget'], HRESULT, 'List',
              ( ['retval', 'out'], POINTER(POINTER(IOSDItems)), 'Value' )),
    COMMETHOD([dispid(301)], HRESULT, 'SendToSystem'),
]
################################################################
## code template for IOSDMessage implementation
##class IOSDMessage_Impl(object):
##    @property
##    def List(self):
##        '-no docstring-'
##        #return Value
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    SenderControlID = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Messages = property(_get, _set, doc = _set.__doc__)
##
##    def Send(self):
##        '-no docstring-'
##        #return 
##
##    def SendToSystem(self):
##        '-no docstring-'
##        #return 
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    TargetWindowId = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    TargetControlId = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Subject = property(_get, _set, doc = _set.__doc__)
##

class Library(object):
    u'DVBViewer COM Bibliothek'
    name = u'DVBViewerServer'
    _reg_typelib_ = ('{017FD4A8-5E00-4DF8-A388-434B8E592CC4}', 1, 1)

IMatch._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'FreeDB_DiscID',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(202), 'propget'], HRESULT, 'Category',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(203), 'propget'], HRESULT, 'DiscTitle',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
]
################################################################
## code template for IMatch implementation
##class IMatch_Impl(object):
##    @property
##    def Category(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def FreeDB_DiscID(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def DiscTitle(self):
##        '-no docstring-'
##        #return Value
##

class IDVBViewer2(IDVBViewer):
    _case_insensitive_ = True
    _iid_ = GUID('{E3D9301C-266A-4C1A-A35B-E0CD06AD69C1}')
    _idlflags_ = ['dual', 'oleautomation']
class IEPGManager2(IEPGManager):
    _case_insensitive_ = True
    _iid_ = GUID('{524D1181-FACB-4F5D-A5AF-F68B188AFEE7}')
    _idlflags_ = ['dual', 'oleautomation']
class IChannelCollection2(IChannelCollection):
    _case_insensitive_ = True
    _iid_ = GUID('{EE3F03D3-3471-4B8D-86D7-A321E36956B0}')
    _idlflags_ = ['dual', 'oleautomation']
IDVBViewer2._methods_ = [
    COMMETHOD([dispid(302), 'propget'], HRESULT, 'EPGManager2',
              ( ['retval', 'out'], POINTER(POINTER(IEPGManager2)), 'Value' )),
    COMMETHOD([dispid(301), 'propget'], HRESULT, 'ChannelCollection',
              ( ['retval', 'out'], POINTER(POINTER(IChannelCollection2)), 'Value' )),
    COMMETHOD([dispid(303), helpstring(u'Async = Postmessage else Sendmessage')], HRESULT, 'executeAction',
              ( ['in'], c_int, 'Action' ),
              ( ['in'], VARIANT_BOOL, 'async' )),
]
################################################################
## code template for IDVBViewer2 implementation
##class IDVBViewer2_Impl(object):
##    @property
##    def ChannelCollection(self):
##        '-no docstring-'
##        #return Value
##
##    def executeAction(self, Action, async):
##        u'Async = Postmessage else Sendmessage'
##        #return 
##
##    @property
##    def EPGManager2(self):
##        '-no docstring-'
##        #return Value
##


# values for enumeration 'TExeType'
texScript = 0
texApp = 1
texCMD = 2
texFunct = 3
texHyperlink = 4
TExeType = c_int # enum
IChannelItem._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Root',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(202), 'propget'], HRESULT, 'Name',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(203), 'propget'], HRESULT, 'Category',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(204), 'propget'], HRESULT, 'Encrypted',
              ( ['retval', 'out'], POINTER(c_ubyte), 'Value' )),
    COMMETHOD([dispid(205), 'propget'], HRESULT, 'Tuner',
              ( ['retval', 'out'], POINTER(POINTER(ITuner)), 'Value' )),
    COMMETHOD([dispid(206), 'propget'], HRESULT, 'ChannelID',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(207), 'propget'], HRESULT, 'EPGChannelID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
]
################################################################
## code template for IChannelItem implementation
##class IChannelItem_Impl(object):
##    @property
##    def Category(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Name(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Encrypted(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def ChannelID(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def EPGChannelID(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Tuner(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Root(self):
##        '-no docstring-'
##        #return Value
##

class IEPGAddBuffer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{8BD0691B-7A1A-4F21-AAD0-44396FFFA821}')
    _idlflags_ = ['dual', 'oleautomation']
IEPGManager._methods_ = [
    COMMETHOD([dispid(1610743808), 'propget'], HRESULT, 'EPGNow',
              ( ['retval', 'out'], POINTER(POINTER(IEPGItem)), 'Value' )),
    COMMETHOD([dispid(202), 'propget'], HRESULT, 'EPGNext',
              ( ['retval', 'out'], POINTER(POINTER(IEPGItem)), 'Value' )),
    COMMETHOD([dispid(204)], HRESULT, 'Get',
              ( ['in'], c_int, 'SID' ),
              ( ['in'], c_int, 'TID' ),
              ( ['in'], c_double, 'StartTime' ),
              ( ['in'], c_double, 'EndTime' ),
              ( ['retval', 'out'], POINTER(POINTER(IEPGCollection)), 'Result' )),
    COMMETHOD([dispid(203)], HRESULT, 'NewEPGItem',
              ( ['retval', 'out'], POINTER(POINTER(IEPGItem)), 'Result' )),
    COMMETHOD([dispid(205)], HRESULT, 'Clear'),
    COMMETHOD([dispid(206)], HRESULT, 'AddItem',
              ( ['in'], POINTER(IEPGItem), 'Entry' )),
    COMMETHOD([dispid(207)], HRESULT, 'Commit'),
    COMMETHOD([dispid(208)], HRESULT, 'GetAsArray',
              ( ['in'], c_int, 'ChannelID' ),
              ( ['in'], c_double, 'StartTime' ),
              ( ['in'], c_double, 'EndTime' ),
              ( ['out'], POINTER(VARIANT), 'List' ),
              ( ['retval', 'out'], POINTER(c_int), 'Result' )),
    COMMETHOD([dispid(209)], HRESULT, 'HasEPG',
              ( ['in'], c_int, 'EPGChannelID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Result' )),
    COMMETHOD([dispid(210)], HRESULT, 'SplitEPGChannelID',
              ( ['in'], c_int, 'EPGChannelID' ),
              ( ['out'], POINTER(c_int), 'SID' ),
              ( ['out'], POINTER(c_int), 'TID' )),
    COMMETHOD([dispid(201)], HRESULT, 'AddEPG',
              ( ['retval', 'out'], POINTER(POINTER(IEPGAddBuffer)), 'Value' )),
]
################################################################
## code template for IEPGManager implementation
##class IEPGManager_Impl(object):
##    def NewEPGItem(self):
##        '-no docstring-'
##        #return Result
##
##    def HasEPG(self, EPGChannelID):
##        '-no docstring-'
##        #return Result
##
##    def Get(self, SID, TID, StartTime, EndTime):
##        '-no docstring-'
##        #return Result
##
##    def Clear(self):
##        '-no docstring-'
##        #return 
##
##    def AddItem(self, Entry):
##        '-no docstring-'
##        #return 
##
##    def GetAsArray(self, ChannelID, StartTime, EndTime):
##        '-no docstring-'
##        #return List, Result
##
##    def SplitEPGChannelID(self, EPGChannelID):
##        '-no docstring-'
##        #return SID, TID
##
##    @property
##    def EPGNext(self):
##        '-no docstring-'
##        #return Value
##
##    def AddEPG(self):
##        '-no docstring-'
##        #return Value
##
##    def Commit(self):
##        '-no docstring-'
##        #return 
##
##    @property
##    def EPGNow(self):
##        '-no docstring-'
##        #return Value
##

IEPGManager2._methods_ = [
    COMMETHOD([dispid(301)], HRESULT, 'ImportEPG',
              ( ['in'], BSTR, 'XMLData' )),
    COMMETHOD([dispid(302)], HRESULT, 'GetAsArray2',
              ( ['in'], c_longlong, 'ChannelID' ),
              ( ['in'], c_double, 'StartTime' ),
              ( ['in'], c_double, 'EndTime' ),
              ( ['out'], POINTER(VARIANT), 'List' ),
              ( ['retval', 'out'], POINTER(c_int), 'Result' )),
    COMMETHOD([dispid(303)], HRESULT, 'HasEPG2',
              ( ['in'], c_longlong, 'EPGChannelID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Result' )),
    COMMETHOD([dispid(304), helpstring(u'Tunertype is the tunertype of the tuner +1!')], HRESULT, 'SplitEPGChannelID2',
              ( ['in'], c_longlong, 'EPGChannelID' ),
              ( ['out'], POINTER(c_int), 'SID' ),
              ( ['out'], POINTER(c_int), 'TID' ),
              ( ['out'], POINTER(c_int), 'ONID' ),
              ( ['out'], POINTER(c_int), 'TunerType' )),
    COMMETHOD([dispid(305)], HRESULT, 'Search',
              ( ['in'], BSTR, 'Searchphrase' ),
              ( ['in'], VARIANT_BOOL, 'inTitle' ),
              ( ['in'], VARIANT_BOOL, 'inEvent' ),
              ( ['in'], VARIANT_BOOL, 'inDescription' ),
              ( ['in'], VARIANT_BOOL, 'IgnoreCase' ),
              ( ['in'], VARIANT_BOOL, 'isRegEx' ),
              ( ['in'], c_double, 'Startdate' ),
              ( ['in'], c_double, 'EndDate' ),
              ( ['in'], c_double, 'StartTime' ),
              ( ['in'], c_double, 'EndTime' ),
              ( ['in'], c_int, 'DurationMin' ),
              ( ['in'], c_int, 'DurationMax' ),
              ( ['in'], c_int, 'Genre' ),
              ( ['in'], VARIANT, 'Channels' ),
              ( ['in'], c_int, 'MaxResults' ),
              ( ['out'], POINTER(VARIANT), 'EPGList' ),
              ( ['retval', 'out'], POINTER(c_int), 'Result' )),
]
################################################################
## code template for IEPGManager2 implementation
##class IEPGManager2_Impl(object):
##    def GetAsArray2(self, ChannelID, StartTime, EndTime):
##        '-no docstring-'
##        #return List, Result
##
##    def Search(self, Searchphrase, inTitle, inEvent, inDescription, IgnoreCase, isRegEx, Startdate, EndDate, StartTime, EndTime, DurationMin, DurationMax, Genre, Channels, MaxResults):
##        '-no docstring-'
##        #return EPGList, Result
##
##    def HasEPG2(self, EPGChannelID):
##        '-no docstring-'
##        #return Result
##
##    def SplitEPGChannelID2(self, EPGChannelID):
##        u'Tunertype is the tunertype of the tuner +1!'
##        #return SID, TID, ONID, TunerType
##
##    def ImportEPG(self, XMLData):
##        '-no docstring-'
##        #return 
##

class ITagreader(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'The Tagreaderobject offers you reading and writing of various tag formats'
    _iid_ = GUID('{2B361414-EDCF-48AD-BABB-5104348432ED}')
    _idlflags_ = ['dual', 'oleautomation']
IUtils._methods_ = [
    COMMETHOD([dispid(201), helpstring(u'The function filters all html tags')], HRESULT, 'HTML2Text',
              ( ['in'], BSTR, 'inText' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(202), helpstring(u'the function disconnect a dial-up Connection')], HRESULT, 'NetDisconnect'),
    COMMETHOD([dispid(203), helpstring(u'the function connects a dial-up Connection')], HRESULT, 'NetConnect',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(204), helpstring(u'the function download a file from a URL')], HRESULT, 'DownloadFileFromURL',
              ( ['in'], BSTR, 'SourceURL' ),
              ( ['in'], BSTR, 'Destination' ),
              ( ['in'], BSTR, 'Username' ),
              ( ['in'], BSTR, 'Password' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(205), helpstring(u'the function downloads a htmlfile as a string')], HRESULT, 'GetHTML',
              ( ['in'], BSTR, 'AUrl' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(206), helpstring(u'Helperfunction to break up a URL')], HRESULT, 'ParseURL',
              ( ['in'], BSTR, 'Url' ),
              ( ['in', 'out'], POINTER(BSTR), 'Hostname' ),
              ( ['in', 'out'], POINTER(BSTR), 'Filename' )),
    COMMETHOD([dispid(207), helpstring(u'Helperfunction to retrieve a unique CD-Serial as used by the Windowsmediaplayer')], HRESULT, 'GetCDSerialNo',
              ( ['in'], BSTR, 'Drive' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(208), helpstring(u'The Tagreaderobject offers you reading and writing of various tag formats'), 'propget'], HRESULT, 'Tagreader',
              ( ['retval', 'out'], POINTER(POINTER(ITagreader)), 'Value' )),
    COMMETHOD([dispid(209), helpstring(u'The FreeDB object allows you to download informations about a AudioCD from freedb'), 'propget'], HRESULT, 'FreeDB',
              ( ['retval', 'out'], POINTER(POINTER(IFreeDB_HTTP)), 'Value' )),
]
################################################################
## code template for IUtils implementation
##class IUtils_Impl(object):
##    def ParseURL(self, Url):
##        u'Helperfunction to break up a URL'
##        #return Hostname, Filename
##
##    def GetHTML(self, AUrl):
##        u'the function downloads a htmlfile as a string'
##        #return Value
##
##    def NetDisconnect(self):
##        u'the function disconnect a dial-up Connection'
##        #return 
##
##    @property
##    def Tagreader(self):
##        u'The Tagreaderobject offers you reading and writing of various tag formats'
##        #return Value
##
##    def DownloadFileFromURL(self, SourceURL, Destination, Username, Password):
##        u'the function download a file from a URL'
##        #return Value
##
##    def NetConnect(self):
##        u'the function connects a dial-up Connection'
##        #return Value
##
##    def GetCDSerialNo(self, Drive):
##        u'Helperfunction to retrieve a unique CD-Serial as used by the Windowsmediaplayer'
##        #return Value
##
##    def HTML2Text(self, inText):
##        u'The function filters all html tags'
##        #return Value
##
##    @property
##    def FreeDB(self):
##        u'The FreeDB object allows you to download informations about a AudioCD from freedb'
##        #return Value
##


# values for enumeration 'TRendererTyp'
rtUnknown = 0
rtVideoAudioDVD = 1
rtDVB = 2
rtMPG2TS = 3
TRendererTyp = c_int # enum

# values for enumeration 'TPlaystates'
cpsStop = 0
cpsPause = 1
cpsPlay = 2
TPlaystates = c_int # enum
IDVBViewerEvents._disp_methods_ = [
    DISPMETHOD([dispid(201)], HRESULT, 'OnChannelChange',
               ( ['in'], c_int, 'ChannelNr' )),
    DISPMETHOD([dispid(202)], HRESULT, 'onRDS',
               ( ['in'], BSTR, 'RDS' )),
    DISPMETHOD([dispid(203)], HRESULT, 'onOSDWindow',
               ( ['in'], c_int, 'WindowID' )),
    DISPMETHOD([dispid(204)], HRESULT, 'onDVBVClose'),
    DISPMETHOD([dispid(205)], HRESULT, 'onStartRecord',
               ( ['in'], c_int, 'ID' )),
    DISPMETHOD([dispid(206)], HRESULT, 'onEndRecord'),
    DISPMETHOD([dispid(207)], HRESULT, 'onPlaybackstart'),
    DISPMETHOD([dispid(208)], HRESULT, 'OnPlaybackEnd'),
    DISPMETHOD([dispid(209)], HRESULT, 'OnPlaystatechange',
               ( ['in'], TRendererTyp, 'RendererType' ),
               ( ['in'], TPlaystates, 'State' )),
    DISPMETHOD([dispid(210)], HRESULT, 'onAction',
               ( ['in'], c_int, 'ActionID' )),
    DISPMETHOD([dispid(211)], HRESULT, 'onPlaylist',
               ( ['in'], BSTR, 'Filename' )),
    DISPMETHOD([dispid(212)], HRESULT, 'onAddRecord',
               ( ['in'], c_int, 'ID' )),
    DISPMETHOD([dispid(213)], HRESULT, 'onControlChange',
               ( ['in'], c_int, 'WindowID' ),
               ( ['in'], c_int, 'ControlID' )),
    DISPMETHOD([dispid(214)], HRESULT, 'onSelectedItemChange'),
]

# values for enumeration 'TAlarmMode'
pamOnce = 0
pamYearly = 1
pamMonthly = 2
pamWeekly = 3
pamDaily = 4
pamHourly = 5
pamMinutely = 6
TAlarmMode = c_int # enum
IMessageEv._disp_methods_ = [
    DISPMETHOD([dispid(201)], HRESULT, 'onMessage',
               ( ['in'], POINTER(IOSDMessage), 'Value' )),
]
IMessageEvents._methods_ = [
]
################################################################
## code template for IMessageEvents implementation
##class IMessageEvents_Impl(object):

ITeletextEvents._disp_methods_ = [
    DISPMETHOD([dispid(201)], HRESULT, 'onDataArrive',
               ( ['in'], c_int, 'PageNr' ),
               ( ['in'], c_int, 'SubPageNr' )),
]
IMainMenuConfig._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Active',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(201), 'propput'], HRESULT, 'Active',
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD([dispid(202)], HRESULT, 'Refresh'),
    COMMETHOD([dispid(203), 'propget'], HRESULT, 'BackColor',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(203), 'propput'], HRESULT, 'BackColor',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(204), 'propget'], HRESULT, 'DisabledFontColor',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(204), 'propput'], HRESULT, 'DisabledFontColor',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(205), 'propget'], HRESULT, 'FontColor',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(205), 'propput'], HRESULT, 'FontColor',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(206), 'propget'], HRESULT, 'IconBackColor',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(206), 'propput'], HRESULT, 'IconBackColor',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(207), 'propget'], HRESULT, 'SelectedBkColor',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(207), 'propput'], HRESULT, 'SelectedBkColor',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(208), 'propget'], HRESULT, 'SeparatorColor',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(208), 'propput'], HRESULT, 'SeparatorColor',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(209), 'propget'], HRESULT, 'SelectedFontColor',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(209), 'propput'], HRESULT, 'SelectedFontColor',
              ( ['in'], c_int, 'Value' )),
]
################################################################
## code template for IMainMenuConfig implementation
##class IMainMenuConfig_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    BackColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    SeparatorColor = property(_get, _set, doc = _set.__doc__)
##
##    def Refresh(self):
##        '-no docstring-'
##        #return 
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    SelectedFontColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    SelectedBkColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    IconBackColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    FontColor = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Active = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    DisabledFontColor = property(_get, _set, doc = _set.__doc__)
##

class IRecording(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{663FF9A7-E59F-4700-8076-375200A1A122}')
    _idlflags_ = ['dual', 'oleautomation']
IRecordManager._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(0), 'defaultcollelem', 'propget'], HRESULT, 'Items',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(IRecording)), 'Value' )),
    COMMETHOD([dispid(203), 'propget'], HRESULT, 'Filterby',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(203), 'propput'], HRESULT, 'Filterby',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(202)], HRESULT, 'DeleteEntry',
              ( ['in'], c_int, 'ID' )),
    COMMETHOD([dispid(-4), 'propget'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Value' )),
]
################################################################
## code template for IRecordManager implementation
##class IRecordManager_Impl(object):
##    @property
##    def Count(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Items(self, Index):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Value
##
##    def DeleteEntry(self, ID):
##        '-no docstring-'
##        #return 
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Filterby = property(_get, _set, doc = _set.__doc__)
##

IWindowManager._methods_ = [
    COMMETHOD([dispid(201)], HRESULT, 'ShowWindow',
              ( ['in'], c_int, 'WindowID' )),
    COMMETHOD([dispid(203)], HRESULT, 'ActiveWindowHasBackground',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(204)], HRESULT, 'ActiveWindowID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(205)], HRESULT, 'ActiveWindowNr',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(209)], HRESULT, 'IsOverlay',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(212)], HRESULT, 'PreviousWindow'),
    COMMETHOD([dispid(213)], HRESULT, 'OverlayWindowID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(215)], HRESULT, 'CloseOverlay'),
]
################################################################
## code template for IWindowManager implementation
##class IWindowManager_Impl(object):
##    def IsOverlay(self):
##        '-no docstring-'
##        #return Value
##
##    def CloseOverlay(self):
##        '-no docstring-'
##        #return 
##
##    def PreviousWindow(self):
##        '-no docstring-'
##        #return 
##
##    def ActiveWindowHasBackground(self):
##        '-no docstring-'
##        #return Value
##
##    def ActiveWindowNr(self):
##        '-no docstring-'
##        #return Value
##
##    def ActiveWindowID(self):
##        '-no docstring-'
##        #return Value
##
##    def OverlayWindowID(self):
##        '-no docstring-'
##        #return Value
##
##    def ShowWindow(self, WindowID):
##        '-no docstring-'
##        #return 
##

IChannelCollection._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(0), 'defaultcollelem', 'propget'], HRESULT, 'Item',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(IChannelItem)), 'Value' )),
    COMMETHOD([dispid(202)], HRESULT, 'GetNr',
              ( ['in'], BSTR, 'ID' ),
              ( ['retval', 'out'], POINTER(c_int), 'Result' )),
    COMMETHOD([dispid(203)], HRESULT, 'GetChannelname',
              ( ['in'], c_int, 'SID' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Result' )),
    COMMETHOD([dispid(204)], HRESULT, 'GetChannelID',
              ( ['in'], c_int, 'SID' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Result' )),
    COMMETHOD([dispid(205)], HRESULT, 'GetChannel',
              ( ['in'], BSTR, 'ID' ),
              ( ['in', 'out'], POINTER(c_int), 'Nr' ),
              ( ['retval', 'out'], POINTER(POINTER(IChannelItem)), 'Result' )),
    COMMETHOD([dispid(206)], HRESULT, 'GetbyChannelname',
              ( ['in'], BSTR, 'Name' ),
              ( ['retval', 'out'], POINTER(c_int), 'Nr' )),
    COMMETHOD([dispid(207)], HRESULT, 'GetChannelList',
              ( ['out'], POINTER(VARIANT), 'List' ),
              ( ['retval', 'out'], POINTER(c_int), 'Result' )),
    COMMETHOD([dispid(208)], HRESULT, 'GetByEPGChannelID',
              ( ['in'], c_int, 'EPGChannelID' ),
              ( ['retval', 'out'], POINTER(POINTER(IChannelItem)), 'Value' )),
    COMMETHOD([dispid(-4), 'propget'], HRESULT, '_NewEnum',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'Value' )),
    COMMETHOD([dispid(209)], HRESULT, 'GetChannelByTID',
              ( ['in'], c_int, 'SID' ),
              ( ['in'], c_int, 'TID' ),
              ( ['retval', 'out'], POINTER(POINTER(IChannelItem)), 'Value' )),
]
################################################################
## code template for IChannelCollection implementation
##class IChannelCollection_Impl(object):
##    @property
##    def Count(self):
##        '-no docstring-'
##        #return Value
##
##    def GetChannelByTID(self, SID, TID):
##        '-no docstring-'
##        #return Value
##
##    def GetChannelList(self):
##        '-no docstring-'
##        #return List, Result
##
##    @property
##    def _NewEnum(self):
##        '-no docstring-'
##        #return Value
##
##    def GetByEPGChannelID(self, EPGChannelID):
##        '-no docstring-'
##        #return Value
##
##    def GetNr(self, ID):
##        '-no docstring-'
##        #return Result
##
##    def GetbyChannelname(self, Name):
##        '-no docstring-'
##        #return Nr
##
##    def GetChannelname(self, SID):
##        '-no docstring-'
##        #return Result
##
##    def GetChannel(self, ID):
##        '-no docstring-'
##        #return Nr, Result
##
##    @property
##    def Item(self, Index):
##        '-no docstring-'
##        #return Value
##
##    def GetChannelID(self, SID):
##        '-no docstring-'
##        #return Result
##

IDVBOSD._methods_ = [
    COMMETHOD([dispid(204), helpstring(u'Gets the current Channelname'), 'propget'], HRESULT, 'ChannelName',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(203), helpstring(u'Shows the input dialog and returns the input')], HRESULT, 'GetText',
              ( ['in'], BSTR, 'Msg' ),
              ( ['in'], BSTR, 'strline' ),
              ( ['in'], VARIANT_BOOL, 'NumbersOnly' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(205), helpstring(u'Closes the OSD')], HRESULT, 'GoHome'),
    COMMETHOD([dispid(211), helpstring(u'set muted')], HRESULT, 'SetMute',
              ( ['in'], VARIANT_BOOL, 'Mute' )),
    COMMETHOD([dispid(212), helpstring(u'signal the OSD to redraw itself')], HRESULT, 'SetRefresh',
              ( ['in'], VARIANT_BOOL, 'Value' )),
    COMMETHOD([dispid(215), helpstring(u'true if the OSD is global activated'), 'propget'], HRESULT, 'Running',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(213), helpstring(u'shows a Message on the TV screen')], HRESULT, 'ShowInfoinTVPic',
              ( ['in'], BSTR, 'Info' ),
              ( ['in'], c_int, 'Timeout', 5000 )),
    COMMETHOD([dispid(216), helpstring(u'shows a YES/No dialog and returns the selection: True for Yes')], HRESULT, 'ShowYesNo',
              ( ['in'], BSTR, 'Heading' ),
              ( ['in'], BSTR, 'Line1' ),
              ( ['in'], BSTR, 'Line2' ),
              ( ['in'], BSTR, 'Line3' ),
              ( ['in'], VARIANT_BOOL, 'Selected', False ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Result' )),
    COMMETHOD([dispid(217)], HRESULT, 'Getfile',
              ( ['in'], BSTR, 'Heading' ),
              ( ['in'], BSTR, 'StartDir' ),
              ( ['in'], BSTR, 'Ext' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(218)], HRESULT, 'ShowPopUp',
              ( ['in'], BSTR, 'Heading' ),
              ( ['in'], BSTR, 'Options' ),
              ( ['in'], VARIANT_BOOL, 'Centered', True ),
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(219)], HRESULT, 'ExecProc',
              ( ['in'], BSTR, 'MyProcStr' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(220)], HRESULT, 'AppVersion',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(201)], HRESULT, 'AppDir',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(207)], HRESULT, 'IsPlaying',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(206)], HRESULT, 'IsFullscreen',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(214)], HRESULT, 'SettingDir',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(208)], HRESULT, 'IsPlayingVideo',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(209)], HRESULT, 'isVisible',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(210)], HRESULT, 'ShowInfo',
              ( ['in'], BSTR, 'Heading' ),
              ( ['in'], BSTR, 'Line1' ),
              ( ['in'], BSTR, 'Line2' ),
              ( ['in'], c_int, 'secTimeout' ),
              ( ['in'], BSTR, 'ButtonCaption' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Result' )),
    COMMETHOD([dispid(221)], HRESULT, 'newOSDMessage',
              ( ['in'], c_int, 'MsgID' ),
              ( ['in'], c_int, 'WindowID' ),
              ( ['in'], c_int, 'SenderId' ),
              ( ['retval', 'out'], POINTER(POINTER(IOSDMessage)), 'Value' )),
    COMMETHOD([dispid(202)], HRESULT, 'ShowImage',
              ( ['in'], BSTR, 'Filename' ),
              ( ['in'], c_int, 'Timeout' )),
    COMMETHOD([dispid(222)], HRESULT, 'CreateAlarm',
              ( ['in'], c_double, 'Interval' ),
              ( ['in'], TAlarmMode, 'Mode' ),
              ( ['in'], c_double, 'StartTime' ),
              ( ['in'], VARIANT_BOOL, 'Save' ),
              ( ['in'], POINTER(IOSDMessage), 'Data' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(223)], HRESULT, 'CloseAlarm',
              ( ['in'], BSTR, 'ID' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(224)], HRESULT, 'AddButton',
              ( ['in'], c_int, 'X' ),
              ( ['in'], c_int, 'Y' ),
              ( ['in'], c_int, 'width' ),
              ( ['in'], c_int, 'Height' ),
              ( ['in'], c_int, 'WindowID' ),
              ( ['in'], c_int, 'ActionID' ),
              ( ['in'], c_int, 'Hyperlink' ),
              ( ['in'], BSTR, 'Labeltext' ),
              ( ['in'], BSTR, 'Funktion' ),
              ( ['in'], BSTR, 'App' ),
              ( ['in'], BSTR, 'Arg' )),
    COMMETHOD([dispid(225)], HRESULT, 'ExecNewProcess',
              ( ['in'], BSTR, 'ProgramName' ),
              ( ['in'], BSTR, 'Params' ),
              ( ['in'], VARIANT_BOOL, 'Wait' ),
              ( ['in'], VARIANT_BOOL, 'LowPriority' )),
    COMMETHOD([dispid(226)], HRESULT, 'ShowInfoHelp',
              ( ['in'], BSTR, 'Heading' ),
              ( ['in'], BSTR, 'Line1' )),
    COMMETHOD([dispid(228)], HRESULT, 'AddMenuButton',
              ( ['in'], c_int, 'WindowID' ),
              ( ['in'], c_int, 'Hyperlink' ),
              ( ['in'], BSTR, 'ButtonText' ),
              ( ['in'], BSTR, 'PictureImage' ),
              ( ['in'], BSTR, 'Programm' ),
              ( ['in'], BSTR, 'Argument' ),
              ( ['in'], BSTR, 'DVBVFunction' )),
    COMMETHOD([dispid(227), 'propget'], HRESULT, 'Skinpath',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
]
################################################################
## code template for IDVBOSD implementation
##class IDVBOSD_Impl(object):
##    def ShowInfo(self, Heading, Line1, Line2, secTimeout, ButtonCaption):
##        '-no docstring-'
##        #return Result
##
##    def SetMute(self, Mute):
##        u'set muted'
##        #return 
##
##    def ExecProc(self, MyProcStr):
##        '-no docstring-'
##        #return Value
##
##    def IsPlayingVideo(self):
##        '-no docstring-'
##        #return Value
##
##    def GoHome(self):
##        u'Closes the OSD'
##        #return 
##
##    def ShowInfoHelp(self, Heading, Line1):
##        '-no docstring-'
##        #return 
##
##    def ExecNewProcess(self, ProgramName, Params, Wait, LowPriority):
##        '-no docstring-'
##        #return 
##
##    def newOSDMessage(self, MsgID, WindowID, SenderId):
##        '-no docstring-'
##        #return Value
##
##    def GetText(self, Msg, strline, NumbersOnly):
##        u'Shows the input dialog and returns the input'
##        #return Value
##
##    def AddButton(self, X, Y, width, Height, WindowID, ActionID, Hyperlink, Labeltext, Funktion, App, Arg):
##        '-no docstring-'
##        #return 
##
##    @property
##    def Running(self):
##        u'true if the OSD is global activated'
##        #return Value
##
##    def SettingDir(self):
##        '-no docstring-'
##        #return Value
##
##    def AddMenuButton(self, WindowID, Hyperlink, ButtonText, PictureImage, Programm, Argument, DVBVFunction):
##        '-no docstring-'
##        #return 
##
##    def AppDir(self):
##        '-no docstring-'
##        #return Value
##
##    def ShowInfoinTVPic(self, Info, Timeout):
##        u'shows a Message on the TV screen'
##        #return 
##
##    def AppVersion(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Skinpath(self):
##        '-no docstring-'
##        #return Value
##
##    def IsFullscreen(self):
##        '-no docstring-'
##        #return Value
##
##    def ShowYesNo(self, Heading, Line1, Line2, Line3, Selected):
##        u'shows a YES/No dialog and returns the selection: True for Yes'
##        #return Result
##
##    def ShowPopUp(self, Heading, Options, Centered):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def ChannelName(self):
##        u'Gets the current Channelname'
##        #return Value
##
##    def SetRefresh(self, Value):
##        u'signal the OSD to redraw itself'
##        #return 
##
##    def CloseAlarm(self, ID):
##        '-no docstring-'
##        #return Value
##
##    def ShowImage(self, Filename, Timeout):
##        '-no docstring-'
##        #return 
##
##    def isVisible(self):
##        '-no docstring-'
##        #return Value
##
##    def CreateAlarm(self, Interval, Mode, StartTime, Save, Data):
##        '-no docstring-'
##        #return Value
##
##    def Getfile(self, Heading, StartDir, Ext):
##        '-no docstring-'
##        #return Value
##
##    def IsPlaying(self):
##        '-no docstring-'
##        #return Value
##

IChannelCollection2._methods_ = [
    COMMETHOD([dispid(301)], HRESULT, 'GetByEPGChannelID2',
              ( ['in'], c_longlong, 'ID' ),
              ( ['in'], c_int, 'AudioPID' ),
              ( ['retval', 'out'], POINTER(POINTER(IChannelItem)), 'Result' )),
]
################################################################
## code template for IChannelCollection2 implementation
##class IChannelCollection2_Impl(object):
##    def GetByEPGChannelID2(self, ID, AudioPID):
##        '-no docstring-'
##        #return Result
##

IEPGAddBuffer._methods_ = [
    COMMETHOD([dispid(201)], HRESULT, 'NewItem',
              ( ['retval', 'out'], POINTER(POINTER(IEPGItem)), 'Value' )),
    COMMETHOD([dispid(202)], HRESULT, 'Add',
              ( ['in'], POINTER(IEPGItem), 'Entry' )),
    COMMETHOD([dispid(203)], HRESULT, 'Commit'),
    COMMETHOD([dispid(204)], HRESULT, 'Clear'),
]
################################################################
## code template for IEPGAddBuffer implementation
##class IEPGAddBuffer_Impl(object):
##    def NewItem(self):
##        '-no docstring-'
##        #return Value
##
##    def Commit(self):
##        '-no docstring-'
##        #return 
##
##    def Add(self, Entry):
##        '-no docstring-'
##        #return 
##
##    def Clear(self):
##        '-no docstring-'
##        #return 
##

IPlayListManager._methods_ = [
    COMMETHOD([dispid(201)], HRESULT, 'GetNext',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(202)], HRESULT, 'GetPlaylist',
              ( ['in'], c_int, 'Playlist' ),
              ( ['retval', 'out'], POINTER(POINTER(IPlaylist)), 'Value' )),
    COMMETHOD([dispid(203)], HRESULT, 'HasChanged',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(204)], HRESULT, 'LoadPlayList',
              ( ['in'], BSTR, 'Filename' ),
              ( ['retval', 'out'], POINTER(POINTER(IPlaylist)), 'Value' )),
    COMMETHOD([dispid(205)], HRESULT, 'NewPlaylistItem',
              ( ['retval', 'out'], POINTER(POINTER(IPlaylistItem)), 'Value' )),
    COMMETHOD([dispid(206)], HRESULT, 'NewPlayList',
              ( ['retval', 'out'], POINTER(POINTER(IPlaylist)), 'Value' )),
    COMMETHOD([dispid(210)], HRESULT, 'Play',
              ( ['in'], c_int, 'TitleNr' ),
              ( ['in'], c_double, 'Position' )),
    COMMETHOD([dispid(211)], HRESULT, 'PlayFile',
              ( ['in'], BSTR, 'Filename' )),
    COMMETHOD([dispid(212)], HRESULT, 'PlayNext',
              ( ['in'], VARIANT_BOOL, 'Autostart' ),
              ( ['in'], c_double, 'Position' )),
    COMMETHOD([dispid(213)], HRESULT, 'PlayPrevious'),
    COMMETHOD([dispid(214)], HRESULT, 'Remove',
              ( ['in'], c_int, 'Typ' ),
              ( ['in'], BSTR, 'Filename' )),
    COMMETHOD([dispid(215)], HRESULT, 'Reset'),
    COMMETHOD([dispid(216), 'propget'], HRESULT, 'CurrentPlaylist',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(216), 'propput'], HRESULT, 'CurrentPlaylist',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(217), 'propget'], HRESULT, 'CurrentTitle',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(217), 'propput'], HRESULT, 'CurrentTitle',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(218), 'propget'], HRESULT, 'EntriesNotPresent',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(219), 'propget'], HRESULT, 'IsPlaying',
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
]
################################################################
## code template for IPlayListManager implementation
##class IPlayListManager_Impl(object):
##    def GetNext(self):
##        '-no docstring-'
##        #return Value
##
##    def PlayPrevious(self):
##        '-no docstring-'
##        #return 
##
##    def NewPlaylistItem(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def IsPlaying(self):
##        '-no docstring-'
##        #return Value
##
##    def Play(self, TitleNr, Position):
##        '-no docstring-'
##        #return 
##
##    def Remove(self, Typ, Filename):
##        '-no docstring-'
##        #return 
##
##    def PlayNext(self, Autostart, Position):
##        '-no docstring-'
##        #return 
##
##    @property
##    def EntriesNotPresent(self):
##        '-no docstring-'
##        #return Value
##
##    def NewPlayList(self):
##        '-no docstring-'
##        #return Value
##
##    def PlayFile(self, Filename):
##        '-no docstring-'
##        #return 
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    CurrentPlaylist = property(_get, _set, doc = _set.__doc__)
##
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def LoadPlayList(self, Filename):
##        '-no docstring-'
##        #return Value
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    CurrentTitle = property(_get, _set, doc = _set.__doc__)
##
##    def GetPlaylist(self, Playlist):
##        '-no docstring-'
##        #return Value
##
##    def HasChanged(self):
##        '-no docstring-'
##        #return Value
##

class IfreedbReturnTrackData(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{4051D261-1D97-4C5E-8A18-4FB99494160B}')
    _idlflags_ = ['dual', 'oleautomation']
IMusicCD._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'TrackCount',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(201), 'propput'], HRESULT, 'TrackCount',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(202), 'propget'], HRESULT, 'Playorder',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(202), 'propput'], HRESULT, 'Playorder',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(203), 'propget'], HRESULT, 'DiscID',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(203), 'propput'], HRESULT, 'DiscID',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(204), 'propget'], HRESULT, 'Submitted_Via',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(204), 'propput'], HRESULT, 'Submitted_Via',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(205), 'propget'], HRESULT, 'freedb_Revision',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(205), 'propput'], HRESULT, 'freedb_Revision',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(206), 'propget'], HRESULT, 'ExtendedData',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(206), 'propput'], HRESULT, 'ExtendedData',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(208), 'propget'], HRESULT, 'Disc_Length',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(208), 'propput'], HRESULT, 'Disc_Length',
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([dispid(209), 'propget'], HRESULT, 'DiscYear',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(209), 'propput'], HRESULT, 'DiscYear',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(210), 'propget'], HRESULT, 'DiscTitle',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(210), 'propput'], HRESULT, 'DiscTitle',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(211), 'propget'], HRESULT, 'DiscGenre',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(211), 'propput'], HRESULT, 'DiscGenre',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(212), 'propget'], HRESULT, 'DiscArtist',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(212), 'propput'], HRESULT, 'DiscArtist',
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(207), 'propget'], HRESULT, 'Track',
              ( ['in'], c_int, 'Index' ),
              ( ['retval', 'out'], POINTER(POINTER(IfreedbReturnTrackData)), 'Value' )),
    COMMETHOD([dispid(213)], HRESULT, 'GetTrackList',
              ( ['in', 'out'], POINTER(VARIANT), 'Value' ),
              ( ['retval', 'out'], POINTER(c_int), 'Result' )),
]
################################################################
## code template for IMusicCD implementation
##class IMusicCD_Impl(object):
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    DiscArtist = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Disc_Length = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    DiscID = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def Track(self, Index):
##        '-no docstring-'
##        #return Value
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    DiscTitle = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Playorder = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    DiscYear = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    TrackCount = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    freedb_Revision = property(_get, _set, doc = _set.__doc__)
##
##    def GetTrackList(self):
##        '-no docstring-'
##        #return Value, Result
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    ExtendedData = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    DiscGenre = property(_get, _set, doc = _set.__doc__)
##
##    def _get(self):
##        '-no docstring-'
##        #return Value
##    def _set(self, Value):
##        '-no docstring-'
##    Submitted_Via = property(_get, _set, doc = _set.__doc__)
##

IRecording._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Channel',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(202), 'propget'], HRESULT, 'Played',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(203), 'propget'], HRESULT, 'Filename',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(204), 'propget'], HRESULT, 'Title',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(205), 'propget'], HRESULT, 'Description',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(206), 'propget'], HRESULT, 'Date',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([dispid(207), 'propget'], HRESULT, 'Duration',
              ( ['retval', 'out'], POINTER(c_double), 'Value' )),
    COMMETHOD([dispid(208), 'propget'], HRESULT, 'recID',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
]
################################################################
## code template for IRecording implementation
##class IRecording_Impl(object):
##    @property
##    def Description(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Title(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Played(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Filename(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Duration(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def recID(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Date(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Channel(self):
##        '-no docstring-'
##        #return Value
##

IfreedbReturnTrackData._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Frame_Offset',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(202), 'propget'], HRESULT, 'Duration',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(203), 'propget'], HRESULT, 'TrackArtist',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(204), 'propget'], HRESULT, 'TrackTitle',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(205), 'propget'], HRESULT, 'ExtendedTrackData',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
]
################################################################
## code template for IfreedbReturnTrackData implementation
##class IfreedbReturnTrackData_Impl(object):
##    @property
##    def Duration(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def ExtendedTrackData(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def TrackArtist(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def TrackTitle(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Frame_Offset(self):
##        '-no docstring-'
##        #return Value
##

IVideotext._methods_ = [
    COMMETHOD([dispid(201)], HRESULT, 'GetPage',
              ( ['in'], c_int, 'Page' ),
              ( ['in'], c_int, 'Subpage' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Result' )),
    COMMETHOD([dispid(202)], HRESULT, 'GetPageAsHTML',
              ( ['in'], c_int, 'PageNr' ),
              ( ['in'], c_int, 'Subpage' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Param3' )),
    COMMETHOD([dispid(203)], HRESULT, 'NextAvailable',
              ( ['in', 'out'], POINTER(c_int), 'Page' ),
              ( ['in', 'out'], POINTER(c_int), 'Subpage' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(204)], HRESULT, 'PrevAvailable',
              ( ['in', 'out'], POINTER(c_int), 'Page' ),
              ( ['in', 'out'], POINTER(c_int), 'Subpage' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
    COMMETHOD([dispid(205)], HRESULT, 'GetPageAsRaw',
              ( ['in'], c_int, 'Page' ),
              ( ['in'], c_int, 'Sub' ),
              ( ['out'], POINTER(VARIANT), 'List' ),
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(206)], HRESULT, 'FindPage',
              ( ['in'], c_int, 'Page' ),
              ( ['in'], c_int, 'Sub' ),
              ( ['retval', 'out'], POINTER(VARIANT_BOOL), 'Value' )),
]
################################################################
## code template for IVideotext implementation
##class IVideotext_Impl(object):
##    def FindPage(self, Page, Sub):
##        '-no docstring-'
##        #return Value
##
##    def NextAvailable(self):
##        '-no docstring-'
##        #return Page, Subpage, Value
##
##    def GetPage(self, Page, Subpage):
##        '-no docstring-'
##        #return Result
##
##    def GetPageAsRaw(self, Page, Sub):
##        '-no docstring-'
##        #return List, Value
##
##    def GetPageAsHTML(self, PageNr, Subpage):
##        '-no docstring-'
##        #return Param3
##
##    def PrevAvailable(self):
##        '-no docstring-'
##        #return Page, Subpage, Value
##

ITagreader._methods_ = [
    COMMETHOD([dispid(203)], HRESULT, 'SaveTag',
              ( ['in'], BSTR, 'Filename' ),
              ( ['in'], BSTR, 'Title' ),
              ( ['in'], BSTR, 'Artist' ),
              ( ['in'], BSTR, 'Album' ),
              ( ['in'], BSTR, 'Track' ),
              ( ['in'], BSTR, 'Genre' ),
              ( ['in'], BSTR, 'Year' ),
              ( ['in'], BSTR, 'Comment' ),
              ( ['in'], Tagtype, 'Typ' )),
    COMMETHOD([dispid(201)], HRESULT, 'ReadTag',
              ( ['in'], BSTR, 'Filename' ),
              ( ['retval', 'out'], POINTER(POINTER(IMusicTag)), 'Value' )),
]
################################################################
## code template for ITagreader implementation
##class ITagreader_Impl(object):
##    def ReadTag(self, Filename):
##        '-no docstring-'
##        #return Value
##
##    def SaveTag(self, Filename, Title, Artist, Album, Track, Genre, Year, Comment, Typ):
##        '-no docstring-'
##        #return 
##

IDataManager._methods_ = [
    COMMETHOD([dispid(201), 'propget'], HRESULT, 'Keys',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(202), 'propget'], HRESULT, 'Value',
              ( ['in'], BSTR, 'Key' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(202), 'propput'], HRESULT, 'Value',
              ( ['in'], BSTR, 'Key' ),
              ( ['in'], BSTR, 'Value' )),
    COMMETHOD([dispid(203), 'propget'], HRESULT, 'Count',
              ( ['retval', 'out'], POINTER(c_int), 'Value' )),
    COMMETHOD([dispid(204)], HRESULT, 'Parse',
              ( ['in'], BSTR, 'Valu' ),
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
    COMMETHOD([dispid(205)], HRESULT, 'GetAll',
              ( ['retval', 'out'], POINTER(BSTR), 'Value' )),
]
################################################################
## code template for IDataManager implementation
##class IDataManager_Impl(object):
##    @property
##    def Keys(self):
##        '-no docstring-'
##        #return Value
##
##    @property
##    def Count(self):
##        '-no docstring-'
##        #return Value
##
##    def Parse(self, Valu):
##        '-no docstring-'
##        #return Value
##
##    def GetAll(self):
##        '-no docstring-'
##        #return Value
##
##    def _get(self, Key):
##        '-no docstring-'
##        #return Value
##    def _set(self, Key, Value):
##        '-no docstring-'
##    Value = property(_get, _set, doc = _set.__doc__)
##

__all__ = ['cpsPause', 'TRendererTyp', 'ITimerCollection',
           'texScript', 'Record_', 'IDVBOSD', 'TPlaystates',
           'IEPGManager2', 'IRecordManager', 'ITuner', 'DVBViewer',
           'IWindowManager', 'IPlaylist', 'rtDVB', 'ttSatellite',
           'IDataManager', 'IRecording', 'IPlayListManager',
           'Playlist', 'DVBViewerEvents', 'IfreedbReturnTrackData',
           'IMusicTag', 'Tagtype', 'PowerOff', 'pamMonthly',
           'cpsStop', 'IDVBViewerEventhelper', 'IEPGCollection',
           'Hibernate', 'IEPGAddBuffer', 'texHyperlink', 'texCMD',
           'ttCable', 'Slumbermode', 'IMessageEv', 'MessageEvents',
           'TExeType', 'ITimerItem', 'None', 'Standby', 'ITagreader',
           'IOSDItem', 'IOSDMessage', 'ttATSC', 'tpFlac', 'IMusicCD',
           'IEPGManager', 'TDVBVTunerType', 'tpID3v2', 'tpID3v1',
           'IDVBViewerEvents', 'IEPGItem2', 'AudioPlugin',
           'Teletextmanager', 'rtUnknown', 'texApp', 'TAlarmMode',
           'IMessageEvents', 'pamYearly', 'IChannelCollection2',
           'tpVorbis', 'tpApe', 'IMatch', 'IOSDItems', 'cpsPlay',
           'Tune', 'rtMPG2TS', 'IDVBViewer', 'pamHourly',
           'IFavoritesManager', 'IChannelItem', 'pamMinutely',
           'ITeletextEvents', 'Close', 'pamDaily',
           'IFavoritesCollection', 'IFavoritesItem', 'IPlaylistItem',
           'IVideotext', 'IUtils', 'pamWeekly', 'pamOnce',
           'Videoplugin', 'IFreeDB_HTTP', 'IMainMenuConfig',
           'IDVBHardware', 'texFunct', 'TDVBVTimerAction',
           'IChannelCollection', 'TDVBVShutdown', 'ttTerrestrial',
           'rtVideoAudioDVD', 'IDVBViewer2', 'IEPGItem']
from comtypes import _check_version; _check_version('501')
