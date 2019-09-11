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

    def post(self, uri=None, p_params=None, payload=None, basic_auth=True, token_auth=False):

        # Format the path
        target = self.url

        if uri:
            target = self.url + uri

        # Take key value pairs from dict and format them ex: /user/{userID} and append to the target
        if p_params:
            p_string = '/'
            for key in p_params:
                p_string = p_string + key + '/' + str(p_params[key]) + '/'
            target = target + p_string[:-1]

        # return target

        # Perform the call using basic authorization
        if basic_auth:
            auth = (self.username, self.password)
            req = requests.post(target, auth=auth, headers=self.headers, data=json.dumps(payload))
            res = {}

            if (req.status_code >= 200) or (req.status_code <= 299):
                res['status_code'] = req.status_code
                res['body'] = json.loads(req.text)
                res['headers'] = req.headers
                logging.info('POST success to {}'.format(target))

            elif (req.status_code >= 400) or (req.status_code <= 499):
                res = None
                logging.error('POST failure to {}'.format(target))

            return res

    def get(self, uri=None, q_params=None, p_params=None, basic_auth=True, token_auth=False):

        # Format the path
        target = self.url

        if uri:
            target = target + uri

        # Take key value pairs from dict and format them ex: /user/{userID} and append to the target
        if p_params:
            p_string = '/'
            for key in p_params:
                p_string = p_string + key + '/' + str(p_params[key]) + '/'
            target = target + p_string[:-1]

        # Take key value pairs from dict and format them ex: ?user={userID} and append to the target
        if q_params:
            q_string = '?'
            for key in q_params:
                q_string = q_string + key + '=' + str(q_params[key]) + '&'
            target = target + q_string[:-1]

        # return target

        # Perform the call using basic authorization
        if basic_auth:
            auth = (self.username, self.password)
            req = requests.get(target, auth=auth, headers=self.headers)
            res = {}

            if (req.status_code >= 200) or (req.status_code <= 299):
                res['status_code'] = req.status_code
                res['body'] = json.loads(req.text)
                res['headers'] = req.headers
                logging.info('GET success from {}'.format(target))

            elif (req.status_code >= 400) or (req.status_code <= 499):
                res = None
                logging.error('GET failure from {}'.format(target))

            return res
