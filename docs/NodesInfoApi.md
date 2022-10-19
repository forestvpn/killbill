# killbill.NodesInfoApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nodes_info**](NodesInfoApi.md#get_nodes_info) | **GET** /1.0/kb/nodesInfo | Retrieve all the nodes infos
[**trigger_node_command**](NodesInfoApi.md#trigger_node_command) | **POST** /1.0/kb/nodesInfo | Trigger a node command

# **get_nodes_info**
> list[PluginInfo] get_nodes_info()

Retrieve all the nodes infos

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.NodesInfoApi(killbill.ApiClient(configuration))

try:
    # Retrieve all the nodes infos
    api_response = api_instance.get_nodes_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodesInfoApi->get_nodes_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PluginInfo]**](PluginInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_node_command**
> trigger_node_command(body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, local_node_only=local_node_only)

Trigger a node command

### Example
```python
from __future__ import print_function
import time
import killbill
from killbill.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = killbill.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = killbill.NodesInfoApi(killbill.ApiClient(configuration))
body = killbill.NodeCommand() # NodeCommand | 
x_killbill_created_by = 'x_killbill_created_by_example' # str | 
x_killbill_reason = 'x_killbill_reason_example' # str |  (optional)
x_killbill_comment = 'x_killbill_comment_example' # str |  (optional)
local_node_only = false # bool |  (optional) (default to false)

try:
    # Trigger a node command
    api_instance.trigger_node_command(body, x_killbill_created_by, x_killbill_reason=x_killbill_reason, x_killbill_comment=x_killbill_comment, local_node_only=local_node_only)
except ApiException as e:
    print("Exception when calling NodesInfoApi->trigger_node_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NodeCommand**](NodeCommand.md)|  | 
 **x_killbill_created_by** | **str**|  | 
 **x_killbill_reason** | **str**|  | [optional] 
 **x_killbill_comment** | **str**|  | [optional] 
 **local_node_only** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

