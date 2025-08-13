<?php
require_once "MailproClient.php";

$client = new MailproClient("YOUR_API_KEY");

try {
    $response = $client->addContact(
        "LIST_ID_HERE",
        "newcontact@example.com",
        "John",
        "Doe"
    );
    print_r($response);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
