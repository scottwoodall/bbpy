################################################## 
# CourseMembership_WS_services.py 
# generated by ZSI.generate.wsdl2python
##################################################


from CourseMembership_WS_services_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
import ZSI

# Locator
class CourseMembership_WSLocator:
    CourseMembership_WSPortType_address = "https://dev.bblearn.nau.edu/webapps/ws/services/CourseMembership.WS"
    def getCourseMembership_WSPortTypeAddress(self):
        return CourseMembership_WSLocator.CourseMembership_WSPortType_address
    def getCourseMembership_WSPortType(self, url=None, **kw):
        if url:
            url = url + "/webapps/ws/services/CourseMembership.WS"
            return CourseMembership_WSSOAP11BindingSOAP(url, **kw)
        else:
            return CourseMembership_WSSOAP11BindingSOAP(CourseMembership_WSLocator.CourseMembership_WSPortType_address, **kw)
        

# Methods
class CourseMembership_WSSOAP11BindingSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: initializeCourseMembershipWS
    def initializeCourseMembershipWS(self, request):
        if isinstance(request, initializeCourseMembershipWSRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="initializeCourseMembershipWS", **kw)
        # no output wsaction
        response = self.binding.Receive(initializeCourseMembershipWSResponse.typecode)
        return response

    # op: saveCourseMembership
    def saveCourseMembership(self, request):
        if isinstance(request, saveCourseMembershipRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="saveCourseMembership", **kw)
        # no output wsaction
        response = self.binding.Receive(saveCourseMembershipResponse.typecode)
        return response

    # op: getCourseMembership
    def getCourseMembership(self, request):
        if isinstance(request, getCourseMembershipRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="getCourseMembership", **kw)
        # no output wsaction
        response = self.binding.Receive(getCourseMembershipResponse.typecode)
        return response

    # op: saveGroupMembership
    def saveGroupMembership(self, request):
        if isinstance(request, saveGroupMembershipRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="saveGroupMembership", **kw)
        # no output wsaction
        response = self.binding.Receive(saveGroupMembershipResponse.typecode)
        return response

    # op: getServerVersion
    def getServerVersion(self, request):
        if isinstance(request, getServerVersionRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="getServerVersion", **kw)
        # no output wsaction
        response = self.binding.Receive(getServerVersionResponse.typecode)
        return response

    # op: deleteCourseMembership
    def deleteCourseMembership(self, request):
        if isinstance(request, deleteCourseMembershipRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="deleteCourseMembership", **kw)
        # no output wsaction
        response = self.binding.Receive(deleteCourseMembershipResponse.typecode)
        return response

    # op: deleteGroupMembership
    def deleteGroupMembership(self, request):
        if isinstance(request, deleteGroupMembershipRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="deleteGroupMembership", **kw)
        # no output wsaction
        response = self.binding.Receive(deleteGroupMembershipResponse.typecode)
        return response

    # op: getGroupMembership
    def getGroupMembership(self, request):
        if isinstance(request, getGroupMembershipRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="getGroupMembership", **kw)
        # no output wsaction
        response = self.binding.Receive(getGroupMembershipResponse.typecode)
        return response

    # op: getCourseRoles
    def getCourseRoles(self, request):
        if isinstance(request, getCourseRolesRequest) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        kw = {}
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="getCourseRoles", **kw)
        # no output wsaction
        response = self.binding.Receive(getCourseRolesResponse.typecode)
        return response

initializeCourseMembershipWSRequest = course_membership_ns1.initializeCourseMembershipWS_Dec().pyclass

initializeCourseMembershipWSResponse = course_membership_ns1.initializeCourseMembershipWSResponse_Dec().pyclass

saveCourseMembershipRequest = course_membership_ns1.saveCourseMembership_Dec().pyclass

saveCourseMembershipResponse = course_membership_ns1.saveCourseMembershipResponse_Dec().pyclass

getCourseMembershipRequest = course_membership_ns1.getCourseMembership_Dec().pyclass

getCourseMembershipResponse = course_membership_ns1.getCourseMembershipResponse_Dec().pyclass

saveGroupMembershipRequest = course_membership_ns1.saveGroupMembership_Dec().pyclass

saveGroupMembershipResponse = course_membership_ns1.saveGroupMembershipResponse_Dec().pyclass

getServerVersionRequest = course_membership_ns1.getServerVersion_Dec().pyclass

getServerVersionResponse = course_membership_ns1.getServerVersionResponse_Dec().pyclass

deleteCourseMembershipRequest = course_membership_ns1.deleteCourseMembership_Dec().pyclass

deleteCourseMembershipResponse = course_membership_ns1.deleteCourseMembershipResponse_Dec().pyclass

deleteGroupMembershipRequest = course_membership_ns1.deleteGroupMembership_Dec().pyclass

deleteGroupMembershipResponse = course_membership_ns1.deleteGroupMembershipResponse_Dec().pyclass

getGroupMembershipRequest = course_membership_ns1.getGroupMembership_Dec().pyclass

getGroupMembershipResponse = course_membership_ns1.getGroupMembershipResponse_Dec().pyclass

getCourseRolesRequest = course_membership_ns1.getCourseRoles_Dec().pyclass

getCourseRolesResponse = course_membership_ns1.getCourseRolesResponse_Dec().pyclass