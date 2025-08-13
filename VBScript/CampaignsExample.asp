<%
<!--#include file="MailproClient.asp" -->

Dim client, campaignData, response
Set client = New MailproClient
client.Init("YOUR_API_KEY_HERE")

Set campaignData = CreateObject("Scripting.Dictionary")
campaignData("name") = "August Newsletter"
campaignData("subject") = "Our Latest News"
campaignData("content") = "<h1>Hello from Mailpro</h1><p>Here's our latest update!</p>"

response = client.CreateCampaign(campaignData)

Response.Write("<pre>" & Server.HTMLEncode(response) & "</pre>")
%>
