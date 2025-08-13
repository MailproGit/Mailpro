public class CampaignsExample {
    public static void main(String[] args) {
        try {
            MailproClient client = new MailproClient("YOUR_API_KEY");

            String campaignName = "Java Campaign";
            String subject = "Special Offer";
            String from = "marketing@example.com";

            String response = client.createCampaign(campaignName, subject, from);
            System.out.println("Create Campaign Response: " + response);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
