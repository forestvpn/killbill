# killbill.CreditApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credits**](CreditApi.md#create_credits) | **POST** /1.0/kb/credits | Create a credit
[**get_credit**](CreditApi.md#get_credit) | **GET** /1.0/kb/credits/{creditId} | Retrieve a credit by id

# **create_credits**
> list[InvoiceItem] create_credits(body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, auto_commit=auto_commit, plugin_property=plugin_property)

Create a credit

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
api_instance = killbill.CreditApi(killbill.ApiClient(configuration))
body = [killbill.InvoiceItem()] # list[InvoiceItem] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)
auto_commit = false # bool |  (optional) (default to false)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)

try:
    # Create a credit
    api_response = api_instance.create_credits(body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, auto_commit=auto_commit, plugin_property=plugin_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditApi->create_credits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[InvoiceItem]**](InvoiceItem.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 
 **auto_commit** | **bool**|  | [optional] [default to false]
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**list[InvoiceItem]**](InvoiceItem.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credit**
> InvoiceItem get_credit(credit_id)

Retrieve a credit by id

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
api_instance = killbill.CreditApi(killbill.ApiClient(configuration))
credit_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve a credit by id
    api_response = api_instance.get_credit(credit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditApi->get_credit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_id** | [**str**](.md)|  | 

### Return type

[**InvoiceItem**](InvoiceItem.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

