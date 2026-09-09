# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#    # Look at the parts of a tag
#    print 'TAG:',tag
#    print 'URL:',tag.get('href', None)
#    print 'Contents:',tag.contents[0]
#    print 'Attrs:',tag.attrs

import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ').strip()
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')
total = 0
for tag in tags:
    total += int(tag.contents[0])

print(total.get('class', None))

# .get('class', None) looks at HTML attributes.
# .contents (or .text) looks at the content inside the tags.
# the numbers you want are written between the tags: <span>90</span>. The number 90 is the text content, not an attribute. Therefore, tag.contents[0] pulls out that actual text ("90"), which you can then convert into an integer to add to your sum.

# Use .get() when you want to read HTML attributes (like href links or class names).

# Use .contents[0] (or .text) when you want to read the actual text/numbers hidden inside the HTML tags.

# At the very end of your program, you just want to print the final number, so it should just be print(total).