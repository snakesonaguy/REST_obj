import requests
import logging
import json


class RestEndpoint:

    def __init__(self, url=None, username=None, password=None):

        self.url = url
        self.username = username
        self.password = password
        self.token = None
        self.headers = None

    def set_headers(self, headers=None):

        self.headers = headers

    def post(self, uri=None, payload=None, basic_auth=True, token_auth=False):

        if (uri is None) or (payload is None):
            logging.warning('Valid URI and payload required to make POST')
            return

        if basic_auth:
            auth = (self.username, self.password)
            target = self.url + uri
            req = requests.post(target, auth=auth, headers=self.headers, data=json.dumps(payload))
            res = {}

            if (req.status_code >= 200) or (req.status_code <= 299):
                res['status_code'] = req.status_code
                res['body'] = json.loads(req.text)
                logging.info('POST success to {}'.format(target))

            elif (req.status_code >= 400) or (req.status_code <= 499):
                res = None
                logging.error('POST failure to {}'.format(target))

            return res
