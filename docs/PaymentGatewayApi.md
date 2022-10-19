# killbill.PaymentGatewayApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_combo_form_descriptor**](PaymentGatewayApi.md#build_combo_form_descriptor) | **POST** /1.0/kb/paymentGateways/hosted/form | Combo API to generate form data to redirect the customer to the gateway
[**build_form_descriptor**](PaymentGatewayApi.md#build_form_descriptor) | **POST** /1.0/kb/paymentGateways/hosted/form/{accountId} | Generate form data to redirect the customer to the gateway
[**process_notification**](PaymentGatewayApi.md#process_notification) | **POST** /1.0/kb/paymentGateways/notification/{pluginName} | Process a gateway notification

# **build_combo_form_descriptor**
> HostedPaymentPageFormDescriptor build_combo_form_descriptor(body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, control_plugin_name=control_plugin_name, plugin_property=plugin_property)

Combo API to generate form data to redirect the customer to the gateway

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
api_instance = killbill.PaymentGatewayApi(killbill.ApiClient(configuration))
body = killbill.ComboHostedPaymentPage() # ComboHostedPaymentPage | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)

try:
    # Combo API to generate form data to redirect the customer to the gateway
    api_response = api_instance.build_combo_form_descriptor(body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, control_plugin_name=control_plugin_name, plugin_property=plugin_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentGatewayApi->build_combo_form_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ComboHostedPaymentPage**](ComboHostedPaymentPage.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**HostedPaymentPageFormDescriptor**](HostedPaymentPageFormDescriptor.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build_form_descriptor**
> HostedPaymentPageFormDescriptor build_form_descriptor(body, x_killbill_created_by, account_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, payment_method_id=payment_method_id, control_plugin_name=control_plugin_name, plugin_property=plugin_property)

Generate form data to redirect the customer to the gateway

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
api_instance = killbill.PaymentGatewayApi(killbill.ApiClient(configuration))
body = killbill.HostedPaymentPageFields() # HostedPaymentPageFields | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
account_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)
payment_method_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)

try:
    # Generate form data to redirect the customer to the gateway
    api_response = api_instance.build_form_descriptor(body, x_killbill_created_by, account_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, payment_method_id=payment_method_id, control_plugin_name=control_plugin_name, plugin_property=plugin_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentGatewayApi->build_form_descriptor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostedPaymentPageFields**](HostedPaymentPageFields.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **account_id** | [**str**](.md)|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 
 **payment_method_id** | [**str**](.md)|  | [optional] 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**HostedPaymentPageFormDescriptor**](HostedPaymentPageFormDescriptor.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_notification**
> process_notification(body, x_killbill_created_by, plugin_name, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, control_plugin_name=control_plugin_name, plugin_property=plugin_property)

Process a gateway notification

The response is built by the appropriate plugin

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
api_instance = killbill.PaymentGatewayApi(killbill.ApiClient(configuration))
body = 'body_example' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
plugin_name = 'plugin_name_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)
control_plugin_name = ['control_plugin_name_example'] # list[str] |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)

try:
    # Process a gateway notification
    api_instance.process_notification(body, x_killbill_created_by, plugin_name, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, control_plugin_name=control_plugin_name, plugin_property=plugin_property)
except ApiException as e:
    print("Exception when calling PaymentGatewayApi->process_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **plugin_name** | **str**|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 
 **control_plugin_name** | [**list[str]**](str.md)|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

