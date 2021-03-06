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


class IaasLicenseInfoAllOf(object):
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
        'license_expiration_date': 'str',
        'license_keys_info': 'list[IaasLicenseKeysInfo]',
        'license_type': 'str',
        'license_utilization_info': 'list[IaasLicenseUtilizationInfo]',
        'guid': 'IaasUcsdInfo'
    }

    attribute_map = {
        'license_expiration_date': 'LicenseExpirationDate',
        'license_keys_info': 'LicenseKeysInfo',
        'license_type': 'LicenseType',
        'license_utilization_info': 'LicenseUtilizationInfo',
        'guid': 'Guid'
    }

    def __init__(self,
                 license_expiration_date=None,
                 license_keys_info=None,
                 license_type=None,
                 license_utilization_info=None,
                 guid=None,
                 local_vars_configuration=None):  # noqa: E501
        """IaasLicenseInfoAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._license_expiration_date = None
        self._license_keys_info = None
        self._license_type = None
        self._license_utilization_info = None
        self._guid = None
        self.discriminator = None

        if license_expiration_date is not None:
            self.license_expiration_date = license_expiration_date
        if license_keys_info is not None:
            self.license_keys_info = license_keys_info
        if license_type is not None:
            self.license_type = license_type
        if license_utilization_info is not None:
            self.license_utilization_info = license_utilization_info
        if guid is not None:
            self.guid = guid

    @property
    def license_expiration_date(self):
        """Gets the license_expiration_date of this IaasLicenseInfoAllOf.  # noqa: E501

        Licese expiration date.    # noqa: E501

        :return: The license_expiration_date of this IaasLicenseInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._license_expiration_date

    @license_expiration_date.setter
    def license_expiration_date(self, license_expiration_date):
        """Sets the license_expiration_date of this IaasLicenseInfoAllOf.

        Licese expiration date.    # noqa: E501

        :param license_expiration_date: The license_expiration_date of this IaasLicenseInfoAllOf.  # noqa: E501
        :type: str
        """

        self._license_expiration_date = license_expiration_date

    @property
    def license_keys_info(self):
        """Gets the license_keys_info of this IaasLicenseInfoAllOf.  # noqa: E501


        :return: The license_keys_info of this IaasLicenseInfoAllOf.  # noqa: E501
        :rtype: list[IaasLicenseKeysInfo]
        """
        return self._license_keys_info

    @license_keys_info.setter
    def license_keys_info(self, license_keys_info):
        """Sets the license_keys_info of this IaasLicenseInfoAllOf.


        :param license_keys_info: The license_keys_info of this IaasLicenseInfoAllOf.  # noqa: E501
        :type: list[IaasLicenseKeysInfo]
        """

        self._license_keys_info = license_keys_info

    @property
    def license_type(self):
        """Gets the license_type of this IaasLicenseInfoAllOf.  # noqa: E501

        License type of UCSD whether it is EVAL/Permanent/Subscription..    # noqa: E501

        :return: The license_type of this IaasLicenseInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """Sets the license_type of this IaasLicenseInfoAllOf.

        License type of UCSD whether it is EVAL/Permanent/Subscription..    # noqa: E501

        :param license_type: The license_type of this IaasLicenseInfoAllOf.  # noqa: E501
        :type: str
        """

        self._license_type = license_type

    @property
    def license_utilization_info(self):
        """Gets the license_utilization_info of this IaasLicenseInfoAllOf.  # noqa: E501


        :return: The license_utilization_info of this IaasLicenseInfoAllOf.  # noqa: E501
        :rtype: list[IaasLicenseUtilizationInfo]
        """
        return self._license_utilization_info

    @license_utilization_info.setter
    def license_utilization_info(self, license_utilization_info):
        """Sets the license_utilization_info of this IaasLicenseInfoAllOf.


        :param license_utilization_info: The license_utilization_info of this IaasLicenseInfoAllOf.  # noqa: E501
        :type: list[IaasLicenseUtilizationInfo]
        """

        self._license_utilization_info = license_utilization_info

    @property
    def guid(self):
        """Gets the guid of this IaasLicenseInfoAllOf.  # noqa: E501


        :return: The guid of this IaasLicenseInfoAllOf.  # noqa: E501
        :rtype: IaasUcsdInfo
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this IaasLicenseInfoAllOf.


        :param guid: The guid of this IaasLicenseInfoAllOf.  # noqa: E501
        :type: IaasUcsdInfo
        """

        self._guid = guid

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
        if not isinstance(other, IaasLicenseInfoAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IaasLicenseInfoAllOf):
            return True

        return self.to_dict() != other.to_dict()
