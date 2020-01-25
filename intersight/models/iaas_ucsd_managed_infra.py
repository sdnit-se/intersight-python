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


class IaasUcsdManagedInfra(object):
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
        'advanced_catalog_count': 'int',
        'bm_catalog_count': 'int',
        'container_catalog_count': 'int',
        'esxi_host_count': 'int',
        'external_group_count': 'int',
        'hyperv_host_count': 'int',
        'local_group_count': 'int',
        'standard_catalog_count': 'int',
        'user_count': 'int',
        'vdc_count': 'int',
        'vm_count': 'int',
        'guid': 'IaasUcsdInfo'
    }

    attribute_map = {
        'advanced_catalog_count': 'AdvancedCatalogCount',
        'bm_catalog_count': 'BmCatalogCount',
        'container_catalog_count': 'ContainerCatalogCount',
        'esxi_host_count': 'EsxiHostCount',
        'external_group_count': 'ExternalGroupCount',
        'hyperv_host_count': 'HypervHostCount',
        'local_group_count': 'LocalGroupCount',
        'standard_catalog_count': 'StandardCatalogCount',
        'user_count': 'UserCount',
        'vdc_count': 'VdcCount',
        'vm_count': 'VmCount',
        'guid': 'Guid'
    }

    def __init__(self,
                 advanced_catalog_count=None,
                 bm_catalog_count=None,
                 container_catalog_count=None,
                 esxi_host_count=None,
                 external_group_count=None,
                 hyperv_host_count=None,
                 local_group_count=None,
                 standard_catalog_count=None,
                 user_count=None,
                 vdc_count=None,
                 vm_count=None,
                 guid=None,
                 local_vars_configuration=None):  # noqa: E501
        """IaasUcsdManagedInfra - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._advanced_catalog_count = None
        self._bm_catalog_count = None
        self._container_catalog_count = None
        self._esxi_host_count = None
        self._external_group_count = None
        self._hyperv_host_count = None
        self._local_group_count = None
        self._standard_catalog_count = None
        self._user_count = None
        self._vdc_count = None
        self._vm_count = None
        self._guid = None
        self.discriminator = None

        if advanced_catalog_count is not None:
            self.advanced_catalog_count = advanced_catalog_count
        if bm_catalog_count is not None:
            self.bm_catalog_count = bm_catalog_count
        if container_catalog_count is not None:
            self.container_catalog_count = container_catalog_count
        if esxi_host_count is not None:
            self.esxi_host_count = esxi_host_count
        if external_group_count is not None:
            self.external_group_count = external_group_count
        if hyperv_host_count is not None:
            self.hyperv_host_count = hyperv_host_count
        if local_group_count is not None:
            self.local_group_count = local_group_count
        if standard_catalog_count is not None:
            self.standard_catalog_count = standard_catalog_count
        if user_count is not None:
            self.user_count = user_count
        if vdc_count is not None:
            self.vdc_count = vdc_count
        if vm_count is not None:
            self.vm_count = vm_count
        if guid is not None:
            self.guid = guid

    @property
    def advanced_catalog_count(self):
        """Gets the advanced_catalog_count of this IaasUcsdManagedInfra.  # noqa: E501

        Total advanced catalogs in UCSD.    # noqa: E501

        :return: The advanced_catalog_count of this IaasUcsdManagedInfra.  # noqa: E501
        :rtype: int
        """
        return self._advanced_catalog_count

    @advanced_catalog_count.setter
    def advanced_catalog_count(self, advanced_catalog_count):
        """Sets the advanced_catalog_count of this IaasUcsdManagedInfra.

        Total advanced catalogs in UCSD.    # noqa: E501

        :param advanced_catalog_count: The advanced_catalog_count of this IaasUcsdManagedInfra.  # noqa: E501
        :type: int
        """

        self._advanced_catalog_count = advanced_catalog_count

    @property
    def bm_catalog_count(self):
        """Gets the bm_catalog_count of this IaasUcsdManagedInfra.  # noqa: E501

        Total bare metal catalogs in UCSD.    # noqa: E501

        :return: The bm_catalog_count of this IaasUcsdManagedInfra.  # noqa: E501
        :rtype: int
        """
        return self._bm_catalog_count

    @bm_catalog_count.setter
    def bm_catalog_count(self, bm_catalog_count):
        """Sets the bm_catalog_count of this IaasUcsdManagedInfra.

        Total bare metal catalogs in UCSD.    # noqa: E501

        :param bm_catalog_count: The bm_catalog_count of this IaasUcsdManagedInfra.  # noqa: E501
        :type: int
        """

        self._bm_catalog_count = bm_catalog_count

    @property
    def container_catalog_count(self):
        """Gets the container_catalog_count of this IaasUcsdManagedInfra.  # noqa: E501

        Total service container catalogs in UCSD.    # noqa: E501

        :return: The container_catalog_count of this IaasUcsdManagedInfra.  # noqa: E501
        :rtype: int
        """
        return self._container_catalog_count

    @container_catalog_count.setter
    def container_catalog_count(self, container_catalog_count):
        """Sets the container_catalog_count of this IaasUcsdManagedInfra.

        Total service container catalogs in UCSD.    # noqa: E501

        :param container_catalog_count: The container_catalog_count of this IaasUcsdManagedInfra.  # noqa: E501
        :type: int
        """

        self._container_catalog_count = container_catalog_count

    @property
    def esxi_host_count(self):
        """Gets the esxi_host_count of this IaasUcsdManagedInfra.  # noqa: E501

        Total ESXi hosts in UCSD.    # noqa: E501

        :return: The esxi_host_count of this IaasUcsdManagedInfra.  # noqa: E501
        :rtype: int
        """
        return self._esxi_host_count

    @esxi_host_count.setter
    def esxi_host_count(self, esxi_host_count):
        """Sets the esxi_host_count of this IaasUcsdManagedInfra.

        Total ESXi hosts in UCSD.    # noqa: E501

        :param esxi_host_count: The esxi_host_count of this IaasUcsdManagedInfra.  # noqa: E501
        :type: int
        """

        self._esxi_host_count = esxi_host_count

    @property
    def external_group_count(self):
        """Gets the external_group_count of this IaasUcsdManagedInfra.  # noqa: E501

        Total external (Ldap) groups in UCSD.    # noqa: E501

        :return: The external_group_count of this IaasUcsdManagedInfra.  # noqa: E501
        :rtype: int
        """
        return self._external_group_count

    @external_group_count.setter
    def external_group_count(self, external_group_count):
        """Sets the external_group_count of this IaasUcsdManagedInfra.

        Total external (Ldap) groups in UCSD.    # noqa: E501

        :param external_group_count: The external_group_count of this IaasUcsdManagedInfra.  # noqa: E501
        :type: int
        """

        self._external_group_count = external_group_count

    @property
    def hyperv_host_count(self):
        """Gets the hyperv_host_count of this IaasUcsdManagedInfra.  # noqa: E501

        Total HyperV hosts in UCSD.    # noqa: E501

        :return: The hyperv_host_count of this IaasUcsdManagedInfra.  # noqa: E501
        :rtype: int
        """
        return self._hyperv_host_count

    @hyperv_host_count.setter
    def hyperv_host_count(self, hyperv_host_count):
        """Sets the hyperv_host_count of this IaasUcsdManagedInfra.

        Total HyperV hosts in UCSD.    # noqa: E501

        :param hyperv_host_count: The hyperv_host_count of this IaasUcsdManagedInfra.  # noqa: E501
        :type: int
        """

        self._hyperv_host_count = hyperv_host_count

    @property
    def local_group_count(self):
        """Gets the local_group_count of this IaasUcsdManagedInfra.  # noqa: E501

        Total local groups in UCSD.    # noqa: E501

        :return: The local_group_count of this IaasUcsdManagedInfra.  # noqa: E501
        :rtype: int
        """
        return self._local_group_count

    @local_group_count.setter
    def local_group_count(self, local_group_count):
        """Sets the local_group_count of this IaasUcsdManagedInfra.

        Total local groups in UCSD.    # noqa: E501

        :param local_group_count: The local_group_count of this IaasUcsdManagedInfra.  # noqa: E501
        :type: int
        """

        self._local_group_count = local_group_count

    @property
    def standard_catalog_count(self):
        """Gets the standard_catalog_count of this IaasUcsdManagedInfra.  # noqa: E501

        Total standard catalogs in UCSD.    # noqa: E501

        :return: The standard_catalog_count of this IaasUcsdManagedInfra.  # noqa: E501
        :rtype: int
        """
        return self._standard_catalog_count

    @standard_catalog_count.setter
    def standard_catalog_count(self, standard_catalog_count):
        """Sets the standard_catalog_count of this IaasUcsdManagedInfra.

        Total standard catalogs in UCSD.    # noqa: E501

        :param standard_catalog_count: The standard_catalog_count of this IaasUcsdManagedInfra.  # noqa: E501
        :type: int
        """

        self._standard_catalog_count = standard_catalog_count

    @property
    def user_count(self):
        """Gets the user_count of this IaasUcsdManagedInfra.  # noqa: E501

        Total user accounts in UCSD.    # noqa: E501

        :return: The user_count of this IaasUcsdManagedInfra.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this IaasUcsdManagedInfra.

        Total user accounts in UCSD.    # noqa: E501

        :param user_count: The user_count of this IaasUcsdManagedInfra.  # noqa: E501
        :type: int
        """

        self._user_count = user_count

    @property
    def vdc_count(self):
        """Gets the vdc_count of this IaasUcsdManagedInfra.  # noqa: E501

        Total virtual datacenters in UCSD.    # noqa: E501

        :return: The vdc_count of this IaasUcsdManagedInfra.  # noqa: E501
        :rtype: int
        """
        return self._vdc_count

    @vdc_count.setter
    def vdc_count(self, vdc_count):
        """Sets the vdc_count of this IaasUcsdManagedInfra.

        Total virtual datacenters in UCSD.    # noqa: E501

        :param vdc_count: The vdc_count of this IaasUcsdManagedInfra.  # noqa: E501
        :type: int
        """

        self._vdc_count = vdc_count

    @property
    def vm_count(self):
        """Gets the vm_count of this IaasUcsdManagedInfra.  # noqa: E501

        Total Virtual machines in UCSD.     # noqa: E501

        :return: The vm_count of this IaasUcsdManagedInfra.  # noqa: E501
        :rtype: int
        """
        return self._vm_count

    @vm_count.setter
    def vm_count(self, vm_count):
        """Sets the vm_count of this IaasUcsdManagedInfra.

        Total Virtual machines in UCSD.     # noqa: E501

        :param vm_count: The vm_count of this IaasUcsdManagedInfra.  # noqa: E501
        :type: int
        """

        self._vm_count = vm_count

    @property
    def guid(self):
        """Gets the guid of this IaasUcsdManagedInfra.  # noqa: E501


        :return: The guid of this IaasUcsdManagedInfra.  # noqa: E501
        :rtype: IaasUcsdInfo
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this IaasUcsdManagedInfra.


        :param guid: The guid of this IaasUcsdManagedInfra.  # noqa: E501
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
        if not isinstance(other, IaasUcsdManagedInfra):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IaasUcsdManagedInfra):
            return True

        return self.to_dict() != other.to_dict()
