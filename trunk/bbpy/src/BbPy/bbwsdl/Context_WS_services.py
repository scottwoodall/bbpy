################################################## 
# Context_WS_services.py 
# generated by ZSI.generate.wsdl2python
##################################################


from Context_WS_services_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
import ZSI

# Locator
class Context_WSLocator:
    Context_WSPortType_address = "https://dev.bblearn.nau.edu/webapps/ws/services/Context.WS"
    
    def getContext_WSPortTypeAddress(self):
        return Context_WSLocator.Context_WSPortType_address
    def getContext_WSPortType(self, url=None, **kw):
        if url:
            url = url + "/webapps/ws/services/Context.WS"
            return Context_WSSOAP11BindingSOAP(url, **kw)
        else:
            return Context_WSSOAP11BindingSOAP(Context_WSLocator.Context_WSPortType_address, **kw)
         

# Methods
class Context_WSSOAP11BindingSOAP:
    def __init__(self, url, endPointReference=None, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        self.endPointReference = endPointReference

    # op: deactivateTool
    def deactivateTool(self, request):
        if isinstance(request, deactivateToolRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/deactivateToolRequest"
        self.binding.Send(None, None, request, soapaction="deactivateTool", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/deactivateToolResponse"
        response = self.binding.Receive(deactivateToolResponse.typecode, wsaction=wsaction)
        return response

    # op: initializeVersion2
    def initializeVersion2(self, request):
        if isinstance(request, initializeVersion2Request) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/initializeVersion2Request"
        self.binding.Send(None, None, request, soapaction="initializeVersion2", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/initializeVersion2Response"
        response = self.binding.Receive(initializeVersion2Response.typecode, wsaction=wsaction)
        return response

    # op: loginTicket
    def loginTicket(self, request):
        if isinstance(request, loginTicketRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/loginTicketRequest"
        self.binding.Send(None, None, request, soapaction="loginTicket", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/loginTicketResponse"
        response = self.binding.Receive(loginTicketResponse.typecode, wsaction=wsaction)
        return response

    # op: extendSessionLife
    def extendSessionLife(self, request):
        if isinstance(request, extendSessionLifeRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/extendSessionLifeRequest"
        self.binding.Send(None, None, request, soapaction="extendSessionLife", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/extendSessionLifeResponse"
        response = self.binding.Receive(extendSessionLifeResponse.typecode, wsaction=wsaction)
        return response

    # op: registerTool
    def registerTool(self, request):
        if isinstance(request, registerToolRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/registerToolRequest"
        self.binding.Send(None, None, request, soapaction="registerTool", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/registerToolResponse"
        response = self.binding.Receive(registerToolResponse.typecode, wsaction=wsaction)
        return response

    # op: getMemberships
    def getMemberships(self, request):
        if isinstance(request, getMembershipsRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/getMembershipsRequest"
        self.binding.Send(None, None, request, soapaction="getMemberships", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/getMembershipsResponse"
        response = self.binding.Receive(getMembershipsResponse.typecode, wsaction=wsaction)
        return response

    # op: getMyMemberships
    def getMyMemberships(self, request):
        if isinstance(request, getMyMembershipsRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/getMyMembershipsRequest"
        self.binding.Send(None, None, request, soapaction="getMyMemberships", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/getMyMembershipsResponse"
        response = self.binding.Receive(getMyMembershipsResponse.typecode, wsaction=wsaction)
        return response

    # op: getRequiredEntitlements
    def getRequiredEntitlements(self, request):
        if isinstance(request, getRequiredEntitlementsRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/getRequiredEntitlementsRequest"
        self.binding.Send(None, None, request, soapaction="getRequiredEntitlements", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/getRequiredEntitlementsResponse"
        response = self.binding.Receive(getRequiredEntitlementsResponse.typecode, wsaction=wsaction)
        return response

    # op: loginTool
    def loginTool(self, request):
        if isinstance(request, loginToolRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/loginToolRequest"
        self.binding.Send(None, None, request, soapaction="loginTool", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/loginToolResponse"
        response = self.binding.Receive(loginToolResponse.typecode, wsaction=wsaction)
        return response

    # op: logout
    def logout(self, request):
        if isinstance(request, logoutRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/logoutRequest"
        self.binding.Send(None, None, request, soapaction="logout", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/logoutResponse"
        response = self.binding.Receive(logoutResponse.typecode, wsaction=wsaction)
        return response

    # op: getSystemInstallationId
    def getSystemInstallationId(self, request):
        if isinstance(request, getSystemInstallationIdRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/getSystemInstallationIdRequest"
        self.binding.Send(None, None, request, soapaction="getSystemInstallationId", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/getSystemInstallationIdResponse"
        response = self.binding.Receive(getSystemInstallationIdResponse.typecode, wsaction=wsaction)
        return response

    # op: login
    def login(self, request):
        if isinstance(request, loginRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/loginRequest"
        self.binding.Send(None, None, request, soapaction="login", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/loginResponse"
        response = self.binding.Receive(loginResponse.typecode, wsaction=wsaction)
        return response

    # op: getServerVersion
    def getServerVersion(self, request):
        if isinstance(request, getServerVersionRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/getServerVersionRequest"
        self.binding.Send(None, None, request, soapaction="getServerVersion", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/getServerVersionResponse"
        response = self.binding.Receive(getServerVersionResponse.typecode, wsaction=wsaction)
        return response

    # op: emulateUser
    def emulateUser(self, request):
        if isinstance(request, emulateUserRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/emulateUserRequest"
        self.binding.Send(None, None, request, soapaction="emulateUser", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/emulateUserResponse"
        response = self.binding.Receive(emulateUserResponse.typecode, wsaction=wsaction)
        return response

    # op: initialize
    def initialize(self, request):
        if isinstance(request, initializeRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        wsaction = "http://context.ws.blackboard/Context.WSPortType/initializeRequest"
        self.binding.Send(None, None, request, soapaction="initialize", wsaction=wsaction, endPointReference=self.endPointReference, **kw)
        wsaction = "http://context.ws.blackboard/Context.WSPortType/initializeResponse"
        response = self.binding.Receive(initializeResponse.typecode, wsaction=wsaction)
        return response

deactivateToolRequest = context_ns2.deactivateTool_Dec().pyclass

deactivateToolResponse = context_ns2.deactivateToolResponse_Dec().pyclass

initializeVersion2Request = context_ns2.getServerVersion_Dec().pyclass

initializeVersion2Response = context_ns2.initializeVersion2Response_Dec().pyclass

loginTicketRequest = context_ns2.loginTicket_Dec().pyclass

loginTicketResponse = context_ns2.loginTicketResponse_Dec().pyclass

extendSessionLifeRequest = context_ns2.extendSessionLife_Dec().pyclass

extendSessionLifeResponse = context_ns2.extendSessionLifeResponse_Dec().pyclass

registerToolRequest = context_ns2.registerTool_Dec().pyclass

registerToolResponse = context_ns2.registerToolResponse_Dec().pyclass

getMembershipsRequest = context_ns2.getMemberships_Dec().pyclass

getMembershipsResponse = context_ns2.getMembershipsResponse_Dec().pyclass

getMyMembershipsRequest = context_ns2.getServerVersion_Dec().pyclass

getMyMembershipsResponse = context_ns2.getMyMembershipsResponse_Dec().pyclass

getRequiredEntitlementsRequest = context_ns2.getRequiredEntitlements_Dec().pyclass

getRequiredEntitlementsResponse = context_ns2.getRequiredEntitlementsResponse_Dec().pyclass

loginToolRequest = context_ns2.loginTool_Dec().pyclass

loginToolResponse = context_ns2.loginToolResponse_Dec().pyclass

logoutRequest = context_ns2.getServerVersion_Dec().pyclass

logoutResponse = context_ns2.logoutResponse_Dec().pyclass

getSystemInstallationIdRequest = context_ns2.getServerVersion_Dec().pyclass

getSystemInstallationIdResponse = context_ns2.getSystemInstallationIdResponse_Dec().pyclass

loginRequest = context_ns2.login_Dec().pyclass

loginResponse = context_ns2.loginResponse_Dec().pyclass

getServerVersionRequest = context_ns2.getServerVersion_Dec().pyclass

getServerVersionResponse = context_ns2.getServerVersionResponse_Dec().pyclass

emulateUserRequest = context_ns2.emulateUser_Dec().pyclass

emulateUserResponse = context_ns2.emulateUserResponse_Dec().pyclass

initializeRequest = context_ns2.getServerVersion_Dec().pyclass

initializeResponse = context_ns2.initializeResponse_Dec().pyclass