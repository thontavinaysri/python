#25341a05l1 vinay
import re
def redact_emails(text):
    return re.sub(r"\b[\w.-]+@[\w.-]+\.\w+\b", "[EMAIL HIDDEN]", text)
text = "Contact me at john@gmail.com or support@example.com."
print(redact_emails(text))

'''output:
Contact me at [EMAIL HIDDEN] or [EMAIL HIDDEN].'''