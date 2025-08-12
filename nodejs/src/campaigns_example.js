const MailproClient = require('./mailproClient');

(async () => {
  try {
    const client = new MailproClient('YOUR_API_KEY');

    // Create a new campaign
    const campaignData = {
      name: 'My First Campaign',
      subject: 'Welcome!',
      from: 'you@example.com',
      html: '<h1>Hello Subscribers</h1><p>This is my first campaign!</p>'
    };
    const createRes = await client.createCampaign(campaignData);
    console.log('Campaign created:', createRes);

    // Fetch details of the campaign
    if (createRes.id) {
      const details = await client.getCampaign(createRes.id);
      console.log('Campaign details:', details);
    }
  } catch (err) {
    console.error('Error with campaigns:', err.message);
  }
})();
