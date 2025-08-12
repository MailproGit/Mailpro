const MailproClient = require('./mailproClient');

(async () => {
  try {
    const client = new MailproClient('YOUR_API_KEY');

    // Create a new contact
    const newContact = {
      email: 'newcontact@example.com',
      firstName: 'John',
      lastName: 'Doe'
    };
    const createRes = await client.createContact(newContact);
    console.log('Contact created:', createRes);

    // Fetch all contacts
    const contacts = await client.getContacts();
    console.log('All contacts:', contacts);
  } catch (err) {
    console.error('Error managing contacts:', err.message);
  }
})();
