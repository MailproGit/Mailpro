const MailproClient = require('./mailproClient');

(async () => {
  const client = new MailproClient({ token: process.env.MAILPRO_TOKEN });
  try {
    const resp = await client.sendEmail(
      12345, // idFrom (replace with a real sender id from your Mailpro account)
      [{ email: 'recipient@example.com', name: 'Recipient' }],
      'Test from Mailpro SDK Starter',
      '<h1>Hello from Mailpro</h1><p>This is a test.</p>'
    );
    console.log('API response:', resp);
  } catch (err) {
    console.error('Error:', err);
  }
})();
