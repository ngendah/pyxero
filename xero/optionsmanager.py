from __future__ import unicode_literals

import requests

from .basemanager import BaseManager
from .constants import XERO_API_URL


class OptionsManager(BaseManager):

    def __init__(self, credentials, user_agent=None):
        from xero import __version__ as VERSION
        self.credentials = credentials
        self.singular = 'Option'
        self.name = 'Options'
        self.base_url = credentials.base_url + XERO_API_URL
        if user_agent is None:
            self.user_agent = 'pyxero/%s ' % VERSION + requests.utils.default_user_agent()

        method = self._put
        setattr(self, 'put', self._get_data(method))

    def _put(self, tracking_category_id, data, summarize_errors=True, headers=None):
        uri = '/'.join([self.base_url, 'TrackingCategories', tracking_category_id, self.name])
        params = {}
        method = 'put'
        body = {'xml': self._prepare_data_for_save(data)}
        if not summarize_errors:
            params['summarizeErrors'] = 'false'
        return uri, params, method, body, headers, False
