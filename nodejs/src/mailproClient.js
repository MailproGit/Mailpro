const fetch = require('node-fetch');

class MailproClient {
  constructor(apiKey) {
    this.apiKey = apiKey;
    this.baseUrl = 'https://api.mailpro.com/v3';
  }

  async request(endpoint, method = 'GET', body = null) {
    const res = await fetch(`${this.baseUrl}${endpoint}`, {
      method,
      headers: {
        'Authorization': `Bearer ${this.apiKey}`,
        'Content-Type': 'application/json'
      },
      body: body ? JSON.stringify(body) : null
    });
    if (!res.ok) {
      const errText = await res.text();
      throw new Error(`Mailpro API error: ${res.status} ${errText}`);
    }
    return res.json();
  }

  sendEmail(payload) {
    return this.request('/emails', 'POST', payload);
  }

  getContacts() {
    return this.request('/contacts', 'GET');
  }

  createContact(payload) {
    return this.request('/contacts', 'POST', payload);
  }

  createCampaign(payload) {
    return this.request('/campaigns', 'POST', payload);
  }

  getCampaign(id) {
    return this.request(`/campaigns/${id}`, 'GET');
  }
}

module.exports = MailproClient;
