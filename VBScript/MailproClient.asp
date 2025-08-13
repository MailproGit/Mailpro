<%
Class MailproClient
    Private apiKey
    Private baseUrl

    Public Sub Init(ByVal pApiKey)
        apiKey = pApiKey
        baseUrl = "https://api.mailpro.com/v1"
    End Sub

    Private Function HttpRequest(ByVal method, ByVal endpoint, ByVal data)
        Dim http, url, body
        url = baseUrl & endpoint

        Set http = Server.CreateObject("MSXML2.ServerXMLHTTP.6.0")
        http.open method, url, False
        http.setRequestHeader "Content-Type", "application/json"
        http.setRequestHeader "Authorization", "Bearer " & apiKey

        If IsObject(data) Then
            body = JSONStringify(data)
        Else
            body = data
        End If

        If method = "GET" Then
            http.send
        Else
            http.send body
        End If

        HttpRequest = http.responseText
        Set http = Nothing
    End Function

    Public Function SendEmail(ByVal emailData)
        SendEmail = HttpRequest("POST", "/emails/send", emailData)
    End Function

    Public Function AddContact(ByVal contactData)
        AddContact = HttpRequest("POST", "/contacts", contactData)
    End Function

    Public Function CreateCampaign(ByVal campaignData)
        CreateCampaign = HttpRequest("POST", "/campaigns", campaignData)
    End Function

    ' Simple JSON serializer (basic key-value only)
    Private Function JSONStringify(ByVal dict)
        Dim k, result, sep
        result = "{"
        sep = ""
        For Each k In dict
            result = result & sep & """" & k & """:""" & dict(k) & """"
            sep = ","
        Next
        result = result & "}"
        JSONStringify = result
    End Function
End Class
%>
