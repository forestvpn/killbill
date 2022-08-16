# coding: utf-8

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.22.22-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from killbill.configuration import Configuration


class RoleDefinition(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'role': 'str',
        'permissions': 'list[str]'
    }

    attribute_map = {
        'role': 'role',
        'permissions': 'permissions'
    }

    def __init__(self, role=None, permissions=None, _configuration=None):  # noqa: E501
        """RoleDefinition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._role = None
        self._permissions = None
        self.discriminator = None

        self.role = role
        self.permissions = permissions

    @property
    def role(self):
        """Gets the role of this RoleDefinition.  # noqa: E501


        :return: The role of this RoleDefinition.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this RoleDefinition.


        :param role: The role of this RoleDefinition.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def permissions(self):
        """Gets the permissions of this RoleDefinition.  # noqa: E501


        :return: The permissions of this RoleDefinition.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this RoleDefinition.


        :param permissions: The permissions of this RoleDefinition.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(RoleDefinition, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RoleDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleDefinition):
            return True

        return self.to_dict() != other.to_dict()