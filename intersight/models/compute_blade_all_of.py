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


class ComputeBladeAllOf(object):
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
        'chassis_id': 'str',
        'scaled_mode': 'str',
        'slot_id': 'int',
        'adapters': 'list[AdapterUnit]',
        'bios_units': 'list[BiosUnit]',
        'bmc': 'ManagementController',
        'board': 'ComputeBoard',
        'equipment_chassis': 'EquipmentChassis',
        'equipment_io_expanders': 'list[EquipmentIoExpander]',
        'generic_inventory_holders': 'list[InventoryGenericInventoryHolder]',
        'locator_led': 'EquipmentLocatorLed',
        'pci_devices': 'list[PciDevice]',
        'registered_device': 'AssetDeviceRegistration',
        'storage_enclosures': 'list[StorageEnclosure]',
        'top_system': 'TopSystem'
    }

    attribute_map = {
        'chassis_id': 'ChassisId',
        'scaled_mode': 'ScaledMode',
        'slot_id': 'SlotId',
        'adapters': 'Adapters',
        'bios_units': 'BiosUnits',
        'bmc': 'Bmc',
        'board': 'Board',
        'equipment_chassis': 'EquipmentChassis',
        'equipment_io_expanders': 'EquipmentIoExpanders',
        'generic_inventory_holders': 'GenericInventoryHolders',
        'locator_led': 'LocatorLed',
        'pci_devices': 'PciDevices',
        'registered_device': 'RegisteredDevice',
        'storage_enclosures': 'StorageEnclosures',
        'top_system': 'TopSystem'
    }

    def __init__(self,
                 chassis_id=None,
                 scaled_mode=None,
                 slot_id=None,
                 adapters=None,
                 bios_units=None,
                 bmc=None,
                 board=None,
                 equipment_chassis=None,
                 equipment_io_expanders=None,
                 generic_inventory_holders=None,
                 locator_led=None,
                 pci_devices=None,
                 registered_device=None,
                 storage_enclosures=None,
                 top_system=None,
                 local_vars_configuration=None):  # noqa: E501
        """ComputeBladeAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._chassis_id = None
        self._scaled_mode = None
        self._slot_id = None
        self._adapters = None
        self._bios_units = None
        self._bmc = None
        self._board = None
        self._equipment_chassis = None
        self._equipment_io_expanders = None
        self._generic_inventory_holders = None
        self._locator_led = None
        self._pci_devices = None
        self._registered_device = None
        self._storage_enclosures = None
        self._top_system = None
        self.discriminator = None

        if chassis_id is not None:
            self.chassis_id = chassis_id
        if scaled_mode is not None:
            self.scaled_mode = scaled_mode
        if slot_id is not None:
            self.slot_id = slot_id
        if adapters is not None:
            self.adapters = adapters
        if bios_units is not None:
            self.bios_units = bios_units
        if bmc is not None:
            self.bmc = bmc
        if board is not None:
            self.board = board
        if equipment_chassis is not None:
            self.equipment_chassis = equipment_chassis
        if equipment_io_expanders is not None:
            self.equipment_io_expanders = equipment_io_expanders
        if generic_inventory_holders is not None:
            self.generic_inventory_holders = generic_inventory_holders
        if locator_led is not None:
            self.locator_led = locator_led
        if pci_devices is not None:
            self.pci_devices = pci_devices
        if registered_device is not None:
            self.registered_device = registered_device
        if storage_enclosures is not None:
            self.storage_enclosures = storage_enclosures
        if top_system is not None:
            self.top_system = top_system

    @property
    def chassis_id(self):
        """Gets the chassis_id of this ComputeBladeAllOf.  # noqa: E501

        The id of the chassis that the blade is located in.    # noqa: E501

        :return: The chassis_id of this ComputeBladeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._chassis_id

    @chassis_id.setter
    def chassis_id(self, chassis_id):
        """Sets the chassis_id of this ComputeBladeAllOf.

        The id of the chassis that the blade is located in.    # noqa: E501

        :param chassis_id: The chassis_id of this ComputeBladeAllOf.  # noqa: E501
        :type: str
        """

        self._chassis_id = chassis_id

    @property
    def scaled_mode(self):
        """Gets the scaled_mode of this ComputeBladeAllOf.  # noqa: E501


        :return: The scaled_mode of this ComputeBladeAllOf.  # noqa: E501
        :rtype: str
        """
        return self._scaled_mode

    @scaled_mode.setter
    def scaled_mode(self, scaled_mode):
        """Sets the scaled_mode of this ComputeBladeAllOf.


        :param scaled_mode: The scaled_mode of this ComputeBladeAllOf.  # noqa: E501
        :type: str
        """

        self._scaled_mode = scaled_mode

    @property
    def slot_id(self):
        """Gets the slot_id of this ComputeBladeAllOf.  # noqa: E501


        :return: The slot_id of this ComputeBladeAllOf.  # noqa: E501
        :rtype: int
        """
        return self._slot_id

    @slot_id.setter
    def slot_id(self, slot_id):
        """Sets the slot_id of this ComputeBladeAllOf.


        :param slot_id: The slot_id of this ComputeBladeAllOf.  # noqa: E501
        :type: int
        """

        self._slot_id = slot_id

    @property
    def adapters(self):
        """Gets the adapters of this ComputeBladeAllOf.  # noqa: E501

        A reference to a adapterUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The adapters of this ComputeBladeAllOf.  # noqa: E501
        :rtype: list[AdapterUnit]
        """
        return self._adapters

    @adapters.setter
    def adapters(self, adapters):
        """Sets the adapters of this ComputeBladeAllOf.

        A reference to a adapterUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param adapters: The adapters of this ComputeBladeAllOf.  # noqa: E501
        :type: list[AdapterUnit]
        """

        self._adapters = adapters

    @property
    def bios_units(self):
        """Gets the bios_units of this ComputeBladeAllOf.  # noqa: E501

        A reference to a biosUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The bios_units of this ComputeBladeAllOf.  # noqa: E501
        :rtype: list[BiosUnit]
        """
        return self._bios_units

    @bios_units.setter
    def bios_units(self, bios_units):
        """Sets the bios_units of this ComputeBladeAllOf.

        A reference to a biosUnit resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param bios_units: The bios_units of this ComputeBladeAllOf.  # noqa: E501
        :type: list[BiosUnit]
        """

        self._bios_units = bios_units

    @property
    def bmc(self):
        """Gets the bmc of this ComputeBladeAllOf.  # noqa: E501


        :return: The bmc of this ComputeBladeAllOf.  # noqa: E501
        :rtype: ManagementController
        """
        return self._bmc

    @bmc.setter
    def bmc(self, bmc):
        """Sets the bmc of this ComputeBladeAllOf.


        :param bmc: The bmc of this ComputeBladeAllOf.  # noqa: E501
        :type: ManagementController
        """

        self._bmc = bmc

    @property
    def board(self):
        """Gets the board of this ComputeBladeAllOf.  # noqa: E501


        :return: The board of this ComputeBladeAllOf.  # noqa: E501
        :rtype: ComputeBoard
        """
        return self._board

    @board.setter
    def board(self, board):
        """Sets the board of this ComputeBladeAllOf.


        :param board: The board of this ComputeBladeAllOf.  # noqa: E501
        :type: ComputeBoard
        """

        self._board = board

    @property
    def equipment_chassis(self):
        """Gets the equipment_chassis of this ComputeBladeAllOf.  # noqa: E501


        :return: The equipment_chassis of this ComputeBladeAllOf.  # noqa: E501
        :rtype: EquipmentChassis
        """
        return self._equipment_chassis

    @equipment_chassis.setter
    def equipment_chassis(self, equipment_chassis):
        """Sets the equipment_chassis of this ComputeBladeAllOf.


        :param equipment_chassis: The equipment_chassis of this ComputeBladeAllOf.  # noqa: E501
        :type: EquipmentChassis
        """

        self._equipment_chassis = equipment_chassis

    @property
    def equipment_io_expanders(self):
        """Gets the equipment_io_expanders of this ComputeBladeAllOf.  # noqa: E501

        A reference to a equipmentIoExpander resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The equipment_io_expanders of this ComputeBladeAllOf.  # noqa: E501
        :rtype: list[EquipmentIoExpander]
        """
        return self._equipment_io_expanders

    @equipment_io_expanders.setter
    def equipment_io_expanders(self, equipment_io_expanders):
        """Sets the equipment_io_expanders of this ComputeBladeAllOf.

        A reference to a equipmentIoExpander resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param equipment_io_expanders: The equipment_io_expanders of this ComputeBladeAllOf.  # noqa: E501
        :type: list[EquipmentIoExpander]
        """

        self._equipment_io_expanders = equipment_io_expanders

    @property
    def generic_inventory_holders(self):
        """Gets the generic_inventory_holders of this ComputeBladeAllOf.  # noqa: E501

        A reference to a inventoryGenericInventoryHolder resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The generic_inventory_holders of this ComputeBladeAllOf.  # noqa: E501
        :rtype: list[InventoryGenericInventoryHolder]
        """
        return self._generic_inventory_holders

    @generic_inventory_holders.setter
    def generic_inventory_holders(self, generic_inventory_holders):
        """Sets the generic_inventory_holders of this ComputeBladeAllOf.

        A reference to a inventoryGenericInventoryHolder resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param generic_inventory_holders: The generic_inventory_holders of this ComputeBladeAllOf.  # noqa: E501
        :type: list[InventoryGenericInventoryHolder]
        """

        self._generic_inventory_holders = generic_inventory_holders

    @property
    def locator_led(self):
        """Gets the locator_led of this ComputeBladeAllOf.  # noqa: E501


        :return: The locator_led of this ComputeBladeAllOf.  # noqa: E501
        :rtype: EquipmentLocatorLed
        """
        return self._locator_led

    @locator_led.setter
    def locator_led(self, locator_led):
        """Sets the locator_led of this ComputeBladeAllOf.


        :param locator_led: The locator_led of this ComputeBladeAllOf.  # noqa: E501
        :type: EquipmentLocatorLed
        """

        self._locator_led = locator_led

    @property
    def pci_devices(self):
        """Gets the pci_devices of this ComputeBladeAllOf.  # noqa: E501

        A reference to a pciDevice resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The pci_devices of this ComputeBladeAllOf.  # noqa: E501
        :rtype: list[PciDevice]
        """
        return self._pci_devices

    @pci_devices.setter
    def pci_devices(self, pci_devices):
        """Sets the pci_devices of this ComputeBladeAllOf.

        A reference to a pciDevice resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param pci_devices: The pci_devices of this ComputeBladeAllOf.  # noqa: E501
        :type: list[PciDevice]
        """

        self._pci_devices = pci_devices

    @property
    def registered_device(self):
        """Gets the registered_device of this ComputeBladeAllOf.  # noqa: E501


        :return: The registered_device of this ComputeBladeAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this ComputeBladeAllOf.


        :param registered_device: The registered_device of this ComputeBladeAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

    @property
    def storage_enclosures(self):
        """Gets the storage_enclosures of this ComputeBladeAllOf.  # noqa: E501

        A reference to a storageEnclosure resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The storage_enclosures of this ComputeBladeAllOf.  # noqa: E501
        :rtype: list[StorageEnclosure]
        """
        return self._storage_enclosures

    @storage_enclosures.setter
    def storage_enclosures(self, storage_enclosures):
        """Sets the storage_enclosures of this ComputeBladeAllOf.

        A reference to a storageEnclosure resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param storage_enclosures: The storage_enclosures of this ComputeBladeAllOf.  # noqa: E501
        :type: list[StorageEnclosure]
        """

        self._storage_enclosures = storage_enclosures

    @property
    def top_system(self):
        """Gets the top_system of this ComputeBladeAllOf.  # noqa: E501


        :return: The top_system of this ComputeBladeAllOf.  # noqa: E501
        :rtype: TopSystem
        """
        return self._top_system

    @top_system.setter
    def top_system(self, top_system):
        """Sets the top_system of this ComputeBladeAllOf.


        :param top_system: The top_system of this ComputeBladeAllOf.  # noqa: E501
        :type: TopSystem
        """

        self._top_system = top_system

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
        if not isinstance(other, ComputeBladeAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComputeBladeAllOf):
            return True

        return self.to_dict() != other.to_dict()