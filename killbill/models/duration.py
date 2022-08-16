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


class Duration(object):
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
        'unit': 'str',
        'number': 'int'
    }

    attribute_map = {
        'unit': 'unit',
        'number': 'number'
    }

    def __init__(self, unit=None, number=None, _configuration=None):  # noqa: E501
        """Duration - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._unit = None
        self._number = None
        self.discriminator = None

        if unit is not None:
            self.unit = unit
        if number is not None:
            self.number = number

    @property
    def unit(self):
        """Gets the unit of this Duration.  # noqa: E501


        :return: The unit of this Duration.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Duration.


        :param unit: The unit of this Duration.  # noqa: E501
        :type: str
        """
        allowed_values = ["DAYS", "WEEKS", "MONTHS", "YEARS", "UNLIMITED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                unit not in allowed_values):
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"  # noqa: E501
                .format(unit, allowed_values)
            )

        self._unit = unit

    @property
    def number(self):
        """Gets the number of this Duration.  # noqa: E501


        :return: The number of this Duration.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Duration.


        :param number: The number of this Duration.  # noqa: E501
        :type: int
        """

        self._number = number

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
        if issubclass(Duration, dict):
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
        if not isinstance(other, Duration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Duration):
            return True

        return self.to_dict() != other.to_dict()