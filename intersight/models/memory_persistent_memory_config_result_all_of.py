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


class MemoryPersistentMemoryConfigResultAllOf(object):
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
        'config_error_desc': 'str',
        'config_result': 'str',
        'config_sequence_no': 'int',
        'config_state': 'str',
        'memory_persistent_memory_configuration':
        'MemoryPersistentMemoryConfiguration',
        'persistent_memory_namespace_config_results':
        'list[MemoryPersistentMemoryNamespaceConfigResult]',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'config_error_desc': 'ConfigErrorDesc',
        'config_result': 'ConfigResult',
        'config_sequence_no': 'ConfigSequenceNo',
        'config_state': 'ConfigState',
        'memory_persistent_memory_configuration':
        'MemoryPersistentMemoryConfiguration',
        'persistent_memory_namespace_config_results':
        'PersistentMemoryNamespaceConfigResults',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 config_error_desc=None,
                 config_result=None,
                 config_sequence_no=None,
                 config_state=None,
                 memory_persistent_memory_configuration=None,
                 persistent_memory_namespace_config_results=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """MemoryPersistentMemoryConfigResultAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._config_error_desc = None
        self._config_result = None
        self._config_sequence_no = None
        self._config_state = None
        self._memory_persistent_memory_configuration = None
        self._persistent_memory_namespace_config_results = None
        self._registered_device = None
        self.discriminator = None

        if config_error_desc is not None:
            self.config_error_desc = config_error_desc
        if config_result is not None:
            self.config_result = config_result
        if config_sequence_no is not None:
            self.config_sequence_no = config_sequence_no
        if config_state is not None:
            self.config_state = config_state
        if memory_persistent_memory_configuration is not None:
            self.memory_persistent_memory_configuration = memory_persistent_memory_configuration
        if persistent_memory_namespace_config_results is not None:
            self.persistent_memory_namespace_config_results = persistent_memory_namespace_config_results
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def config_error_desc(self):
        """Gets the config_error_desc of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501

        This describes the error in the result of a previously applied Persistent Memory Configuration on a server.    # noqa: E501

        :return: The config_error_desc of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501
        :rtype: str
        """
        return self._config_error_desc

    @config_error_desc.setter
    def config_error_desc(self, config_error_desc):
        """Sets the config_error_desc of this MemoryPersistentMemoryConfigResultAllOf.

        This describes the error in the result of a previously applied Persistent Memory Configuration on a server.    # noqa: E501

        :param config_error_desc: The config_error_desc of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501
        :type: str
        """

        self._config_error_desc = config_error_desc

    @property
    def config_result(self):
        """Gets the config_result of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501

        This represents the result of a previously applied Persistent Memory Configuration on a server.    # noqa: E501

        :return: The config_result of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501
        :rtype: str
        """
        return self._config_result

    @config_result.setter
    def config_result(self, config_result):
        """Sets the config_result of this MemoryPersistentMemoryConfigResultAllOf.

        This represents the result of a previously applied Persistent Memory Configuration on a server.    # noqa: E501

        :param config_result: The config_result of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501
        :type: str
        """

        self._config_result = config_result

    @property
    def config_sequence_no(self):
        """Gets the config_sequence_no of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501

        This represents the sequence number of a previously applied Persistent Memory Configuration on a server.    # noqa: E501

        :return: The config_sequence_no of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501
        :rtype: int
        """
        return self._config_sequence_no

    @config_sequence_no.setter
    def config_sequence_no(self, config_sequence_no):
        """Sets the config_sequence_no of this MemoryPersistentMemoryConfigResultAllOf.

        This represents the sequence number of a previously applied Persistent Memory Configuration on a server.    # noqa: E501

        :param config_sequence_no: The config_sequence_no of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501
        :type: int
        """

        self._config_sequence_no = config_sequence_no

    @property
    def config_state(self):
        """Gets the config_state of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501

        This represents the state of a previously applied Persistent Memory Configuration on a server.     # noqa: E501

        :return: The config_state of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501
        :rtype: str
        """
        return self._config_state

    @config_state.setter
    def config_state(self, config_state):
        """Sets the config_state of this MemoryPersistentMemoryConfigResultAllOf.

        This represents the state of a previously applied Persistent Memory Configuration on a server.     # noqa: E501

        :param config_state: The config_state of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501
        :type: str
        """

        self._config_state = config_state

    @property
    def memory_persistent_memory_configuration(self):
        """Gets the memory_persistent_memory_configuration of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501


        :return: The memory_persistent_memory_configuration of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501
        :rtype: MemoryPersistentMemoryConfiguration
        """
        return self._memory_persistent_memory_configuration

    @memory_persistent_memory_configuration.setter
    def memory_persistent_memory_configuration(
            self, memory_persistent_memory_configuration):
        """Sets the memory_persistent_memory_configuration of this MemoryPersistentMemoryConfigResultAllOf.


        :param memory_persistent_memory_configuration: The memory_persistent_memory_configuration of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501
        :type: MemoryPersistentMemoryConfiguration
        """

        self._memory_persistent_memory_configuration = memory_persistent_memory_configuration

    @property
    def persistent_memory_namespace_config_results(self):
        """Gets the persistent_memory_namespace_config_results of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501

        A reference to a memoryPersistentMemoryNamespaceConfigResult resource. When the $expand query parameter is specified, the referenced resource is returned inline. This represents the collection of all the results of the previously applied Persistent Memory Namespaces on a server.   # noqa: E501

        :return: The persistent_memory_namespace_config_results of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501
        :rtype: list[MemoryPersistentMemoryNamespaceConfigResult]
        """
        return self._persistent_memory_namespace_config_results

    @persistent_memory_namespace_config_results.setter
    def persistent_memory_namespace_config_results(
            self, persistent_memory_namespace_config_results):
        """Sets the persistent_memory_namespace_config_results of this MemoryPersistentMemoryConfigResultAllOf.

        A reference to a memoryPersistentMemoryNamespaceConfigResult resource. When the $expand query parameter is specified, the referenced resource is returned inline. This represents the collection of all the results of the previously applied Persistent Memory Namespaces on a server.   # noqa: E501

        :param persistent_memory_namespace_config_results: The persistent_memory_namespace_config_results of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501
        :type: list[MemoryPersistentMemoryNamespaceConfigResult]
        """

        self._persistent_memory_namespace_config_results = persistent_memory_namespace_config_results

    @property
    def registered_device(self):
        """Gets the registered_device of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501


        :return: The registered_device of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this MemoryPersistentMemoryConfigResultAllOf.


        :param registered_device: The registered_device of this MemoryPersistentMemoryConfigResultAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

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
        if not isinstance(other, MemoryPersistentMemoryConfigResultAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MemoryPersistentMemoryConfigResultAllOf):
            return True

        return self.to_dict() != other.to_dict()
