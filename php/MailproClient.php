<?php

class MailproClient {
    private $apiKey;
    private $baseUrl;

    public function __construct($apiKey, $baseUrl = "https://api.mailpro.com/v1/") {
        $this->apiKey = $apiKey;
        $this->baseUrl = rtrim($baseUrl, "/") . "/";
    }

    private function request($endpoint, $method = "GET", $data = null) {
        $url = $this->baseUrl . $endpoint;
        $headers = [
            "Authorization: Bearer " . $this->apiKey,
            "Content-Type: application/json"
        ];

        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

        if ($method === "POST") {
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
        } elseif ($method === "PUT") {
            curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "PUT");
            curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
        }

        $response = curl_exec($ch);
        if (curl_errno($ch)) {
            throw new Exception("Curl error: " . curl_error($ch));
        }
        curl_close($ch);

        return json_decode($response, true);
    }

    public function sendEmail($from, $to, $subject, $html) {
        return $this->request("email/send", "POST", [
            "from" => $from,
            "to" => $to,
            "subject" => $subject,
            "html" => $html
        ]);
    }

    public function addContact($listId, $email, $firstName = "", $lastName = "") {
        return $this->request("contacts", "POST", [
            "listId" => $listId,
            "email" => $email,
            "firstName" => $firstName,
            "lastName" => $lastName
        ]);
    }

    public function createCampaign($name, $subject, $content, $listId) {
        return $this->request("campaigns", "POST", [
            "name" => $name,
            "subject" => $subject,
            "content" => $content,
            "listId" => $listId
        ]);
    }
}

?>
