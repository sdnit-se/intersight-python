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


class WorkflowWebApiAllOf(object):
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
        'headers': 'object',
        'method': 'str',
        'protocol': 'str',
        'target_type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'headers': 'Headers',
        'method': 'Method',
        'protocol': 'Protocol',
        'target_type': 'TargetType',
        'url': 'Url'
    }

    def __init__(self,
                 headers=None,
                 method=None,
                 protocol=None,
                 target_type='Endpoint',
                 url=None,
                 local_vars_configuration=None):  # noqa: E501
        """WorkflowWebApiAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._headers = None
        self._method = None
        self._protocol = None
        self._target_type = None
        self._url = None
        self.discriminator = None

        if headers is not None:
            self.headers = headers
        if method is not None:
            self.method = method
        if protocol is not None:
            self.protocol = protocol
        if target_type is not None:
            self.target_type = target_type
        if url is not None:
            self.url = url

    @property
    def headers(self):
        """Gets the headers of this WorkflowWebApiAllOf.  # noqa: E501

        Collection of key value pairs to set in the request header.     # noqa: E501

        :return: The headers of this WorkflowWebApiAllOf.  # noqa: E501
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this WorkflowWebApiAllOf.

        Collection of key value pairs to set in the request header.     # noqa: E501

        :param headers: The headers of this WorkflowWebApiAllOf.  # noqa: E501
        :type: object
        """

        self._headers = headers

    @property
    def method(self):
        """Gets the method of this WorkflowWebApiAllOf.  # noqa: E501

        The HTTP method to be executed in the given URL (GET, POST, PUT, etc). If the value is not specified, GET will be used as default.     # noqa: E501

        :return: The method of this WorkflowWebApiAllOf.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this WorkflowWebApiAllOf.

        The HTTP method to be executed in the given URL (GET, POST, PUT, etc). If the value is not specified, GET will be used as default.     # noqa: E501

        :param method: The method of this WorkflowWebApiAllOf.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def protocol(self):
        """Gets the protocol of this WorkflowWebApiAllOf.  # noqa: E501

        The accepted web protocol values are http and https.     # noqa: E501

        :return: The protocol of this WorkflowWebApiAllOf.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this WorkflowWebApiAllOf.

        The accepted web protocol values are http and https.     # noqa: E501

        :param protocol: The protocol of this WorkflowWebApiAllOf.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def target_type(self):
        """Gets the target_type of this WorkflowWebApiAllOf.  # noqa: E501

        If the web API is to be executed in a remote device connected to the Intersight through device connector, 'Endpoint' is expected as the value whereas if the API is an Intersight API, 'Local' is expected as the value.     # noqa: E501

        :return: The target_type of this WorkflowWebApiAllOf.  # noqa: E501
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this WorkflowWebApiAllOf.

        If the web API is to be executed in a remote device connected to the Intersight through device connector, 'Endpoint' is expected as the value whereas if the API is an Intersight API, 'Local' is expected as the value.     # noqa: E501

        :param target_type: The target_type of this WorkflowWebApiAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Endpoint", "Local"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and target_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `target_type` ({0}), must be one of {1}"  # noqa: E501
                .format(target_type, allowed_values))

        self._target_type = target_type

    @property
    def url(self):
        """Gets the url of this WorkflowWebApiAllOf.  # noqa: E501

        The URL of the resource in the target to which the API request is made.      # noqa: E501

        :return: The url of this WorkflowWebApiAllOf.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WorkflowWebApiAllOf.

        The URL of the resource in the target to which the API request is made.      # noqa: E501

        :param url: The url of this WorkflowWebApiAllOf.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, WorkflowWebApiAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowWebApiAllOf):
            return True

        return self.to_dict() != other.to_dict()
