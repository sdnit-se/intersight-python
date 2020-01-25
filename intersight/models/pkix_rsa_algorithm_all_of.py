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


class PkixRsaAlgorithmAllOf(object):
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
    openapi_types = {'modulus': 'int'}

    attribute_map = {'modulus': 'Modulus'}

    def __init__(self, modulus=2048,
                 local_vars_configuration=None):  # noqa: E501
        """PkixRsaAlgorithmAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._modulus = None
        self.discriminator = None

        if modulus is not None:
            self.modulus = modulus

    @property
    def modulus(self):
        """Gets the modulus of this PkixRsaAlgorithmAllOf.  # noqa: E501

        The length of the RSA key, expressed in bits, for both public and private keys.     # noqa: E501

        :return: The modulus of this PkixRsaAlgorithmAllOf.  # noqa: E501
        :rtype: int
        """
        return self._modulus

    @modulus.setter
    def modulus(self, modulus):
        """Sets the modulus of this PkixRsaAlgorithmAllOf.

        The length of the RSA key, expressed in bits, for both public and private keys.     # noqa: E501

        :param modulus: The modulus of this PkixRsaAlgorithmAllOf.  # noqa: E501
        :type: int
        """
        allowed_values = [2048, 2560, 3072, 3584, 4096]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and modulus not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `modulus` ({0}), must be one of {1}"  # noqa: E501
                .format(modulus, allowed_values))

        self._modulus = modulus

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
        if not isinstance(other, PkixRsaAlgorithmAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PkixRsaAlgorithmAllOf):
            return True

        return self.to_dict() != other.to_dict()
