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


class StorageReplicationBlackout(object):
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
    openapi_types = {'end': 'str', 'start': 'str'}

    attribute_map = {'end': 'End', 'start': 'Start'}

    def __init__(self, end=None, start=None,
                 local_vars_configuration=None):  # noqa: E501
        """StorageReplicationBlackout - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._end = None
        self._start = None
        self.discriminator = None

        if end is not None:
            self.end = end
        if start is not None:
            self.start = start

    @property
    def end(self):
        """Gets the end of this StorageReplicationBlackout.  # noqa: E501

        The end time of day for replication blackout window. Example: 17:00:01 which is 17 hours, 0 minutes, 1 seconds.     # noqa: E501

        :return: The end of this StorageReplicationBlackout.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this StorageReplicationBlackout.

        The end time of day for replication blackout window. Example: 17:00:01 which is 17 hours, 0 minutes, 1 seconds.     # noqa: E501

        :param end: The end of this StorageReplicationBlackout.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def start(self):
        """Gets the start of this StorageReplicationBlackout.  # noqa: E501

        The start time of day when replication blackout is active. When replication blackout is active, the storage array temporarily disables replication. Example: 15:04:03.123 which is 15 hours, 4 minutes, 3 seconds and 123 milliseconds. The fractional seconds are written using the standard decimal notation which can be used for setting milliseconds and microseconds.      # noqa: E501

        :return: The start of this StorageReplicationBlackout.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this StorageReplicationBlackout.

        The start time of day when replication blackout is active. When replication blackout is active, the storage array temporarily disables replication. Example: 15:04:03.123 which is 15 hours, 4 minutes, 3 seconds and 123 milliseconds. The fractional seconds are written using the standard decimal notation which can be used for setting milliseconds and microseconds.      # noqa: E501

        :param start: The start of this StorageReplicationBlackout.  # noqa: E501
        :type: str
        """

        self._start = start

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
        if not isinstance(other, StorageReplicationBlackout):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageReplicationBlackout):
            return True

        return self.to_dict() != other.to_dict()
