# coding: utf-8

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.22.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from killbill.api_client import ApiClient


class CreditApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_credits(self, body, x_killbill_created_by, **kwargs):  # noqa: E501
        """Create a credit  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_credits(body, x_killbill_created_by, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[InvoiceItem] body: (required)
        :param str x_killbill_created_by: (required)
        :param str x_killbill_reason:
        :param str x_killbill_comment:
        :param bool auto_commit:
        :param list[str] plugin_property:
        :return: list[InvoiceItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_credits_with_http_info(body, x_killbill_created_by, **kwargs)  # noqa: E501
        else:
            (data) = self.create_credits_with_http_info(body, x_killbill_created_by, **kwargs)  # noqa: E501
            return data

    def create_credits_with_http_info(self, body, x_killbill_created_by, **kwargs):  # noqa: E501
        """Create a credit  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_credits_with_http_info(body, x_killbill_created_by, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[InvoiceItem] body: (required)
        :param str x_killbill_created_by: (required)
        :param str x_killbill_reason:
        :param str x_killbill_comment:
        :param bool auto_commit:
        :param list[str] plugin_property:
        :return: list[InvoiceItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_killbill_created_by', 'x_killbill_reason', 'x_killbill_comment', 'auto_commit', 'plugin_property']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_credits" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_credits`")  # noqa: E501
        # verify the required parameter 'x_killbill_created_by' is set
        if ('x_killbill_created_by' not in params or
                params['x_killbill_created_by'] is None):
            raise ValueError("Missing the required parameter `x_killbill_created_by` when calling `create_credits`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'auto_commit' in params:
            query_params.append(('autoCommit', params['auto_commit']))  # noqa: E501
        if 'plugin_property' in params:
            query_params.append(('pluginProperty', params['plugin_property']))  # noqa: E501
            collection_formats['pluginProperty'] = 'multi'  # noqa: E501

        header_params = {}
        if 'x_killbill_created_by' in params:
            header_params['X-Killbill-CreatedBy'] = params['x_killbill_created_by']  # noqa: E501
        if 'x_killbill_reason' in params:
            header_params['X-Killbill-Reason'] = params['x_killbill_reason']  # noqa: E501
        if 'x_killbill_comment' in params:
            header_params['X-Killbill-Comment'] = params['x_killbill_comment']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Killbill Api Key', 'Killbill Api Secret', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/credits', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InvoiceItem]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_credit(self, credit_id, **kwargs):  # noqa: E501
        """Retrieve a credit by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_credit(credit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_id: (required)
        :return: InvoiceItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_credit_with_http_info(credit_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_credit_with_http_info(credit_id, **kwargs)  # noqa: E501
            return data

    def get_credit_with_http_info(self, credit_id, **kwargs):  # noqa: E501
        """Retrieve a credit by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_credit_with_http_info(credit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credit_id: (required)
        :return: InvoiceItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_credit" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credit_id' is set
        if ('credit_id' not in params or
                params['credit_id'] is None):
            raise ValueError("Missing the required parameter `credit_id` when calling `get_credit`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'credit_id' in params:
            path_params['creditId'] = params['credit_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Killbill Api Key', 'Killbill Api Secret', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/credits/{creditId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InvoiceItem',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
