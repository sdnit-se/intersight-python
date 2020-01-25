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


class EquipmentRackEnclosure(object):
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
        'enclosure_id': 'int',
        'fanmodules': 'list[EquipmentFanModule]',
        'psus': 'list[EquipmentPsu]',
        'registered_device': 'AssetDeviceRegistration',
        'slots': 'list[EquipmentRackEnclosureSlot]'
    }

    attribute_map = {
        'enclosure_id': 'EnclosureId',
        'fanmodules': 'Fanmodules',
        'psus': 'Psus',
        'registered_device': 'RegisteredDevice',
        'slots': 'Slots'
    }

    def __init__(self,
                 enclosure_id=None,
                 fanmodules=None,
                 psus=None,
                 registered_device=None,
                 slots=None,
                 local_vars_configuration=None):  # noqa: E501
        """EquipmentRackEnclosure - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enclosure_id = None
        self._fanmodules = None
        self._psus = None
        self._registered_device = None
        self._slots = None
        self.discriminator = None

        if enclosure_id is not None:
            self.enclosure_id = enclosure_id
        if fanmodules is not None:
            self.fanmodules = fanmodules
        if psus is not None:
            self.psus = psus
        if registered_device is not None:
            self.registered_device = registered_device
        if slots is not None:
            self.slots = slots

    @property
    def enclosure_id(self):
        """Gets the enclosure_id of this EquipmentRackEnclosure.  # noqa: E501


        :return: The enclosure_id of this EquipmentRackEnclosure.  # noqa: E501
        :rtype: int
        """
        return self._enclosure_id

    @enclosure_id.setter
    def enclosure_id(self, enclosure_id):
        """Sets the enclosure_id of this EquipmentRackEnclosure.


        :param enclosure_id: The enclosure_id of this EquipmentRackEnclosure.  # noqa: E501
        :type: int
        """

        self._enclosure_id = enclosure_id

    @property
    def fanmodules(self):
        """Gets the fanmodules of this EquipmentRackEnclosure.  # noqa: E501

        A reference to a equipmentFanModule resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The fanmodules of this EquipmentRackEnclosure.  # noqa: E501
        :rtype: list[EquipmentFanModule]
        """
        return self._fanmodules

    @fanmodules.setter
    def fanmodules(self, fanmodules):
        """Sets the fanmodules of this EquipmentRackEnclosure.

        A reference to a equipmentFanModule resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param fanmodules: The fanmodules of this EquipmentRackEnclosure.  # noqa: E501
        :type: list[EquipmentFanModule]
        """

        self._fanmodules = fanmodules

    @property
    def psus(self):
        """Gets the psus of this EquipmentRackEnclosure.  # noqa: E501

        A reference to a equipmentPsu resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The psus of this EquipmentRackEnclosure.  # noqa: E501
        :rtype: list[EquipmentPsu]
        """
        return self._psus

    @psus.setter
    def psus(self, psus):
        """Sets the psus of this EquipmentRackEnclosure.

        A reference to a equipmentPsu resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param psus: The psus of this EquipmentRackEnclosure.  # noqa: E501
        :type: list[EquipmentPsu]
        """

        self._psus = psus

    @property
    def registered_device(self):
        """Gets the registered_device of this EquipmentRackEnclosure.  # noqa: E501


        :return: The registered_device of this EquipmentRackEnclosure.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this EquipmentRackEnclosure.


        :param registered_device: The registered_device of this EquipmentRackEnclosure.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

    @property
    def slots(self):
        """Gets the slots of this EquipmentRackEnclosure.  # noqa: E501

        A reference to a equipmentRackEnclosureSlot resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :return: The slots of this EquipmentRackEnclosure.  # noqa: E501
        :rtype: list[EquipmentRackEnclosureSlot]
        """
        return self._slots

    @slots.setter
    def slots(self, slots):
        """Sets the slots of this EquipmentRackEnclosure.

        A reference to a equipmentRackEnclosureSlot resource. When the $expand query parameter is specified, the referenced resource is returned inline.   # noqa: E501

        :param slots: The slots of this EquipmentRackEnclosure.  # noqa: E501
        :type: list[EquipmentRackEnclosureSlot]
        """

        self._slots = slots

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
        if not isinstance(other, EquipmentRackEnclosure):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EquipmentRackEnclosure):
            return True

        return self.to_dict() != other.to_dict()
