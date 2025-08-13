public class SendEmailExample {
    public static void main(String[] args) {
        try {
            MailproClient client = new MailproClient("YOUR_API_KEY");

            String subject = "Test Email from Java";
            String from = "sender@example.com";
            String to = "recipient@example.com";
            String html = "<h1>Hello from Java!</h1><p>This is a test email.</p>";

            String response = client.sendEmail(subject, from, to, html);
            System.out.println("Send Email Response: " + response);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
