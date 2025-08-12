const MailproClient = require('./mailproClient');

(async () => {
  try {
    const client = new MailproClient('YOUR_API_KEY');

    const emailPayload = {
      from: 'you@example.com',
      to: 'recipient@example.com',
      subject: 'Hello from Mailpro API',
      html: '<p>This is a test email sent via the Mailpro API SDK!</p>'
    };

    const result = await client.sendEmail(emailPayload);
    console.log('Email sent successfully:', result);
  } catch (err) {
    console.error('Error sending email:', err.message);
  }
})();
