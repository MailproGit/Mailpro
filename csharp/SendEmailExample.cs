using System;
using System.Threading.Tasks;

public class SendEmailExample
{
    public static async Task Main()
    {
        var client = new MailproClient("YOUR_API_KEY");

        var emailPayload = @"{
            ""from"": ""you@example.com"",
            ""to"": ""recipient@example.com"",
            ""subject"": ""Test Email from C#"",
            ""html"": ""<p>Hello from Mailpro C# example!</p>""
        }";

        try
        {
            var result = await client.PostAsync("https://api.mailpro.com/v1/send", emailPayload);
            Console.WriteLine("Email sent successfully: " + result);
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error sending email: " + ex.Message);
        }
    }
}
