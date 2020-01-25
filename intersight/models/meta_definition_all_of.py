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


class MetaDefinitionAllOf(object):
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
        'access_privileges': 'list[MetaAccessPrivilege]',
        'ancestor_classes': 'list[str]',
        'is_concrete': 'bool',
        'meta_type': 'str',
        'name': 'str',
        'namespace': 'str',
        'parent_class': 'str',
        'permission_supported': 'bool',
        'properties': 'list[MetaPropDefinition]',
        'rbac_resource': 'bool',
        'relationships': 'list[MetaRelationshipDefinition]',
        'rest_path': 'str',
        'version': 'str'
    }

    attribute_map = {
        'access_privileges': 'AccessPrivileges',
        'ancestor_classes': 'AncestorClasses',
        'is_concrete': 'IsConcrete',
        'meta_type': 'MetaType',
        'name': 'Name',
        'namespace': 'Namespace',
        'parent_class': 'ParentClass',
        'permission_supported': 'PermissionSupported',
        'properties': 'Properties',
        'rbac_resource': 'RbacResource',
        'relationships': 'Relationships',
        'rest_path': 'RestPath',
        'version': 'Version'
    }

    def __init__(self,
                 access_privileges=None,
                 ancestor_classes=None,
                 is_concrete=None,
                 meta_type='ManagedObject',
                 name=None,
                 namespace=None,
                 parent_class=None,
                 permission_supported=None,
                 properties=None,
                 rbac_resource=None,
                 relationships=None,
                 rest_path=None,
                 version=None,
                 local_vars_configuration=None):  # noqa: E501
        """MetaDefinitionAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_privileges = None
        self._ancestor_classes = None
        self._is_concrete = None
        self._meta_type = None
        self._name = None
        self._namespace = None
        self._parent_class = None
        self._permission_supported = None
        self._properties = None
        self._rbac_resource = None
        self._relationships = None
        self._rest_path = None
        self._version = None
        self.discriminator = None

        if access_privileges is not None:
            self.access_privileges = access_privileges
        if ancestor_classes is not None:
            self.ancestor_classes = ancestor_classes
        if is_concrete is not None:
            self.is_concrete = is_concrete
        if meta_type is not None:
            self.meta_type = meta_type
        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if parent_class is not None:
            self.parent_class = parent_class
        if permission_supported is not None:
            self.permission_supported = permission_supported
        if properties is not None:
            self.properties = properties
        if rbac_resource is not None:
            self.rbac_resource = rbac_resource
        if relationships is not None:
            self.relationships = relationships
        if rest_path is not None:
            self.rest_path = rest_path
        if version is not None:
            self.version = version

    @property
    def access_privileges(self):
        """Gets the access_privileges of this MetaDefinitionAllOf.  # noqa: E501


        :return: The access_privileges of this MetaDefinitionAllOf.  # noqa: E501
        :rtype: list[MetaAccessPrivilege]
        """
        return self._access_privileges

    @access_privileges.setter
    def access_privileges(self, access_privileges):
        """Sets the access_privileges of this MetaDefinitionAllOf.


        :param access_privileges: The access_privileges of this MetaDefinitionAllOf.  # noqa: E501
        :type: list[MetaAccessPrivilege]
        """

        self._access_privileges = access_privileges

    @property
    def ancestor_classes(self):
        """Gets the ancestor_classes of this MetaDefinitionAllOf.  # noqa: E501


        :return: The ancestor_classes of this MetaDefinitionAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._ancestor_classes

    @ancestor_classes.setter
    def ancestor_classes(self, ancestor_classes):
        """Sets the ancestor_classes of this MetaDefinitionAllOf.


        :param ancestor_classes: The ancestor_classes of this MetaDefinitionAllOf.  # noqa: E501
        :type: list[str]
        """

        self._ancestor_classes = ancestor_classes

    @property
    def is_concrete(self):
        """Gets the is_concrete of this MetaDefinitionAllOf.  # noqa: E501

        Boolean flag to specify whether the meta class is a concrete class or not.    # noqa: E501

        :return: The is_concrete of this MetaDefinitionAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._is_concrete

    @is_concrete.setter
    def is_concrete(self, is_concrete):
        """Sets the is_concrete of this MetaDefinitionAllOf.

        Boolean flag to specify whether the meta class is a concrete class or not.    # noqa: E501

        :param is_concrete: The is_concrete of this MetaDefinitionAllOf.  # noqa: E501
        :type: bool
        """

        self._is_concrete = is_concrete

    @property
    def meta_type(self):
        """Gets the meta_type of this MetaDefinitionAllOf.  # noqa: E501

        Indicates whether the meta class is a complex type or managed object.    # noqa: E501

        :return: The meta_type of this MetaDefinitionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._meta_type

    @meta_type.setter
    def meta_type(self, meta_type):
        """Sets the meta_type of this MetaDefinitionAllOf.

        Indicates whether the meta class is a complex type or managed object.    # noqa: E501

        :param meta_type: The meta_type of this MetaDefinitionAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["ManagedObject", "ComplexType"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and meta_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `meta_type` ({0}), must be one of {1}"  # noqa: E501
                .format(meta_type, allowed_values))

        self._meta_type = meta_type

    @property
    def name(self):
        """Gets the name of this MetaDefinitionAllOf.  # noqa: E501

        The fully-qualified class name of the Managed Object or complex type. For example, \"compute:Blade\" where the Managed Object is \"Blade\" and the package is 'compute'.    # noqa: E501

        :return: The name of this MetaDefinitionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetaDefinitionAllOf.

        The fully-qualified class name of the Managed Object or complex type. For example, \"compute:Blade\" where the Managed Object is \"Blade\" and the package is 'compute'.    # noqa: E501

        :param name: The name of this MetaDefinitionAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this MetaDefinitionAllOf.  # noqa: E501

        The namespace of the meta.    # noqa: E501

        :return: The namespace of this MetaDefinitionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this MetaDefinitionAllOf.

        The namespace of the meta.    # noqa: E501

        :param namespace: The namespace of this MetaDefinitionAllOf.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def parent_class(self):
        """Gets the parent_class of this MetaDefinitionAllOf.  # noqa: E501

        The fully-qualified name of the parent metaclass in the class inheritance hierarchy.    # noqa: E501

        :return: The parent_class of this MetaDefinitionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._parent_class

    @parent_class.setter
    def parent_class(self, parent_class):
        """Sets the parent_class of this MetaDefinitionAllOf.

        The fully-qualified name of the parent metaclass in the class inheritance hierarchy.    # noqa: E501

        :param parent_class: The parent_class of this MetaDefinitionAllOf.  # noqa: E501
        :type: str
        """

        self._parent_class = parent_class

    @property
    def permission_supported(self):
        """Gets the permission_supported of this MetaDefinitionAllOf.  # noqa: E501

        Boolean flag to specify whether instances of this class type can be specified in permissions for instance based access control. Permissions can be created for entire Intersight account or to a subset of resources (instance based access control). In the first release, permissions are supported for entire account or for a subset of organizations.     # noqa: E501

        :return: The permission_supported of this MetaDefinitionAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._permission_supported

    @permission_supported.setter
    def permission_supported(self, permission_supported):
        """Sets the permission_supported of this MetaDefinitionAllOf.

        Boolean flag to specify whether instances of this class type can be specified in permissions for instance based access control. Permissions can be created for entire Intersight account or to a subset of resources (instance based access control). In the first release, permissions are supported for entire account or for a subset of organizations.     # noqa: E501

        :param permission_supported: The permission_supported of this MetaDefinitionAllOf.  # noqa: E501
        :type: bool
        """

        self._permission_supported = permission_supported

    @property
    def properties(self):
        """Gets the properties of this MetaDefinitionAllOf.  # noqa: E501


        :return: The properties of this MetaDefinitionAllOf.  # noqa: E501
        :rtype: list[MetaPropDefinition]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this MetaDefinitionAllOf.


        :param properties: The properties of this MetaDefinitionAllOf.  # noqa: E501
        :type: list[MetaPropDefinition]
        """

        self._properties = properties

    @property
    def rbac_resource(self):
        """Gets the rbac_resource of this MetaDefinitionAllOf.  # noqa: E501

        Boolean flag to specify whether instances of this class type can be assigned to resource groups that are part of an organization for access control. Inventoried physical/logical objects which needs access control should have rbacResource=yes. These objects are not part of any organization by default like device registrations and should be assigned to organizations for access control. Profiles, policies, workflow definitions which are created by specifying organization need not have this flag set.     # noqa: E501

        :return: The rbac_resource of this MetaDefinitionAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._rbac_resource

    @rbac_resource.setter
    def rbac_resource(self, rbac_resource):
        """Sets the rbac_resource of this MetaDefinitionAllOf.

        Boolean flag to specify whether instances of this class type can be assigned to resource groups that are part of an organization for access control. Inventoried physical/logical objects which needs access control should have rbacResource=yes. These objects are not part of any organization by default like device registrations and should be assigned to organizations for access control. Profiles, policies, workflow definitions which are created by specifying organization need not have this flag set.     # noqa: E501

        :param rbac_resource: The rbac_resource of this MetaDefinitionAllOf.  # noqa: E501
        :type: bool
        """

        self._rbac_resource = rbac_resource

    @property
    def relationships(self):
        """Gets the relationships of this MetaDefinitionAllOf.  # noqa: E501


        :return: The relationships of this MetaDefinitionAllOf.  # noqa: E501
        :rtype: list[MetaRelationshipDefinition]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this MetaDefinitionAllOf.


        :param relationships: The relationships of this MetaDefinitionAllOf.  # noqa: E501
        :type: list[MetaRelationshipDefinition]
        """

        self._relationships = relationships

    @property
    def rest_path(self):
        """Gets the rest_path of this MetaDefinitionAllOf.  # noqa: E501

        Restful URL path for the meta.    # noqa: E501

        :return: The rest_path of this MetaDefinitionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._rest_path

    @rest_path.setter
    def rest_path(self, rest_path):
        """Sets the rest_path of this MetaDefinitionAllOf.

        Restful URL path for the meta.    # noqa: E501

        :param rest_path: The rest_path of this MetaDefinitionAllOf.  # noqa: E501
        :type: str
        """

        self._rest_path = rest_path

    @property
    def version(self):
        """Gets the version of this MetaDefinitionAllOf.  # noqa: E501

        The version of the service that defines the meta-data.     # noqa: E501

        :return: The version of this MetaDefinitionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MetaDefinitionAllOf.

        The version of the service that defines the meta-data.     # noqa: E501

        :param version: The version of this MetaDefinitionAllOf.  # noqa: E501
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
        if not isinstance(other, MetaDefinitionAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetaDefinitionAllOf):
            return True

        return self.to_dict() != other.to_dict()
