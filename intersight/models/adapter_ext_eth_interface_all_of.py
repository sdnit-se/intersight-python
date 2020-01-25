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


class AdapterExtEthInterfaceAllOf(object):
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
        'admin_state': 'str',
        'ep_dn': 'str',
        'ext_eth_interface_id': 'str',
        'interface_type': 'str',
        'mac_address': 'str',
        'oper_state': 'str',
        'peer_dn': 'str',
        'adapter_unit': 'AdapterUnit',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'admin_state': 'AdminState',
        'ep_dn': 'EpDn',
        'ext_eth_interface_id': 'ExtEthInterfaceId',
        'interface_type': 'InterfaceType',
        'mac_address': 'MacAddress',
        'oper_state': 'OperState',
        'peer_dn': 'PeerDn',
        'adapter_unit': 'AdapterUnit',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 admin_state=None,
                 ep_dn=None,
                 ext_eth_interface_id=None,
                 interface_type=None,
                 mac_address=None,
                 oper_state=None,
                 peer_dn=None,
                 adapter_unit=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """AdapterExtEthInterfaceAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._admin_state = None
        self._ep_dn = None
        self._ext_eth_interface_id = None
        self._interface_type = None
        self._mac_address = None
        self._oper_state = None
        self._peer_dn = None
        self._adapter_unit = None
        self._registered_device = None
        self.discriminator = None

        if admin_state is not None:
            self.admin_state = admin_state
        if ep_dn is not None:
            self.ep_dn = ep_dn
        if ext_eth_interface_id is not None:
            self.ext_eth_interface_id = ext_eth_interface_id
        if interface_type is not None:
            self.interface_type = interface_type
        if mac_address is not None:
            self.mac_address = mac_address
        if oper_state is not None:
            self.oper_state = oper_state
        if peer_dn is not None:
            self.peer_dn = peer_dn
        if adapter_unit is not None:
            self.adapter_unit = adapter_unit
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def admin_state(self):
        """Gets the admin_state of this AdapterExtEthInterfaceAllOf.  # noqa: E501


        :return: The admin_state of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """Sets the admin_state of this AdapterExtEthInterfaceAllOf.


        :param admin_state: The admin_state of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._admin_state = admin_state

    @property
    def ep_dn(self):
        """Gets the ep_dn of this AdapterExtEthInterfaceAllOf.  # noqa: E501


        :return: The ep_dn of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ep_dn

    @ep_dn.setter
    def ep_dn(self, ep_dn):
        """Sets the ep_dn of this AdapterExtEthInterfaceAllOf.


        :param ep_dn: The ep_dn of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._ep_dn = ep_dn

    @property
    def ext_eth_interface_id(self):
        """Gets the ext_eth_interface_id of this AdapterExtEthInterfaceAllOf.  # noqa: E501


        :return: The ext_eth_interface_id of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ext_eth_interface_id

    @ext_eth_interface_id.setter
    def ext_eth_interface_id(self, ext_eth_interface_id):
        """Sets the ext_eth_interface_id of this AdapterExtEthInterfaceAllOf.


        :param ext_eth_interface_id: The ext_eth_interface_id of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._ext_eth_interface_id = ext_eth_interface_id

    @property
    def interface_type(self):
        """Gets the interface_type of this AdapterExtEthInterfaceAllOf.  # noqa: E501


        :return: The interface_type of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._interface_type

    @interface_type.setter
    def interface_type(self, interface_type):
        """Sets the interface_type of this AdapterExtEthInterfaceAllOf.


        :param interface_type: The interface_type of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._interface_type = interface_type

    @property
    def mac_address(self):
        """Gets the mac_address of this AdapterExtEthInterfaceAllOf.  # noqa: E501


        :return: The mac_address of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this AdapterExtEthInterfaceAllOf.


        :param mac_address: The mac_address of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def oper_state(self):
        """Gets the oper_state of this AdapterExtEthInterfaceAllOf.  # noqa: E501


        :return: The oper_state of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """Sets the oper_state of this AdapterExtEthInterfaceAllOf.


        :param oper_state: The oper_state of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._oper_state = oper_state

    @property
    def peer_dn(self):
        """Gets the peer_dn of this AdapterExtEthInterfaceAllOf.  # noqa: E501


        :return: The peer_dn of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._peer_dn

    @peer_dn.setter
    def peer_dn(self, peer_dn):
        """Sets the peer_dn of this AdapterExtEthInterfaceAllOf.


        :param peer_dn: The peer_dn of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :type: str
        """

        self._peer_dn = peer_dn

    @property
    def adapter_unit(self):
        """Gets the adapter_unit of this AdapterExtEthInterfaceAllOf.  # noqa: E501


        :return: The adapter_unit of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :rtype: AdapterUnit
        """
        return self._adapter_unit

    @adapter_unit.setter
    def adapter_unit(self, adapter_unit):
        """Sets the adapter_unit of this AdapterExtEthInterfaceAllOf.


        :param adapter_unit: The adapter_unit of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :type: AdapterUnit
        """

        self._adapter_unit = adapter_unit

    @property
    def registered_device(self):
        """Gets the registered_device of this AdapterExtEthInterfaceAllOf.  # noqa: E501


        :return: The registered_device of this AdapterExtEthInterfaceAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this AdapterExtEthInterfaceAllOf.


        :param registered_device: The registered_device of this AdapterExtEthInterfaceAllOf.  # noqa: E501
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
        if not isinstance(other, AdapterExtEthInterfaceAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdapterExtEthInterfaceAllOf):
            return True

        return self.to_dict() != other.to_dict()
