using System;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var token = Environment.GetEnvironmentVariable("MAILPRO_TOKEN");
        var client = new MailproClient(token);
        var to = new[] { new { email = "recipient@example.com", name = "Recipient" } };
        var resp = await client.SendEmailAsync(12345, to, "Test", "<p>hi</p>");
        Console.WriteLine(resp);
    }
}
