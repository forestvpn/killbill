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
from killbill.api.nodes_info_api import NodesInfoApi  # noqa: E501
from killbill.rest import ApiException


class TestNodesInfoApi(unittest.TestCase):
    """NodesInfoApi unit test stubs"""

    def setUp(self):
        self.api = killbill.api.nodes_info_api.NodesInfoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_nodes_info(self):
        """Test case for get_nodes_info

        Retrieve all the nodes infos  # noqa: E501
        """
        pass

    def test_trigger_node_command(self):
        """Test case for trigger_node_command

        Trigger a node command  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
