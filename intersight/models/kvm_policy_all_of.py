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


class KvmPolicyAllOf(object):
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
        'enable_local_server_video': 'bool',
        'enable_video_encryption': 'bool',
        'enabled': 'bool',
        'maximum_sessions': 'int',
        'remote_port': 'int',
        'organization': 'OrganizationOrganization',
        'profiles': 'list[PolicyAbstractConfigProfile]'
    }

    attribute_map = {
        'enable_local_server_video': 'EnableLocalServerVideo',
        'enable_video_encryption': 'EnableVideoEncryption',
        'enabled': 'Enabled',
        'maximum_sessions': 'MaximumSessions',
        'remote_port': 'RemotePort',
        'organization': 'Organization',
        'profiles': 'Profiles'
    }

    def __init__(self,
                 enable_local_server_video=None,
                 enable_video_encryption=None,
                 enabled=None,
                 maximum_sessions=None,
                 remote_port=None,
                 organization=None,
                 profiles=None,
                 local_vars_configuration=None):  # noqa: E501
        """KvmPolicyAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enable_local_server_video = None
        self._enable_video_encryption = None
        self._enabled = None
        self._maximum_sessions = None
        self._remote_port = None
        self._organization = None
        self._profiles = None
        self.discriminator = None

        if enable_local_server_video is not None:
            self.enable_local_server_video = enable_local_server_video
        if enable_video_encryption is not None:
            self.enable_video_encryption = enable_video_encryption
        if enabled is not None:
            self.enabled = enabled
        if maximum_sessions is not None:
            self.maximum_sessions = maximum_sessions
        if remote_port is not None:
            self.remote_port = remote_port
        if organization is not None:
            self.organization = organization
        if profiles is not None:
            self.profiles = profiles

    @property
    def enable_local_server_video(self):
        """Gets the enable_local_server_video of this KvmPolicyAllOf.  # noqa: E501

        If enabled, displays KVM session on any monitor attached to the server.    # noqa: E501

        :return: The enable_local_server_video of this KvmPolicyAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._enable_local_server_video

    @enable_local_server_video.setter
    def enable_local_server_video(self, enable_local_server_video):
        """Sets the enable_local_server_video of this KvmPolicyAllOf.

        If enabled, displays KVM session on any monitor attached to the server.    # noqa: E501

        :param enable_local_server_video: The enable_local_server_video of this KvmPolicyAllOf.  # noqa: E501
        :type: bool
        """

        self._enable_local_server_video = enable_local_server_video

    @property
    def enable_video_encryption(self):
        """Gets the enable_video_encryption of this KvmPolicyAllOf.  # noqa: E501

        If enabled, encrypts all video information sent through KVM.    # noqa: E501

        :return: The enable_video_encryption of this KvmPolicyAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._enable_video_encryption

    @enable_video_encryption.setter
    def enable_video_encryption(self, enable_video_encryption):
        """Sets the enable_video_encryption of this KvmPolicyAllOf.

        If enabled, encrypts all video information sent through KVM.    # noqa: E501

        :param enable_video_encryption: The enable_video_encryption of this KvmPolicyAllOf.  # noqa: E501
        :type: bool
        """

        self._enable_video_encryption = enable_video_encryption

    @property
    def enabled(self):
        """Gets the enabled of this KvmPolicyAllOf.  # noqa: E501

        State of the vKVM service on the endpoint.    # noqa: E501

        :return: The enabled of this KvmPolicyAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this KvmPolicyAllOf.

        State of the vKVM service on the endpoint.    # noqa: E501

        :param enabled: The enabled of this KvmPolicyAllOf.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def maximum_sessions(self):
        """Gets the maximum_sessions of this KvmPolicyAllOf.  # noqa: E501

        The maximum number of concurrent KVM sessions allowed.    # noqa: E501

        :return: The maximum_sessions of this KvmPolicyAllOf.  # noqa: E501
        :rtype: int
        """
        return self._maximum_sessions

    @maximum_sessions.setter
    def maximum_sessions(self, maximum_sessions):
        """Sets the maximum_sessions of this KvmPolicyAllOf.

        The maximum number of concurrent KVM sessions allowed.    # noqa: E501

        :param maximum_sessions: The maximum_sessions of this KvmPolicyAllOf.  # noqa: E501
        :type: int
        """

        self._maximum_sessions = maximum_sessions

    @property
    def remote_port(self):
        """Gets the remote_port of this KvmPolicyAllOf.  # noqa: E501

        The port used for KVM communication.     # noqa: E501

        :return: The remote_port of this KvmPolicyAllOf.  # noqa: E501
        :rtype: int
        """
        return self._remote_port

    @remote_port.setter
    def remote_port(self, remote_port):
        """Sets the remote_port of this KvmPolicyAllOf.

        The port used for KVM communication.     # noqa: E501

        :param remote_port: The remote_port of this KvmPolicyAllOf.  # noqa: E501
        :type: int
        """

        self._remote_port = remote_port

    @property
    def organization(self):
        """Gets the organization of this KvmPolicyAllOf.  # noqa: E501


        :return: The organization of this KvmPolicyAllOf.  # noqa: E501
        :rtype: OrganizationOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this KvmPolicyAllOf.


        :param organization: The organization of this KvmPolicyAllOf.  # noqa: E501
        :type: OrganizationOrganization
        """

        self._organization = organization

    @property
    def profiles(self):
        """Gets the profiles of this KvmPolicyAllOf.  # noqa: E501

        A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the profile object.   # noqa: E501

        :return: The profiles of this KvmPolicyAllOf.  # noqa: E501
        :rtype: list[PolicyAbstractConfigProfile]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this KvmPolicyAllOf.

        A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the profile object.   # noqa: E501

        :param profiles: The profiles of this KvmPolicyAllOf.  # noqa: E501
        :type: list[PolicyAbstractConfigProfile]
        """

        self._profiles = profiles

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
        if not isinstance(other, KvmPolicyAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KvmPolicyAllOf):
            return True

        return self.to_dict() != other.to_dict()
