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


class RecoveryRestoreAllOf(object):
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
        'config_params': 'RecoveryConfigParams',
        'backup_info': 'RecoveryAbstractBackupInfo',
        'device': 'AssetDeviceRegistration',
        'organization': 'OrganizationOrganization',
        'workflow': 'WorkflowWorkflowInfo'
    }

    attribute_map = {
        'config_params': 'ConfigParams',
        'backup_info': 'BackupInfo',
        'device': 'Device',
        'organization': 'Organization',
        'workflow': 'Workflow'
    }

    def __init__(self,
                 config_params=None,
                 backup_info=None,
                 device=None,
                 organization=None,
                 workflow=None,
                 local_vars_configuration=None):  # noqa: E501
        """RecoveryRestoreAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._config_params = None
        self._backup_info = None
        self._device = None
        self._organization = None
        self._workflow = None
        self.discriminator = None

        if config_params is not None:
            self.config_params = config_params
        if backup_info is not None:
            self.backup_info = backup_info
        if device is not None:
            self.device = device
        if organization is not None:
            self.organization = organization
        if workflow is not None:
            self.workflow = workflow

    @property
    def config_params(self):
        """Gets the config_params of this RecoveryRestoreAllOf.  # noqa: E501


        :return: The config_params of this RecoveryRestoreAllOf.  # noqa: E501
        :rtype: RecoveryConfigParams
        """
        return self._config_params

    @config_params.setter
    def config_params(self, config_params):
        """Sets the config_params of this RecoveryRestoreAllOf.


        :param config_params: The config_params of this RecoveryRestoreAllOf.  # noqa: E501
        :type: RecoveryConfigParams
        """

        self._config_params = config_params

    @property
    def backup_info(self):
        """Gets the backup_info of this RecoveryRestoreAllOf.  # noqa: E501


        :return: The backup_info of this RecoveryRestoreAllOf.  # noqa: E501
        :rtype: RecoveryAbstractBackupInfo
        """
        return self._backup_info

    @backup_info.setter
    def backup_info(self, backup_info):
        """Sets the backup_info of this RecoveryRestoreAllOf.


        :param backup_info: The backup_info of this RecoveryRestoreAllOf.  # noqa: E501
        :type: RecoveryAbstractBackupInfo
        """

        self._backup_info = backup_info

    @property
    def device(self):
        """Gets the device of this RecoveryRestoreAllOf.  # noqa: E501


        :return: The device of this RecoveryRestoreAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this RecoveryRestoreAllOf.


        :param device: The device of this RecoveryRestoreAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._device = device

    @property
    def organization(self):
        """Gets the organization of this RecoveryRestoreAllOf.  # noqa: E501


        :return: The organization of this RecoveryRestoreAllOf.  # noqa: E501
        :rtype: OrganizationOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this RecoveryRestoreAllOf.


        :param organization: The organization of this RecoveryRestoreAllOf.  # noqa: E501
        :type: OrganizationOrganization
        """

        self._organization = organization

    @property
    def workflow(self):
        """Gets the workflow of this RecoveryRestoreAllOf.  # noqa: E501


        :return: The workflow of this RecoveryRestoreAllOf.  # noqa: E501
        :rtype: WorkflowWorkflowInfo
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this RecoveryRestoreAllOf.


        :param workflow: The workflow of this RecoveryRestoreAllOf.  # noqa: E501
        :type: WorkflowWorkflowInfo
        """

        self._workflow = workflow

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
        if not isinstance(other, RecoveryRestoreAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecoveryRestoreAllOf):
            return True

        return self.to_dict() != other.to_dict()
