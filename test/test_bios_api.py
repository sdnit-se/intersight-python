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
from intersight.api.bios_api import BiosApi  # noqa: E501
from intersight.rest import ApiException


class TestBiosApi(unittest.TestCase):
    """BiosApi unit test stubs"""
    def setUp(self):
        self.api = intersight.api.bios_api.BiosApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_bios_policy(self):
        """Test case for create_bios_policy

        Create a 'bios.Policy' resource.  # noqa: E501
        """
        pass

    def test_delete_bios_policy(self):
        """Test case for delete_bios_policy

        Delete a 'bios.Policy' resource.  # noqa: E501
        """
        pass

    def test_get_bios_boot_mode_by_moid(self):
        """Test case for get_bios_boot_mode_by_moid

        Read a 'bios.BootMode' resource.  # noqa: E501
        """
        pass

    def test_get_bios_boot_mode_list(self):
        """Test case for get_bios_boot_mode_list

        Read a 'bios.BootMode' resource.  # noqa: E501
        """
        pass

    def test_get_bios_policy_by_moid(self):
        """Test case for get_bios_policy_by_moid

        Read a 'bios.Policy' resource.  # noqa: E501
        """
        pass

    def test_get_bios_policy_list(self):
        """Test case for get_bios_policy_list

        Read a 'bios.Policy' resource.  # noqa: E501
        """
        pass

    def test_get_bios_unit_by_moid(self):
        """Test case for get_bios_unit_by_moid

        Read a 'bios.Unit' resource.  # noqa: E501
        """
        pass

    def test_get_bios_unit_list(self):
        """Test case for get_bios_unit_list

        Read a 'bios.Unit' resource.  # noqa: E501
        """
        pass

    def test_patch_bios_boot_mode(self):
        """Test case for patch_bios_boot_mode

        Update a 'bios.BootMode' resource.  # noqa: E501
        """
        pass

    def test_patch_bios_policy(self):
        """Test case for patch_bios_policy

        Update a 'bios.Policy' resource.  # noqa: E501
        """
        pass

    def test_patch_bios_unit(self):
        """Test case for patch_bios_unit

        Update a 'bios.Unit' resource.  # noqa: E501
        """
        pass

    def test_update_bios_boot_mode(self):
        """Test case for update_bios_boot_mode

        Update a 'bios.BootMode' resource.  # noqa: E501
        """
        pass

    def test_update_bios_policy(self):
        """Test case for update_bios_policy

        Update a 'bios.Policy' resource.  # noqa: E501
        """
        pass

    def test_update_bios_unit(self):
        """Test case for update_bios_unit

        Update a 'bios.Unit' resource.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
