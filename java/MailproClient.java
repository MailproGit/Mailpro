import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;

public class MailproClient {
    private final String apiKey;
    private final String baseUrl;

    public MailproClient(String apiKey) {
        this.apiKey = apiKey;
        this.baseUrl = "https://api.mailpro.com/v1";
    }

    private String request(String endpoint, String method, String jsonBody) throws IOException {
        URL url = new URL(baseUrl + endpoint);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod(method);
        conn.setRequestProperty("Authorization", "Bearer " + apiKey);
        conn.setRequestProperty("Content-Type", "application/json");

        if (jsonBody != null && !jsonBody.isEmpty()) {
            conn.setDoOutput(true);
            try (OutputStream os = conn.getOutputStream()) {
                os.write(jsonBody.getBytes("UTF-8"));
            }
        }

        int responseCode = conn.getResponseCode();
        InputStream is = (responseCode < HttpURLConnection.HTTP_BAD_REQUEST) ?
                conn.getInputStream() : conn.getErrorStream();

        BufferedReader br = new BufferedReader(new InputStreamReader(is));
        StringBuilder response = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            response.append(line);
        }
        br.close();
        return response.toString();
    }

    public String sendEmail(String subject, String from, String to, String htmlBody) throws IOException {
        String json = String.format(
            "{\"subject\":\"%s\",\"from\":\"%s\",\"to\":\"%s\",\"html\":\"%s\"}",
            subject, from, to, htmlBody.replace("\"", "\\\"")
        );
        return request("/email/send", "POST", json);
    }

    public String addContact(String listId, String email) throws IOException {
        String json = String.format("{\"listId\":\"%s\",\"email\":\"%s\"}", listId, email);
        return request("/contacts/add", "POST", json);
    }

    public String createCampaign(String name, String subject, String from) throws IOException {
        String json = String.format("{\"name\":\"%s\",\"subject\":\"%s\",\"from\":\"%s\"}", name, subject, from);
        return request("/campaigns/create", "POST", json);
    }
}
