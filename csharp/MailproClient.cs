using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

public class MailproClient
{
    private readonly HttpClient _http;
    public MailproClient(string token, string baseUrl = "https://api.mailpro.com")
    {
        _http = new HttpClient { BaseAddress = new Uri(baseUrl) };
        _http.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
        _http.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
    }

    public async Task<string> SendEmailAsync(long idFrom, object to, string subject, string html)
    {
        var payload = new {
            idFrom = idFrom,
            to = to,
            subject = subject,
            bodyHtml = html
        };
        var json = System.Text.Json.JsonSerializer.Serialize(payload);
        var res = await _http.PostAsync("/v3/email/send", new StringContent(json, Encoding.UTF8, "application/json"));
        res.EnsureSuccessStatusCode();
        return await res.Content.ReadAsStringAsync();
    }
}
