const MailproClient = require('./mailproClient');

(async () => {
  const token = process.env.MAILPRO_TOKEN;
  const client = new MailproClient({ token });
  try {
    const resp = await client.sendEmail(
      12345,
      [{ email: 'recipient@example.com', name: 'Recipient' }],
      'Test from Mailpro SDK Starter',
      '<h1>Hello from Mailpro</h1><p>This is a test.</p>'
    );
    console.log('Send email response:', resp);
  } catch (err) {
    console.error('Error sending email:', err.message);
  }
})();
