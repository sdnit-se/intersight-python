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


class SecurityUnit(object):
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
        'oper_state': 'str',
        'operability': 'str',
        'part_number': 'str',
        'pci_slot': 'str',
        'power': 'str',
        'presence': 'str',
        'thermal': 'str',
        'unit_id': 'int',
        'vid': 'str',
        'voltage': 'str',
        'compute_board': 'ComputeBoard',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'oper_state': 'OperState',
        'operability': 'Operability',
        'part_number': 'PartNumber',
        'pci_slot': 'PciSlot',
        'power': 'Power',
        'presence': 'Presence',
        'thermal': 'Thermal',
        'unit_id': 'UnitId',
        'vid': 'Vid',
        'voltage': 'Voltage',
        'compute_board': 'ComputeBoard',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 oper_state=None,
                 operability=None,
                 part_number=None,
                 pci_slot=None,
                 power=None,
                 presence=None,
                 thermal=None,
                 unit_id=None,
                 vid=None,
                 voltage=None,
                 compute_board=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """SecurityUnit - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._oper_state = None
        self._operability = None
        self._part_number = None
        self._pci_slot = None
        self._power = None
        self._presence = None
        self._thermal = None
        self._unit_id = None
        self._vid = None
        self._voltage = None
        self._compute_board = None
        self._registered_device = None
        self.discriminator = None

        if oper_state is not None:
            self.oper_state = oper_state
        if operability is not None:
            self.operability = operability
        if part_number is not None:
            self.part_number = part_number
        if pci_slot is not None:
            self.pci_slot = pci_slot
        if power is not None:
            self.power = power
        if presence is not None:
            self.presence = presence
        if thermal is not None:
            self.thermal = thermal
        if unit_id is not None:
            self.unit_id = unit_id
        if vid is not None:
            self.vid = vid
        if voltage is not None:
            self.voltage = voltage
        if compute_board is not None:
            self.compute_board = compute_board
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def oper_state(self):
        """Gets the oper_state of this SecurityUnit.  # noqa: E501


        :return: The oper_state of this SecurityUnit.  # noqa: E501
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """Sets the oper_state of this SecurityUnit.


        :param oper_state: The oper_state of this SecurityUnit.  # noqa: E501
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """Gets the operability of this SecurityUnit.  # noqa: E501


        :return: The operability of this SecurityUnit.  # noqa: E501
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """Sets the operability of this SecurityUnit.


        :param operability: The operability of this SecurityUnit.  # noqa: E501
        :type: str
        """

        self._operability = operability

    @property
    def part_number(self):
        """Gets the part_number of this SecurityUnit.  # noqa: E501


        :return: The part_number of this SecurityUnit.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this SecurityUnit.


        :param part_number: The part_number of this SecurityUnit.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def pci_slot(self):
        """Gets the pci_slot of this SecurityUnit.  # noqa: E501


        :return: The pci_slot of this SecurityUnit.  # noqa: E501
        :rtype: str
        """
        return self._pci_slot

    @pci_slot.setter
    def pci_slot(self, pci_slot):
        """Sets the pci_slot of this SecurityUnit.


        :param pci_slot: The pci_slot of this SecurityUnit.  # noqa: E501
        :type: str
        """

        self._pci_slot = pci_slot

    @property
    def power(self):
        """Gets the power of this SecurityUnit.  # noqa: E501


        :return: The power of this SecurityUnit.  # noqa: E501
        :rtype: str
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this SecurityUnit.


        :param power: The power of this SecurityUnit.  # noqa: E501
        :type: str
        """

        self._power = power

    @property
    def presence(self):
        """Gets the presence of this SecurityUnit.  # noqa: E501


        :return: The presence of this SecurityUnit.  # noqa: E501
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """Sets the presence of this SecurityUnit.


        :param presence: The presence of this SecurityUnit.  # noqa: E501
        :type: str
        """

        self._presence = presence

    @property
    def thermal(self):
        """Gets the thermal of this SecurityUnit.  # noqa: E501


        :return: The thermal of this SecurityUnit.  # noqa: E501
        :rtype: str
        """
        return self._thermal

    @thermal.setter
    def thermal(self, thermal):
        """Sets the thermal of this SecurityUnit.


        :param thermal: The thermal of this SecurityUnit.  # noqa: E501
        :type: str
        """

        self._thermal = thermal

    @property
    def unit_id(self):
        """Gets the unit_id of this SecurityUnit.  # noqa: E501


        :return: The unit_id of this SecurityUnit.  # noqa: E501
        :rtype: int
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        """Sets the unit_id of this SecurityUnit.


        :param unit_id: The unit_id of this SecurityUnit.  # noqa: E501
        :type: int
        """

        self._unit_id = unit_id

    @property
    def vid(self):
        """Gets the vid of this SecurityUnit.  # noqa: E501


        :return: The vid of this SecurityUnit.  # noqa: E501
        :rtype: str
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """Sets the vid of this SecurityUnit.


        :param vid: The vid of this SecurityUnit.  # noqa: E501
        :type: str
        """

        self._vid = vid

    @property
    def voltage(self):
        """Gets the voltage of this SecurityUnit.  # noqa: E501


        :return: The voltage of this SecurityUnit.  # noqa: E501
        :rtype: str
        """
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        """Sets the voltage of this SecurityUnit.


        :param voltage: The voltage of this SecurityUnit.  # noqa: E501
        :type: str
        """

        self._voltage = voltage

    @property
    def compute_board(self):
        """Gets the compute_board of this SecurityUnit.  # noqa: E501


        :return: The compute_board of this SecurityUnit.  # noqa: E501
        :rtype: ComputeBoard
        """
        return self._compute_board

    @compute_board.setter
    def compute_board(self, compute_board):
        """Sets the compute_board of this SecurityUnit.


        :param compute_board: The compute_board of this SecurityUnit.  # noqa: E501
        :type: ComputeBoard
        """

        self._compute_board = compute_board

    @property
    def registered_device(self):
        """Gets the registered_device of this SecurityUnit.  # noqa: E501


        :return: The registered_device of this SecurityUnit.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this SecurityUnit.


        :param registered_device: The registered_device of this SecurityUnit.  # noqa: E501
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
        if not isinstance(other, SecurityUnit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SecurityUnit):
            return True

        return self.to_dict() != other.to_dict()
