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


class Plan(object):
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
        'name': 'str',
        'pretty_name': 'str',
        'billing_period': 'str',
        'phases': 'list[Phase]'
    }

    attribute_map = {
        'name': 'name',
        'pretty_name': 'prettyName',
        'billing_period': 'billingPeriod',
        'phases': 'phases'
    }

    def __init__(self, name=None, pretty_name=None, billing_period=None, phases=None, _configuration=None):  # noqa: E501
        """Plan - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._pretty_name = None
        self._billing_period = None
        self._phases = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if pretty_name is not None:
            self.pretty_name = pretty_name
        if billing_period is not None:
            self.billing_period = billing_period
        if phases is not None:
            self.phases = phases

    @property
    def name(self):
        """Gets the name of this Plan.  # noqa: E501


        :return: The name of this Plan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Plan.


        :param name: The name of this Plan.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pretty_name(self):
        """Gets the pretty_name of this Plan.  # noqa: E501


        :return: The pretty_name of this Plan.  # noqa: E501
        :rtype: str
        """
        return self._pretty_name

    @pretty_name.setter
    def pretty_name(self, pretty_name):
        """Sets the pretty_name of this Plan.


        :param pretty_name: The pretty_name of this Plan.  # noqa: E501
        :type: str
        """

        self._pretty_name = pretty_name

    @property
    def billing_period(self):
        """Gets the billing_period of this Plan.  # noqa: E501


        :return: The billing_period of this Plan.  # noqa: E501
        :rtype: str
        """
        return self._billing_period

    @billing_period.setter
    def billing_period(self, billing_period):
        """Sets the billing_period of this Plan.


        :param billing_period: The billing_period of this Plan.  # noqa: E501
        :type: str
        """
        allowed_values = ["DAILY", "WEEKLY", "BIWEEKLY", "THIRTY_DAYS", "SIXTY_DAYS", "NINETY_DAYS", "MONTHLY", "BIMESTRIAL", "QUARTERLY", "TRIANNUAL", "BIANNUAL", "ANNUAL", "BIENNIAL", "NO_BILLING_PERIOD"]  # noqa: E501
        if (self._configuration.client_side_validation and
                billing_period not in allowed_values):
            raise ValueError(
                "Invalid value for `billing_period` ({0}), must be one of {1}"  # noqa: E501
                .format(billing_period, allowed_values)
            )

        self._billing_period = billing_period

    @property
    def phases(self):
        """Gets the phases of this Plan.  # noqa: E501


        :return: The phases of this Plan.  # noqa: E501
        :rtype: list[Phase]
        """
        return self._phases

    @phases.setter
    def phases(self, phases):
        """Sets the phases of this Plan.


        :param phases: The phases of this Plan.  # noqa: E501
        :type: list[Phase]
        """

        self._phases = phases

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
        if issubclass(Plan, dict):
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
        if not isinstance(other, Plan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Plan):
            return True

        return self.to_dict() != other.to_dict()