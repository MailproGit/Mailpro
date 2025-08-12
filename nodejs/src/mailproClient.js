const fetch = require('node-fetch');

class MailproClient {
  constructor({ baseUrl = 'https://api.mailpro.com', token }) {
    this.baseUrl = baseUrl.replace(/\/$/, '');
    this.token = token; // OAuth2 bearer token or API token depending on your setup
  }

  async request(path, method = 'GET', body = null, qs = null) {
    const url = new URL(this.baseUrl + path);
    if (qs) Object.keys(qs).forEach(k => url.searchParams.append(k, qs[k]));
    const opts = {
      method,
      headers: {
        'Accept': 'application/json',
        'Authorization': `Bearer ${this.token}`
      }
    };
    if (body) {
      opts.headers['Content-Type'] = 'application/json';
      opts.body = JSON.stringify(body);
    }
    const res = await fetch(url.toString(), opts);
    const txt = await res.text();
    try { return JSON.parse(txt); } catch (e) { return txt; }
  }

  // Example: send a single transactional email
  async sendEmail(fromId, to, subject, html) {
    const body = {
      idFrom: fromId,
      to: to,
      subject: subject,
      bodyHtml: html
    };
    return this.request('/v3/email/send', 'POST', body);
  }
}

module.exports = MailproClient;
