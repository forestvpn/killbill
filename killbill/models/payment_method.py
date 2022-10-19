# coding: utf-8

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.22.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaymentMethod(object):
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
        'payment_method_id': 'str',
        'external_key': 'str',
        'account_id': 'str',
        'is_default': 'bool',
        'plugin_name': 'str',
        'plugin_info': 'PaymentMethodPluginDetail',
        'audit_logs': 'list[AuditLog]'
    }

    attribute_map = {
        'payment_method_id': 'paymentMethodId',
        'external_key': 'externalKey',
        'account_id': 'accountId',
        'is_default': 'isDefault',
        'plugin_name': 'pluginName',
        'plugin_info': 'pluginInfo',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, payment_method_id=None, external_key=None, account_id=None, is_default=None, plugin_name=None, plugin_info=None, audit_logs=None):  # noqa: E501
        """PaymentMethod - a model defined in Swagger"""  # noqa: E501
        self._payment_method_id = None
        self._external_key = None
        self._account_id = None
        self._is_default = None
        self._plugin_name = None
        self._plugin_info = None
        self._audit_logs = None
        self.discriminator = None
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if external_key is not None:
            self.external_key = external_key
        if account_id is not None:
            self.account_id = account_id
        if is_default is not None:
            self.is_default = is_default
        if plugin_name is not None:
            self.plugin_name = plugin_name
        if plugin_info is not None:
            self.plugin_info = plugin_info
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this PaymentMethod.  # noqa: E501


        :return: The payment_method_id of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this PaymentMethod.


        :param payment_method_id: The payment_method_id of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._payment_method_id = payment_method_id

    @property
    def external_key(self):
        """Gets the external_key of this PaymentMethod.  # noqa: E501


        :return: The external_key of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """Sets the external_key of this PaymentMethod.


        :param external_key: The external_key of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._external_key = external_key

    @property
    def account_id(self):
        """Gets the account_id of this PaymentMethod.  # noqa: E501


        :return: The account_id of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this PaymentMethod.


        :param account_id: The account_id of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def is_default(self):
        """Gets the is_default of this PaymentMethod.  # noqa: E501


        :return: The is_default of this PaymentMethod.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this PaymentMethod.


        :param is_default: The is_default of this PaymentMethod.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def plugin_name(self):
        """Gets the plugin_name of this PaymentMethod.  # noqa: E501


        :return: The plugin_name of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this PaymentMethod.


        :param plugin_name: The plugin_name of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._plugin_name = plugin_name

    @property
    def plugin_info(self):
        """Gets the plugin_info of this PaymentMethod.  # noqa: E501


        :return: The plugin_info of this PaymentMethod.  # noqa: E501
        :rtype: PaymentMethodPluginDetail
        """
        return self._plugin_info

    @plugin_info.setter
    def plugin_info(self, plugin_info):
        """Sets the plugin_info of this PaymentMethod.


        :param plugin_info: The plugin_info of this PaymentMethod.  # noqa: E501
        :type: PaymentMethodPluginDetail
        """

        self._plugin_info = plugin_info

    @property
    def audit_logs(self):
        """Gets the audit_logs of this PaymentMethod.  # noqa: E501


        :return: The audit_logs of this PaymentMethod.  # noqa: E501
        :rtype: list[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this PaymentMethod.


        :param audit_logs: The audit_logs of this PaymentMethod.  # noqa: E501
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
        if issubclass(PaymentMethod, dict):
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
        if not isinstance(other, PaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
