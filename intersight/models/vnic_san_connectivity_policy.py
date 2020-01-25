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


class VnicSanConnectivityPolicy(object):
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
        'fc_ifs': 'list[VnicFcIf]',
        'organization': 'OrganizationOrganization',
        'profiles': 'list[PolicyAbstractConfigProfile]'
    }

    attribute_map = {
        'fc_ifs': 'FcIfs',
        'organization': 'Organization',
        'profiles': 'Profiles'
    }

    def __init__(self,
                 fc_ifs=None,
                 organization=None,
                 profiles=None,
                 local_vars_configuration=None):  # noqa: E501
        """VnicSanConnectivityPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._fc_ifs = None
        self._organization = None
        self._profiles = None
        self.discriminator = None

        if fc_ifs is not None:
            self.fc_ifs = fc_ifs
        if organization is not None:
            self.organization = organization
        if profiles is not None:
            self.profiles = profiles

    @property
    def fc_ifs(self):
        """Gets the fc_ifs of this VnicSanConnectivityPolicy.  # noqa: E501

        A reference to a vnicFcIf resource. When the $expand query parameter is specified, the referenced resource is returned inline. A collection of references to the [vnic.FcIf](mo://vnic.FcIf) Managed Object.  When this managed object is deleted, the referenced [vnic.FcIf](mo://vnic.FcIf) MOs on the other side of the relationship are deleted.   # noqa: E501

        :return: The fc_ifs of this VnicSanConnectivityPolicy.  # noqa: E501
        :rtype: list[VnicFcIf]
        """
        return self._fc_ifs

    @fc_ifs.setter
    def fc_ifs(self, fc_ifs):
        """Sets the fc_ifs of this VnicSanConnectivityPolicy.

        A reference to a vnicFcIf resource. When the $expand query parameter is specified, the referenced resource is returned inline. A collection of references to the [vnic.FcIf](mo://vnic.FcIf) Managed Object.  When this managed object is deleted, the referenced [vnic.FcIf](mo://vnic.FcIf) MOs on the other side of the relationship are deleted.   # noqa: E501

        :param fc_ifs: The fc_ifs of this VnicSanConnectivityPolicy.  # noqa: E501
        :type: list[VnicFcIf]
        """

        self._fc_ifs = fc_ifs

    @property
    def organization(self):
        """Gets the organization of this VnicSanConnectivityPolicy.  # noqa: E501


        :return: The organization of this VnicSanConnectivityPolicy.  # noqa: E501
        :rtype: OrganizationOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this VnicSanConnectivityPolicy.


        :param organization: The organization of this VnicSanConnectivityPolicy.  # noqa: E501
        :type: OrganizationOrganization
        """

        self._organization = organization

    @property
    def profiles(self):
        """Gets the profiles of this VnicSanConnectivityPolicy.  # noqa: E501

        A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the server profile.   # noqa: E501

        :return: The profiles of this VnicSanConnectivityPolicy.  # noqa: E501
        :rtype: list[PolicyAbstractConfigProfile]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this VnicSanConnectivityPolicy.

        A reference to a policyAbstractConfigProfile resource. When the $expand query parameter is specified, the referenced resource is returned inline. Relationship to the server profile.   # noqa: E501

        :param profiles: The profiles of this VnicSanConnectivityPolicy.  # noqa: E501
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
        if not isinstance(other, VnicSanConnectivityPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VnicSanConnectivityPolicy):
            return True

        return self.to_dict() != other.to_dict()
