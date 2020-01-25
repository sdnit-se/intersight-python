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


class PolicyinventoryJobInfoAllOf(object):
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
        'execution_status': 'str',
        'last_scheduled_time': 'datetime',
        'policy_id': 'str',
        'policy_name': 'str'
    }

    attribute_map = {
        'execution_status': 'ExecutionStatus',
        'last_scheduled_time': 'LastScheduledTime',
        'policy_id': 'PolicyId',
        'policy_name': 'PolicyName'
    }

    def __init__(self,
                 execution_status='Scheduled',
                 last_scheduled_time=None,
                 policy_id=None,
                 policy_name=None,
                 local_vars_configuration=None):  # noqa: E501
        """PolicyinventoryJobInfoAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._execution_status = None
        self._last_scheduled_time = None
        self._policy_id = None
        self._policy_name = None
        self.discriminator = None

        if execution_status is not None:
            self.execution_status = execution_status
        if last_scheduled_time is not None:
            self.last_scheduled_time = last_scheduled_time
        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name

    @property
    def execution_status(self):
        """Gets the execution_status of this PolicyinventoryJobInfoAllOf.  # noqa: E501

        Execution status of the inventory job.    # noqa: E501

        :return: The execution_status of this PolicyinventoryJobInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._execution_status

    @execution_status.setter
    def execution_status(self, execution_status):
        """Sets the execution_status of this PolicyinventoryJobInfoAllOf.

        Execution status of the inventory job.    # noqa: E501

        :param execution_status: The execution_status of this PolicyinventoryJobInfoAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Scheduled", "Completed", "Error"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and execution_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `execution_status` ({0}), must be one of {1}"  # noqa: E501
                .format(execution_status, allowed_values))

        self._execution_status = execution_status

    @property
    def last_scheduled_time(self):
        """Gets the last_scheduled_time of this PolicyinventoryJobInfoAllOf.  # noqa: E501

        Last scheduled time of the inventory job.    # noqa: E501

        :return: The last_scheduled_time of this PolicyinventoryJobInfoAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._last_scheduled_time

    @last_scheduled_time.setter
    def last_scheduled_time(self, last_scheduled_time):
        """Sets the last_scheduled_time of this PolicyinventoryJobInfoAllOf.

        Last scheduled time of the inventory job.    # noqa: E501

        :param last_scheduled_time: The last_scheduled_time of this PolicyinventoryJobInfoAllOf.  # noqa: E501
        :type: datetime
        """

        self._last_scheduled_time = last_scheduled_time

    @property
    def policy_id(self):
        """Gets the policy_id of this PolicyinventoryJobInfoAllOf.  # noqa: E501

        Policy ID for the inventory job.    # noqa: E501

        :return: The policy_id of this PolicyinventoryJobInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this PolicyinventoryJobInfoAllOf.

        Policy ID for the inventory job.    # noqa: E501

        :param policy_id: The policy_id of this PolicyinventoryJobInfoAllOf.  # noqa: E501
        :type: str
        """

        self._policy_id = policy_id

    @property
    def policy_name(self):
        """Gets the policy_name of this PolicyinventoryJobInfoAllOf.  # noqa: E501

        Policy name for the inventory job.     # noqa: E501

        :return: The policy_name of this PolicyinventoryJobInfoAllOf.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this PolicyinventoryJobInfoAllOf.

        Policy name for the inventory job.     # noqa: E501

        :param policy_name: The policy_name of this PolicyinventoryJobInfoAllOf.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

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
        if not isinstance(other, PolicyinventoryJobInfoAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyinventoryJobInfoAllOf):
            return True

        return self.to_dict() != other.to_dict()
