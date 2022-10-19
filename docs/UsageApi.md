# killbill.UsageApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_usage**](UsageApi.md#get_all_usage) | **GET** /1.0/kb/usages/{subscriptionId} | Retrieve usage for a subscription
[**get_usage**](UsageApi.md#get_usage) | **GET** /1.0/kb/usages/{subscriptionId}/{unitType} | Retrieve usage for a subscription and unit type
[**record_usage**](UsageApi.md#record_usage) | **POST** /1.0/kb/usages | Record usage for a subscription

# **get_all_usage**
> RolledUpUsage get_all_usage(subscription_id, start_date=start_date, end_date=end_date)

Retrieve usage for a subscription

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
api_instance = killbill.UsageApi(killbill.ApiClient(configuration))
subscription_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
start_date = '2013-10-20' # date |  (optional)
end_date = '2013-10-20' # date |  (optional)

try:
    # Retrieve usage for a subscription
    api_response = api_instance.get_all_usage(subscription_id, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_all_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
 **start_date** | **date**|  | [optional] 
 **end_date** | **date**|  | [optional] 

### Return type

[**RolledUpUsage**](RolledUpUsage.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_usage**
> RolledUpUsage get_usage(subscription_id, unit_type, start_date=start_date, end_date=end_date)

Retrieve usage for a subscription and unit type

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
api_instance = killbill.UsageApi(killbill.ApiClient(configuration))
subscription_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
unit_type = 'unit_type_example' # str | 
start_date = '2013-10-20' # date |  (optional)
end_date = '2013-10-20' # date |  (optional)

try:
    # Retrieve usage for a subscription and unit type
    api_response = api_instance.get_usage(subscription_id, unit_type, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | [**str**](.md)|  | 
 **unit_type** | **str**|  | 
 **start_date** | **date**|  | [optional] 
 **end_date** | **date**|  | [optional] 

### Return type

[**RolledUpUsage**](RolledUpUsage.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_usage**
> record_usage(body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Record usage for a subscription

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
api_instance = killbill.UsageApi(killbill.ApiClient(configuration))
body = killbill.SubscriptionUsageRecord() # SubscriptionUsageRecord | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Record usage for a subscription
    api_instance.record_usage(body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling UsageApi->record_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionUsageRecord**](SubscriptionUsageRecord.md)|  | 
 **x_killbill_created_by** | **str**|  | 
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

