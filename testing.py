from rest_classes.RestEndpoint import RestEndpoint

endpoint = RestEndpoint(url='https://jsonplaceholder.typicode.com')
endpoint.set_headers(headers={'Content-type': 'application/json', 'Accept': 'application/json'})

payload1 = ['foo', {'bar': ('baz', None, 1.0, 2)}]
payload2 = [{'foo': 'bar'}]

call1 = endpoint.post(uri='/posts', payload=payload1)
print(call1['status_code'])
print(call1['body'])
print(call1['headers'])
print('-----------------------')

call2 = endpoint.post(uri='/posts', payload=payload2)
print(call2['status_code'])
print(call2['body'])
print(call2['headers'])
print('-----------------------')

call3 = endpoint.get(uri='/posts')
print(call3['status_code'])
print(call3['body'])
print(call3['headers'])
