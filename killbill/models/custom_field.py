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


class CustomField(object):
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
        'custom_field_id': 'str',
        'object_id': 'str',
        'object_type': 'str',
        'name': 'str',
        'value': 'str',
        'audit_logs': 'list[AuditLog]'
    }

    attribute_map = {
        'custom_field_id': 'customFieldId',
        'object_id': 'objectId',
        'object_type': 'objectType',
        'name': 'name',
        'value': 'value',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, custom_field_id=None, object_id=None, object_type=None, name=None, value=None, audit_logs=None, _configuration=None):  # noqa: E501
        """CustomField - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._custom_field_id = None
        self._object_id = None
        self._object_type = None
        self._name = None
        self._value = None
        self._audit_logs = None
        self.discriminator = None

        if custom_field_id is not None:
            self.custom_field_id = custom_field_id
        if object_id is not None:
            self.object_id = object_id
        if object_type is not None:
            self.object_type = object_type
        self.name = name
        self.value = value
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def custom_field_id(self):
        """Gets the custom_field_id of this CustomField.  # noqa: E501


        :return: The custom_field_id of this CustomField.  # noqa: E501
        :rtype: str
        """
        return self._custom_field_id

    @custom_field_id.setter
    def custom_field_id(self, custom_field_id):
        """Sets the custom_field_id of this CustomField.


        :param custom_field_id: The custom_field_id of this CustomField.  # noqa: E501
        :type: str
        """

        self._custom_field_id = custom_field_id

    @property
    def object_id(self):
        """Gets the object_id of this CustomField.  # noqa: E501


        :return: The object_id of this CustomField.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this CustomField.


        :param object_id: The object_id of this CustomField.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def object_type(self):
        """Gets the object_type of this CustomField.  # noqa: E501


        :return: The object_type of this CustomField.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this CustomField.


        :param object_type: The object_type of this CustomField.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCOUNT", "ACCOUNT_EMAIL", "BLOCKING_STATES", "BUNDLE", "CUSTOM_FIELD", "INVOICE", "PAYMENT", "TRANSACTION", "INVOICE_ITEM", "INVOICE_PAYMENT", "SUBSCRIPTION", "SUBSCRIPTION_EVENT", "SERVICE_BROADCAST", "PAYMENT_ATTEMPT", "PAYMENT_METHOD", "TAG", "TAG_DEFINITION", "TENANT", "TENANT_KVS"]  # noqa: E501
        if (self._configuration.client_side_validation and
                object_type not in allowed_values):
            raise ValueError(
                "Invalid value for `object_type` ({0}), must be one of {1}"  # noqa: E501
                .format(object_type, allowed_values)
            )

        self._object_type = object_type

    @property
    def name(self):
        """Gets the name of this CustomField.  # noqa: E501


        :return: The name of this CustomField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomField.


        :param name: The name of this CustomField.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this CustomField.  # noqa: E501


        :return: The value of this CustomField.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomField.


        :param value: The value of this CustomField.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def audit_logs(self):
        """Gets the audit_logs of this CustomField.  # noqa: E501


        :return: The audit_logs of this CustomField.  # noqa: E501
        :rtype: list[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this CustomField.


        :param audit_logs: The audit_logs of this CustomField.  # noqa: E501
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
        if issubclass(CustomField, dict):
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
        if not isinstance(other, CustomField):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomField):
            return True

        return self.to_dict() != other.to_dict()
