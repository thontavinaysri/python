#25341a05l1 vinay
import re

text = "Important dates are 20/09/2026, 15/08/2025 and 01/01/2024."

# Extract dates using groups
dates = re.findall(r"(\d{2})/(\d{2})/(\d{4})", text)
print("Extracted dates:", dates)

# Convert DD/MM/YYYY to YYYY-MM-DD
result = re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1", text)

print("Reformatted text:", result)
'''output:
Extracted dates: [('20', '09', '2026'), ('15', '08', '2025'), ('01', '01', '2024')]
Reformatted text: Important dates are 2026-09-20, 2025-08-15 and 2024-01-01.
'''