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
from killbill.api.tag_definition_api import TagDefinitionApi  # noqa: E501
from killbill.rest import ApiException


class TestTagDefinitionApi(unittest.TestCase):
    """TagDefinitionApi unit test stubs"""

    def setUp(self):
        self.api = killbill.api.tag_definition_api.TagDefinitionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tag_definition(self):
        """Test case for create_tag_definition

        Create a tag definition  # noqa: E501
        """
        pass

    def test_delete_tag_definition(self):
        """Test case for delete_tag_definition

        Delete a tag definition  # noqa: E501
        """
        pass

    def test_get_tag_definition(self):
        """Test case for get_tag_definition

        Retrieve a tag definition  # noqa: E501
        """
        pass

    def test_get_tag_definition_audit_logs_with_history(self):
        """Test case for get_tag_definition_audit_logs_with_history

        Retrieve tag definition audit logs with history by id  # noqa: E501
        """
        pass

    def test_get_tag_definitions(self):
        """Test case for get_tag_definitions

        List tag definitions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
