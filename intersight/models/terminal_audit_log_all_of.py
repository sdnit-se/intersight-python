# coding: utf-8
"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations.   # noqa: E501

    The version of the OpenAPI document: 1.0.9-1295
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from intersight.configuration import Configuration


class TerminalAuditLogAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'end_time': 'datetime',
        'start_time': 'datetime',
        'device_registration': 'AssetDeviceConnection',
        'user': 'IamUser'
    }

    attribute_map = {
        'end_time': 'EndTime',
        'start_time': 'StartTime',
        'device_registration': 'DeviceRegistration',
        'user': 'User'
    }

    def __init__(self,
                 end_time=None,
                 start_time=None,
                 device_registration=None,
                 user=None,
                 local_vars_configuration=None):  # noqa: E501
        """TerminalAuditLogAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._end_time = None
        self._start_time = None
        self._device_registration = None
        self._user = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if start_time is not None:
            self.start_time = start_time
        if device_registration is not None:
            self.device_registration = device_registration
        if user is not None:
            self.user = user

    @property
    def end_time(self):
        """Gets the end_time of this TerminalAuditLogAllOf.  # noqa: E501

        The time the terminal was closed. If terminal has not closed, value is zero time.     # noqa: E501

        :return: The end_time of this TerminalAuditLogAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TerminalAuditLogAllOf.

        The time the terminal was closed. If terminal has not closed, value is zero time.     # noqa: E501

        :param end_time: The end_time of this TerminalAuditLogAllOf.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def start_time(self):
        """Gets the start_time of this TerminalAuditLogAllOf.  # noqa: E501

        The time the terminal session was opened.     # noqa: E501

        :return: The start_time of this TerminalAuditLogAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TerminalAuditLogAllOf.

        The time the terminal session was opened.     # noqa: E501

        :param start_time: The start_time of this TerminalAuditLogAllOf.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def device_registration(self):
        """Gets the device_registration of this TerminalAuditLogAllOf.  # noqa: E501


        :return: The device_registration of this TerminalAuditLogAllOf.  # noqa: E501
        :rtype: AssetDeviceConnection
        """
        return self._device_registration

    @device_registration.setter
    def device_registration(self, device_registration):
        """Sets the device_registration of this TerminalAuditLogAllOf.


        :param device_registration: The device_registration of this TerminalAuditLogAllOf.  # noqa: E501
        :type: AssetDeviceConnection
        """

        self._device_registration = device_registration

    @property
    def user(self):
        """Gets the user of this TerminalAuditLogAllOf.  # noqa: E501


        :return: The user of this TerminalAuditLogAllOf.  # noqa: E501
        :rtype: IamUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TerminalAuditLogAllOf.


        :param user: The user of this TerminalAuditLogAllOf.  # noqa: E501
        :type: IamUser
        """

        self._user = user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TerminalAuditLogAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TerminalAuditLogAllOf):
            return True

        return self.to_dict() != other.to_dict()
