from xml.dom.minidom import parseString
from time import gmtime, strftime
import httplib
import hashlib
import hmac
import base64
import urllib2


# Call Amazon API and search for books by a keyword
def get_amazon_suggestions(keyword):
    amazon_access_key = "AKIAJLEWU2SSPY43LYTQ"
    host = "http://ecs.amazonaws.com"
    service = "/onca/xml?"
    datetime_utc = strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())
    datetime_utc_enc = datetime_utc.replace(":", "%3A")
    # The keyword is a professor's first and last name
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

    request = host + service + params + "&Signature=" + signature

    books = []

    try:
        req = urllib2.Request(request)
        response = urllib2.urlopen(req)
        response = response.read()
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
            item_link = item.getElementsByTagName('ItemLink')[0]
            url_node = item_link.getElementsByTagName('URL')[0]
            url = url_node.childNodes[0].nodeValue

            item_attributes = item.getElementsByTagName('ItemAttributes')
            for attribute in item_attributes:
                author_list = attribute.getElementsByTagName('Author')
                for a in author_list:
                    author = a.childNodes[0].nodeValue

                title_list = attribute.getElementsByTagName('Title')
                for a in title_list:
                    title = a.childNodes[0].nodeValue

                book_suggestion = BookSuggestion(author, title, url)
                books.append(book_suggestion)
    except urllib2.HTTPError, e:
        print 'HTTPError = ' + str(e.code)
    except urllib2.URLError, e:
        print 'URLError = ' + str(e.reason)
    except httplib.HTTPException, e:
        print'HTTPException'
    except Exception:
        import traceback
        print 'Generic exception: ' + traceback.format_exc()

    return books
