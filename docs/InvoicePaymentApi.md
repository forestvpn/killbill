# killbill.InvoicePaymentApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_invoice_payment_transaction**](InvoicePaymentApi.md#complete_invoice_payment_transaction) | **PUT** /1.0/kb/invoicePayments/{paymentId} | Complete an existing transaction
[**create_chargeback**](InvoicePaymentApi.md#create_chargeback) | **POST** /1.0/kb/invoicePayments/{paymentId}/chargebacks | Record a chargeback
[**create_chargeback_reversal**](InvoicePaymentApi.md#create_chargeback_reversal) | **POST** /1.0/kb/invoicePayments/{paymentId}/chargebackReversals | Record a chargebackReversal
[**create_invoice_payment_custom_fields**](InvoicePaymentApi.md#create_invoice_payment_custom_fields) | **POST** /1.0/kb/invoicePayments/{paymentId}/customFields | Add custom fields to payment
[**create_invoice_payment_tags**](InvoicePaymentApi.md#create_invoice_payment_tags) | **POST** /1.0/kb/invoicePayments/{paymentId}/tags | Add tags to payment
[**create_refund_with_adjustments**](InvoicePaymentApi.md#create_refund_with_adjustments) | **POST** /1.0/kb/invoicePayments/{paymentId}/refunds | Refund a payment, and adjust the invoice if needed
[**delete_invoice_payment_custom_fields**](InvoicePaymentApi.md#delete_invoice_payment_custom_fields) | **DELETE** /1.0/kb/invoicePayments/{paymentId}/customFields | Remove custom fields from payment
[**delete_invoice_payment_tags**](InvoicePaymentApi.md#delete_invoice_payment_tags) | **DELETE** /1.0/kb/invoicePayments/{paymentId}/tags | Remove tags from payment
[**get_invoice_payment**](InvoicePaymentApi.md#get_invoice_payment) | **GET** /1.0/kb/invoicePayments/{paymentId} | Retrieve a payment by id
[**get_invoice_payment_audit_logs_with_history**](InvoicePaymentApi.md#get_invoice_payment_audit_logs_with_history) | **GET** /1.0/kb/invoicePayments/{invoicePaymentId}/auditLogsWithHistory | Retrieve invoice payment audit logs with history by id
[**get_invoice_payment_custom_fields**](InvoicePaymentApi.md#get_invoice_payment_custom_fields) | **GET** /1.0/kb/invoicePayments/{paymentId}/customFields | Retrieve payment custom fields
[**get_invoice_payment_tags**](InvoicePaymentApi.md#get_invoice_payment_tags) | **GET** /1.0/kb/invoicePayments/{paymentId}/tags | Retrieve payment tags
[**modify_invoice_payment_custom_fields**](InvoicePaymentApi.md#modify_invoice_payment_custom_fields) | **PUT** /1.0/kb/invoicePayments/{paymentId}/customFields | Modify custom fields to payment

# **complete_invoice_payment_transaction**
> complete_invoice_payment_transaction(body, x_killbill_created_by, payment_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, control_plugin_name=control_plugin_name, plugin_property=plugin_property)

Complete an existing transaction

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure API key authorization: Killbill Api Key
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiKey'] = 'Bearer'
# Configure API key authorization: Killbill Api Secret
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiSecret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiSecret'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.InvoicePaymentApi(killbill.ApiClient(configuration))
body = killbill.PaymentTransaction() # PaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
payment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)

try:
    # Complete an existing transaction
    api_instance.complete_invoice_payment_transaction(body, x_killbill_created_by, payment_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, control_plugin_name=control_plugin_name, plugin_property=plugin_property)
except ApiException as e:
    print("Exception when calling InvoicePaymentApi->complete_invoice_payment_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PaymentTransaction**](PaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **payment_id** | [**str**](.md)|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_chargeback**
> InvoicePayment create_chargeback(body, x_killbill_created_by, payment_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, plugin_property=plugin_property)

Record a chargeback

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure API key authorization: Killbill Api Key
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiKey'] = 'Bearer'
# Configure API key authorization: Killbill Api Secret
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiSecret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiSecret'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.InvoicePaymentApi(killbill.ApiClient(configuration))
body = killbill.InvoicePaymentTransaction() # InvoicePaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
payment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)

try:
    # Record a chargeback
    api_response = api_instance.create_chargeback(body, x_killbill_created_by, payment_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, plugin_property=plugin_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicePaymentApi->create_chargeback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoicePaymentTransaction**](InvoicePaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **payment_id** | [**str**](.md)|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InvoicePayment**](InvoicePayment.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_chargeback_reversal**
> InvoicePayment create_chargeback_reversal(body, x_killbill_created_by, payment_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, plugin_property=plugin_property)

Record a chargebackReversal

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure API key authorization: Killbill Api Key
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiKey'] = 'Bearer'
# Configure API key authorization: Killbill Api Secret
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiSecret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiSecret'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.InvoicePaymentApi(killbill.ApiClient(configuration))
body = killbill.InvoicePaymentTransaction() # InvoicePaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
payment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)

try:
    # Record a chargebackReversal
    api_response = api_instance.create_chargeback_reversal(body, x_killbill_created_by, payment_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, plugin_property=plugin_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicePaymentApi->create_chargeback_reversal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoicePaymentTransaction**](InvoicePaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **payment_id** | [**str**](.md)|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InvoicePayment**](InvoicePayment.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice_payment_custom_fields**
> list[CustomField] create_invoice_payment_custom_fields(body, x_killbill_created_by, payment_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add custom fields to payment

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure API key authorization: Killbill Api Key
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiKey'] = 'Bearer'
# Configure API key authorization: Killbill Api Secret
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiSecret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiSecret'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.InvoicePaymentApi(killbill.ApiClient(configuration))
body = [killbill.CustomField()] # list[CustomField] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
payment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add custom fields to payment
    api_response = api_instance.create_invoice_payment_custom_fields(body, x_killbill_created_by, payment_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicePaymentApi->create_invoice_payment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[CustomField]**](CustomField.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **payment_id** | [**str**](.md)|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**list[CustomField]**](CustomField.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_invoice_payment_tags**
> list[Tag] create_invoice_payment_tags(body, x_killbill_created_by, payment_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add tags to payment

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure API key authorization: Killbill Api Key
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiKey'] = 'Bearer'
# Configure API key authorization: Killbill Api Secret
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiSecret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiSecret'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.InvoicePaymentApi(killbill.ApiClient(configuration))
body = ['body_example'] # list[str] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
payment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add tags to payment
    api_response = api_instance.create_invoice_payment_tags(body, x_killbill_created_by, payment_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicePaymentApi->create_invoice_payment_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **payment_id** | [**str**](.md)|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_refund_with_adjustments**
> InvoicePayment create_refund_with_adjustments(body, x_killbill_created_by, payment_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, external_payment=external_payment, payment_method_id=payment_method_id, plugin_property=plugin_property)

Refund a payment, and adjust the invoice if needed

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure API key authorization: Killbill Api Key
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiKey'] = 'Bearer'
# Configure API key authorization: Killbill Api Secret
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiSecret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiSecret'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.InvoicePaymentApi(killbill.ApiClient(configuration))
body = killbill.InvoicePaymentTransaction() # InvoicePaymentTransaction | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
payment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)
external_payment = false # bool |  (optional) (default to false)
payment_method_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)

try:
    # Refund a payment, and adjust the invoice if needed
    api_response = api_instance.create_refund_with_adjustments(body, x_killbill_created_by, payment_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, external_payment=external_payment, payment_method_id=payment_method_id, plugin_property=plugin_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicePaymentApi->create_refund_with_adjustments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InvoicePaymentTransaction**](InvoicePaymentTransaction.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **payment_id** | [**str**](.md)|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 
 **external_payment** | **bool**|  | [optional] [default to false]
 **payment_method_id** | [**str**](.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**InvoicePayment**](InvoicePayment.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_payment_custom_fields**
> delete_invoice_payment_custom_fields(payment_id, x_killbill_created_by, custom_field=custom_field, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Remove custom fields from payment

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure API key authorization: Killbill Api Key
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiKey'] = 'Bearer'
# Configure API key authorization: Killbill Api Secret
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiSecret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiSecret'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.InvoicePaymentApi(killbill.ApiClient(configuration))
payment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
custom_field = ['custom_field_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Remove custom fields from payment
    api_instance.delete_invoice_payment_custom_fields(payment_id, x_killbill_created_by, custom_field=custom_field, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling InvoicePaymentApi->delete_invoice_payment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **custom_field** | [**list[str]**](str.md)|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_payment_tags**
> delete_invoice_payment_tags(payment_id, x_killbill_created_by, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Remove tags from payment

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure API key authorization: Killbill Api Key
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiKey'] = 'Bearer'
# Configure API key authorization: Killbill Api Secret
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiSecret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiSecret'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.InvoicePaymentApi(killbill.ApiClient(configuration))
payment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
tag_def = ['tag_def_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Remove tags from payment
    api_instance.delete_invoice_payment_tags(payment_id, x_killbill_created_by, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling InvoicePaymentApi->delete_invoice_payment_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **tag_def** | [**list[str]**](str.md)|  | [optional] 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_payment**
> InvoicePayment get_invoice_payment(payment_id, with_plugin_info=with_plugin_info, with_attempts=with_attempts, plugin_property=plugin_property, audit=audit)

Retrieve a payment by id

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure API key authorization: Killbill Api Key
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiKey'] = 'Bearer'
# Configure API key authorization: Killbill Api Secret
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiSecret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiSecret'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.InvoicePaymentApi(killbill.ApiClient(configuration))
payment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
with_plugin_info = false # bool |  (optional) (default to false)
with_attempts = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve a payment by id
    api_response = api_instance.get_invoice_payment(payment_id, with_plugin_info=with_plugin_info, with_attempts=with_attempts, plugin_property=plugin_property, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicePaymentApi->get_invoice_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
 **with_plugin_info** | **bool**|  | [optional] [default to false]
 **with_attempts** | **bool**|  | [optional] [default to false]
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**InvoicePayment**](InvoicePayment.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_payment_audit_logs_with_history**
> list[AuditLog] get_invoice_payment_audit_logs_with_history(invoice_payment_id)

Retrieve invoice payment audit logs with history by id

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure API key authorization: Killbill Api Key
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiKey'] = 'Bearer'
# Configure API key authorization: Killbill Api Secret
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiSecret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiSecret'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.InvoicePaymentApi(killbill.ApiClient(configuration))
invoice_payment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve invoice payment audit logs with history by id
    api_response = api_instance.get_invoice_payment_audit_logs_with_history(invoice_payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicePaymentApi->get_invoice_payment_audit_logs_with_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_payment_id** | [**str**](.md)|  | 

### Return type

[**list[AuditLog]**](AuditLog.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_payment_custom_fields**
> list[CustomField] get_invoice_payment_custom_fields(payment_id, audit=audit)

Retrieve payment custom fields

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure API key authorization: Killbill Api Key
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiKey'] = 'Bearer'
# Configure API key authorization: Killbill Api Secret
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiSecret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiSecret'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.InvoicePaymentApi(killbill.ApiClient(configuration))
payment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve payment custom fields
    api_response = api_instance.get_invoice_payment_custom_fields(payment_id, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicePaymentApi->get_invoice_payment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[CustomField]**](CustomField.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_payment_tags**
> list[Tag] get_invoice_payment_tags(payment_id, included_deleted=included_deleted, plugin_property=plugin_property, audit=audit)

Retrieve payment tags

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure API key authorization: Killbill Api Key
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiKey'] = 'Bearer'
# Configure API key authorization: Killbill Api Secret
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiSecret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiSecret'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.InvoicePaymentApi(killbill.ApiClient(configuration))
payment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
included_deleted = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve payment tags
    api_response = api_instance.get_invoice_payment_tags(payment_id, included_deleted=included_deleted, plugin_property=plugin_property, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicePaymentApi->get_invoice_payment_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)|  | 
 **included_deleted** | **bool**|  | [optional] [default to false]
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_invoice_payment_custom_fields**
> modify_invoice_payment_custom_fields(body, x_killbill_created_by, payment_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Modify custom fields to payment

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint

# Configure API key authorization: Killbill Api Key
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiKey'] = 'Bearer'
# Configure API key authorization: Killbill Api Secret
configuration = killbill.Configuration()
configuration.api_key['X-Killbill-ApiSecret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Killbill-ApiSecret'] = 'Bearer'# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.InvoicePaymentApi(killbill.ApiClient(configuration))
body = [killbill.CustomField()] # list[CustomField] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
payment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Modify custom fields to payment
    api_instance.modify_invoice_payment_custom_fields(body, x_killbill_created_by, payment_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling InvoicePaymentApi->modify_invoice_payment_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[CustomField]**](CustomField.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **payment_id** | [**str**](.md)|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

