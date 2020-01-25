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


class PolicyConfigResultContextAllOf(object):
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
        'entity_data': 'object',
        'entity_moid': 'str',
        'entity_name': 'str',
        'entity_type': 'str'
    }

    attribute_map = {
        'entity_data': 'EntityData',
        'entity_moid': 'EntityMoid',
        'entity_name': 'EntityName',
        'entity_type': 'EntityType'
    }

    def __init__(self,
                 entity_data=None,
                 entity_moid=None,
                 entity_name=None,
                 entity_type=None,
                 local_vars_configuration=None):  # noqa: E501
        """PolicyConfigResultContextAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._entity_data = None
        self._entity_moid = None
        self._entity_name = None
        self._entity_type = None
        self.discriminator = None

        if entity_data is not None:
            self.entity_data = entity_data
        if entity_moid is not None:
            self.entity_moid = entity_moid
        if entity_name is not None:
            self.entity_name = entity_name
        if entity_type is not None:
            self.entity_type = entity_type

    @property
    def entity_data(self):
        """Gets the entity_data of this PolicyConfigResultContextAllOf.  # noqa: E501

        The data of the object present in config result context.    # noqa: E501

        :return: The entity_data of this PolicyConfigResultContextAllOf.  # noqa: E501
        :rtype: object
        """
        return self._entity_data

    @entity_data.setter
    def entity_data(self, entity_data):
        """Sets the entity_data of this PolicyConfigResultContextAllOf.

        The data of the object present in config result context.    # noqa: E501

        :param entity_data: The entity_data of this PolicyConfigResultContextAllOf.  # noqa: E501
        :type: object
        """

        self._entity_data = entity_data

    @property
    def entity_moid(self):
        """Gets the entity_moid of this PolicyConfigResultContextAllOf.  # noqa: E501

        The Moid of the object present in config result context.    # noqa: E501

        :return: The entity_moid of this PolicyConfigResultContextAllOf.  # noqa: E501
        :rtype: str
        """
        return self._entity_moid

    @entity_moid.setter
    def entity_moid(self, entity_moid):
        """Sets the entity_moid of this PolicyConfigResultContextAllOf.

        The Moid of the object present in config result context.    # noqa: E501

        :param entity_moid: The entity_moid of this PolicyConfigResultContextAllOf.  # noqa: E501
        :type: str
        """

        self._entity_moid = entity_moid

    @property
    def entity_name(self):
        """Gets the entity_name of this PolicyConfigResultContextAllOf.  # noqa: E501

        The name of the object present in config result context.    # noqa: E501

        :return: The entity_name of this PolicyConfigResultContextAllOf.  # noqa: E501
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """Sets the entity_name of this PolicyConfigResultContextAllOf.

        The name of the object present in config result context.    # noqa: E501

        :param entity_name: The entity_name of this PolicyConfigResultContextAllOf.  # noqa: E501
        :type: str
        """

        self._entity_name = entity_name

    @property
    def entity_type(self):
        """Gets the entity_type of this PolicyConfigResultContextAllOf.  # noqa: E501

        The type of the object present in config result context.     # noqa: E501

        :return: The entity_type of this PolicyConfigResultContextAllOf.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this PolicyConfigResultContextAllOf.

        The type of the object present in config result context.     # noqa: E501

        :param entity_type: The entity_type of this PolicyConfigResultContextAllOf.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

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
        if not isinstance(other, PolicyConfigResultContextAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyConfigResultContextAllOf):
            return True

        return self.to_dict() != other.to_dict()
