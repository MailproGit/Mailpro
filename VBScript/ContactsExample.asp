<%
<!--#include file="MailproClient.asp" -->

Dim client, contactData, response
Set client = New MailproClient
client.Init("YOUR_API_KEY_HERE")

Set contactData = CreateObject("Scripting.Dictionary")
contactData("email") = "newcontact@example.com"
contactData("firstname") = "John"
contactData("lastname") = "Doe"

response = client.AddContact(contactData)

Response.Write("<pre>" & Server.HTMLEncode(response) & "</pre>")
%>
