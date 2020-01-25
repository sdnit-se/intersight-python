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


class VnicFcErrorRecoverySettings(object):
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
        'enabled': 'bool',
        'io_retry_count': 'int',
        'io_retry_timeout': 'int',
        'link_down_timeout': 'int',
        'port_down_timeout': 'int'
    }

    attribute_map = {
        'enabled': 'Enabled',
        'io_retry_count': 'IoRetryCount',
        'io_retry_timeout': 'IoRetryTimeout',
        'link_down_timeout': 'LinkDownTimeout',
        'port_down_timeout': 'PortDownTimeout'
    }

    def __init__(self,
                 enabled=None,
                 io_retry_count=None,
                 io_retry_timeout=None,
                 link_down_timeout=None,
                 port_down_timeout=None,
                 local_vars_configuration=None):  # noqa: E501
        """VnicFcErrorRecoverySettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enabled = None
        self._io_retry_count = None
        self._io_retry_timeout = None
        self._link_down_timeout = None
        self._port_down_timeout = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if io_retry_count is not None:
            self.io_retry_count = io_retry_count
        if io_retry_timeout is not None:
            self.io_retry_timeout = io_retry_timeout
        if link_down_timeout is not None:
            self.link_down_timeout = link_down_timeout
        if port_down_timeout is not None:
            self.port_down_timeout = port_down_timeout

    @property
    def enabled(self):
        """Gets the enabled of this VnicFcErrorRecoverySettings.  # noqa: E501

        Enables Fibre Channel Error recovery.    # noqa: E501

        :return: The enabled of this VnicFcErrorRecoverySettings.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this VnicFcErrorRecoverySettings.

        Enables Fibre Channel Error recovery.    # noqa: E501

        :param enabled: The enabled of this VnicFcErrorRecoverySettings.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def io_retry_count(self):
        """Gets the io_retry_count of this VnicFcErrorRecoverySettings.  # noqa: E501

        The number of times an I/O request to a port is retried because the port is busy before the system decides the port is unavailable.    # noqa: E501

        :return: The io_retry_count of this VnicFcErrorRecoverySettings.  # noqa: E501
        :rtype: int
        """
        return self._io_retry_count

    @io_retry_count.setter
    def io_retry_count(self, io_retry_count):
        """Sets the io_retry_count of this VnicFcErrorRecoverySettings.

        The number of times an I/O request to a port is retried because the port is busy before the system decides the port is unavailable.    # noqa: E501

        :param io_retry_count: The io_retry_count of this VnicFcErrorRecoverySettings.  # noqa: E501
        :type: int
        """

        self._io_retry_count = io_retry_count

    @property
    def io_retry_timeout(self):
        """Gets the io_retry_timeout of this VnicFcErrorRecoverySettings.  # noqa: E501

        The number of seconds the adapter waits before aborting the pending command and resending the same IO request.    # noqa: E501

        :return: The io_retry_timeout of this VnicFcErrorRecoverySettings.  # noqa: E501
        :rtype: int
        """
        return self._io_retry_timeout

    @io_retry_timeout.setter
    def io_retry_timeout(self, io_retry_timeout):
        """Sets the io_retry_timeout of this VnicFcErrorRecoverySettings.

        The number of seconds the adapter waits before aborting the pending command and resending the same IO request.    # noqa: E501

        :param io_retry_timeout: The io_retry_timeout of this VnicFcErrorRecoverySettings.  # noqa: E501
        :type: int
        """

        self._io_retry_timeout = io_retry_timeout

    @property
    def link_down_timeout(self):
        """Gets the link_down_timeout of this VnicFcErrorRecoverySettings.  # noqa: E501

        The number of milliseconds the port should actually be down before it is marked down and fabric connectivity is lost.    # noqa: E501

        :return: The link_down_timeout of this VnicFcErrorRecoverySettings.  # noqa: E501
        :rtype: int
        """
        return self._link_down_timeout

    @link_down_timeout.setter
    def link_down_timeout(self, link_down_timeout):
        """Sets the link_down_timeout of this VnicFcErrorRecoverySettings.

        The number of milliseconds the port should actually be down before it is marked down and fabric connectivity is lost.    # noqa: E501

        :param link_down_timeout: The link_down_timeout of this VnicFcErrorRecoverySettings.  # noqa: E501
        :type: int
        """

        self._link_down_timeout = link_down_timeout

    @property
    def port_down_timeout(self):
        """Gets the port_down_timeout of this VnicFcErrorRecoverySettings.  # noqa: E501

        The number of milliseconds a remote Fibre Channel port should be offline before informing the SCSI upper layer that the port is unavailable. For a server with a VIC adapter running ESXi, the recommended value is 10000. For a server with a port used to boot a Windows OS from the SAN, the recommended value is 5000 milliseconds.     # noqa: E501

        :return: The port_down_timeout of this VnicFcErrorRecoverySettings.  # noqa: E501
        :rtype: int
        """
        return self._port_down_timeout

    @port_down_timeout.setter
    def port_down_timeout(self, port_down_timeout):
        """Sets the port_down_timeout of this VnicFcErrorRecoverySettings.

        The number of milliseconds a remote Fibre Channel port should be offline before informing the SCSI upper layer that the port is unavailable. For a server with a VIC adapter running ESXi, the recommended value is 10000. For a server with a port used to boot a Windows OS from the SAN, the recommended value is 5000 milliseconds.     # noqa: E501

        :param port_down_timeout: The port_down_timeout of this VnicFcErrorRecoverySettings.  # noqa: E501
        :type: int
        """

        self._port_down_timeout = port_down_timeout

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
        if not isinstance(other, VnicFcErrorRecoverySettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VnicFcErrorRecoverySettings):
            return True

        return self.to_dict() != other.to_dict()
