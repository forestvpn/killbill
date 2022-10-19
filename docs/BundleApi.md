# killbill.BundleApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bundle_blocking_state**](BundleApi.md#add_bundle_blocking_state) | **POST** /1.0/kb/bundles/{bundleId}/block | Block a bundle
[**create_bundle_custom_fields**](BundleApi.md#create_bundle_custom_fields) | **POST** /1.0/kb/bundles/{bundleId}/customFields | Add custom fields to bundle
[**create_bundle_tags**](BundleApi.md#create_bundle_tags) | **POST** /1.0/kb/bundles/{bundleId}/tags | Add tags to bundle
[**delete_bundle_custom_fields**](BundleApi.md#delete_bundle_custom_fields) | **DELETE** /1.0/kb/bundles/{bundleId}/customFields | Remove custom fields from bundle
[**delete_bundle_tags**](BundleApi.md#delete_bundle_tags) | **DELETE** /1.0/kb/bundles/{bundleId}/tags | Remove tags from bundle
[**get_bundle**](BundleApi.md#get_bundle) | **GET** /1.0/kb/bundles/{bundleId} | Retrieve a bundle by id
[**get_bundle_audit_logs_with_history**](BundleApi.md#get_bundle_audit_logs_with_history) | **GET** /1.0/kb/bundles/{bundleId}/auditLogsWithHistory | Retrieve bundle audit logs with history by id
[**get_bundle_by_key**](BundleApi.md#get_bundle_by_key) | **GET** /1.0/kb/bundles | Retrieve a bundle by external key
[**get_bundle_custom_fields**](BundleApi.md#get_bundle_custom_fields) | **GET** /1.0/kb/bundles/{bundleId}/customFields | Retrieve bundle custom fields
[**get_bundle_tags**](BundleApi.md#get_bundle_tags) | **GET** /1.0/kb/bundles/{bundleId}/tags | Retrieve bundle tags
[**get_bundles**](BundleApi.md#get_bundles) | **GET** /1.0/kb/bundles/pagination | List bundles
[**modify_bundle_custom_fields**](BundleApi.md#modify_bundle_custom_fields) | **PUT** /1.0/kb/bundles/{bundleId}/customFields | Modify custom fields to bundle
[**pause_bundle**](BundleApi.md#pause_bundle) | **PUT** /1.0/kb/bundles/{bundleId}/pause | Pause a bundle
[**rename_external_key**](BundleApi.md#rename_external_key) | **PUT** /1.0/kb/bundles/{bundleId}/renameKey | Update a bundle externalKey
[**resume_bundle**](BundleApi.md#resume_bundle) | **PUT** /1.0/kb/bundles/{bundleId}/resume | Resume a bundle
[**search_bundles**](BundleApi.md#search_bundles) | **GET** /1.0/kb/bundles/search/{searchKey} | Search bundles
[**transfer_bundle**](BundleApi.md#transfer_bundle) | **POST** /1.0/kb/bundles/{bundleId} | Transfer a bundle to another account

# **add_bundle_blocking_state**
> list[BlockingState] add_bundle_blocking_state(body, x_killbill_created_by, bundle_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, requested_date=requested_date, plugin_property=plugin_property)

Block a bundle

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
body = killbill.BlockingState() # BlockingState | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
bundle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)
requested_date = '2013-10-20' # date |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)

try:
    # Block a bundle
    api_response = api_instance.add_bundle_blocking_state(body, x_killbill_created_by, bundle_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, requested_date=requested_date, plugin_property=plugin_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleApi->add_bundle_blocking_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BlockingState**](BlockingState.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **bundle_id** | [**str**](.md)|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 
 **requested_date** | **date**|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**list[BlockingState]**](BlockingState.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bundle_custom_fields**
> list[CustomField] create_bundle_custom_fields(body, x_killbill_created_by, bundle_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add custom fields to bundle

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
body = [killbill.CustomField()] # list[CustomField] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
bundle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add custom fields to bundle
    api_response = api_instance.create_bundle_custom_fields(body, x_killbill_created_by, bundle_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleApi->create_bundle_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[CustomField]**](CustomField.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **bundle_id** | [**str**](.md)|  | 
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

# **create_bundle_tags**
> list[Tag] create_bundle_tags(body, x_killbill_created_by, bundle_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Add tags to bundle

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
body = ['body_example'] # list[str] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
bundle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Add tags to bundle
    api_response = api_instance.create_bundle_tags(body, x_killbill_created_by, bundle_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleApi->create_bundle_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **bundle_id** | [**str**](.md)|  | 
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

# **delete_bundle_custom_fields**
> delete_bundle_custom_fields(bundle_id, x_killbill_created_by, custom_field=custom_field, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Remove custom fields from bundle

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
bundle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
custom_field = ['custom_field_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Remove custom fields from bundle
    api_instance.delete_bundle_custom_fields(bundle_id, x_killbill_created_by, custom_field=custom_field, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling BundleApi->delete_bundle_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | [**str**](.md)|  | 
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

# **delete_bundle_tags**
> delete_bundle_tags(bundle_id, x_killbill_created_by, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Remove tags from bundle

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
bundle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
tag_def = ['tag_def_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Remove tags from bundle
    api_instance.delete_bundle_tags(bundle_id, x_killbill_created_by, tag_def=tag_def, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling BundleApi->delete_bundle_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | [**str**](.md)|  | 
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

# **get_bundle**
> Bundle get_bundle(bundle_id, audit=audit)

Retrieve a bundle by id

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
bundle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve a bundle by id
    api_response = api_instance.get_bundle(bundle_id, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleApi->get_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | [**str**](.md)|  | 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**Bundle**](Bundle.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_audit_logs_with_history**
> list[AuditLog] get_bundle_audit_logs_with_history(bundle_id)

Retrieve bundle audit logs with history by id

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
bundle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve bundle audit logs with history by id
    api_response = api_instance.get_bundle_audit_logs_with_history(bundle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleApi->get_bundle_audit_logs_with_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | [**str**](.md)|  | 

### Return type

[**list[AuditLog]**](AuditLog.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_by_key**
> list[Bundle] get_bundle_by_key(external_key, included_deleted=included_deleted, audit=audit)

Retrieve a bundle by external key

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
external_key = 'external_key_example' # str | 
included_deleted = false # bool |  (optional) (default to false)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve a bundle by external key
    api_response = api_instance.get_bundle_by_key(external_key, included_deleted=included_deleted, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleApi->get_bundle_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_key** | **str**|  | 
 **included_deleted** | **bool**|  | [optional] [default to false]
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Bundle]**](Bundle.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_custom_fields**
> list[CustomField] get_bundle_custom_fields(bundle_id, audit=audit)

Retrieve bundle custom fields

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
bundle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve bundle custom fields
    api_response = api_instance.get_bundle_custom_fields(bundle_id, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleApi->get_bundle_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | [**str**](.md)|  | 
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[CustomField]**](CustomField.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundle_tags**
> list[Tag] get_bundle_tags(bundle_id, included_deleted=included_deleted, audit=audit)

Retrieve bundle tags

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
bundle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
included_deleted = false # bool |  (optional) (default to false)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Retrieve bundle tags
    api_response = api_instance.get_bundle_tags(bundle_id, included_deleted=included_deleted, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleApi->get_bundle_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | [**str**](.md)|  | 
 **included_deleted** | **bool**|  | [optional] [default to false]
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Tag]**](Tag.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundles**
> list[Bundle] get_bundles(offset=offset, limit=limit, audit=audit)

List bundles

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # List bundles
    api_response = api_instance.get_bundles(offset=offset, limit=limit, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleApi->get_bundles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Bundle]**](Bundle.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_bundle_custom_fields**
> modify_bundle_custom_fields(body, x_killbill_created_by, bundle_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Modify custom fields to bundle

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
body = [killbill.CustomField()] # list[CustomField] | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
bundle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Modify custom fields to bundle
    api_instance.modify_bundle_custom_fields(body, x_killbill_created_by, bundle_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling BundleApi->modify_bundle_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[CustomField]**](CustomField.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **bundle_id** | [**str**](.md)|  | 
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

# **pause_bundle**
> pause_bundle(bundle_id, x_killbill_created_by, requested_date=requested_date, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Pause a bundle

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
bundle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
requested_date = '2013-10-20' # date |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Pause a bundle
    api_instance.pause_bundle(bundle_id, x_killbill_created_by, requested_date=requested_date, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling BundleApi->pause_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **requested_date** | **date**|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
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

# **rename_external_key**
> rename_external_key(body, x_killbill_created_by, bundle_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Update a bundle externalKey

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
body = killbill.Bundle() # Bundle | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
bundle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Update a bundle externalKey
    api_instance.rename_external_key(body, x_killbill_created_by, bundle_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling BundleApi->rename_external_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Bundle**](Bundle.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **bundle_id** | [**str**](.md)|  | 
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

# **resume_bundle**
> resume_bundle(bundle_id, x_killbill_created_by, requested_date=requested_date, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)

Resume a bundle

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
bundle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
requested_date = '2013-10-20' # date |  (optional)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)

try:
    # Resume a bundle
    api_instance.resume_bundle(bundle_id, x_killbill_created_by, requested_date=requested_date, plugin_property=plugin_property, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment)
except ApiException as e:
    print("Exception when calling BundleApi->resume_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle_id** | [**str**](.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **requested_date** | **date**|  | [optional] 
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 
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

# **search_bundles**
> list[Bundle] search_bundles(search_key, offset=offset, limit=limit, audit=audit)

Search bundles

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
search_key = 'search_key_example' # str | 
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)
audit = 'NONE' # str |  (optional) (default to NONE)

try:
    # Search bundles
    api_response = api_instance.search_bundles(search_key, offset=offset, limit=limit, audit=audit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleApi->search_bundles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_key** | **str**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]
 **audit** | **str**|  | [optional] [default to NONE]

### Return type

[**list[Bundle]**](Bundle.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_bundle**
> Bundle transfer_bundle(body, x_killbill_created_by, bundle_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, requested_date=requested_date, billing_policy=billing_policy, plugin_property=plugin_property)

Transfer a bundle to another account

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
api_instance = killbill.BundleApi(killbill.ApiClient(configuration))
body = killbill.Bundle() # Bundle | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
bundle_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)
requested_date = '2013-10-20' # date |  (optional)
billing_policy = 'END_OF_TERM' # str |  (optional) (default to END_OF_TERM)
plugin_property = ['plugin_property_example'] # list[str] |  (optional)

try:
    # Transfer a bundle to another account
    api_response = api_instance.transfer_bundle(body, x_killbill_created_by, bundle_id, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, requested_date=requested_date, billing_policy=billing_policy, plugin_property=plugin_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleApi->transfer_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Bundle**](Bundle.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **bundle_id** | [**str**](.md)|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 
 **requested_date** | **date**|  | [optional] 
 **billing_policy** | **str**|  | [optional] [default to END_OF_TERM]
 **plugin_property** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**Bundle**](Bundle.md)

### Authorization

[Killbill Api Key](../README.md#Killbill Api Key), [Killbill Api Secret](../README.md#Killbill Api Secret), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

