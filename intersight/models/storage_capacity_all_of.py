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


class StorageCapacityAllOf(object):
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
        'available': 'int',
        'free': 'int',
        'total': 'int',
        'used': 'int'
    }

    attribute_map = {
        'available': 'Available',
        'free': 'Free',
        'total': 'Total',
        'used': 'Used'
    }

    def __init__(self,
                 available=None,
                 free=None,
                 total=None,
                 used=None,
                 local_vars_configuration=None):  # noqa: E501
        """StorageCapacityAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._available = None
        self._free = None
        self._total = None
        self._used = None
        self.discriminator = None

        if available is not None:
            self.available = available
        if free is not None:
            self.free = free
        if total is not None:
            self.total = total
        if used is not None:
            self.used = used

    @property
    def available(self):
        """Gets the available of this StorageCapacityAllOf.  # noqa: E501

        Total consumable storage capacity represented in bytes. System may reserve some space for internal purpose which is excluded from total capacity.    # noqa: E501

        :return: The available of this StorageCapacityAllOf.  # noqa: E501
        :rtype: int
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this StorageCapacityAllOf.

        Total consumable storage capacity represented in bytes. System may reserve some space for internal purpose which is excluded from total capacity.    # noqa: E501

        :param available: The available of this StorageCapacityAllOf.  # noqa: E501
        :type: int
        """

        self._available = available

    @property
    def free(self):
        """Gets the free of this StorageCapacityAllOf.  # noqa: E501

        Unused space available for user to consume, represented in bytes.    # noqa: E501

        :return: The free of this StorageCapacityAllOf.  # noqa: E501
        :rtype: int
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this StorageCapacityAllOf.

        Unused space available for user to consume, represented in bytes.    # noqa: E501

        :param free: The free of this StorageCapacityAllOf.  # noqa: E501
        :type: int
        """

        self._free = free

    @property
    def total(self):
        """Gets the total of this StorageCapacityAllOf.  # noqa: E501

        Total storage capacity, represented in bytes. It is set by the component manufacture.    # noqa: E501

        :return: The total of this StorageCapacityAllOf.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this StorageCapacityAllOf.

        Total storage capacity, represented in bytes. It is set by the component manufacture.    # noqa: E501

        :param total: The total of this StorageCapacityAllOf.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def used(self):
        """Gets the used of this StorageCapacityAllOf.  # noqa: E501

        Used or consumed storage capacity, represented in bytes.     # noqa: E501

        :return: The used of this StorageCapacityAllOf.  # noqa: E501
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this StorageCapacityAllOf.

        Used or consumed storage capacity, represented in bytes.     # noqa: E501

        :param used: The used of this StorageCapacityAllOf.  # noqa: E501
        :type: int
        """

        self._used = used

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
        if not isinstance(other, StorageCapacityAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageCapacityAllOf):
            return True

        return self.to_dict() != other.to_dict()
