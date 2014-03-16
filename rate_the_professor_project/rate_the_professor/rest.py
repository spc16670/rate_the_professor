from xml.dom.minidom import parseString
from time import gmtime, strftime
import httplib
import hashlib
import hmac
import base64


def get_amazon_suggestions(keyword):
    amazon_access_key = "AKIAJLEWU2SSPY43LYTQ"

    host = "ecs.amazonaws.com:80"
    service = "/onca/xml?"

    datetime_utc = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
    datetime_utc_enc = datetime_utc.replace(":", "%3A")
    keyword_f = keyword.replace(" ", "%20")
    sign_head = "GET\necs.amazonaws.com\n/onca/xml\n"

    params = "AWSAccessKeyId=" + amazon_access_key + "&" \
        "AssociateTag=PutYourAssociateTagHere&" \
        "Keywords=" + keyword_f + "&" \
        "Operation=ItemSearch&" \
        "SearchIndex=Books&" \
        "Service=AWSECommerceService&" \
        "Timestamp=" + datetime_utc_enc + "&" \
        "Version=2011-08-01"

    string_to_sign = sign_head + params

    dig = hmac.new(b'mERr4dAusZ9Tk1cwHXW4lpdY4C6w6LFNuzWe6gl8', msg=string_to_sign, digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(dig).decode()

    request = service + params + "&Signature=" + signature

    books = []

    try:
        connection = httplib.HTTPConnection(host)
        connection.request('GET', request)

        response = connection.getresponse().read()

        dom = parseString(response)

        class BookSuggestion(object):
            author = ""
            title = ""
            url = ""

            def __init__(self, author, title, url):
                self.author = author
                self.title = title
                self.url = url

        items = dom.getElementsByTagName('Item')
        for item in items:
            itemLink = item.getElementsByTagName('ItemLink')[0]
            urlnode = itemLink.getElementsByTagName('URL')[0]
            url = urlnode.childNodes[0].nodeValue

            item_atts = dom.getElementsByTagName('ItemAttributes')
            for item_att in item_atts:
                authorlist = item_att.getElementsByTagName('Author')
                for a in authorlist:
                    author = a.childNodes[0].nodeValue

                titlelist = item_att.getElementsByTagName('Title')
                for a in titlelist:
                    title = a.childNodes[0].nodeValue

                book_suggestion = BookSuggestion(author, title, url)
                books.append(book_suggestion)
    except httplib.HTTPException, error:
        if error.code == 404:
            print "Page not found!"
        elif error.code == 403:
            print "Access denied!"
        else:
            print "Something happened! Error code", error.code
    # Not specifying exception is really bad, I know
    except httplib.ImproperConnectionState, error:
        print error.message

    return books
