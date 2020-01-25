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


class IamPermissionAllOf(object):
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
        'description': 'str',
        'name': 'str',
        'account': 'IamAccount',
        'end_point_roles': 'list[IamEndPointRole]',
        'resource_roles': 'list[IamResourceRoles]',
        'roles': 'list[IamRole]',
        'user_groups': 'list[IamUserGroup]',
        'users': 'list[IamUser]'
    }

    attribute_map = {
        'description': 'Description',
        'name': 'Name',
        'account': 'Account',
        'end_point_roles': 'EndPointRoles',
        'resource_roles': 'ResourceRoles',
        'roles': 'Roles',
        'user_groups': 'UserGroups',
        'users': 'Users'
    }

    def __init__(self,
                 description=None,
                 name=None,
                 account=None,
                 end_point_roles=None,
                 resource_roles=None,
                 roles=None,
                 user_groups=None,
                 users=None,
                 local_vars_configuration=None):  # noqa: E501
        """IamPermissionAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._name = None
        self._account = None
        self._end_point_roles = None
        self._resource_roles = None
        self._roles = None
        self._user_groups = None
        self._users = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if account is not None:
            self.account = account
        if end_point_roles is not None:
            self.end_point_roles = end_point_roles
        if resource_roles is not None:
            self.resource_roles = resource_roles
        if roles is not None:
            self.roles = roles
        if user_groups is not None:
            self.user_groups = user_groups
        if users is not None:
            self.users = users

    @property
    def description(self):
        """Gets the description of this IamPermissionAllOf.  # noqa: E501

        The informative description about each permission.    # noqa: E501

        :return: The description of this IamPermissionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IamPermissionAllOf.

        The informative description about each permission.    # noqa: E501

        :param description: The description of this IamPermissionAllOf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this IamPermissionAllOf.  # noqa: E501

        The name of the permission which has to be granted to user.       # noqa: E501

        :return: The name of this IamPermissionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IamPermissionAllOf.

        The name of the permission which has to be granted to user.       # noqa: E501

        :param name: The name of this IamPermissionAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def account(self):
        """Gets the account of this IamPermissionAllOf.  # noqa: E501


        :return: The account of this IamPermissionAllOf.  # noqa: E501
        :rtype: IamAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this IamPermissionAllOf.


        :param account: The account of this IamPermissionAllOf.  # noqa: E501
        :type: IamAccount
        """

        self._account = account

    @property
    def end_point_roles(self):
        """Gets the end_point_roles of this IamPermissionAllOf.  # noqa: E501

        A reference to a iamEndPointRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. The end point roles assigned to this permission. The user can perform end point operations like GUI/CLI cross launch.   # noqa: E501

        :return: The end_point_roles of this IamPermissionAllOf.  # noqa: E501
        :rtype: list[IamEndPointRole]
        """
        return self._end_point_roles

    @end_point_roles.setter
    def end_point_roles(self, end_point_roles):
        """Sets the end_point_roles of this IamPermissionAllOf.

        A reference to a iamEndPointRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. The end point roles assigned to this permission. The user can perform end point operations like GUI/CLI cross launch.   # noqa: E501

        :param end_point_roles: The end_point_roles of this IamPermissionAllOf.  # noqa: E501
        :type: list[IamEndPointRole]
        """

        self._end_point_roles = end_point_roles

    @property
    def resource_roles(self):
        """Gets the resource_roles of this IamPermissionAllOf.  # noqa: E501

        A reference to a iamResourceRoles resource. When the $expand query parameter is specified, the referenced resource is returned inline. The resource and roles assigned to this permission. Resource role specifies the organization and the collection of roles the permission has on the organization.   # noqa: E501

        :return: The resource_roles of this IamPermissionAllOf.  # noqa: E501
        :rtype: list[IamResourceRoles]
        """
        return self._resource_roles

    @resource_roles.setter
    def resource_roles(self, resource_roles):
        """Sets the resource_roles of this IamPermissionAllOf.

        A reference to a iamResourceRoles resource. When the $expand query parameter is specified, the referenced resource is returned inline. The resource and roles assigned to this permission. Resource role specifies the organization and the collection of roles the permission has on the organization.   # noqa: E501

        :param resource_roles: The resource_roles of this IamPermissionAllOf.  # noqa: E501
        :type: list[IamResourceRoles]
        """

        self._resource_roles = resource_roles

    @property
    def roles(self):
        """Gets the roles of this IamPermissionAllOf.  # noqa: E501

        A reference to a iamRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. The roles assigned to this permission. Role is a collection of privilege sets. Roles are assigned to a user using the permission object.   # noqa: E501

        :return: The roles of this IamPermissionAllOf.  # noqa: E501
        :rtype: list[IamRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this IamPermissionAllOf.

        A reference to a iamRole resource. When the $expand query parameter is specified, the referenced resource is returned inline. The roles assigned to this permission. Role is a collection of privilege sets. Roles are assigned to a user using the permission object.   # noqa: E501

        :param roles: The roles of this IamPermissionAllOf.  # noqa: E501
        :type: list[IamRole]
        """

        self._roles = roles

    @property
    def user_groups(self):
        """Gets the user_groups of this IamPermissionAllOf.  # noqa: E501

        A reference to a iamUserGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline. A collection of references to the [iam.UserGroup](mo://iam.UserGroup) Managed Object.  When this managed object is deleted, the referenced [iam.UserGroup](mo://iam.UserGroup) MOs unset their reference to this deleted MO.   # noqa: E501

        :return: The user_groups of this IamPermissionAllOf.  # noqa: E501
        :rtype: list[IamUserGroup]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """Sets the user_groups of this IamPermissionAllOf.

        A reference to a iamUserGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline. A collection of references to the [iam.UserGroup](mo://iam.UserGroup) Managed Object.  When this managed object is deleted, the referenced [iam.UserGroup](mo://iam.UserGroup) MOs unset their reference to this deleted MO.   # noqa: E501

        :param user_groups: The user_groups of this IamPermissionAllOf.  # noqa: E501
        :type: list[IamUserGroup]
        """

        self._user_groups = user_groups

    @property
    def users(self):
        """Gets the users of this IamPermissionAllOf.  # noqa: E501

        A reference to a iamUser resource. When the $expand query parameter is specified, the referenced resource is returned inline. A collection of references to the [iam.User](mo://iam.User) Managed Object.  When this managed object is deleted, the referenced [iam.User](mo://iam.User) MOs unset their reference to this deleted MO.   # noqa: E501

        :return: The users of this IamPermissionAllOf.  # noqa: E501
        :rtype: list[IamUser]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this IamPermissionAllOf.

        A reference to a iamUser resource. When the $expand query parameter is specified, the referenced resource is returned inline. A collection of references to the [iam.User](mo://iam.User) Managed Object.  When this managed object is deleted, the referenced [iam.User](mo://iam.User) MOs unset their reference to this deleted MO.   # noqa: E501

        :param users: The users of this IamPermissionAllOf.  # noqa: E501
        :type: list[IamUser]
        """

        self._users = users

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
        if not isinstance(other, IamPermissionAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IamPermissionAllOf):
            return True

        return self.to_dict() != other.to_dict()
