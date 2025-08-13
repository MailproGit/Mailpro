using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

public class MailproClient
{
    private readonly string _apiKey;
    private readonly HttpClient _httpClient;

    public MailproClient(string apiKey)
    {
        _apiKey = apiKey;
        _httpClient = new HttpClient();
        _httpClient.DefaultRequestHeaders.Add("Authorization", $"Bearer {_apiKey}");
    }

    public async Task<string> GetAsync(string endpoint)
    {
        var response = await _httpClient.GetAsync(endpoint);
        response.EnsureSuccessStatusCode();
        return await response.Content.ReadAsStringAsync();
    }

    public async Task<string> PostAsync(string endpoint, string jsonBody)
    {
        var content = new StringContent(jsonBody, Encoding.UTF8, "application/json");
        var response = await _httpClient.PostAsync(endpoint, content);
        response.EnsureSuccessStatusCode();
        return await response.Content.ReadAsStringAsync();
    }
}
