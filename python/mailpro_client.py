import requests
import json

class MailproClient:
    def __init__(self, token, base_url='https://api.mailpro.com'):
        self.base_url = base_url.rstrip('/')
        self.token = token
        self.headers = {
            'Authorization': f'Bearer {self.token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def post(self, path, payload):
        url = f"{self.base_url}{path}"
        r = requests.post(url, headers=self.headers, data=json.dumps(payload))
        r.raise_for_status()
        try:
            return r.json()
        except ValueError:
            return r.text

    def send_email(self, id_from, to, subject, html):
        payload = {
            'idFrom': id_from,
            'to': to,
            'subject': subject,
            'bodyHtml': html
        }
        return self.post('/v3/email/send', payload)


# Example usage in send_email_example.py
if __name__ == '__main__':
    import os
    client = MailproClient(os.getenv('MAILPRO_TOKEN'))
    resp = client.send_email(12345, [{'email':'recipient@example.com','name':'Recipient'}], 'Hello', '<p>hi</p>')
    print(resp)
