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


class ComboPaymentTransaction(object):
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
        'account': 'Account',
        'payment_method': 'PaymentMethod',
        'transaction': 'PaymentTransaction',
        'payment_method_plugin_properties': 'list[PluginProperty]',
        'transaction_plugin_properties': 'list[PluginProperty]',
        'audit_logs': 'list[AuditLog]'
    }

    attribute_map = {
        'account': 'account',
        'payment_method': 'paymentMethod',
        'transaction': 'transaction',
        'payment_method_plugin_properties': 'paymentMethodPluginProperties',
        'transaction_plugin_properties': 'transactionPluginProperties',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, account=None, payment_method=None, transaction=None, payment_method_plugin_properties=None, transaction_plugin_properties=None, audit_logs=None, _configuration=None):  # noqa: E501
        """ComboPaymentTransaction - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account = None
        self._payment_method = None
        self._transaction = None
        self._payment_method_plugin_properties = None
        self._transaction_plugin_properties = None
        self._audit_logs = None
        self.discriminator = None

        if account is not None:
            self.account = account
        if payment_method is not None:
            self.payment_method = payment_method
        if transaction is not None:
            self.transaction = transaction
        if payment_method_plugin_properties is not None:
            self.payment_method_plugin_properties = payment_method_plugin_properties
        if transaction_plugin_properties is not None:
            self.transaction_plugin_properties = transaction_plugin_properties
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def account(self):
        """Gets the account of this ComboPaymentTransaction.  # noqa: E501


        :return: The account of this ComboPaymentTransaction.  # noqa: E501
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this ComboPaymentTransaction.


        :param account: The account of this ComboPaymentTransaction.  # noqa: E501
        :type: Account
        """

        self._account = account

    @property
    def payment_method(self):
        """Gets the payment_method of this ComboPaymentTransaction.  # noqa: E501


        :return: The payment_method of this ComboPaymentTransaction.  # noqa: E501
        :rtype: PaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this ComboPaymentTransaction.


        :param payment_method: The payment_method of this ComboPaymentTransaction.  # noqa: E501
        :type: PaymentMethod
        """

        self._payment_method = payment_method

    @property
    def transaction(self):
        """Gets the transaction of this ComboPaymentTransaction.  # noqa: E501


        :return: The transaction of this ComboPaymentTransaction.  # noqa: E501
        :rtype: PaymentTransaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this ComboPaymentTransaction.


        :param transaction: The transaction of this ComboPaymentTransaction.  # noqa: E501
        :type: PaymentTransaction
        """

        self._transaction = transaction

    @property
    def payment_method_plugin_properties(self):
        """Gets the payment_method_plugin_properties of this ComboPaymentTransaction.  # noqa: E501


        :return: The payment_method_plugin_properties of this ComboPaymentTransaction.  # noqa: E501
        :rtype: list[PluginProperty]
        """
        return self._payment_method_plugin_properties

    @payment_method_plugin_properties.setter
    def payment_method_plugin_properties(self, payment_method_plugin_properties):
        """Sets the payment_method_plugin_properties of this ComboPaymentTransaction.


        :param payment_method_plugin_properties: The payment_method_plugin_properties of this ComboPaymentTransaction.  # noqa: E501
        :type: list[PluginProperty]
        """

        self._payment_method_plugin_properties = payment_method_plugin_properties

    @property
    def transaction_plugin_properties(self):
        """Gets the transaction_plugin_properties of this ComboPaymentTransaction.  # noqa: E501


        :return: The transaction_plugin_properties of this ComboPaymentTransaction.  # noqa: E501
        :rtype: list[PluginProperty]
        """
        return self._transaction_plugin_properties

    @transaction_plugin_properties.setter
    def transaction_plugin_properties(self, transaction_plugin_properties):
        """Sets the transaction_plugin_properties of this ComboPaymentTransaction.


        :param transaction_plugin_properties: The transaction_plugin_properties of this ComboPaymentTransaction.  # noqa: E501
        :type: list[PluginProperty]
        """

        self._transaction_plugin_properties = transaction_plugin_properties

    @property
    def audit_logs(self):
        """Gets the audit_logs of this ComboPaymentTransaction.  # noqa: E501


        :return: The audit_logs of this ComboPaymentTransaction.  # noqa: E501
        :rtype: list[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this ComboPaymentTransaction.


        :param audit_logs: The audit_logs of this ComboPaymentTransaction.  # noqa: E501
        :type: list[AuditLog]
        """

        self._audit_logs = audit_logs

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
        if issubclass(ComboPaymentTransaction, dict):
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
        if not isinstance(other, ComboPaymentTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComboPaymentTransaction):
            return True

        return self.to_dict() != other.to_dict()