const MailproClient = require('./mailproClient');

(async () => {
  const token = process.env.MAILPRO_TOKEN;
  const client = new MailproClient({ token });
  try {
    // Create
    const newContact = { email: 'new@example.com', firstName: 'New', lastName: 'Contact' };
    const created = await client.createContact(newContact);
    console.log('Created contact:', created);

    // Update
    const contactId = created && created.id ? created.id : null;
    if (contactId) {
      const updated = await client.updateContact(contactId, { lastName: 'Updated' });
      console.log('Updated contact:', updated);

      // Delete
      // const del = await client.deleteContact(contactId);
      // console.log('Deleted contact:', del);
    }
  } catch (err) {
    console.error('Contacts error:', err.message);
  }
})();
