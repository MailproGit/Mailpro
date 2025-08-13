<?php
require_once "MailproClient.php";

$client = new MailproClient("YOUR_API_KEY");

try {
    $response = $client->createCampaign(
        "New Campaign",
        "Special Offer",
        "<h1>Don't miss our offer!</h1><p>Get 50% off today.</p>",
        "LIST_ID_HERE"
    );
    print_r($response);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
?>
