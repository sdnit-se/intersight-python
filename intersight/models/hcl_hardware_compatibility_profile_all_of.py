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


class HclHardwareCompatibilityProfileAllOf(object):
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
        'driver_iso_url': 'str',
        'error_code': 'str',
        'id': 'str',
        'os_vendor': 'str',
        'os_version': 'str',
        'processor_model': 'str',
        'products': 'list[HclProduct]',
        'server_model': 'str',
        'server_revision': 'str',
        'ucs_version': 'str',
        'version_type': 'str'
    }

    attribute_map = {
        'driver_iso_url': 'DriverIsoUrl',
        'error_code': 'ErrorCode',
        'id': 'Id',
        'os_vendor': 'OsVendor',
        'os_version': 'OsVersion',
        'processor_model': 'ProcessorModel',
        'products': 'Products',
        'server_model': 'ServerModel',
        'server_revision': 'ServerRevision',
        'ucs_version': 'UcsVersion',
        'version_type': 'VersionType'
    }

    def __init__(self,
                 driver_iso_url=None,
                 error_code='Success',
                 id=None,
                 os_vendor=None,
                 os_version=None,
                 processor_model=None,
                 products=None,
                 server_model=None,
                 server_revision=None,
                 ucs_version=None,
                 version_type='UCSM',
                 local_vars_configuration=None):  # noqa: E501
        """HclHardwareCompatibilityProfileAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._driver_iso_url = None
        self._error_code = None
        self._id = None
        self._os_vendor = None
        self._os_version = None
        self._processor_model = None
        self._products = None
        self._server_model = None
        self._server_revision = None
        self._ucs_version = None
        self._version_type = None
        self.discriminator = None

        if driver_iso_url is not None:
            self.driver_iso_url = driver_iso_url
        if error_code is not None:
            self.error_code = error_code
        if id is not None:
            self.id = id
        if os_vendor is not None:
            self.os_vendor = os_vendor
        if os_version is not None:
            self.os_version = os_version
        if processor_model is not None:
            self.processor_model = processor_model
        if products is not None:
            self.products = products
        if server_model is not None:
            self.server_model = server_model
        if server_revision is not None:
            self.server_revision = server_revision
        if ucs_version is not None:
            self.ucs_version = ucs_version
        if version_type is not None:
            self.version_type = version_type

    @property
    def driver_iso_url(self):
        """Gets the driver_iso_url of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501

        Url for the ISO with the drivers supported for the server.    # noqa: E501

        :return: The driver_iso_url of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :rtype: str
        """
        return self._driver_iso_url

    @driver_iso_url.setter
    def driver_iso_url(self, driver_iso_url):
        """Sets the driver_iso_url of this HclHardwareCompatibilityProfileAllOf.

        Url for the ISO with the drivers supported for the server.    # noqa: E501

        :param driver_iso_url: The driver_iso_url of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :type: str
        """

        self._driver_iso_url = driver_iso_url

    @property
    def error_code(self):
        """Gets the error_code of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501

        Error code indicating the compatibility status.    # noqa: E501

        :return: The error_code of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this HclHardwareCompatibilityProfileAllOf.

        Error code indicating the compatibility status.    # noqa: E501

        :param error_code: The error_code of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Success", "Unknown", "UnknownServer", "InvalidUcsVersion",
            "ProcessorNotSupported", "OSNotSupported", "OSUnknown",
            "UCSVersionNotSupported",
            "UcsVersionServerOSCombinationNotSupported", "ProductUnknown",
            "ProductNotSupported", "DriverNameNotSupported",
            "FirmwareVersionNotSupported", "DriverVersionNotSupported",
            "FirmwareVersionDriverVersionCombinationNotSupported",
            "FirmwareVersionAndDriverVersionNotSupported",
            "FirmwareVersionAndDriverNameNotSupported", "InternalError",
            "MarshallingError", "Exempted"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and error_code not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `error_code` ({0}), must be one of {1}"  # noqa: E501
                .format(error_code, allowed_values))

        self._error_code = error_code

    @property
    def id(self):
        """Gets the id of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501

        Identifier of the hardware compatibility profile.    # noqa: E501

        :return: The id of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HclHardwareCompatibilityProfileAllOf.

        Identifier of the hardware compatibility profile.    # noqa: E501

        :param id: The id of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def os_vendor(self):
        """Gets the os_vendor of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501

        Vendor of the Operating System running on the server.    # noqa: E501

        :return: The os_vendor of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :rtype: str
        """
        return self._os_vendor

    @os_vendor.setter
    def os_vendor(self, os_vendor):
        """Sets the os_vendor of this HclHardwareCompatibilityProfileAllOf.

        Vendor of the Operating System running on the server.    # noqa: E501

        :param os_vendor: The os_vendor of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :type: str
        """

        self._os_vendor = os_vendor

    @property
    def os_version(self):
        """Gets the os_version of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501

        Version of the Operating System running on the server.    # noqa: E501

        :return: The os_version of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this HclHardwareCompatibilityProfileAllOf.

        Version of the Operating System running on the server.    # noqa: E501

        :param os_version: The os_version of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :type: str
        """

        self._os_version = os_version

    @property
    def processor_model(self):
        """Gets the processor_model of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501

        Model of the processor present in the server.    # noqa: E501

        :return: The processor_model of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :rtype: str
        """
        return self._processor_model

    @processor_model.setter
    def processor_model(self, processor_model):
        """Sets the processor_model of this HclHardwareCompatibilityProfileAllOf.

        Model of the processor present in the server.    # noqa: E501

        :param processor_model: The processor_model of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :type: str
        """

        self._processor_model = processor_model

    @property
    def products(self):
        """Gets the products of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501


        :return: The products of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :rtype: list[HclProduct]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this HclHardwareCompatibilityProfileAllOf.


        :param products: The products of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :type: list[HclProduct]
        """

        self._products = products

    @property
    def server_model(self):
        """Gets the server_model of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501

        Model of the server as returned by UCSM/CIMC XML API.    # noqa: E501

        :return: The server_model of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :rtype: str
        """
        return self._server_model

    @server_model.setter
    def server_model(self, server_model):
        """Sets the server_model of this HclHardwareCompatibilityProfileAllOf.

        Model of the server as returned by UCSM/CIMC XML API.    # noqa: E501

        :param server_model: The server_model of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :type: str
        """

        self._server_model = server_model

    @property
    def server_revision(self):
        """Gets the server_revision of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501

        Revision of the server model.    # noqa: E501

        :return: The server_revision of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :rtype: str
        """
        return self._server_revision

    @server_revision.setter
    def server_revision(self, server_revision):
        """Sets the server_revision of this HclHardwareCompatibilityProfileAllOf.

        Revision of the server model.    # noqa: E501

        :param server_revision: The server_revision of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :type: str
        """

        self._server_revision = server_revision

    @property
    def ucs_version(self):
        """Gets the ucs_version of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501

        Version of the UCS software.    # noqa: E501

        :return: The ucs_version of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ucs_version

    @ucs_version.setter
    def ucs_version(self, ucs_version):
        """Sets the ucs_version of this HclHardwareCompatibilityProfileAllOf.

        Version of the UCS software.    # noqa: E501

        :param ucs_version: The ucs_version of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :type: str
        """

        self._ucs_version = ucs_version

    @property
    def version_type(self):
        """Gets the version_type of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501

        Type of the UCS version indicating whether it is a UCSM release vesion or a IMC release.     # noqa: E501

        :return: The version_type of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :rtype: str
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        """Sets the version_type of this HclHardwareCompatibilityProfileAllOf.

        Type of the UCS version indicating whether it is a UCSM release vesion or a IMC release.     # noqa: E501

        :param version_type: The version_type of this HclHardwareCompatibilityProfileAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["UCSM", "IMC"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and version_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `version_type` ({0}), must be one of {1}"  # noqa: E501
                .format(version_type, allowed_values))

        self._version_type = version_type

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
        if not isinstance(other, HclHardwareCompatibilityProfileAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HclHardwareCompatibilityProfileAllOf):
            return True

        return self.to_dict() != other.to_dict()
