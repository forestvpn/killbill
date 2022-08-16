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


class PluginServiceInfo(object):
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
        'service_type_name': 'str',
        'registration_name': 'str'
    }

    attribute_map = {
        'service_type_name': 'serviceTypeName',
        'registration_name': 'registrationName'
    }

    def __init__(self, service_type_name=None, registration_name=None, _configuration=None):  # noqa: E501
        """PluginServiceInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._service_type_name = None
        self._registration_name = None
        self.discriminator = None

        if service_type_name is not None:
            self.service_type_name = service_type_name
        if registration_name is not None:
            self.registration_name = registration_name

    @property
    def service_type_name(self):
        """Gets the service_type_name of this PluginServiceInfo.  # noqa: E501


        :return: The service_type_name of this PluginServiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._service_type_name

    @service_type_name.setter
    def service_type_name(self, service_type_name):
        """Sets the service_type_name of this PluginServiceInfo.


        :param service_type_name: The service_type_name of this PluginServiceInfo.  # noqa: E501
        :type: str
        """

        self._service_type_name = service_type_name

    @property
    def registration_name(self):
        """Gets the registration_name of this PluginServiceInfo.  # noqa: E501


        :return: The registration_name of this PluginServiceInfo.  # noqa: E501
        :rtype: str
        """
        return self._registration_name

    @registration_name.setter
    def registration_name(self, registration_name):
        """Sets the registration_name of this PluginServiceInfo.


        :param registration_name: The registration_name of this PluginServiceInfo.  # noqa: E501
        :type: str
        """

        self._registration_name = registration_name

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
        if issubclass(PluginServiceInfo, dict):
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
        if not isinstance(other, PluginServiceInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PluginServiceInfo):
            return True

        return self.to_dict() != other.to_dict()
