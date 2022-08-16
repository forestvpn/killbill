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


class AuditLog(object):
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
        'change_type': 'str',
        'change_date': 'datetime',
        'object_type': 'str',
        'object_id': 'str',
        'changed_by': 'str',
        'reason_code': 'str',
        'comments': 'str',
        'user_token': 'str',
        'history': 'Entity'
    }

    attribute_map = {
        'change_type': 'changeType',
        'change_date': 'changeDate',
        'object_type': 'objectType',
        'object_id': 'objectId',
        'changed_by': 'changedBy',
        'reason_code': 'reasonCode',
        'comments': 'comments',
        'user_token': 'userToken',
        'history': 'history'
    }

    def __init__(self, change_type=None, change_date=None, object_type=None, object_id=None, changed_by=None, reason_code=None, comments=None, user_token=None, history=None, _configuration=None):  # noqa: E501
        """AuditLog - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._change_type = None
        self._change_date = None
        self._object_type = None
        self._object_id = None
        self._changed_by = None
        self._reason_code = None
        self._comments = None
        self._user_token = None
        self._history = None
        self.discriminator = None

        if change_type is not None:
            self.change_type = change_type
        if change_date is not None:
            self.change_date = change_date
        if object_type is not None:
            self.object_type = object_type
        if object_id is not None:
            self.object_id = object_id
        if changed_by is not None:
            self.changed_by = changed_by
        if reason_code is not None:
            self.reason_code = reason_code
        if comments is not None:
            self.comments = comments
        if user_token is not None:
            self.user_token = user_token
        if history is not None:
            self.history = history

    @property
    def change_type(self):
        """Gets the change_type of this AuditLog.  # noqa: E501


        :return: The change_type of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """Sets the change_type of this AuditLog.


        :param change_type: The change_type of this AuditLog.  # noqa: E501
        :type: str
        """

        self._change_type = change_type

    @property
    def change_date(self):
        """Gets the change_date of this AuditLog.  # noqa: E501


        :return: The change_date of this AuditLog.  # noqa: E501
        :rtype: datetime
        """
        return self._change_date

    @change_date.setter
    def change_date(self, change_date):
        """Sets the change_date of this AuditLog.


        :param change_date: The change_date of this AuditLog.  # noqa: E501
        :type: datetime
        """

        self._change_date = change_date

    @property
    def object_type(self):
        """Gets the object_type of this AuditLog.  # noqa: E501


        :return: The object_type of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this AuditLog.


        :param object_type: The object_type of this AuditLog.  # noqa: E501
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
    def object_id(self):
        """Gets the object_id of this AuditLog.  # noqa: E501


        :return: The object_id of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this AuditLog.


        :param object_id: The object_id of this AuditLog.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def changed_by(self):
        """Gets the changed_by of this AuditLog.  # noqa: E501


        :return: The changed_by of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._changed_by

    @changed_by.setter
    def changed_by(self, changed_by):
        """Sets the changed_by of this AuditLog.


        :param changed_by: The changed_by of this AuditLog.  # noqa: E501
        :type: str
        """

        self._changed_by = changed_by

    @property
    def reason_code(self):
        """Gets the reason_code of this AuditLog.  # noqa: E501


        :return: The reason_code of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._reason_code

    @reason_code.setter
    def reason_code(self, reason_code):
        """Sets the reason_code of this AuditLog.


        :param reason_code: The reason_code of this AuditLog.  # noqa: E501
        :type: str
        """

        self._reason_code = reason_code

    @property
    def comments(self):
        """Gets the comments of this AuditLog.  # noqa: E501


        :return: The comments of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this AuditLog.


        :param comments: The comments of this AuditLog.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def user_token(self):
        """Gets the user_token of this AuditLog.  # noqa: E501


        :return: The user_token of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._user_token

    @user_token.setter
    def user_token(self, user_token):
        """Sets the user_token of this AuditLog.


        :param user_token: The user_token of this AuditLog.  # noqa: E501
        :type: str
        """

        self._user_token = user_token

    @property
    def history(self):
        """Gets the history of this AuditLog.  # noqa: E501


        :return: The history of this AuditLog.  # noqa: E501
        :rtype: Entity
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this AuditLog.


        :param history: The history of this AuditLog.  # noqa: E501
        :type: Entity
        """

        self._history = history

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
        if issubclass(AuditLog, dict):
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
        if not isinstance(other, AuditLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuditLog):
            return True

        return self.to_dict() != other.to_dict()
