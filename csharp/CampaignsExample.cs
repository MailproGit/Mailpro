using System;
using System.Threading.Tasks;

public class CampaignsExample
{
    public static async Task Main()
    {
        var client = new MailproClient("YOUR_API_KEY");

        try
        {
            var campaigns = await client.GetAsync("https://api.mailpro.com/v1/campaigns");
            Console.WriteLine("Campaigns List:\n" + campaigns);
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error fetching campaigns: " + ex.Message);
        }
    }
}
