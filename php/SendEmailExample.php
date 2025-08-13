<?php
require_once "MailproClient.php";

$client = new MailproClient("YOUR_API_KEY");

try {
    $response = $client->sendEmail(
        "you@example.com",
        "recipient@example.com",
        "Hello from Mailpro PHP!",
        "<p>This is a test email sent via the Mailpro API using PHP.</p>"
    );
    print_r($response);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
