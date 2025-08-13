const MailproClient = require('./mailproClient');

(async () => {
  const token = process.env.MAILPRO_TOKEN;
  const client = new MailproClient({ token });
  try {
    const campaignPayload = {
      name: 'SDK Starter Campaign',
      subject: 'Hello from SDK',
      idFrom: 12345,
      listIds: [1],
      html: '<h1>Campaign</h1><p>Example</p>'
    };
    const created = await client.createCampaign(campaignPayload);
    console.log('Created campaign:', created);

    if (created && created.id) {
      const status = await client.getCampaign(created.id);
      console.log('Campaign status:', status);

      // To send
      // const sendResp = await client.sendCampaign(created.id);
      // console.log('Send response:', sendResp);
    }
  } catch (err) {
    console.error('Campaign error:', err.message);
  }
})();
