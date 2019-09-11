from rest_classes.RestEndpoint import RestEndpoint
import json

endpoint = RestEndpoint(url='https://jsonplaceholder.typicode.com')

headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

endpoint.set_headers(headers=headers)

payload = ['foo', {'bar': ('baz', None, 1.0, 2)}]

status = endpoint.post(uri='/posts', payload=payload)
print(status['status_code'])
print(status['body'])

print(endpoint.url + '/posts')
print(json.dumps(payload))
print(payload)
