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


class IamIdpAllOf(object):
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
        'domain_name': 'str',
        'idp_entity_id': 'str',
        'metadata': 'str',
        'name': 'str',
        'type': 'str',
        'account': 'IamAccount',
        'system': 'IamSystem',
        'user_preferences': 'list[IamUserPreference]',
        'usergroups': 'list[IamUserGroup]',
        'users': 'list[IamUser]'
    }

    attribute_map = {
        'domain_name': 'DomainName',
        'idp_entity_id': 'IdpEntityId',
        'metadata': 'Metadata',
        'name': 'Name',
        'type': 'Type',
        'account': 'Account',
        'system': 'System',
        'user_preferences': 'UserPreferences',
        'usergroups': 'Usergroups',
        'users': 'Users'
    }

    def __init__(self,
                 domain_name=None,
                 idp_entity_id=None,
                 metadata=None,
                 name=None,
                 type='saml',
                 account=None,
                 system=None,
                 user_preferences=None,
                 usergroups=None,
                 users=None,
                 local_vars_configuration=None):  # noqa: E501
        """IamIdpAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._domain_name = None
        self._idp_entity_id = None
        self._metadata = None
        self._name = None
        self._type = None
        self._account = None
        self._system = None
        self._user_preferences = None
        self._usergroups = None
        self._users = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if idp_entity_id is not None:
            self.idp_entity_id = idp_entity_id
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if account is not None:
            self.account = account
        if system is not None:
            self.system = system
        if user_preferences is not None:
            self.user_preferences = user_preferences
        if usergroups is not None:
            self.usergroups = usergroups
        if users is not None:
            self.users = users

    @property
    def domain_name(self):
        """Gets the domain_name of this IamIdpAllOf.  # noqa: E501

        Email domain name of the user for this IdP. When a user enters an email during login in the Intersight home page, the IdP is picked by matching this domain name with the email domain name for authentication.    # noqa: E501

        :return: The domain_name of this IamIdpAllOf.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this IamIdpAllOf.

        Email domain name of the user for this IdP. When a user enters an email during login in the Intersight home page, the IdP is picked by matching this domain name with the email domain name for authentication.    # noqa: E501

        :param domain_name: The domain_name of this IamIdpAllOf.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def idp_entity_id(self):
        """Gets the idp_entity_id of this IamIdpAllOf.  # noqa: E501

        The Entity ID of the IdP. In SAML, the entity ID uniquely identifies the IdP or Service Provider.    # noqa: E501

        :return: The idp_entity_id of this IamIdpAllOf.  # noqa: E501
        :rtype: str
        """
        return self._idp_entity_id

    @idp_entity_id.setter
    def idp_entity_id(self, idp_entity_id):
        """Sets the idp_entity_id of this IamIdpAllOf.

        The Entity ID of the IdP. In SAML, the entity ID uniquely identifies the IdP or Service Provider.    # noqa: E501

        :param idp_entity_id: The idp_entity_id of this IamIdpAllOf.  # noqa: E501
        :type: str
        """

        self._idp_entity_id = idp_entity_id

    @property
    def metadata(self):
        """Gets the metadata of this IamIdpAllOf.  # noqa: E501

        SAML metadata of the IdP.    # noqa: E501

        :return: The metadata of this IamIdpAllOf.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this IamIdpAllOf.

        SAML metadata of the IdP.    # noqa: E501

        :param metadata: The metadata of this IamIdpAllOf.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this IamIdpAllOf.  # noqa: E501

        The name of the Identity Provider, for example Cisco, Okta, or OneID.    # noqa: E501

        :return: The name of this IamIdpAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IamIdpAllOf.

        The name of the Identity Provider, for example Cisco, Okta, or OneID.    # noqa: E501

        :param name: The name of this IamIdpAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this IamIdpAllOf.  # noqa: E501

        Authentication protocol used by the IdP.     # noqa: E501

        :return: The type of this IamIdpAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IamIdpAllOf.

        Authentication protocol used by the IdP.     # noqa: E501

        :param type: The type of this IamIdpAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["saml", "oidc", "local"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values))

        self._type = type

    @property
    def account(self):
        """Gets the account of this IamIdpAllOf.  # noqa: E501


        :return: The account of this IamIdpAllOf.  # noqa: E501
        :rtype: IamAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this IamIdpAllOf.


        :param account: The account of this IamIdpAllOf.  # noqa: E501
        :type: IamAccount
        """

        self._account = account

    @property
    def system(self):
        """Gets the system of this IamIdpAllOf.  # noqa: E501


        :return: The system of this IamIdpAllOf.  # noqa: E501
        :rtype: IamSystem
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this IamIdpAllOf.


        :param system: The system of this IamIdpAllOf.  # noqa: E501
        :type: IamSystem
        """

        self._system = system

    @property
    def user_preferences(self):
        """Gets the user_preferences of this IamIdpAllOf.  # noqa: E501

        A reference to a iamUserPreference resource. When the $expand query parameter is specified, the referenced resource is returned inline. The UI preference object for each user logged in through this IdP.   # noqa: E501

        :return: The user_preferences of this IamIdpAllOf.  # noqa: E501
        :rtype: list[IamUserPreference]
        """
        return self._user_preferences

    @user_preferences.setter
    def user_preferences(self, user_preferences):
        """Sets the user_preferences of this IamIdpAllOf.

        A reference to a iamUserPreference resource. When the $expand query parameter is specified, the referenced resource is returned inline. The UI preference object for each user logged in through this IdP.   # noqa: E501

        :param user_preferences: The user_preferences of this IamIdpAllOf.  # noqa: E501
        :type: list[IamUserPreference]
        """

        self._user_preferences = user_preferences

    @property
    def usergroups(self):
        """Gets the usergroups of this IamIdpAllOf.  # noqa: E501

        A reference to a iamUserGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline. User groups added in an IdP. User group provides a way to configure permission assignment for a group of users based on the IdP attributes received after authentication.   # noqa: E501

        :return: The usergroups of this IamIdpAllOf.  # noqa: E501
        :rtype: list[IamUserGroup]
        """
        return self._usergroups

    @usergroups.setter
    def usergroups(self, usergroups):
        """Sets the usergroups of this IamIdpAllOf.

        A reference to a iamUserGroup resource. When the $expand query parameter is specified, the referenced resource is returned inline. User groups added in an IdP. User group provides a way to configure permission assignment for a group of users based on the IdP attributes received after authentication.   # noqa: E501

        :param usergroups: The usergroups of this IamIdpAllOf.  # noqa: E501
        :type: list[IamUserGroup]
        """

        self._usergroups = usergroups

    @property
    def users(self):
        """Gets the users of this IamIdpAllOf.  # noqa: E501

        A reference to a iamUser resource. When the $expand query parameter is specified, the referenced resource is returned inline. Added or logged in users of an IdP who can access an Intersight account.   # noqa: E501

        :return: The users of this IamIdpAllOf.  # noqa: E501
        :rtype: list[IamUser]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this IamIdpAllOf.

        A reference to a iamUser resource. When the $expand query parameter is specified, the referenced resource is returned inline. Added or logged in users of an IdP who can access an Intersight account.   # noqa: E501

        :param users: The users of this IamIdpAllOf.  # noqa: E501
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
        if not isinstance(other, IamIdpAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IamIdpAllOf):
            return True

        return self.to_dict() != other.to_dict()
