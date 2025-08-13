using System;
using System.Threading.Tasks;

public class ContactsExample
{
    public static async Task Main()
    {
        var client = new MailproClient("YOUR_API_KEY");

        var contactPayload = @"{
            ""email"": ""new.contact@example.com"",
            ""firstName"": ""John"",
            ""lastName"": ""Doe""
        }";

        try
        {
            var result = await client.PostAsync("https://api.mailpro.com/v1/contacts", contactPayload);
            Console.WriteLine("Contact added successfully: " + result);
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error adding contact: " + ex.Message);
        }
    }
}
