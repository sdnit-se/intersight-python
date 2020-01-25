# coding: utf-8
"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations.   # noqa: E501

    The version of the OpenAPI document: 1.0.9-1295
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from intersight.api_client import ApiClient
from intersight.exceptions import (ApiTypeError, ApiValueError)


class TaskApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_task_pure_storage_scoped_inventory(
            self, task_pure_storage_scoped_inventory, **kwargs):  # noqa: E501
        """Create a 'task.PureStorageScopedInventory' resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_task_pure_storage_scoped_inventory(task_pure_storage_scoped_inventory, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TaskPureStorageScopedInventory task_pure_storage_scoped_inventory: The 'task.PureStorageScopedInventory' resource to create. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TaskPureStorageScopedInventory
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_task_pure_storage_scoped_inventory_with_http_info(
            task_pure_storage_scoped_inventory, **kwargs)  # noqa: E501

    def create_task_pure_storage_scoped_inventory_with_http_info(
            self, task_pure_storage_scoped_inventory, **kwargs):  # noqa: E501
        """Create a 'task.PureStorageScopedInventory' resource.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_task_pure_storage_scoped_inventory_with_http_info(task_pure_storage_scoped_inventory, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TaskPureStorageScopedInventory task_pure_storage_scoped_inventory: The 'task.PureStorageScopedInventory' resource to create. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TaskPureStorageScopedInventory, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['task_pure_storage_scoped_inventory']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_task_pure_storage_scoped_inventory" %
                    key)
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'task_pure_storage_scoped_inventory' is set
        if self.api_client.client_side_validation and (
                'task_pure_storage_scoped_inventory' not in local_var_params
                or  # noqa: E501
                local_var_params['task_pure_storage_scoped_inventory'] is None
        ):  # noqa: E501
            raise ApiValueError(
                "Missing the required parameter `task_pure_storage_scoped_inventory` when calling `create_task_pure_storage_scoped_inventory`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'task_pure_storage_scoped_inventory' in local_var_params:
            body_params = local_var_params[
                'task_pure_storage_scoped_inventory']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params[
            'Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
                ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['cookieAuth', 'oAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/task/PureStorageScopedInventories',
            'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaskPureStorageScopedInventory',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get(
                '_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
