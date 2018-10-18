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


class MetaRelationshipDefinition(object):
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
        'api_access': 'str',
        'collection': 'bool',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'api_access': 'ApiAccess',
        'collection': 'Collection',
        'name': 'Name',
        'type': 'Type'
    }

    def __init__(self, api_access='NoAccess', collection=None, name=None, type=None):
        """
        MetaRelationshipDefinition - a model defined in Swagger
        """

        self._api_access = None
        self._collection = None
        self._name = None
        self._type = None

        if api_access is not None:
          self.api_access = api_access
        if collection is not None:
          self.collection = collection
        if name is not None:
          self.name = name
        if type is not None:
          self.type = type

    @property
    def api_access(self):
        """
        Gets the api_access of this MetaRelationshipDefinition.
        Api access definition for this relationship  

        :return: The api_access of this MetaRelationshipDefinition.
        :rtype: str
        """
        return self._api_access

    @api_access.setter
    def api_access(self, api_access):
        """
        Sets the api_access of this MetaRelationshipDefinition.
        Api access definition for this relationship  

        :param api_access: The api_access of this MetaRelationshipDefinition.
        :type: str
        """
        allowed_values = ["NoAccess", "ReadOnly", "CreateOnly", "ReadWrite", "WriteOnly", "ReadOnCreate"]
        if api_access not in allowed_values:
            raise ValueError(
                "Invalid value for `api_access` ({0}), must be one of {1}"
                .format(api_access, allowed_values)
            )

        self._api_access = api_access

    @property
    def collection(self):
        """
        Gets the collection of this MetaRelationshipDefinition.
        Specifies whether the relationship is a collection  

        :return: The collection of this MetaRelationshipDefinition.
        :rtype: bool
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """
        Sets the collection of this MetaRelationshipDefinition.
        Specifies whether the relationship is a collection  

        :param collection: The collection of this MetaRelationshipDefinition.
        :type: bool
        """

        self._collection = collection

    @property
    def name(self):
        """
        Gets the name of this MetaRelationshipDefinition.
        Name of the relationship  

        :return: The name of this MetaRelationshipDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MetaRelationshipDefinition.
        Name of the relationship  

        :param name: The name of this MetaRelationshipDefinition.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this MetaRelationshipDefinition.
        Fully qualified type of the foreign managed object.   

        :return: The type of this MetaRelationshipDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MetaRelationshipDefinition.
        Fully qualified type of the foreign managed object.   

        :param type: The type of this MetaRelationshipDefinition.
        :type: str
        """

        self._type = type

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
        if not isinstance(other, MetaRelationshipDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
