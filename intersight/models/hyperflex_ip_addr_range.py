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


class HyperflexIpAddrRange(object):
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
        'end_addr': 'str',
        'gateway': 'str',
        'netmask': 'str',
        'start_addr': 'str'
    }

    attribute_map = {
        'end_addr': 'EndAddr',
        'gateway': 'Gateway',
        'netmask': 'Netmask',
        'start_addr': 'StartAddr'
    }

    def __init__(self, end_addr=None, gateway=None, netmask=None, start_addr=None):
        """
        HyperflexIpAddrRange - a model defined in Swagger
        """

        self._end_addr = None
        self._gateway = None
        self._netmask = None
        self._start_addr = None

        if end_addr is not None:
          self.end_addr = end_addr
        if gateway is not None:
          self.gateway = gateway
        if netmask is not None:
          self.netmask = netmask
        if start_addr is not None:
          self.start_addr = start_addr

    @property
    def end_addr(self):
        """
        Gets the end_addr of this HyperflexIpAddrRange.
        End address  

        :return: The end_addr of this HyperflexIpAddrRange.
        :rtype: str
        """
        return self._end_addr

    @end_addr.setter
    def end_addr(self, end_addr):
        """
        Sets the end_addr of this HyperflexIpAddrRange.
        End address  

        :param end_addr: The end_addr of this HyperflexIpAddrRange.
        :type: str
        """

        self._end_addr = end_addr

    @property
    def gateway(self):
        """
        Gets the gateway of this HyperflexIpAddrRange.
        Gateway  

        :return: The gateway of this HyperflexIpAddrRange.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """
        Sets the gateway of this HyperflexIpAddrRange.
        Gateway  

        :param gateway: The gateway of this HyperflexIpAddrRange.
        :type: str
        """

        self._gateway = gateway

    @property
    def netmask(self):
        """
        Gets the netmask of this HyperflexIpAddrRange.
        Netmask  

        :return: The netmask of this HyperflexIpAddrRange.
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """
        Sets the netmask of this HyperflexIpAddrRange.
        Netmask  

        :param netmask: The netmask of this HyperflexIpAddrRange.
        :type: str
        """

        self._netmask = netmask

    @property
    def start_addr(self):
        """
        Gets the start_addr of this HyperflexIpAddrRange.
        Start address   

        :return: The start_addr of this HyperflexIpAddrRange.
        :rtype: str
        """
        return self._start_addr

    @start_addr.setter
    def start_addr(self, start_addr):
        """
        Sets the start_addr of this HyperflexIpAddrRange.
        Start address   

        :param start_addr: The start_addr of this HyperflexIpAddrRange.
        :type: str
        """

        self._start_addr = start_addr

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
        if not isinstance(other, HyperflexIpAddrRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
