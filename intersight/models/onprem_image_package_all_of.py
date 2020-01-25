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


class OnpremImagePackageAllOf(object):
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
        'file_path': 'str',
        'file_sha': 'str',
        'file_size': 'int',
        'file_time': 'datetime',
        'filename': 'str',
        'name': 'str',
        'package_type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'file_path': 'FilePath',
        'file_sha': 'FileSha',
        'file_size': 'FileSize',
        'file_time': 'FileTime',
        'filename': 'Filename',
        'name': 'Name',
        'package_type': 'PackageType',
        'version': 'Version'
    }

    def __init__(self,
                 file_path=None,
                 file_sha=None,
                 file_size=None,
                 file_time=None,
                 filename=None,
                 name=None,
                 package_type=None,
                 version=None,
                 local_vars_configuration=None):  # noqa: E501
        """OnpremImagePackageAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_path = None
        self._file_sha = None
        self._file_size = None
        self._file_time = None
        self._filename = None
        self._name = None
        self._package_type = None
        self._version = None
        self.discriminator = None

        if file_path is not None:
            self.file_path = file_path
        if file_sha is not None:
            self.file_sha = file_sha
        if file_size is not None:
            self.file_size = file_size
        if file_time is not None:
            self.file_time = file_time
        if filename is not None:
            self.filename = filename
        if name is not None:
            self.name = name
        if package_type is not None:
            self.package_type = package_type
        if version is not None:
            self.version = version

    @property
    def file_path(self):
        """Gets the file_path of this OnpremImagePackageAllOf.  # noqa: E501

        Optional file path of the image package.    # noqa: E501

        :return: The file_path of this OnpremImagePackageAllOf.  # noqa: E501
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this OnpremImagePackageAllOf.

        Optional file path of the image package.    # noqa: E501

        :param file_path: The file_path of this OnpremImagePackageAllOf.  # noqa: E501
        :type: str
        """

        self._file_path = file_path

    @property
    def file_sha(self):
        """Gets the file_sha of this OnpremImagePackageAllOf.  # noqa: E501

        Image file's fingerprint. Fingerprint is calculated using SHA256 algorithm.    # noqa: E501

        :return: The file_sha of this OnpremImagePackageAllOf.  # noqa: E501
        :rtype: str
        """
        return self._file_sha

    @file_sha.setter
    def file_sha(self, file_sha):
        """Sets the file_sha of this OnpremImagePackageAllOf.

        Image file's fingerprint. Fingerprint is calculated using SHA256 algorithm.    # noqa: E501

        :param file_sha: The file_sha of this OnpremImagePackageAllOf.  # noqa: E501
        :type: str
        """

        self._file_sha = file_sha

    @property
    def file_size(self):
        """Gets the file_size of this OnpremImagePackageAllOf.  # noqa: E501

        Image file size in bytes.    # noqa: E501

        :return: The file_size of this OnpremImagePackageAllOf.  # noqa: E501
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this OnpremImagePackageAllOf.

        Image file size in bytes.    # noqa: E501

        :param file_size: The file_size of this OnpremImagePackageAllOf.  # noqa: E501
        :type: int
        """

        self._file_size = file_size

    @property
    def file_time(self):
        """Gets the file_time of this OnpremImagePackageAllOf.  # noqa: E501

        Image file's last modified date and time.    # noqa: E501

        :return: The file_time of this OnpremImagePackageAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._file_time

    @file_time.setter
    def file_time(self, file_time):
        """Sets the file_time of this OnpremImagePackageAllOf.

        Image file's last modified date and time.    # noqa: E501

        :param file_time: The file_time of this OnpremImagePackageAllOf.  # noqa: E501
        :type: datetime
        """

        self._file_time = file_time

    @property
    def filename(self):
        """Gets the filename of this OnpremImagePackageAllOf.  # noqa: E501

        Filename of the image package.    # noqa: E501

        :return: The filename of this OnpremImagePackageAllOf.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this OnpremImagePackageAllOf.

        Filename of the image package.    # noqa: E501

        :param filename: The filename of this OnpremImagePackageAllOf.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def name(self):
        """Gets the name of this OnpremImagePackageAllOf.  # noqa: E501

        Name of the software image package.    # noqa: E501

        :return: The name of this OnpremImagePackageAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OnpremImagePackageAllOf.

        Name of the software image package.    # noqa: E501

        :param name: The name of this OnpremImagePackageAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def package_type(self):
        """Gets the package_type of this OnpremImagePackageAllOf.  # noqa: E501

        Image package type (e.g. service, system etc.).    # noqa: E501

        :return: The package_type of this OnpremImagePackageAllOf.  # noqa: E501
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """Sets the package_type of this OnpremImagePackageAllOf.

        Image package type (e.g. service, system etc.).    # noqa: E501

        :param package_type: The package_type of this OnpremImagePackageAllOf.  # noqa: E501
        :type: str
        """

        self._package_type = package_type

    @property
    def version(self):
        """Gets the version of this OnpremImagePackageAllOf.  # noqa: E501

        Image package version string.     # noqa: E501

        :return: The version of this OnpremImagePackageAllOf.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OnpremImagePackageAllOf.

        Image package version string.     # noqa: E501

        :param version: The version of this OnpremImagePackageAllOf.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, OnpremImagePackageAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OnpremImagePackageAllOf):
            return True

        return self.to_dict() != other.to_dict()
