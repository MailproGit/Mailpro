public class ContactsExample {
    public static void main(String[] args) {
        try {
            MailproClient client = new MailproClient("YOUR_API_KEY");

            String listId = "12345";
            String email = "newcontact@example.com";

            String response = client.addContact(listId, email);
            System.out.println("Add Contact Response: " + response);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
