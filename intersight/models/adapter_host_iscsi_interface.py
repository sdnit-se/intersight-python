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


class AdapterHostIscsiInterface(object):
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
        'adapter_unit': 'AdapterUnitRef',
        'admin_state': 'str',
        'ep_dn': 'str',
        'host_iscsi_interface_id': 'int',
        'host_visible': 'str',
        'mac_address': 'str',
        'name': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'peer_dn': 'str',
        'registered_device': 'AssetDeviceRegistrationRef'
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
        'adapter_unit': 'AdapterUnit',
        'admin_state': 'AdminState',
        'ep_dn': 'EpDn',
        'host_iscsi_interface_id': 'HostIscsiInterfaceId',
        'host_visible': 'HostVisible',
        'mac_address': 'MacAddress',
        'name': 'Name',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'peer_dn': 'PeerDn',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, adapter_unit=None, admin_state=None, ep_dn=None, host_iscsi_interface_id=None, host_visible=None, mac_address=None, name=None, oper_state=None, operability=None, peer_dn=None, registered_device=None):
        """
        AdapterHostIscsiInterface - a model defined in Swagger
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
        self._adapter_unit = None
        self._admin_state = None
        self._ep_dn = None
        self._host_iscsi_interface_id = None
        self._host_visible = None
        self._mac_address = None
        self._name = None
        self._oper_state = None
        self._operability = None
        self._peer_dn = None
        self._registered_device = None

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
        if adapter_unit is not None:
          self.adapter_unit = adapter_unit
        if admin_state is not None:
          self.admin_state = admin_state
        if ep_dn is not None:
          self.ep_dn = ep_dn
        if host_iscsi_interface_id is not None:
          self.host_iscsi_interface_id = host_iscsi_interface_id
        if host_visible is not None:
          self.host_visible = host_visible
        if mac_address is not None:
          self.mac_address = mac_address
        if name is not None:
          self.name = name
        if oper_state is not None:
          self.oper_state = oper_state
        if operability is not None:
          self.operability = operability
        if peer_dn is not None:
          self.peer_dn = peer_dn
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this AdapterHostIscsiInterface.
        The Account ID for this managed object.  

        :return: The account_moid of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this AdapterHostIscsiInterface.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this AdapterHostIscsiInterface.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this AdapterHostIscsiInterface.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this AdapterHostIscsiInterface.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this AdapterHostIscsiInterface.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this AdapterHostIscsiInterface.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this AdapterHostIscsiInterface.
        The time when this managed object was created.  

        :return: The create_time of this AdapterHostIscsiInterface.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this AdapterHostIscsiInterface.
        The time when this managed object was created.  

        :param create_time: The create_time of this AdapterHostIscsiInterface.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this AdapterHostIscsiInterface.
        The time when this managed object was last modified.  

        :return: The mod_time of this AdapterHostIscsiInterface.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this AdapterHostIscsiInterface.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this AdapterHostIscsiInterface.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this AdapterHostIscsiInterface.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this AdapterHostIscsiInterface.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this AdapterHostIscsiInterface.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this AdapterHostIscsiInterface.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this AdapterHostIscsiInterface.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this AdapterHostIscsiInterface.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this AdapterHostIscsiInterface.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this AdapterHostIscsiInterface.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this AdapterHostIscsiInterface.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this AdapterHostIscsiInterface.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this AdapterHostIscsiInterface.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this AdapterHostIscsiInterface.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this AdapterHostIscsiInterface.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this AdapterHostIscsiInterface.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this AdapterHostIscsiInterface.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this AdapterHostIscsiInterface.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this AdapterHostIscsiInterface.
        An array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this AdapterHostIscsiInterface.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this AdapterHostIscsiInterface.
        The versioning info for this managed object   

        :return: The version_context of this AdapterHostIscsiInterface.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this AdapterHostIscsiInterface.
        The versioning info for this managed object   

        :param version_context: The version_context of this AdapterHostIscsiInterface.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this AdapterHostIscsiInterface.

        :return: The device_mo_id of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this AdapterHostIscsiInterface.

        :param device_mo_id: The device_mo_id of this AdapterHostIscsiInterface.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this AdapterHostIscsiInterface.

        :return: The dn of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this AdapterHostIscsiInterface.

        :param dn: The dn of this AdapterHostIscsiInterface.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this AdapterHostIscsiInterface.

        :return: The rn of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this AdapterHostIscsiInterface.

        :param rn: The rn of this AdapterHostIscsiInterface.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this AdapterHostIscsiInterface.

        :return: The model of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this AdapterHostIscsiInterface.

        :param model: The model of this AdapterHostIscsiInterface.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this AdapterHostIscsiInterface.

        :return: The revision of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this AdapterHostIscsiInterface.

        :param revision: The revision of this AdapterHostIscsiInterface.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this AdapterHostIscsiInterface.

        :return: The serial of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this AdapterHostIscsiInterface.

        :param serial: The serial of this AdapterHostIscsiInterface.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this AdapterHostIscsiInterface.

        :return: The vendor of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this AdapterHostIscsiInterface.

        :param vendor: The vendor of this AdapterHostIscsiInterface.
        :type: str
        """

        self._vendor = vendor

    @property
    def adapter_unit(self):
        """
        Gets the adapter_unit of this AdapterHostIscsiInterface.

        :return: The adapter_unit of this AdapterHostIscsiInterface.
        :rtype: AdapterUnitRef
        """
        return self._adapter_unit

    @adapter_unit.setter
    def adapter_unit(self, adapter_unit):
        """
        Sets the adapter_unit of this AdapterHostIscsiInterface.

        :param adapter_unit: The adapter_unit of this AdapterHostIscsiInterface.
        :type: AdapterUnitRef
        """

        self._adapter_unit = adapter_unit

    @property
    def admin_state(self):
        """
        Gets the admin_state of this AdapterHostIscsiInterface.

        :return: The admin_state of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._admin_state

    @admin_state.setter
    def admin_state(self, admin_state):
        """
        Sets the admin_state of this AdapterHostIscsiInterface.

        :param admin_state: The admin_state of this AdapterHostIscsiInterface.
        :type: str
        """

        self._admin_state = admin_state

    @property
    def ep_dn(self):
        """
        Gets the ep_dn of this AdapterHostIscsiInterface.

        :return: The ep_dn of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._ep_dn

    @ep_dn.setter
    def ep_dn(self, ep_dn):
        """
        Sets the ep_dn of this AdapterHostIscsiInterface.

        :param ep_dn: The ep_dn of this AdapterHostIscsiInterface.
        :type: str
        """

        self._ep_dn = ep_dn

    @property
    def host_iscsi_interface_id(self):
        """
        Gets the host_iscsi_interface_id of this AdapterHostIscsiInterface.

        :return: The host_iscsi_interface_id of this AdapterHostIscsiInterface.
        :rtype: int
        """
        return self._host_iscsi_interface_id

    @host_iscsi_interface_id.setter
    def host_iscsi_interface_id(self, host_iscsi_interface_id):
        """
        Sets the host_iscsi_interface_id of this AdapterHostIscsiInterface.

        :param host_iscsi_interface_id: The host_iscsi_interface_id of this AdapterHostIscsiInterface.
        :type: int
        """

        self._host_iscsi_interface_id = host_iscsi_interface_id

    @property
    def host_visible(self):
        """
        Gets the host_visible of this AdapterHostIscsiInterface.

        :return: The host_visible of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._host_visible

    @host_visible.setter
    def host_visible(self, host_visible):
        """
        Sets the host_visible of this AdapterHostIscsiInterface.

        :param host_visible: The host_visible of this AdapterHostIscsiInterface.
        :type: str
        """

        self._host_visible = host_visible

    @property
    def mac_address(self):
        """
        Gets the mac_address of this AdapterHostIscsiInterface.

        :return: The mac_address of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this AdapterHostIscsiInterface.

        :param mac_address: The mac_address of this AdapterHostIscsiInterface.
        :type: str
        """

        self._mac_address = mac_address

    @property
    def name(self):
        """
        Gets the name of this AdapterHostIscsiInterface.

        :return: The name of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AdapterHostIscsiInterface.

        :param name: The name of this AdapterHostIscsiInterface.
        :type: str
        """

        self._name = name

    @property
    def oper_state(self):
        """
        Gets the oper_state of this AdapterHostIscsiInterface.

        :return: The oper_state of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this AdapterHostIscsiInterface.

        :param oper_state: The oper_state of this AdapterHostIscsiInterface.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """
        Gets the operability of this AdapterHostIscsiInterface.

        :return: The operability of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """
        Sets the operability of this AdapterHostIscsiInterface.

        :param operability: The operability of this AdapterHostIscsiInterface.
        :type: str
        """

        self._operability = operability

    @property
    def peer_dn(self):
        """
        Gets the peer_dn of this AdapterHostIscsiInterface.

        :return: The peer_dn of this AdapterHostIscsiInterface.
        :rtype: str
        """
        return self._peer_dn

    @peer_dn.setter
    def peer_dn(self, peer_dn):
        """
        Sets the peer_dn of this AdapterHostIscsiInterface.

        :param peer_dn: The peer_dn of this AdapterHostIscsiInterface.
        :type: str
        """

        self._peer_dn = peer_dn

    @property
    def registered_device(self):
        """
        Gets the registered_device of this AdapterHostIscsiInterface.

        :return: The registered_device of this AdapterHostIscsiInterface.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this AdapterHostIscsiInterface.

        :param registered_device: The registered_device of this AdapterHostIscsiInterface.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

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
        if not isinstance(other, AdapterHostIscsiInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
