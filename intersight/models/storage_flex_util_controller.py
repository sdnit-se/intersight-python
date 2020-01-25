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


class StorageFlexUtilController(object):
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
        'controller_name': 'str',
        'controller_status': 'str',
        'ff_controller_id': 'str',
        'internal_state': 'str',
        'compute_board': 'ComputeBoard',
        'flex_util_physical_drives': 'list[StorageFlexUtilPhysicalDrive]',
        'flex_util_virtual_drives': 'list[StorageFlexUtilVirtualDrive]',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'controller_name': 'ControllerName',
        'controller_status': 'ControllerStatus',
        'ff_controller_id': 'FfControllerId',
        'internal_state': 'InternalState',
        'compute_board': 'ComputeBoard',
        'flex_util_physical_drives': 'FlexUtilPhysicalDrives',
        'flex_util_virtual_drives': 'FlexUtilVirtualDrives',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 controller_name=None,
                 controller_status=None,
                 ff_controller_id=None,
                 internal_state=None,
                 compute_board=None,
                 flex_util_physical_drives=None,
                 flex_util_virtual_drives=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """StorageFlexUtilController - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._controller_name = None
        self._controller_status = None
        self._ff_controller_id = None
        self._internal_state = None
        self._compute_board = None
        self._flex_util_physical_drives = None
        self._flex_util_virtual_drives = None
        self._registered_device = None
        self.discriminator = None

        if controller_name is not None:
            self.controller_name = controller_name
        if controller_status is not None:
            self.controller_status = controller_status
        if ff_controller_id is not None:
            self.ff_controller_id = ff_controller_id
        if internal_state is not None:
            self.internal_state = internal_state
        if compute_board is not None:
            self.compute_board = compute_board
        if flex_util_physical_drives is not None:
            self.flex_util_physical_drives = flex_util_physical_drives
        if flex_util_virtual_drives is not None:
            self.flex_util_virtual_drives = flex_util_virtual_drives
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def controller_name(self):
        """Gets the controller_name of this StorageFlexUtilController.  # noqa: E501


        :return: The controller_name of this StorageFlexUtilController.  # noqa: E501
        :rtype: str
        """
        return self._controller_name

    @controller_name.setter
    def controller_name(self, controller_name):
        """Sets the controller_name of this StorageFlexUtilController.


        :param controller_name: The controller_name of this StorageFlexUtilController.  # noqa: E501
        :type: str
        """

        self._controller_name = controller_name

    @property
    def controller_status(self):
        """Gets the controller_status of this StorageFlexUtilController.  # noqa: E501


        :return: The controller_status of this StorageFlexUtilController.  # noqa: E501
        :rtype: str
        """
        return self._controller_status

    @controller_status.setter
    def controller_status(self, controller_status):
        """Sets the controller_status of this StorageFlexUtilController.


        :param controller_status: The controller_status of this StorageFlexUtilController.  # noqa: E501
        :type: str
        """

        self._controller_status = controller_status

    @property
    def ff_controller_id(self):
        """Gets the ff_controller_id of this StorageFlexUtilController.  # noqa: E501


        :return: The ff_controller_id of this StorageFlexUtilController.  # noqa: E501
        :rtype: str
        """
        return self._ff_controller_id

    @ff_controller_id.setter
    def ff_controller_id(self, ff_controller_id):
        """Sets the ff_controller_id of this StorageFlexUtilController.


        :param ff_controller_id: The ff_controller_id of this StorageFlexUtilController.  # noqa: E501
        :type: str
        """

        self._ff_controller_id = ff_controller_id

    @property
    def internal_state(self):
        """Gets the internal_state of this StorageFlexUtilController.  # noqa: E501


        :return: The internal_state of this StorageFlexUtilController.  # noqa: E501
        :rtype: str
        """
        return self._internal_state

    @internal_state.setter
    def internal_state(self, internal_state):
        """Sets the internal_state of this StorageFlexUtilController.


        :param internal_state: The internal_state of this StorageFlexUtilController.  # noqa: E501
        :type: str
        """

        self._internal_state = internal_state

    @property
    def compute_board(self):
        """Gets the compute_board of this StorageFlexUtilController.  # noqa: E501


        :return: The compute_board of this StorageFlexUtilController.  # noqa: E501
        :rtype: ComputeBoard
        """
        return self._compute_board

    @compute_board.setter
    def compute_board(self, compute_board):
        """Sets the compute_board of this StorageFlexUtilController.


        :param compute_board: The compute_board of this StorageFlexUtilController.  # noqa: E501
        :type: ComputeBoard
        """

        self._compute_board = compute_board

    @property
    def flex_util_physical_drives(self):
        """Gets the flex_util_physical_drives of this StorageFlexUtilController.  # noqa: E501

        A reference to a storageFlexUtilPhysicalDrive resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The flex_util_physical_drives of this StorageFlexUtilController.  # noqa: E501
        :rtype: list[StorageFlexUtilPhysicalDrive]
        """
        return self._flex_util_physical_drives

    @flex_util_physical_drives.setter
    def flex_util_physical_drives(self, flex_util_physical_drives):
        """Sets the flex_util_physical_drives of this StorageFlexUtilController.

        A reference to a storageFlexUtilPhysicalDrive resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param flex_util_physical_drives: The flex_util_physical_drives of this StorageFlexUtilController.  # noqa: E501
        :type: list[StorageFlexUtilPhysicalDrive]
        """

        self._flex_util_physical_drives = flex_util_physical_drives

    @property
    def flex_util_virtual_drives(self):
        """Gets the flex_util_virtual_drives of this StorageFlexUtilController.  # noqa: E501

        A reference to a storageFlexUtilVirtualDrive resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The flex_util_virtual_drives of this StorageFlexUtilController.  # noqa: E501
        :rtype: list[StorageFlexUtilVirtualDrive]
        """
        return self._flex_util_virtual_drives

    @flex_util_virtual_drives.setter
    def flex_util_virtual_drives(self, flex_util_virtual_drives):
        """Sets the flex_util_virtual_drives of this StorageFlexUtilController.

        A reference to a storageFlexUtilVirtualDrive resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param flex_util_virtual_drives: The flex_util_virtual_drives of this StorageFlexUtilController.  # noqa: E501
        :type: list[StorageFlexUtilVirtualDrive]
        """

        self._flex_util_virtual_drives = flex_util_virtual_drives

    @property
    def registered_device(self):
        """Gets the registered_device of this StorageFlexUtilController.  # noqa: E501


        :return: The registered_device of this StorageFlexUtilController.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this StorageFlexUtilController.


        :param registered_device: The registered_device of this StorageFlexUtilController.  # noqa: E501
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
        if not isinstance(other, StorageFlexUtilController):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageFlexUtilController):
            return True

        return self.to_dict() != other.to_dict()
