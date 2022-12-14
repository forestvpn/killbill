# coding: utf-8

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.22.22-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import killbill
from killbill.api.usage_api import UsageApi  # noqa: E501
from killbill.rest import ApiException


class TestUsageApi(unittest.TestCase):
    """UsageApi unit test stubs"""

    def setUp(self):
        self.api = killbill.api.usage_api.UsageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_all_usage(self):
        """Test case for get_all_usage

        Retrieve usage for a subscription  # noqa: E501
        """
        pass

    def test_get_usage(self):
        """Test case for get_usage

        Retrieve usage for a subscription and unit type  # noqa: E501
        """
        pass

    def test_record_usage(self):
        """Test case for record_usage

        Record usage for a subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
