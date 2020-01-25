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


class IamPrivilegeAllOf(object):
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
        'hostname_prefix': 'str',
        'method': 'str',
        'name': 'str',
        'rest_path': 'str',
        'url_prefix': 'str',
        'account': 'IamAccount',
        'system': 'IamSystem'
    }

    attribute_map = {
        'hostname_prefix': 'HostnamePrefix',
        'method': 'Method',
        'name': 'Name',
        'rest_path': 'RestPath',
        'url_prefix': 'UrlPrefix',
        'account': 'Account',
        'system': 'System'
    }

    def __init__(self,
                 hostname_prefix=None,
                 method=None,
                 name=None,
                 rest_path=None,
                 url_prefix=None,
                 account=None,
                 system=None,
                 local_vars_configuration=None):  # noqa: E501
        """IamPrivilegeAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hostname_prefix = None
        self._method = None
        self._name = None
        self._rest_path = None
        self._url_prefix = None
        self._account = None
        self._system = None
        self.discriminator = None

        if hostname_prefix is not None:
            self.hostname_prefix = hostname_prefix
        if method is not None:
            self.method = method
        if name is not None:
            self.name = name
        if rest_path is not None:
            self.rest_path = rest_path
        if url_prefix is not None:
            self.url_prefix = url_prefix
        if account is not None:
            self.account = account
        if system is not None:
            self.system = system

    @property
    def hostname_prefix(self):
        """Gets the hostname_prefix of this IamPrivilegeAllOf.  # noqa: E501

        The hostname prefix of the resource corresponding to this privilege. For example \\'sentry\\' in https://sentry.intersight.com .    # noqa: E501

        :return: The hostname_prefix of this IamPrivilegeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._hostname_prefix

    @hostname_prefix.setter
    def hostname_prefix(self, hostname_prefix):
        """Sets the hostname_prefix of this IamPrivilegeAllOf.

        The hostname prefix of the resource corresponding to this privilege. For example \\'sentry\\' in https://sentry.intersight.com .    # noqa: E501

        :param hostname_prefix: The hostname_prefix of this IamPrivilegeAllOf.  # noqa: E501
        :type: str
        """

        self._hostname_prefix = hostname_prefix

    @property
    def method(self):
        """Gets the method of this IamPrivilegeAllOf.  # noqa: E501

        The API method on the rest resource corresponding to privilege. For example READ, CREATE, UPDATE etc.    # noqa: E501

        :return: The method of this IamPrivilegeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this IamPrivilegeAllOf.

        The API method on the rest resource corresponding to privilege. For example READ, CREATE, UPDATE etc.    # noqa: E501

        :param method: The method of this IamPrivilegeAllOf.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def name(self):
        """Gets the name of this IamPrivilegeAllOf.  # noqa: E501

        The name of the privilege reported by microservice.     # noqa: E501

        :return: The name of this IamPrivilegeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IamPrivilegeAllOf.

        The name of the privilege reported by microservice.     # noqa: E501

        :param name: The name of this IamPrivilegeAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rest_path(self):
        """Gets the rest_path of this IamPrivilegeAllOf.  # noqa: E501

        The REST API path of the resource corresponding to this privilege. For example /v1/iam/Accounts, /v1/iam/Sessions.    # noqa: E501

        :return: The rest_path of this IamPrivilegeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._rest_path

    @rest_path.setter
    def rest_path(self, rest_path):
        """Sets the rest_path of this IamPrivilegeAllOf.

        The REST API path of the resource corresponding to this privilege. For example /v1/iam/Accounts, /v1/iam/Sessions.    # noqa: E501

        :param rest_path: The rest_path of this IamPrivilegeAllOf.  # noqa: E501
        :type: str
        """

        self._rest_path = rest_path

    @property
    def url_prefix(self):
        """Gets the url_prefix of this IamPrivilegeAllOf.  # noqa: E501

        The URL path prefix of the resource corresponding to this privilege. For example /devops/kibana, /devops/grafana etc.      # noqa: E501

        :return: The url_prefix of this IamPrivilegeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._url_prefix

    @url_prefix.setter
    def url_prefix(self, url_prefix):
        """Sets the url_prefix of this IamPrivilegeAllOf.

        The URL path prefix of the resource corresponding to this privilege. For example /devops/kibana, /devops/grafana etc.      # noqa: E501

        :param url_prefix: The url_prefix of this IamPrivilegeAllOf.  # noqa: E501
        :type: str
        """

        self._url_prefix = url_prefix

    @property
    def account(self):
        """Gets the account of this IamPrivilegeAllOf.  # noqa: E501


        :return: The account of this IamPrivilegeAllOf.  # noqa: E501
        :rtype: IamAccount
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this IamPrivilegeAllOf.


        :param account: The account of this IamPrivilegeAllOf.  # noqa: E501
        :type: IamAccount
        """

        self._account = account

    @property
    def system(self):
        """Gets the system of this IamPrivilegeAllOf.  # noqa: E501


        :return: The system of this IamPrivilegeAllOf.  # noqa: E501
        :rtype: IamSystem
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this IamPrivilegeAllOf.


        :param system: The system of this IamPrivilegeAllOf.  # noqa: E501
        :type: IamSystem
        """

        self._system = system

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
        if not isinstance(other, IamPrivilegeAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IamPrivilegeAllOf):
            return True

        return self.to_dict() != other.to_dict()
