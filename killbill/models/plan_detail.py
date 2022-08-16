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


class PlanDetail(object):
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
        'product': 'str',
        'plan': 'str',
        'price_list': 'str',
        'final_phase_billing_period': 'str',
        'final_phase_recurring_price': 'list[Price]'
    }

    attribute_map = {
        'product': 'product',
        'plan': 'plan',
        'price_list': 'priceList',
        'final_phase_billing_period': 'finalPhaseBillingPeriod',
        'final_phase_recurring_price': 'finalPhaseRecurringPrice'
    }

    def __init__(self, product=None, plan=None, price_list=None, final_phase_billing_period=None, final_phase_recurring_price=None, _configuration=None):  # noqa: E501
        """PlanDetail - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product = None
        self._plan = None
        self._price_list = None
        self._final_phase_billing_period = None
        self._final_phase_recurring_price = None
        self.discriminator = None

        if product is not None:
            self.product = product
        if plan is not None:
            self.plan = plan
        if price_list is not None:
            self.price_list = price_list
        if final_phase_billing_period is not None:
            self.final_phase_billing_period = final_phase_billing_period
        if final_phase_recurring_price is not None:
            self.final_phase_recurring_price = final_phase_recurring_price

    @property
    def product(self):
        """Gets the product of this PlanDetail.  # noqa: E501


        :return: The product of this PlanDetail.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this PlanDetail.


        :param product: The product of this PlanDetail.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def plan(self):
        """Gets the plan of this PlanDetail.  # noqa: E501


        :return: The plan of this PlanDetail.  # noqa: E501
        :rtype: str
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this PlanDetail.


        :param plan: The plan of this PlanDetail.  # noqa: E501
        :type: str
        """

        self._plan = plan

    @property
    def price_list(self):
        """Gets the price_list of this PlanDetail.  # noqa: E501


        :return: The price_list of this PlanDetail.  # noqa: E501
        :rtype: str
        """
        return self._price_list

    @price_list.setter
    def price_list(self, price_list):
        """Sets the price_list of this PlanDetail.


        :param price_list: The price_list of this PlanDetail.  # noqa: E501
        :type: str
        """

        self._price_list = price_list

    @property
    def final_phase_billing_period(self):
        """Gets the final_phase_billing_period of this PlanDetail.  # noqa: E501


        :return: The final_phase_billing_period of this PlanDetail.  # noqa: E501
        :rtype: str
        """
        return self._final_phase_billing_period

    @final_phase_billing_period.setter
    def final_phase_billing_period(self, final_phase_billing_period):
        """Sets the final_phase_billing_period of this PlanDetail.


        :param final_phase_billing_period: The final_phase_billing_period of this PlanDetail.  # noqa: E501
        :type: str
        """
        allowed_values = ["DAILY", "WEEKLY", "BIWEEKLY", "THIRTY_DAYS", "SIXTY_DAYS", "NINETY_DAYS", "MONTHLY", "BIMESTRIAL", "QUARTERLY", "TRIANNUAL", "BIANNUAL", "ANNUAL", "BIENNIAL", "NO_BILLING_PERIOD"]  # noqa: E501
        if (self._configuration.client_side_validation and
                final_phase_billing_period not in allowed_values):
            raise ValueError(
                "Invalid value for `final_phase_billing_period` ({0}), must be one of {1}"  # noqa: E501
                .format(final_phase_billing_period, allowed_values)
            )

        self._final_phase_billing_period = final_phase_billing_period

    @property
    def final_phase_recurring_price(self):
        """Gets the final_phase_recurring_price of this PlanDetail.  # noqa: E501


        :return: The final_phase_recurring_price of this PlanDetail.  # noqa: E501
        :rtype: list[Price]
        """
        return self._final_phase_recurring_price

    @final_phase_recurring_price.setter
    def final_phase_recurring_price(self, final_phase_recurring_price):
        """Sets the final_phase_recurring_price of this PlanDetail.


        :param final_phase_recurring_price: The final_phase_recurring_price of this PlanDetail.  # noqa: E501
        :type: list[Price]
        """

        self._final_phase_recurring_price = final_phase_recurring_price

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
        if issubclass(PlanDetail, dict):
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
        if not isinstance(other, PlanDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlanDetail):
            return True

        return self.to_dict() != other.to_dict()