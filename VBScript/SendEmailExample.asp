<%
<!--#include file="MailproClient.asp" -->

Dim client, emailData, response
Set client = New MailproClient
client.Init("YOUR_API_KEY_HERE")

Set emailData = CreateObject("Scripting.Dictionary")
emailData("from") = "you@example.com"
emailData("to") = "recipient@example.com"
emailData("subject") = "Hello from ASP Classic"
emailData("body") = "This is a test email sent via Mailpro API in ASP Classic."

response = client.SendEmail(emailData)

Response.Write("<pre>" & Server.HTMLEncode(response) & "</pre>")
%>
