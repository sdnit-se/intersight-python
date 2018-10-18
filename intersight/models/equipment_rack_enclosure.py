# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-228
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EquipmentRackEnclosure(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_moid': 'str',
        'ancestors': 'list[MoBaseMoRef]',
        'create_time': 'datetime',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'model': 'str',
        'revision': 'str',
        'serial': 'str',
        'vendor': 'str',
        'enclosure_id': 'int',
        'fanmodules': 'list[EquipmentFanModuleRef]',
        'psus': 'list[EquipmentPsuRef]',
        'registered_device': 'AssetDeviceRegistrationRef',
        'slots': 'list[EquipmentRackEnclosureSlotRef]'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'model': 'Model',
        'revision': 'Revision',
        'serial': 'Serial',
        'vendor': 'Vendor',
        'enclosure_id': 'EnclosureId',
        'fanmodules': 'Fanmodules',
        'psus': 'Psus',
        'registered_device': 'RegisteredDevice',
        'slots': 'Slots'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, enclosure_id=None, fanmodules=None, psus=None, registered_device=None, slots=None):
        """
        EquipmentRackEnclosure - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._version_context = None
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._model = None
        self._revision = None
        self._serial = None
        self._vendor = None
        self._enclosure_id = None
        self._fanmodules = None
        self._psus = None
        self._registered_device = None
        self._slots = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if parent is not None:
          self.parent = parent
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if model is not None:
          self.model = model
        if revision is not None:
          self.revision = revision
        if serial is not None:
          self.serial = serial
        if vendor is not None:
          self.vendor = vendor
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
    def account_moid(self):
        """
        Gets the account_moid of this EquipmentRackEnclosure.
        The Account ID for this managed object.  

        :return: The account_moid of this EquipmentRackEnclosure.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this EquipmentRackEnclosure.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this EquipmentRackEnclosure.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this EquipmentRackEnclosure.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this EquipmentRackEnclosure.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this EquipmentRackEnclosure.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this EquipmentRackEnclosure.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this EquipmentRackEnclosure.
        The time when this managed object was created.  

        :return: The create_time of this EquipmentRackEnclosure.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this EquipmentRackEnclosure.
        The time when this managed object was created.  

        :param create_time: The create_time of this EquipmentRackEnclosure.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this EquipmentRackEnclosure.
        The time when this managed object was last modified.  

        :return: The mod_time of this EquipmentRackEnclosure.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this EquipmentRackEnclosure.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this EquipmentRackEnclosure.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this EquipmentRackEnclosure.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this EquipmentRackEnclosure.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this EquipmentRackEnclosure.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this EquipmentRackEnclosure.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this EquipmentRackEnclosure.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this EquipmentRackEnclosure.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this EquipmentRackEnclosure.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this EquipmentRackEnclosure.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this EquipmentRackEnclosure.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this EquipmentRackEnclosure.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this EquipmentRackEnclosure.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this EquipmentRackEnclosure.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this EquipmentRackEnclosure.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this EquipmentRackEnclosure.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this EquipmentRackEnclosure.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this EquipmentRackEnclosure.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this EquipmentRackEnclosure.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this EquipmentRackEnclosure.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this EquipmentRackEnclosure.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this EquipmentRackEnclosure.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this EquipmentRackEnclosure.
        The versioning info for this managed object   

        :return: The version_context of this EquipmentRackEnclosure.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this EquipmentRackEnclosure.
        The versioning info for this managed object   

        :param version_context: The version_context of this EquipmentRackEnclosure.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this EquipmentRackEnclosure.

        :return: The device_mo_id of this EquipmentRackEnclosure.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this EquipmentRackEnclosure.

        :param device_mo_id: The device_mo_id of this EquipmentRackEnclosure.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this EquipmentRackEnclosure.

        :return: The dn of this EquipmentRackEnclosure.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this EquipmentRackEnclosure.

        :param dn: The dn of this EquipmentRackEnclosure.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this EquipmentRackEnclosure.

        :return: The rn of this EquipmentRackEnclosure.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this EquipmentRackEnclosure.

        :param rn: The rn of this EquipmentRackEnclosure.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this EquipmentRackEnclosure.

        :return: The model of this EquipmentRackEnclosure.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this EquipmentRackEnclosure.

        :param model: The model of this EquipmentRackEnclosure.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this EquipmentRackEnclosure.

        :return: The revision of this EquipmentRackEnclosure.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this EquipmentRackEnclosure.

        :param revision: The revision of this EquipmentRackEnclosure.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this EquipmentRackEnclosure.

        :return: The serial of this EquipmentRackEnclosure.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this EquipmentRackEnclosure.

        :param serial: The serial of this EquipmentRackEnclosure.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this EquipmentRackEnclosure.

        :return: The vendor of this EquipmentRackEnclosure.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this EquipmentRackEnclosure.

        :param vendor: The vendor of this EquipmentRackEnclosure.
        :type: str
        """

        self._vendor = vendor

    @property
    def enclosure_id(self):
        """
        Gets the enclosure_id of this EquipmentRackEnclosure.

        :return: The enclosure_id of this EquipmentRackEnclosure.
        :rtype: int
        """
        return self._enclosure_id

    @enclosure_id.setter
    def enclosure_id(self, enclosure_id):
        """
        Sets the enclosure_id of this EquipmentRackEnclosure.

        :param enclosure_id: The enclosure_id of this EquipmentRackEnclosure.
        :type: int
        """

        self._enclosure_id = enclosure_id

    @property
    def fanmodules(self):
        """
        Gets the fanmodules of this EquipmentRackEnclosure.

        :return: The fanmodules of this EquipmentRackEnclosure.
        :rtype: list[EquipmentFanModuleRef]
        """
        return self._fanmodules

    @fanmodules.setter
    def fanmodules(self, fanmodules):
        """
        Sets the fanmodules of this EquipmentRackEnclosure.

        :param fanmodules: The fanmodules of this EquipmentRackEnclosure.
        :type: list[EquipmentFanModuleRef]
        """

        self._fanmodules = fanmodules

    @property
    def psus(self):
        """
        Gets the psus of this EquipmentRackEnclosure.

        :return: The psus of this EquipmentRackEnclosure.
        :rtype: list[EquipmentPsuRef]
        """
        return self._psus

    @psus.setter
    def psus(self, psus):
        """
        Sets the psus of this EquipmentRackEnclosure.

        :param psus: The psus of this EquipmentRackEnclosure.
        :type: list[EquipmentPsuRef]
        """

        self._psus = psus

    @property
    def registered_device(self):
        """
        Gets the registered_device of this EquipmentRackEnclosure.

        :return: The registered_device of this EquipmentRackEnclosure.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this EquipmentRackEnclosure.

        :param registered_device: The registered_device of this EquipmentRackEnclosure.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def slots(self):
        """
        Gets the slots of this EquipmentRackEnclosure.

        :return: The slots of this EquipmentRackEnclosure.
        :rtype: list[EquipmentRackEnclosureSlotRef]
        """
        return self._slots

    @slots.setter
    def slots(self, slots):
        """
        Sets the slots of this EquipmentRackEnclosure.

        :param slots: The slots of this EquipmentRackEnclosure.
        :type: list[EquipmentRackEnclosureSlotRef]
        """

        self._slots = slots

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, EquipmentRackEnclosure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other