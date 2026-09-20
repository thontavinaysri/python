#25341a05l1 vinay
import re

def clean_text(html):
    # Remove all HTML tags
    text = re.sub(r"<[^>]+>", "", html)

    # Replace multiple spaces, tabs, or newlines with one space
    text = re.sub(r"\s+", " ", text)

    return text.strip()


html = "<p>Hello   <b>world</b>!</p>\n\tThis is   a test."

print(clean_text(html))

'''output:
Hello world! This is a test.'''