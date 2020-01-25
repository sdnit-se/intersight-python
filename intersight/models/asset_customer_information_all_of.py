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


class AssetCustomerInformationAllOf(object):
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
        'address': 'AssetAddressInformation',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {'address': 'Address', 'id': 'Id', 'name': 'Name'}

    def __init__(self,
                 address=None,
                 id=None,
                 name=None,
                 local_vars_configuration=None):  # noqa: E501
        """AssetCustomerInformationAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._id = None
        self._name = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def address(self):
        """Gets the address of this AssetCustomerInformationAllOf.  # noqa: E501


        :return: The address of this AssetCustomerInformationAllOf.  # noqa: E501
        :rtype: AssetAddressInformation
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AssetCustomerInformationAllOf.


        :param address: The address of this AssetCustomerInformationAllOf.  # noqa: E501
        :type: AssetAddressInformation
        """

        self._address = address

    @property
    def id(self):
        """Gets the id of this AssetCustomerInformationAllOf.  # noqa: E501

        Unique identifier for an end customer. This identifier is allocated by Cisco.    # noqa: E501

        :return: The id of this AssetCustomerInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AssetCustomerInformationAllOf.

        Unique identifier for an end customer. This identifier is allocated by Cisco.    # noqa: E501

        :param id: The id of this AssetCustomerInformationAllOf.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AssetCustomerInformationAllOf.  # noqa: E501

        Name as per the information provided by the user.     # noqa: E501

        :return: The name of this AssetCustomerInformationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssetCustomerInformationAllOf.

        Name as per the information provided by the user.     # noqa: E501

        :param name: The name of this AssetCustomerInformationAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, AssetCustomerInformationAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AssetCustomerInformationAllOf):
            return True

        return self.to_dict() != other.to_dict()