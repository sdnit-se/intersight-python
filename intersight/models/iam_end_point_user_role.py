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


class IamEndPointUserRole(object):
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
        'change_password': 'bool',
        'enabled': 'bool',
        'is_password_set': 'bool',
        'password': 'str',
        'end_point_role': 'list[IamEndPointRole]',
        'end_point_user': 'IamEndPointUser',
        'end_point_user_policy': 'IamEndPointUserPolicy'
    }

    attribute_map = {
        'change_password': 'ChangePassword',
        'enabled': 'Enabled',
        'is_password_set': 'IsPasswordSet',
        'password': 'Password',
        'end_point_role': 'EndPointRole',
        'end_point_user': 'EndPointUser',
        'end_point_user_policy': 'EndPointUserPolicy'
    }

    def __init__(self,
                 change_password=None,
                 enabled=None,
                 is_password_set=None,
                 password=None,
                 end_point_role=None,
                 end_point_user=None,
                 end_point_user_policy=None,
                 local_vars_configuration=None):  # noqa: E501
        """IamEndPointUserRole - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._change_password = None
        self._enabled = None
        self._is_password_set = None
        self._password = None
        self._end_point_role = None
        self._end_point_user = None
        self._end_point_user_policy = None
        self.discriminator = None

        if change_password is not None:
            self.change_password = change_password
        if enabled is not None:
            self.enabled = enabled
        if is_password_set is not None:
            self.is_password_set = is_password_set
        if password is not None:
            self.password = password
        if end_point_role is not None:
            self.end_point_role = end_point_role
        if end_point_user is not None:
            self.end_point_user = end_point_user
        if end_point_user_policy is not None:
            self.end_point_user_policy = end_point_user_policy

    @property
    def change_password(self):
        """Gets the change_password of this IamEndPointUserRole.  # noqa: E501

        Denotes whether password has changed.    # noqa: E501

        :return: The change_password of this IamEndPointUserRole.  # noqa: E501
        :rtype: bool
        """
        return self._change_password

    @change_password.setter
    def change_password(self, change_password):
        """Sets the change_password of this IamEndPointUserRole.

        Denotes whether password has changed.    # noqa: E501

        :param change_password: The change_password of this IamEndPointUserRole.  # noqa: E501
        :type: bool
        """

        self._change_password = change_password

    @property
    def enabled(self):
        """Gets the enabled of this IamEndPointUserRole.  # noqa: E501

        Enables the user account on the endpoint.    # noqa: E501

        :return: The enabled of this IamEndPointUserRole.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this IamEndPointUserRole.

        Enables the user account on the endpoint.    # noqa: E501

        :param enabled: The enabled of this IamEndPointUserRole.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def is_password_set(self):
        """Gets the is_password_set of this IamEndPointUserRole.  # noqa: E501


        :return: The is_password_set of this IamEndPointUserRole.  # noqa: E501
        :rtype: bool
        """
        return self._is_password_set

    @is_password_set.setter
    def is_password_set(self, is_password_set):
        """Sets the is_password_set of this IamEndPointUserRole.


        :param is_password_set: The is_password_set of this IamEndPointUserRole.  # noqa: E501
        :type: bool
        """

        self._is_password_set = is_password_set

    @property
    def password(self):
        """Gets the password of this IamEndPointUserRole.  # noqa: E501

        Valid login password of the user.     # noqa: E501

        :return: The password of this IamEndPointUserRole.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this IamEndPointUserRole.

        Valid login password of the user.     # noqa: E501

        :param password: The password of this IamEndPointUserRole.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def end_point_role(self):
        """Gets the end_point_role of this IamEndPointUserRole.  # noqa: E501

        A reference to a iamEndPointRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. Roles.   # noqa: E501

        :return: The end_point_role of this IamEndPointUserRole.  # noqa: E501
        :rtype: list[IamEndPointRole]
        """
        return self._end_point_role

    @end_point_role.setter
    def end_point_role(self, end_point_role):
        """Sets the end_point_role of this IamEndPointUserRole.

        A reference to a iamEndPointRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. Roles.   # noqa: E501

        :param end_point_role: The end_point_role of this IamEndPointUserRole.  # noqa: E501
        :type: list[IamEndPointRole]
        """

        self._end_point_role = end_point_role

    @property
    def end_point_user(self):
        """Gets the end_point_user of this IamEndPointUserRole.  # noqa: E501


        :return: The end_point_user of this IamEndPointUserRole.  # noqa: E501
        :rtype: IamEndPointUser
        """
        return self._end_point_user

    @end_point_user.setter
    def end_point_user(self, end_point_user):
        """Sets the end_point_user of this IamEndPointUserRole.


        :param end_point_user: The end_point_user of this IamEndPointUserRole.  # noqa: E501
        :type: IamEndPointUser
        """

        self._end_point_user = end_point_user

    @property
    def end_point_user_policy(self):
        """Gets the end_point_user_policy of this IamEndPointUserRole.  # noqa: E501


        :return: The end_point_user_policy of this IamEndPointUserRole.  # noqa: E501
        :rtype: IamEndPointUserPolicy
        """
        return self._end_point_user_policy

    @end_point_user_policy.setter
    def end_point_user_policy(self, end_point_user_policy):
        """Sets the end_point_user_policy of this IamEndPointUserRole.


        :param end_point_user_policy: The end_point_user_policy of this IamEndPointUserRole.  # noqa: E501
        :type: IamEndPointUserPolicy
        """

        self._end_point_user_policy = end_point_user_policy

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
        if not isinstance(other, IamEndPointUserRole):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IamEndPointUserRole):
            return True

        return self.to_dict() != other.to_dict()
