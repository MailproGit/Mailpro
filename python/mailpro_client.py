import os
import requests

class MailproClient:
    def __init__(self, token=None, base_url='https://api.mailpro.com'):
        self.token = token or os.getenv('MAILPRO_TOKEN')
        if not self.token:
            raise ValueError('MAILPRO_TOKEN required')
        self.base_url = base_url.rstrip('/')
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def _url(self, path):
        return f"{self.base_url}{path}"

    def post(self, path, payload=None):
        r = requests.post(self._url(path), headers=self.headers, json=payload)
        r.raise_for_status()
        return r.json()

    def get(self, path, params=None):
        r = requests.get(self._url(path), headers=self.headers, params=params)
        r.raise_for_status()
        return r.json()

    def put(self, path, payload=None):
        r = requests.put(self._url(path), headers=self.headers, json=payload)
        r.raise_for_status()
        return r.json()

    # Email
    def send_email(self, id_from, to, subject, html, **kwargs):
        payload = dict(idFrom=id_from, to=to, subject=subject, bodyHtml=html)
        payload.update(kwargs)
        return self.post('/v3/email/send', payload)

    # Contacts
    def create_contact(self, payload):
        return self.post('/v3/contacts', payload)

    def update_contact(self, contact_id, payload):
        return self.put(f'/v3/contacts/{contact_id}', payload)

    def delete_contact(self, contact_id):
        r = requests.delete(self._url(f'/v3/contacts/{contact_id}'), headers=self.headers)
        r.raise_for_status()
        return r.json() if r.text else {}

    # Campaigns
    def create_campaign(self, payload):
        return self.post('/v3/campaigns', payload)

    def get_campaign(self, campaign_id):
        return self.get(f'/v3/campaigns/{campaign_id}')

    def send_campaign(self, campaign_id):
        return self.post(f'/v3/campaigns/{campaign_id}/send')
