# coding: utf-8
"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations.   # noqa: E501

    The version of the OpenAPI document: 1.0.9-1295
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import unittest

import intersight
from intersight.api.pci_api import PciApi  # noqa: E501
from intersight.rest import ApiException


class TestPciApi(unittest.TestCase):
    """PciApi unit test stubs"""
    def setUp(self):
        self.api = intersight.api.pci_api.PciApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_pci_coprocessor_card_by_moid(self):
        """Test case for get_pci_coprocessor_card_by_moid

        Read a 'pci.CoprocessorCard' resource.  # noqa: E501
        """
        pass

    def test_get_pci_coprocessor_card_list(self):
        """Test case for get_pci_coprocessor_card_list

        Read a 'pci.CoprocessorCard' resource.  # noqa: E501
        """
        pass

    def test_get_pci_device_by_moid(self):
        """Test case for get_pci_device_by_moid

        Read a 'pci.Device' resource.  # noqa: E501
        """
        pass

    def test_get_pci_device_list(self):
        """Test case for get_pci_device_list

        Read a 'pci.Device' resource.  # noqa: E501
        """
        pass

    def test_get_pci_link_by_moid(self):
        """Test case for get_pci_link_by_moid

        Read a 'pci.Link' resource.  # noqa: E501
        """
        pass

    def test_get_pci_link_list(self):
        """Test case for get_pci_link_list

        Read a 'pci.Link' resource.  # noqa: E501
        """
        pass

    def test_get_pci_switch_by_moid(self):
        """Test case for get_pci_switch_by_moid

        Read a 'pci.Switch' resource.  # noqa: E501
        """
        pass

    def test_get_pci_switch_list(self):
        """Test case for get_pci_switch_list

        Read a 'pci.Switch' resource.  # noqa: E501
        """
        pass

    def test_patch_pci_device(self):
        """Test case for patch_pci_device

        Update a 'pci.Device' resource.  # noqa: E501
        """
        pass

    def test_patch_pci_link(self):
        """Test case for patch_pci_link

        Update a 'pci.Link' resource.  # noqa: E501
        """
        pass

    def test_patch_pci_switch(self):
        """Test case for patch_pci_switch

        Update a 'pci.Switch' resource.  # noqa: E501
        """
        pass

    def test_update_pci_device(self):
        """Test case for update_pci_device

        Update a 'pci.Device' resource.  # noqa: E501
        """
        pass

    def test_update_pci_link(self):
        """Test case for update_pci_link

        Update a 'pci.Link' resource.  # noqa: E501
        """
        pass

    def test_update_pci_switch(self):
        """Test case for update_pci_switch

        Update a 'pci.Switch' resource.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
