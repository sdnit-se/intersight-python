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


class IamLdapBaseProperties(object):
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
        'attribute': 'str',
        'base_dn': 'str',
        'bind_dn': 'str',
        'bind_method': 'str',
        'domain': 'str',
        'enable_encryption': 'bool',
        'enable_group_authorization': 'bool',
        'filter': 'str',
        'group_attribute': 'str',
        'is_password_set': 'bool',
        'nested_group_search_depth': 'int',
        'password': 'str',
        'timeout': 'int'
    }

    attribute_map = {
        'attribute': 'Attribute',
        'base_dn': 'BaseDn',
        'bind_dn': 'BindDn',
        'bind_method': 'BindMethod',
        'domain': 'Domain',
        'enable_encryption': 'EnableEncryption',
        'enable_group_authorization': 'EnableGroupAuthorization',
        'filter': 'Filter',
        'group_attribute': 'GroupAttribute',
        'is_password_set': 'IsPasswordSet',
        'nested_group_search_depth': 'NestedGroupSearchDepth',
        'password': 'Password',
        'timeout': 'Timeout'
    }

    def __init__(self,
                 attribute=None,
                 base_dn=None,
                 bind_dn=None,
                 bind_method='LoginCredentials',
                 domain=None,
                 enable_encryption=None,
                 enable_group_authorization=None,
                 filter=None,
                 group_attribute=None,
                 is_password_set=None,
                 nested_group_search_depth=None,
                 password=None,
                 timeout=None,
                 local_vars_configuration=None):  # noqa: E501
        """IamLdapBaseProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attribute = None
        self._base_dn = None
        self._bind_dn = None
        self._bind_method = None
        self._domain = None
        self._enable_encryption = None
        self._enable_group_authorization = None
        self._filter = None
        self._group_attribute = None
        self._is_password_set = None
        self._nested_group_search_depth = None
        self._password = None
        self._timeout = None
        self.discriminator = None

        if attribute is not None:
            self.attribute = attribute
        if base_dn is not None:
            self.base_dn = base_dn
        if bind_dn is not None:
            self.bind_dn = bind_dn
        if bind_method is not None:
            self.bind_method = bind_method
        if domain is not None:
            self.domain = domain
        if enable_encryption is not None:
            self.enable_encryption = enable_encryption
        if enable_group_authorization is not None:
            self.enable_group_authorization = enable_group_authorization
        if filter is not None:
            self.filter = filter
        if group_attribute is not None:
            self.group_attribute = group_attribute
        if is_password_set is not None:
            self.is_password_set = is_password_set
        if nested_group_search_depth is not None:
            self.nested_group_search_depth = nested_group_search_depth
        if password is not None:
            self.password = password
        if timeout is not None:
            self.timeout = timeout

    @property
    def attribute(self):
        """Gets the attribute of this IamLdapBaseProperties.  # noqa: E501

        Role and locale information of the user.    # noqa: E501

        :return: The attribute of this IamLdapBaseProperties.  # noqa: E501
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this IamLdapBaseProperties.

        Role and locale information of the user.    # noqa: E501

        :param attribute: The attribute of this IamLdapBaseProperties.  # noqa: E501
        :type: str
        """

        self._attribute = attribute

    @property
    def base_dn(self):
        """Gets the base_dn of this IamLdapBaseProperties.  # noqa: E501

        Base Distinguished Name (DN). Starting point from where server will search for users and groups.    # noqa: E501

        :return: The base_dn of this IamLdapBaseProperties.  # noqa: E501
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """Sets the base_dn of this IamLdapBaseProperties.

        Base Distinguished Name (DN). Starting point from where server will search for users and groups.    # noqa: E501

        :param base_dn: The base_dn of this IamLdapBaseProperties.  # noqa: E501
        :type: str
        """

        self._base_dn = base_dn

    @property
    def bind_dn(self):
        """Gets the bind_dn of this IamLdapBaseProperties.  # noqa: E501

        Distinguished Name (DN) of the user, that is used to authenticate against LDAP servers.    # noqa: E501

        :return: The bind_dn of this IamLdapBaseProperties.  # noqa: E501
        :rtype: str
        """
        return self._bind_dn

    @bind_dn.setter
    def bind_dn(self, bind_dn):
        """Sets the bind_dn of this IamLdapBaseProperties.

        Distinguished Name (DN) of the user, that is used to authenticate against LDAP servers.    # noqa: E501

        :param bind_dn: The bind_dn of this IamLdapBaseProperties.  # noqa: E501
        :type: str
        """

        self._bind_dn = bind_dn

    @property
    def bind_method(self):
        """Gets the bind_method of this IamLdapBaseProperties.  # noqa: E501

        Authentication method to access LDAP servers.    # noqa: E501

        :return: The bind_method of this IamLdapBaseProperties.  # noqa: E501
        :rtype: str
        """
        return self._bind_method

    @bind_method.setter
    def bind_method(self, bind_method):
        """Sets the bind_method of this IamLdapBaseProperties.

        Authentication method to access LDAP servers.    # noqa: E501

        :param bind_method: The bind_method of this IamLdapBaseProperties.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "LoginCredentials", "Anonymous", "ConfiguredCredentials"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and bind_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `bind_method` ({0}), must be one of {1}"  # noqa: E501
                .format(bind_method, allowed_values))

        self._bind_method = bind_method

    @property
    def domain(self):
        """Gets the domain of this IamLdapBaseProperties.  # noqa: E501

        The IPv4 domain that all users must be in.    # noqa: E501

        :return: The domain of this IamLdapBaseProperties.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this IamLdapBaseProperties.

        The IPv4 domain that all users must be in.    # noqa: E501

        :param domain: The domain of this IamLdapBaseProperties.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def enable_encryption(self):
        """Gets the enable_encryption of this IamLdapBaseProperties.  # noqa: E501

        If enabled, the endpoint encrypts all information it sends to the LDAP server.    # noqa: E501

        :return: The enable_encryption of this IamLdapBaseProperties.  # noqa: E501
        :rtype: bool
        """
        return self._enable_encryption

    @enable_encryption.setter
    def enable_encryption(self, enable_encryption):
        """Sets the enable_encryption of this IamLdapBaseProperties.

        If enabled, the endpoint encrypts all information it sends to the LDAP server.    # noqa: E501

        :param enable_encryption: The enable_encryption of this IamLdapBaseProperties.  # noqa: E501
        :type: bool
        """

        self._enable_encryption = enable_encryption

    @property
    def enable_group_authorization(self):
        """Gets the enable_group_authorization of this IamLdapBaseProperties.  # noqa: E501

        If enabled, user authorization is also done at the group level for LDAP users not in the local user database.    # noqa: E501

        :return: The enable_group_authorization of this IamLdapBaseProperties.  # noqa: E501
        :rtype: bool
        """
        return self._enable_group_authorization

    @enable_group_authorization.setter
    def enable_group_authorization(self, enable_group_authorization):
        """Sets the enable_group_authorization of this IamLdapBaseProperties.

        If enabled, user authorization is also done at the group level for LDAP users not in the local user database.    # noqa: E501

        :param enable_group_authorization: The enable_group_authorization of this IamLdapBaseProperties.  # noqa: E501
        :type: bool
        """

        self._enable_group_authorization = enable_group_authorization

    @property
    def filter(self):
        """Gets the filter of this IamLdapBaseProperties.  # noqa: E501

        Criteria to identify entries in search requests.    # noqa: E501

        :return: The filter of this IamLdapBaseProperties.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this IamLdapBaseProperties.

        Criteria to identify entries in search requests.    # noqa: E501

        :param filter: The filter of this IamLdapBaseProperties.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def group_attribute(self):
        """Gets the group_attribute of this IamLdapBaseProperties.  # noqa: E501

        Groups to which an LDAP entry belongs.    # noqa: E501

        :return: The group_attribute of this IamLdapBaseProperties.  # noqa: E501
        :rtype: str
        """
        return self._group_attribute

    @group_attribute.setter
    def group_attribute(self, group_attribute):
        """Sets the group_attribute of this IamLdapBaseProperties.

        Groups to which an LDAP entry belongs.    # noqa: E501

        :param group_attribute: The group_attribute of this IamLdapBaseProperties.  # noqa: E501
        :type: str
        """

        self._group_attribute = group_attribute

    @property
    def is_password_set(self):
        """Gets the is_password_set of this IamLdapBaseProperties.  # noqa: E501


        :return: The is_password_set of this IamLdapBaseProperties.  # noqa: E501
        :rtype: bool
        """
        return self._is_password_set

    @is_password_set.setter
    def is_password_set(self, is_password_set):
        """Sets the is_password_set of this IamLdapBaseProperties.


        :param is_password_set: The is_password_set of this IamLdapBaseProperties.  # noqa: E501
        :type: bool
        """

        self._is_password_set = is_password_set

    @property
    def nested_group_search_depth(self):
        """Gets the nested_group_search_depth of this IamLdapBaseProperties.  # noqa: E501

        Search depth to look for a nested LDAP group in an LDAP group map.    # noqa: E501

        :return: The nested_group_search_depth of this IamLdapBaseProperties.  # noqa: E501
        :rtype: int
        """
        return self._nested_group_search_depth

    @nested_group_search_depth.setter
    def nested_group_search_depth(self, nested_group_search_depth):
        """Sets the nested_group_search_depth of this IamLdapBaseProperties.

        Search depth to look for a nested LDAP group in an LDAP group map.    # noqa: E501

        :param nested_group_search_depth: The nested_group_search_depth of this IamLdapBaseProperties.  # noqa: E501
        :type: int
        """

        self._nested_group_search_depth = nested_group_search_depth

    @property
    def password(self):
        """Gets the password of this IamLdapBaseProperties.  # noqa: E501

        Password of the user, that is used to authenticate.    # noqa: E501

        :return: The password of this IamLdapBaseProperties.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this IamLdapBaseProperties.

        Password of the user, that is used to authenticate.    # noqa: E501

        :param password: The password of this IamLdapBaseProperties.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def timeout(self):
        """Gets the timeout of this IamLdapBaseProperties.  # noqa: E501

        LDAP authentication timeout duration, in seconds.     # noqa: E501

        :return: The timeout of this IamLdapBaseProperties.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this IamLdapBaseProperties.

        LDAP authentication timeout duration, in seconds.     # noqa: E501

        :param timeout: The timeout of this IamLdapBaseProperties.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

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
        if not isinstance(other, IamLdapBaseProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IamLdapBaseProperties):
            return True

        return self.to_dict() != other.to_dict()
