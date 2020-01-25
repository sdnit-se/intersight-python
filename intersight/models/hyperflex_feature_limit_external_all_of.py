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


class HyperflexFeatureLimitExternalAllOf(object):
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
        'feature_limit_entries': 'list[HyperflexFeatureLimitEntry]',
        'app_catalog': 'HyperflexAppCatalog'
    }

    attribute_map = {
        'feature_limit_entries': 'FeatureLimitEntries',
        'app_catalog': 'AppCatalog'
    }

    def __init__(self,
                 feature_limit_entries=None,
                 app_catalog=None,
                 local_vars_configuration=None):  # noqa: E501
        """HyperflexFeatureLimitExternalAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._feature_limit_entries = None
        self._app_catalog = None
        self.discriminator = None

        if feature_limit_entries is not None:
            self.feature_limit_entries = feature_limit_entries
        if app_catalog is not None:
            self.app_catalog = app_catalog

    @property
    def feature_limit_entries(self):
        """Gets the feature_limit_entries of this HyperflexFeatureLimitExternalAllOf.  # noqa: E501


        :return: The feature_limit_entries of this HyperflexFeatureLimitExternalAllOf.  # noqa: E501
        :rtype: list[HyperflexFeatureLimitEntry]
        """
        return self._feature_limit_entries

    @feature_limit_entries.setter
    def feature_limit_entries(self, feature_limit_entries):
        """Sets the feature_limit_entries of this HyperflexFeatureLimitExternalAllOf.


        :param feature_limit_entries: The feature_limit_entries of this HyperflexFeatureLimitExternalAllOf.  # noqa: E501
        :type: list[HyperflexFeatureLimitEntry]
        """

        self._feature_limit_entries = feature_limit_entries

    @property
    def app_catalog(self):
        """Gets the app_catalog of this HyperflexFeatureLimitExternalAllOf.  # noqa: E501


        :return: The app_catalog of this HyperflexFeatureLimitExternalAllOf.  # noqa: E501
        :rtype: HyperflexAppCatalog
        """
        return self._app_catalog

    @app_catalog.setter
    def app_catalog(self, app_catalog):
        """Sets the app_catalog of this HyperflexFeatureLimitExternalAllOf.


        :param app_catalog: The app_catalog of this HyperflexFeatureLimitExternalAllOf.  # noqa: E501
        :type: HyperflexAppCatalog
        """

        self._app_catalog = app_catalog

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
        if not isinstance(other, HyperflexFeatureLimitExternalAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HyperflexFeatureLimitExternalAllOf):
            return True

        return self.to_dict() != other.to_dict()
